"""Anexo S2: migracion entre stages y provisiones con las formulas prescritas de la EBA.

Aplica literalmente los recuadros 3 a 9 de la nota metodologica de 2027 (borrador del
11-jun-2026) a la cartera de consumo de la filial mexicana del hilo conductor (anexo S0):

  Prov S1-S1(t+1) = Exp S1(t) * (1 - TR12(t+1) - PD1(t+1)) * PD1(t+2) * LGD1(t+2)
  Prov S2-S1(t+1) = Exp S2(t) * TR21(t+1) * PD1(t+2) * LGD1(t+2)
  Prov S1-S2(t+1) = Exp S1(t) * TR12(t+1) * LRLT S2(t+1)
  Prov S2-S2(t+1) = Exp S2(t) * (1 - TR21(t+1) - PD2(t+1)) * LRLT S2(t+1)
  Prov S1-S3(t+1) = Exp S1(t) * PD1(t+1) * LGD1(t+1)        (acumuladas, sin liberacion)
  Prov S2-S3(t+1) = Exp S2(t) * PD2(t+1) * LGD2(t+1)
  Prov Old S3     = MAX{Exp S3(0) * LGD S3(1); Prov S3(0)}

En el ultimo ano, los parametros "del ano siguiente" del adverso ponderan 5/6 el adverso y
1/6 el base (reversion lineal en seis anos); en el base quedan planos. LRLT S2 se calcula con
prevision perfecta sobre la vida residual, con la misma reversion tras el horizonte.

Los anos se numeran 1, 2 y 3: el escenario es el de la JERS para Mexico del ejercicio 2025,
y las formulas, las del borrador de 2027.
"""
import numpy as np

PARO_0 = 3.0
ESC = {
    "base":    {"pib": [1.3, 2.0, 2.3],   "paro": [3.3, 3.4, 3.5]},
    "adverso": {"pib": [-4.7, -2.2, -0.1], "paro": [5.2, 7.6, 8.8]},
}
SATELITE = (-3.514, 0.215, -0.0802)      # anexo S1: logit PD = a + b*paro(t-1) + c*PIB(t)
STOCK0 = {"S1": 880.0, "S2": 70.0, "S3": 50.0}
M12, M2, TR21, VIDA = 1.5, 3.0, 0.20, 3    # TR12 = M12*PD1; PD2 = M2*PD1; cura S2->S1; vida residual
EXTRA = 12                                 # anos de sendas tras el horizonte


def logistica(z):
    return 1 / (1 + np.exp(-z))


def lgd(paro):
    return min(0.85, 0.70 + 0.01 * (paro - 3.5))


def sendas(esc):
    """PD1 y LGD para t = 0 (partida), 1-3 (horizonte) y 4.. (tras el horizonte)."""
    a, b, c = SATELITE
    paro_prev = [PARO_0] + ESC[esc]["paro"][:-1]
    pd = [logistica(a + b * PARO_0 + c * ESC["base"]["pib"][0])]
    pd += [logistica(a + b * pp + c * g) for pp, g in zip(paro_prev, ESC[esc]["pib"])]
    lg = [lgd(ESC["base"]["paro"][0])] + [lgd(p) for p in ESC[esc]["paro"]]
    return pd, lg


PD_B, LGD_B = sendas("base")


def extender(pd, lg, esc):
    """Tras el ano 3: base plano; adverso revierte linealmente en 6 anos al base del ano 3."""
    pd, lg = list(pd), list(lg)
    for k in range(1, EXTRA + 1):
        if esc == "adverso":
            w = max(0.0, 1 - k / 6)
            pd.append(PD_B[3] + (pd[3] - PD_B[3]) * w)
            lg.append(LGD_B[3] + (lg[3] - LGD_B[3]) * w)
        else:
            pd.append(pd[3])
            lg.append(lg[3])
    return pd, lg


def lrlt_s2(pd, lg, t, prevision_perfecta=True):
    """Perdida a vida de S2 medida al final del ano t (vida residual VIDA)."""
    sup, perd = 1.0, 0.0
    for j in range(1, VIDA + 1):
        k = t + j if prevision_perfecta else t + 1
        p2 = min(0.6, M2 * pd[k])
        perd += sup * p2 * lg[k]
        sup *= 1 - p2
    return perd


