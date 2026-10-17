"""Anexo S6: la misma cartera en tres ejercicios, y el puente entre ellos.

La cartera de consumo de la filial mexicana del hilo conductor (1.000 M EUR: 880 / 70 / 50)
se proyecta tres veces con la misma maquinaria (satelite del anexo S1, formulas de provisiones
del anexo S2) y supuestos distintos:

  1. Europeo (EBA): adverso JERS (k = 1), balance estatico, sin acciones de gestion.
  2. ICAAP: escenario propio mas severo (k = 1,15), balance dinamico: vence un 30 % de lo sano
     cada ano y se repone con produccion nueva mas selectiva (PD x 0,85), sin crecimiento.
  3. Local tipo supervisor mexicano: escenario del supervisor (k = 0,90), plan de negocio con
     crecimiento del 8 % anual de la cartera sana; misma admision que hoy.

k escala la desviacion del adverso sobre el base (paro y PIB). Todos los supuestos de los
ejercicios 2 y 3 son ilustrativos: los escenarios locales y los planes reales no son publicos.
El puente descompone la diferencia con el europeo en efecto escenario y efecto balance.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import s2_migracion as s2  # noqa: E402

BASE = {k: list(v) for k, v in s2.ESC["base"].items()}
ADV = {k: list(v) for k, v in s2.ESC["adverso"].items()}


def sendas_k(k):
    s2.ESC["adverso"] = {v: [b + k * (a - b) for a, b in zip(ADV[v], BASE[v])] for v in ADV}
    pd, lg = s2.extender(*s2.sendas("adverso"), "adverso")
    s2.ESC["adverso"] = {v: list(x) for v, x in ADV.items()}
    return pd, lg


def proyectar(k, vence=0.0, crece=0.0, m_nueva=1.0):
    """Perdida acumulada (deterioro de 3 anos) y exposicion media; formulas del anexo S2."""
    pd, lg = sendas_k(k)
    s1v, s1n, s2_ = s2.STOCK0["S1"], 0.0, s2.STOCK0["S2"]
    s3_viejo = s2.STOCK0["S3"]
    prov_s3_0 = s3_viejo * s2.LGD_B[0]
    prov_ant = (s1v * s2.PD_B[1] * s2.LGD_B[1]
                + s2_ * s2.lrlt_s2(*s2.extender(s2.PD_B, s2.LGD_B, "base"), 0) + prov_s3_0)
    prov_viejo = max(s3_viejo * lg[1], prov_s3_0)
    prov_cum_s3, det_total, expos = 0.0, 0.0, []
    for t in range(3):
        sig = lambda m: m * (pd[t + 2] * lg[t + 2] if t < 2 else  # noqa: E731
                             5 / 6 * pd[3] * lg[3] + 1 / 6 * s2.PD_B[3] * s2.LGD_B[3])
        nuevos = 0.0
        for cohorte, m in (("v", 1.0), ("n", m_nueva)):
            stock = s1v if cohorte == "v" else s1n
            p1 = m * pd[t + 1]
            f13, f12 = stock * p1, stock * s2.M12 * p1
            prov_cum_s3 += f13 * lg[t + 1]
            nuevos += f12
            if cohorte == "v":
                s1v = stock - f13 - f12
            else:
                s1n = stock - f13 - f12
        p2 = min(0.6, s2.M2 * pd[t + 1])
        f23, f21 = s2_ * p2, s2_ * s2.TR21
        prov_cum_s3 += f23 * lg[t + 1]
        s2_ = s2_ - f23 - f21 + nuevos
        s1v += f21
        # vencimientos y produccion nueva (balance dinamico)
        sano_ini = s1v + s1n + s2_
        s1v, s1n, s2_ = (x * (1 - vence) for x in (s1v, s1n, s2_))
        objetivo = (s2.STOCK0["S1"] + s2.STOCK0["S2"]) * (1 + crece) ** (t + 1)
        if vence > 0 or crece > 0:
            s1n += max(0.0, objetivo - (s1v + s1n + s2_)) if crece > 0 else sano_ini * vence
        prov = ((s1v * sig(1.0) + s1n * sig(m_nueva))
                + s2_ * s2.lrlt_s2(pd, lg, t + 1) + prov_cum_s3 + prov_viejo)
        det_total += prov - prov_ant
        prov_ant = prov
        expos.append(s1v + s1n + s2_)
    return det_total, sum(expos) / 3


CASOS = {
    "europeo": dict(k=1.00),
    "icaap": dict(k=1.15, vence=0.30, m_nueva=0.85),
    "local": dict(k=0.90, vence=0.30, crece=0.08),
}


def main():
    res = {}
    for nombre, kw in CASOS.items():
        det, media = proyectar(**kw)
        res[nombre] = det
        print(f"{nombre:8} deterioro 3 anos {det:6.1f} M EUR = {det / 1000:.2%} de la exposicion inicial; "
              f"exposicion sana media {media:6.1f}")
    print("\nPuente con el europeo (puntos de perdida sobre la exposicion inicial):")
    for nombre in ("icaap", "local"):
        kw = CASOS[nombre]
        solo_esc, _ = proyectar(k=kw["k"])
        e_esc = (solo_esc - res["europeo"]) / 10
        e_bal = (res[nombre] - solo_esc) / 10
        print(f"  {nombre:6}: europeo {res['europeo'] / 10:5.2f} + escenario {e_esc:+5.2f} + balance {e_bal:+5.2f}"
              f" = {res[nombre] / 10:5.2f}")


if __name__ == "__main__":
    main()
