"""Anexo S0: un stress test de credito de juguete, de principio a fin.

Una filial mexicana con dos carteras (consumo y empresas), el escenario base y
adverso de la JERS para Mexico del ejercicio 2025, un satelite por cartera,
flujos entre stages, provisiones IFRS 9 con prevision perfecta, RWA estandar y
caida de CET1 atribuible al credito. Balance estatico: lo que vence se repone,
el S3 no se cura ni se da de baja.

Simplificaciones deliberadas (se explican en el capitulo 8):
  - solo credito: no hay margen de intereses, comisiones ni gastos;
  - satelites dados (el de consumo es el estimado en el anexo S1);
  - transiciones a S2 y desde S2 como multiplos fijos de la PD de S1;
  - sin descuento financiero en la perdida a vida.
"""
import numpy as np
import pandas as pd

# ------------------------------------------------------------------
# 1. Escenario JERS 2025 para Mexico (tabla 4.1.1 y 4.1.2 del escenario)
# ------------------------------------------------------------------
ANOS = [2025, 2026, 2027]
PARO_2024 = 3.0
ESC = {
    "base":    {"pib": [1.3, 2.0, 2.3],   "paro": [3.3, 3.4, 3.5]},
    "adverso": {"pib": [-4.7, -2.2, -0.1], "paro": [5.2, 7.6, 8.8]},
}

# ------------------------------------------------------------------
# 2. Las dos carteras (millones de euros) y sus parametros
# ------------------------------------------------------------------
CARTERAS = {
    "consumo": {
        "stock": {"S1": 880.0, "S2": 70.0, "S3": 50.0},
        "satelite": (-3.514, 0.215, -0.0802),   # anexo S1: logit PD = a + b*paro(t-1) + c*PIB(t)
        "m_s1_s2": 1.5,   # tasa S1->S2 = m * PD S1
        "m_s2_s3": 3.0,   # PD S2 = m * PD S1
        "cura_s2": 0.20,  # S2 -> S1 cada ano
        "vida": 3,        # anos de vida residual para la perdida a vida de S2
        "lgd": lambda paro, pib: min(0.85, 0.70 + 0.01 * (paro - 3.5)),
        "pond_rwa": 0.75,
        "margen": {"base": 0.085, "adverso": 0.075},   # margen antes de provisiones, dado
    },
    "empresas": {
        "stock": {"S1": 950.0, "S2": 36.0, "S3": 14.0},
        "satelite": (-4.60, 0.10, -0.12),
        "m_s1_s2": 2.0,
        "m_s2_s3": 6.0,
        "cura_s2": 0.20,
        "vida": 4,
        "lgd": lambda paro, pib: 0.40 + 0.02 * max(0.0, -pib),
        "pond_rwa": 1.00,
        "margen": {"base": 0.015, "adverso": 0.012},
    },
}
TIPO_FISCAL = 0.30
CET1_INICIAL_SOBRE_RWA = 0.13


def logistica(z):
    return 1 / (1 + np.exp(-z))


def sendas(cart, esc):
    """PD de S1 y LGD por ano: 2024 (partida), 2025-2027 y 10 anos mas tras el horizonte.

    Tras 2027: en el base, parametros planos; en el adverso, reversion lineal en
    6 anos a los parametros base de 2027 (como en la metodologia EBA 2027).
    """
    a, b, c = cart["satelite"]
    paro_prev = [PARO_2024] + ESC[esc]["paro"][:-1]
    pd_h = [logistica(a + b * pp + c * g) for pp, g in zip(paro_prev, ESC[esc]["pib"])]
    lgd_h = [cart["lgd"](p, g) for p, g in zip(ESC[esc]["paro"], ESC[esc]["pib"])]
    # punto de partida (fin de 2024): parametros "de hoy" = primer ano del base
    pd0 = logistica(a + b * PARO_2024 + c * ESC["base"]["pib"][0])
    lgd0 = cart["lgd"](ESC["base"]["paro"][0], ESC["base"]["pib"][0])
    # base de 2027 como ancla de la reversion
    pb = [PARO_2024] + ESC["base"]["paro"][:-1]
    pd_b27 = logistica(a + b * pb[2] + c * ESC["base"]["pib"][2])
    lgd_b27 = cart["lgd"](ESC["base"]["paro"][2], ESC["base"]["pib"][2])
    pd_tras, lgd_tras = [], []
    for k in range(1, 11):
        w = max(0.0, 1 - k / 6) if esc == "adverso" else 1.0
        pd_tras.append(pd_b27 + (pd_h[2] - pd_b27) * w if esc == "adverso" else pd_h[2])
        lgd_tras.append(lgd_b27 + (lgd_h[2] - lgd_b27) * w if esc == "adverso" else lgd_h[2])
    return [pd0] + pd_h + pd_tras, [lgd0] + lgd_h + lgd_tras