def proyectar(esc, m12=M12, prevision_perfecta=True, reversion_5_6=True, lgd_s3_vieja=None):
    pd, lg = extender(*sendas(esc), esc)
    # parametro "del ano siguiente" en el ano 3: la nota pondera 5/6 adverso y 1/6 base
    def el_sig(t):
        if t + 1 <= 3 or esc == "base":
            return pd[t + 1] * lg[t + 1]
        if reversion_5_6:
            return 5 / 6 * pd[3] * lg[3] + 1 / 6 * PD_B[3] * LGD_B[3]
        return pd[3] * lg[3]

    s1, s2 = STOCK0["S1"], STOCK0["S2"]
    s3_viejo = STOCK0["S3"]
    # partida: se provisiona con el escenario interno del banco (aqui, el base), igual en los dos
    prov_s3_0 = s3_viejo * LGD_B[0]
    prov0 = (s1 * PD_B[1] * LGD_B[1]
             + s2 * lrlt_s2(*extender(PD_B, LGD_B, "base"), 0)
             + prov_s3_0)
    lgd_s3_1 = lg[1] if lgd_s3_vieja is None else lgd_s3_vieja
    prov_viejo = max(s3_viejo * lgd_s3_1, prov_s3_0)            # recuadro 9
    cum_nuevo_s3, prov_cum_s3 = 0.0, 0.0
    filas, prov_ant = [], prov0
    for t in range(0, 3):                                         # de t a t+1
        p1, p2 = pd[t + 1], min(0.6, M2 * pd[t + 1])
        tr12 = m12 * p1
        flujo_13, flujo_23 = s1 * p1, s2 * p2
        flujo_12, flujo_21 = s1 * tr12, s2 * TR21
        prov_13 = flujo_13 * lg[t + 1]
        prov_23 = flujo_23 * lg[t + 1]
        lrlt = lrlt_s2(pd, lg, t + 1, prevision_perfecta)
        prov_11 = s1 * (1 - tr12 - p1) * el_sig(t + 1)
        prov_21 = flujo_21 * el_sig(t + 1)
        prov_12 = flujo_12 * lrlt
        prov_22 = s2 * (1 - TR21 - p2) * lrlt
        s1, s2 = s1 - flujo_13 - flujo_12 + flujo_21, s2 + flujo_12 - flujo_23 - flujo_21
        cum_nuevo_s3 += flujo_13 + flujo_23
        prov_cum_s3 += prov_13 + prov_23
        stock = {"S1": prov_11 + prov_21, "S2": prov_12 + prov_22, "S3": prov_cum_s3 + prov_viejo}
        total = sum(stock.values())
        filas.append({"ano": t + 1, "S1": s1, "S2": s2, "S3": s3_viejo + cum_nuevo_s3,
                      "prov": total, "deterioro": total - prov_ant, "pd1": p1, "lrlt": lrlt,
                      **{f"prov_{k}": v for k, v in stock.items()}})
        prov_ant = total
    return prov0, filas


def resumen(etiqueta, filas, exp=1000.0):
    det = [f["deterioro"] for f in filas]
    print(f"  {etiqueta:44} " + " / ".join(f"{d:6.1f}" for d in det)
          + f"   total {sum(det):6.1f} ({sum(det) / exp:.2%})  primer ano {det[0] / sum(det):.0%}"
          + f"  S2 final {filas[-1]['S2']:5.1f}  S3 final {filas[-1]['S3'] / exp:.1%}")
    return sum(det)


def main():
    print("Parametros (PD12M S1 y LGD) por ano, 0 = partida:")
    for esc in ESC:
        pd, lg = sendas(esc)
        print(f"  {esc:8} PD1 " + " ".join(f"{p:6.2%}" for p in pd) + "   LGD " + " ".join(f"{x:5.1%}" for x in lg))

    print("\nDeterioro por ano, anos 1 / 2 / 3 (millones de EUR; exposicion 1.000):")
    tot = {}
    for esc in ESC:
        prov0, filas = proyectar(esc)
        tot[esc] = resumen(f"{esc}, formulas EBA", filas)
    print(f"  Adverso menos base: {(tot['adverso'] - tot['base']) / 10:.2f} pp de la exposicion")
    print(f"  Stock de provisiones de partida: {prov0:.1f}")

    print("\nPrevision perfecta (adverso):")
    _, con = proyectar("adverso")
    _, sin = proyectar("adverso", prevision_perfecta=False)
    a = resumen("con prevision perfecta", con)
    b = resumen("sin ella (PD del ano siguiente, plana)", sin)
    print(f"  LRLT S2 al final del ano 1: {con[0]['lrlt']:.2%} con, {sin[0]['lrlt']:.2%} sin")
    print(f"  El primer ano pasa de {sin[0]['deterioro']:.1f} a {con[0]['deterioro']:.1f} "
          f"(+{con[0]['deterioro'] - sin[0]['deterioro']:.1f}); el total cambia {a - b:+.1f}")

    print("\nReversion 5/6 - 1/6 en el ultimo ano (adverso):")
    _, sin_rev = proyectar("adverso", reversion_5_6=False)
    print(f"  Stock de S1 al final del ano 3: {con[2]['prov_S1']:.2f} con la ponderacion, "
          f"{sin_rev[2]['prov_S1']:.2f} con el adverso plano")

    print("\nSICR sin backstop: dos bancos con distinto criterio (adverso):")
    for m in (1.0, 1.5, 2.5):
        _, f = proyectar("adverso", m12=m)
        _, fb = proyectar("base", m12=m)
        resumen(f"TR12 = {m:.1f} x PD1", f)
        print(f"      S2 al final del ano 1: {f[0]['S2']:.1f} (partida 70,0); "
              f"adverso menos base {(sum(x['deterioro'] for x in f) - sum(x['deterioro'] for x in fb)) / 10:.2f} pp")

    print("\nSuelo del S3 antiguo (recuadro 9):")
    for lgd_v in (0.65, 0.70, 0.80):
        _, f = proyectar("adverso", lgd_s3_vieja=lgd_v)
        print(f"  LGD S3 del ano 1 {lgd_v:.0%}: provision del S3 antiguo "
              f"{max(STOCK0['S3'] * lgd_v, STOCK0['S3'] * LGD_B[0]):.1f} (partida {STOCK0['S3'] * LGD_B[0]:.1f})")


if __name__ == "__main__":
    main()
