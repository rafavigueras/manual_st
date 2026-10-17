"""Anexo S1, segunda parte: proyeccion del satelite bajo el escenario JERS y contraste.

1. Proyecta la PD de consumo con el satelite estimado en la primera parte (s1a_satelite.py)
   bajo el base y el adverso de la JERS de 2025 para Mexico y para Espana. Para Espana se
   recalibra solo la constante, de modo que la PD de partida sea la de una cartera espanola
   de consumo tipica (supuesto: 3,0 %); las elasticidades son las mismas.
2. Contrasta la respuesta del satelite con la de un "benchmark" ilustrativo. Los benchmarks
   del BCE no son publicos: aqui el benchmark es otro satelite, mas sensible al paro, con la
   misma PD de partida. Lo que se compara es lo que compara el supervisor: el aumento de la
   PD del adverso sobre el base.
3. LGD hipotecaria bajo escenario: efecto de la caida acumulada de la vivienda (Espana,
   -17,2 % nominal en el adverso de 2025) segun el LTV, con prevision perfecta.
"""
import numpy as np

A, B, C = -3.514, 0.215, -0.0802          # s1a_satelite.py: logit PD = a + b*paro(t-1) + c*PIB(t)

ESC = {  # escenario JERS 2025, tablas 4.1.1 y 4.1.2
    "Mexico": {"paro0": 3.0,
               "base": {"pib": [1.3, 2.0, 2.3], "paro": [3.3, 3.4, 3.5]},
               "adverso": {"pib": [-4.7, -2.2, -0.1], "paro": [5.2, 7.6, 8.8]}},
    "Espana": {"paro0": 11.5,
               "base": {"pib": [2.5, 1.9, 1.7], "paro": [10.8, 10.4, 9.9]},
               "adverso": {"pib": [-2.5, -3.5, 2.0], "paro": [14.1, 16.8, 15.6]}},
}


def logit(p):
    return np.log(p / (1 - p))


def logistica(z):
    return 1 / (1 + np.exp(-z))


def senda(pais, esc, a=A, b=B, c=C):
    e = ESC[pais]
    paro_prev = [e["paro0"]] + e[esc]["paro"][:-1]
    return [logistica(a + b * pp + c * g) for pp, g in zip(paro_prev, e[esc]["pib"])]


def constante_para(pais, pd0, b=B, c=C):
    e = ESC[pais]
    return logit(pd0) - b * e["paro0"] - c * e["base"]["pib"][0]


def imprimir(pais, a, b=B, c=C, etiqueta="satelite"):
    pd0 = logistica(a + b * ESC[pais]["paro0"] + c * ESC[pais]["base"]["pib"][0])
    base, adv = senda(pais, "base", a, b, c), senda(pais, "adverso", a, b, c)
    inc = [x - y for x, y in zip(adv, base)]
    print(f"  {pais:7} {etiqueta:10} partida {pd0:6.2%} | base " + " ".join(f"{x:6.2%}" for x in base)
          + " | adverso " + " ".join(f"{x:6.2%}" for x in adv)
          + " | adv-base " + " ".join(f"{x * 100:5.2f}" for x in inc) + " pp"
          + f" | multiplicador ano 3 {adv[2] / pd0:.2f}x")
    return inc


def main():
    print("1. Proyeccion de la PD de consumo")
    imprimir("Mexico", A)
    a_es = constante_para("Espana", 0.030)
    print(f"  (constante recalibrada para Espana: {a_es:.3f})")
    imprimir("Espana", a_es)

    print("\n2. Contraste con un benchmark ilustrativo (mas sensible al paro)")
    b_bm, c_bm = 0.30, -0.10
    inc_sat = imprimir("Mexico", A, etiqueta="satelite")
    pd0_mx = logistica(A + B * 3.0 + C * 1.3)
    a_bm = constante_para("Mexico", pd0_mx, b_bm, c_bm)
    inc_bm = imprimir("Mexico", a_bm, b_bm, c_bm, etiqueta="benchmark")
    print(f"  Sensibilidad relativa (suma de aumentos adv-base): satelite / benchmark = "
          f"{sum(inc_sat) / sum(inc_bm):.2f}")
    for k in (0.5, 0.75):
        print(f"  Mezcla {k:.0%} satelite / {1 - k:.0%} benchmark, PD adversa ano 3: "
              f"{k * senda('Mexico', 'adverso')[2] + (1 - k) * senda('Mexico', 'adverso', a_bm, b_bm, c_bm)[2]:.2%}")

    print("\n3. LGD hipotecaria de un S3 con la caida de la vivienda (Espana, adverso 2025: -17,2 %)")
    descuento, costes, cura = 0.20, 0.05, 0.30     # venta forzosa, costes de ejecucion, cura implicita
    for ltv in (0.60, 0.80, 0.95):
        out = []
        for caida in (0.0, -0.172):
            garantia = (1 + caida) * (1 - descuento) / ltv          # valor recuperable por euro de deuda
            perdida_ejec = max(0.0, 1 - garantia) + costes
            out.append((1 - cura) * perdida_ejec + cura * 0.05)       # los que se curan pierden 5 %
        print(f"  LTV {ltv:.0%}: LGD sin caida {out[0]:.1%}, con la caida del adverso {out[1]:.1%} "
              f"(+{(out[1] - out[0]) * 100:.1f} pp)")


if __name__ == "__main__":
    main()