def provisiones(cart, stock, pd_s, lgd_s, t, prevision_perfecta=True, prov_s3_vieja=None):
    """Stock de provisiones al final del ano t (t=0 es la partida)."""
    s1 = stock["S1"] * pd_s[t + 1] * lgd_s[t + 1]
    if prevision_perfecta:
        camino = [min(0.6, cart["m_s2_s3"] * pd_s[t + j]) for j in range(1, cart["vida"] + 1)]
    else:
        camino = [min(0.6, cart["m_s2_s3"] * pd_s[t + 1])] * cart["vida"]
    pd_vida = 1 - np.prod([1 - p for p in camino])
    s2 = stock["S2"] * pd_vida * lgd_s[t + 1]
    s3 = stock["S3_nuevo"] * lgd_s[max(t, 1)] + prov_s3_vieja
    return s1 + s2 + s3, {"S1": s1, "S2": s2, "S3": s3}


def proyectar(nombre, esc, prevision_perfecta=True):
    cart = CARTERAS[nombre]
    pd_s, lgd_s = sendas(cart, esc)
    pd_b, lgd_b = sendas(cart, "base")
    st = dict(cart["stock"])
    st["S3_nuevo"] = 0.0
    exp_total = st["S1"] + st["S2"] + st["S3"]
    # el punto de partida es un dato: se provisiona con el escenario interno (el base),
    # igual en los dos escenarios
    prov_s3_0 = st["S3"] * lgd_b[0]
    prov0, _ = provisiones(cart, st, pd_b, lgd_b, 0, True, prov_s3_0)
    filas = [{"ano": 2024, "S1": st["S1"], "S2": st["S2"], "S3": st["S3"], "prov": prov0,
              "deterioro": 0.0, "prov_S3": prov_s3_0}]
    prov_ant = prov0
    prov_s3_vieja = max(prov_s3_0, st["S3"] * lgd_s[1])   # suelo del S3 antiguo
    for t in (1, 2, 3):
        pd1 = pd_s[t]
        pd2 = min(0.6, cart["m_s2_s3"] * pd1)
        a_s3_desde_s1 = st["S1"] * pd1
        a_s2_desde_s1 = st["S1"] * cart["m_s1_s2"] * pd1
        a_s3_desde_s2 = st["S2"] * pd2
        a_s1_desde_s2 = st["S2"] * cart["cura_s2"]
        st["S1"] += -a_s3_desde_s1 - a_s2_desde_s1 + a_s1_desde_s2
        st["S2"] += a_s2_desde_s1 - a_s3_desde_s2 - a_s1_desde_s2
        st["S3_nuevo"] += a_s3_desde_s1 + a_s3_desde_s2
        st["S3"] = cart["stock"]["S3"] + st["S3_nuevo"]
        prov, det = provisiones(cart, st, pd_s, lgd_s, t, prevision_perfecta, prov_s3_vieja)
        filas.append({"ano": ANOS[t - 1], "S1": st["S1"], "S2": st["S2"], "S3": st["S3"],
                      "prov": prov, "deterioro": prov - prov_ant, "pd_s1": pd1,
                      "prov_S1": det["S1"], "prov_S2": det["S2"], "prov_S3": det["S3"]})
        prov_ant = prov
    df = pd.DataFrame(filas)
    # RWA estandar: performing a su ponderacion; S3 al 100 % neto de su provision
    df["rwa"] = (df.S1 + df.S2) * cart["pond_rwa"] + (df.S3 - df.prov_S3).clip(lower=0) * 1.00
    df["margen"] = [0.0] + [exp_total * cart["margen"][esc]] * 3
    return df, exp_total


