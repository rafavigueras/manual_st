"""Cifras de los ejemplos NUMEROS de los capitulos 2, 3 y 4 (Parte I).

Cada bloque reproduce un ejemplo del texto. Si cambia una cifra aqui, cambia en el texto.
"""
import numpy as np

print("== Cap. 2: un banco de 100.000 M EUR y 1.000 M EUR de perdidas ==")
activo, rwa, cet1 = 100_000, 35_000, 4_550
print(f"Partida: CET1 {cet1:,} / RWA {rwa:,} = {cet1 / rwa:.2%}")
perdida = 1_000
neta = perdida * (1 - 0.30)
cet1_b = cet1 - neta
print(f"Perdida antes de impuestos {perdida:,}, despues de impuestos (30 %) {neta:,.0f}")
print(f"Solo numerador: {cet1_b:,.0f} / {rwa:,} = {cet1_b / rwa:.2%} ({(cet1 / rwa - cet1_b / rwa) * 1e4:.0f} pb)")
rwa_b = rwa * 1.05
print(f"Y si los RWA suben un 5 %: {cet1_b:,.0f} / {rwa_b:,.0f} = {cet1_b / rwa_b:.2%} "
      f"({(cet1 / rwa - cet1_b / rwa_b) * 1e4:.0f} pb en total, "
      f"{(cet1_b / rwa - cet1_b / rwa_b) * 1e4:.0f} pb de denominador)")
print(f"Regla rapida: 100 M EUR de perdida antes de impuestos = {100 * 0.7 / rwa * 1e4:.0f} pb de CET1 en este banco")

print("\n== Cap. 3: matriz de transicion de tres estados ==")
M = np.array([[0.94, 0.05, 0.01],
              [0.20, 0.70, 0.10],
              [0.00, 0.00, 1.00]])
x0 = np.array([900.0, 80.0, 20.0])
x = x0.copy()
for t in range(1, 4):
    x = x @ M
    print(f"Ano {t}: S1 {x[0]:7.1f}  S2 {x[1]:6.1f}  S3 {x[2]:6.1f}")
# misma matriz con PD de S1 y S2 al doble (escenario adverso estilizado)
M2 = M.copy()
M2[0] = [0.88, 0.10, 0.02]
M2[1] = [0.15, 0.65, 0.20]
x = x0.copy()
for t in range(1, 4):
    x = x @ M2
print(f"Con transiciones de estres, tras 3 anos: S1 {x[0]:.1f}  S2 {x[1]:.1f}  S3 {x[2]:.1f}")

print("\n== Cap. 4: 1.000 M EUR que pasan de stage 1 a stage 2 ==")
exp_, pd_anual, lgd, vida = 1_000, 0.03, 0.45, 5
ecl12 = exp_ * pd_anual * lgd
pd_vida = 1 - (1 - pd_anual) ** vida
eclv = exp_ * pd_vida * lgd
print(f"PD a 12 meses {pd_anual:.1%}; PD a vida ({vida} anos) {pd_vida:.2%}; LGD {lgd:.0%}")
print(f"Provision en stage 1: {ecl12:.1f} M EUR;  en stage 2: {eclv:.1f} M EUR;  "
      f"salto x{eclv / ecl12:.1f} (+{eclv - ecl12:.1f} M EUR)")
pd_estres = 0.06
eclv_e = exp_ * (1 - (1 - pd_estres) ** vida) * lgd
print(f"Si ademas la PD anual pasa al {pd_estres:.0%}: stage 2 = {eclv_e:.1f} M EUR "
      f"(x{eclv_e / ecl12:.1f} sobre la provision de partida)")

print("\n== Cap. 3: de TTC a PiT con el desplazamiento de Vasicek ==")
from scipy.stats import norm
pd_ttc, rho = 0.02, 0.15
print(f"PD TTC {pd_ttc:.2%}, correlacion {rho}")
for z in (1.0, 0.0, -1.0, -2.0):
    pd_pit = norm.cdf((norm.ppf(pd_ttc) - np.sqrt(rho) * z) / np.sqrt(1 - rho))
    print(f"  factor sistematico Z = {z:+.1f}: PD PiT = {pd_pit:.2%}")
# factor implicito en una tasa observada
for tasa in (0.012, 0.035):
    z = (norm.ppf(pd_ttc) - np.sqrt(1 - rho) * norm.ppf(tasa)) / np.sqrt(rho)
    print(f"  una tasa observada del {tasa:.1%} implica Z = {z:+.2f}")

print("\n== Cap. 3: anual frente a trimestral ==")
q = 0.012
print(f"PD trimestral {q:.1%} -> anual 1-(1-q)^4 = {1 - (1 - q) ** 4:.3%} (no 4q = {4 * q:.1%})")
a = 0.10
print(f"PD anual {a:.0%} -> trimestral 1-(1-a)^(1/4) = {1 - (1 - a) ** 0.25:.3%} (no a/4 = {a / 4:.2%})")

print("\n== Cap. 4: estructura temporal y prevision perfecta ==")
expo, lgd = 1_000, 0.45
sendas = {
    "PD plana del 3 %":              [0.03] * 5,
    "adverso conocido (3,6,8,6,4 %)": [0.03, 0.06, 0.08, 0.06, 0.04],
}
for nombre, pds in sendas.items():
    sup = 1.0
    marg = []
    for p in pds:
        marg.append(sup * p)
        sup *= 1 - p
    print(f"  {nombre:32} PD marginales: " + " ".join(f"{m:.2%}" for m in marg)
          + f"  -> PD a vida {1 - sup:.2%}, provision stage 2 {expo * (1 - sup) * lgd:.1f}")