def main():
    pd.set_option("display.width", 140)
    resultados = {}
    print("PD de S1 que da el satelite (fin 2024 y 2025-2027)")
    for nombre, cart in CARTERAS.items():
        for esc in ESC:
            pd_s, lgd_s = sendas(cart, esc)
            print(f"  {nombre:8} {esc:7}  PD: " + "  ".join(f"{p:6.2%}" for p in pd_s[:4])
                  + "   LGD: " + "  ".join(f"{l:5.1%}" for l in lgd_s[:4]))

    for esc in ESC:
        print(f"\n===== Escenario {esc} =====")
        tot = None
        for nombre in CARTERAS:
            df, exp_total = proyectar(nombre, esc)
            resultados[(nombre, esc)] = (df, exp_total)
            print(f"\n{nombre} (exposicion {exp_total:,.0f} M EUR)")
            print(df[["ano", "S1", "S2", "S3", "prov", "deterioro", "rwa"]].round(1).to_string(index=False))
            acum = df.deterioro.sum()
            print(f"  deterioro acumulado: {acum:,.1f} M EUR = {acum / exp_total:.2%} de la exposicion; "
                  f"S3 final {df.S3.iloc[-1] / exp_total:.2%}; primer ano {df.deterioro.iloc[1] / acum:.0%} del total")
            cols = ["deterioro", "rwa", "margen"]
            tot = df[cols] if tot is None else tot + df[cols]
        rwa0 = tot.rwa.iloc[0]
        for etiqueta, con_margen in (("solo perdidas de credito", False), ("con el margen dado", True)):
            cet1 = CET1_INICIAL_SOBRE_RWA * rwa0
            ratios = [cet1 / rwa0]
            for t in (1, 2, 3):
                resultado = -tot.deterioro.iloc[t] + (tot.margen.iloc[t] if con_margen else 0.0)
                cet1 += resultado * (1 - TIPO_FISCAL) if resultado > 0 else resultado * (1 - TIPO_FISCAL)
                # suelo metodologico: el RWA no puede bajar del de partida (EBA 2027, parr. 153)
                ratios.append(cet1 / max(tot.rwa.iloc[t], rwa0))
            print(f"Filial, CET1 {etiqueta:26}: " + " -> ".join(f"{r:.2%}" for r in ratios)
                  + f"  (caida maxima {(ratios[0] - min(ratios)) * 1e4:,.0f} pb)")
        print(f"RWA de la filial sin suelo: {rwa0:,.0f} -> " + " -> ".join(f"{x:,.0f}" for x in tot.rwa.iloc[1:])
              + f"  (con el suelo, nunca por debajo de {rwa0:,.0f})")

    print("\n===== Adverso menos base =====")
    for nombre in CARTERAS:
        da = resultados[(nombre, "adverso")][0].deterioro.sum()
        db = resultados[(nombre, "base")][0].deterioro.sum()
        e = resultados[(nombre, "base")][1]
        print(f"  {nombre:8} adverso {da / e:.2%}  base {db / e:.2%}  diferencia {(da - db) / e * 100:.2f} pp")

    print("\n===== Prevision perfecta: de donde sale el primer ano (consumo, adverso) =====")
    df_pp, _ = proyectar("consumo", "adverso", True)
    df_np, _ = proyectar("consumo", "adverso", False)
    for etiqueta, df in (("con prevision perfecta", df_pp), ("con la PD del ano siguiente fija", df_np)):
        print(f"  {etiqueta:34} deterioro por ano: "
              + "  ".join(f"{d:6.1f}" for d in df.deterioro.iloc[1:])
              + f"   total {df.deterioro.sum():6.1f}")
    fila = df_pp.iloc[1]
    print(f"  Primer ano, composicion del stock: S1 {fila.prov_S1:.1f}, S2 {fila.prov_S2:.1f}, S3 {fila.prov_S3:.1f}")


if __name__ == "__main__":
    main()


def sensibilidad():
    """Mueve un supuesto cada vez y mide la perdida acumulada de consumo en el adverso."""
    import copy
    original = copy.deepcopy(CARTERAS["consumo"])
    base_df, e = proyectar("consumo", "adverso")
    ref = base_df.deterioro.sum() / e
    print(f"\n===== Sensibilidad (consumo, adverso; referencia {ref:.2%}) =====")
    pruebas = [
        ("LGD 5 puntos menos", "lgd", lambda f: (lambda p, g: f(p, g) - 0.05)),
        ("LGD 5 puntos mas", "lgd", lambda f: (lambda p, g: f(p, g) + 0.05)),
        ("coef. del paro x0,8", "satelite", lambda s: (s[0], s[1] * 0.8, s[2])),
        ("coef. del paro x1,2", "satelite", lambda s: (s[0], s[1] * 1.2, s[2])),
        ("paso a S2 = 1,0 x PD", "m_s1_s2", lambda v: 1.0),
        ("paso a S2 = 2,0 x PD", "m_s1_s2", lambda v: 2.0),
        ("PD de S2 = 2 x PD S1", "m_s2_s3", lambda v: 2.0),
        ("PD de S2 = 4 x PD S1", "m_s2_s3", lambda v: 4.0),
        ("cura de S2 del 10 %", "cura_s2", lambda v: 0.10),
        ("cura de S2 del 30 %", "cura_s2", lambda v: 0.30),
        ("vida residual 2 anos", "vida", lambda v: 2),
        ("vida residual 4 anos", "vida", lambda v: 4),
    ]
    for nombre, clave, cambio in pruebas:
        CARTERAS["consumo"] = copy.deepcopy(original)
        CARTERAS["consumo"][clave] = cambio(original[clave])
        df, e = proyectar("consumo", "adverso")
        v = df.deterioro.sum() / e
        print(f"  {nombre:24} {v:7.2%}  ({(v - ref) * 100:+6.2f} pp)")
    CARTERAS["consumo"] = original


if __name__ == "__main__":
    sensibilidad()
