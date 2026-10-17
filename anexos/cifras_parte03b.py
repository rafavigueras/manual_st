"""Cifras de los ejemplos NUMEROS de los capitulos 22 a 27 (Parte III, bloque B).

Reutiliza los datos sinteticos del anexo S1 (s1a_satelite.py, veinte anos trimestrales con
dos recesiones y una pequena no linealidad en recesion) para tres experimentos:
  - cap. 22: ventana corta sin recesiones y un periodo atipico tipo pandemia (el PIB se
    desploma y los impagos no suben, por moratorias y avales);
  - cap. 23: especificacion no lineal frente a lineal en el punto adverso;
  - cap. 26: choque de valor anadido sectorial con el mismo satelite.
"""
import contextlib
import io
import runpy
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

AQUI = Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(str(AQUI / "s1a_satelite.py"))
df = g["df"].copy()
df["logit_td"] = np.log(df.td / (1 - df.td))
df["rec"] = np.maximum(0, -df.pib)


def ajusta(d, cols):
    return sm.OLS(d.logit_td, sm.add_constant(d[cols])).fit()


def tasa(m, paro, pib):
    z = m.params["const"] + m.params["paro_l1"] * paro + m.params["pib"] * pib
    if "rec" in m.params:
        z += m.params["rec"] * max(0.0, -pib)
    return 1 / (1 + np.exp(-z))


print("== Cap. 22: ventanas y periodos atipicos ==")
completo = ajusta(df, ["paro_l1", "pib"])
corta = ajusta(df.iloc[40:56], ["paro_l1", "pib"])          # 4 anos sin recesion
print(f"  20 anos: paro {completo.params['paro_l1']:.3f}, PIB {completo.params['pib']:.4f}")
print(f"  ventana de 4 anos sin recesion: paro {corta.params['paro_l1']:.3f} (error {corta.bse['paro_l1']:.3f}), "
      f"PIB {corta.params['pib']:.4f} (error {corta.bse['pib']:.4f}); "
      f"paro de la ventana {df.paro_l1.iloc[40:56].min():.1f}-{df.paro_l1.iloc[40:56].max():.1f} %; "
      f"punto adverso {tasa(corta, 8.8, -4.7):.2%} frente a {tasa(completo, 8.8, -4.7):.2%}")
# periodo tipo pandemia: 6 trimestres con PIB -10 a -3 % y tasa de impago plana (moratorias)
pand = df.tail(6).copy()
pand["pib"] = [-3.0, -10.0, -8.0, -5.0, -3.0, 1.0]
pand["paro_l1"] = df.paro_l1.iloc[-1] + np.array([0.0, 0.3, 0.8, 1.0, 0.9, 0.7])
pand["logit_td"] = df.logit_td.iloc[-1]
pand["rec"] = np.maximum(0, -pand.pib)
d2 = pd.concat([df, pand], ignore_index=True)
d2["pand"] = [0] * len(df) + [1] * len(pand)
sin_tratar = ajusta(d2, ["paro_l1", "pib"])
con_dummy = ajusta(d2, ["paro_l1", "pib", "pand"])
excluido = ajusta(d2[d2.pand == 0], ["paro_l1", "pib"])
for nombre, m in (("pandemia sin tratar", sin_tratar), ("con variable ficticia", con_dummy),
                  ("excluyendo esos trimestres", excluido)):
    print(f"  {nombre:28} paro {m.params['paro_l1']:.3f}, PIB {m.params['pib']:.4f}; "
          f"tasa en el punto adverso {tasa(m, 8.8, -4.7):.2%}")

print("\n== Cap. 23: no linealidad ==")
lineal = completo
no_lineal = ajusta(df, ["paro_l1", "pib", "rec"])
print(f"  termino de recesion estimado: {no_lineal.params['rec']:.4f} (error {no_lineal.bse['rec']:.4f})")
for nombre, m in (("lineal", lineal), ("no lineal", no_lineal)):
    print(f"  {nombre:10} punto adverso (paro 8,8, PIB -4,7): {tasa(m, 8.8, -4.7):.2%}; "
          f"punto extremo (paro 10,5, PIB -8): {tasa(m, 10.5, -8.0):.2%}")
print(f"  rango de la muestra: paro {df.paro_l1.min():.1f}-{df.paro_l1.max():.1f} %, "
      f"PIB {df.pib.min():.1f} a {df.pib.max():.1f} %")

print("\n== Cap. 26: choque de valor anadido sectorial (ilustrativo) ==")
pd0 = 0.02
for choque in (-3.0, -8.0, -15.0):
    z = np.log(pd0 / (1 - pd0)) + completo.params["pib"] * choque
    print(f"  VAB {choque:+.0f} pp frente al base: PD {pd0:.2%} -> {1 / (1 + np.exp(-z)):.2%}")

print("\n== Cap. 27: un modelo por tramos (como un arbol) no extrapola ==")
q_paro = pd.qcut(df.paro_l1, 4, labels=False)
q_pib = pd.qcut(df.pib, 4, labels=False)
celda = df.groupby([q_paro, q_pib]).td.mean()
extremo = celda.loc[(3, 0)]
print(f"  4x4 tramos de paro y PIB; tasa media en el tramo mas adverso (paro alto, PIB bajo): {extremo:.2%}")
print(f"  maxima tasa observada en la muestra: {df.td.max():.2%}")
for paro_v, pib_v in ((8.8, -4.7), (10.5, -8.0)):
    print(f"  punto paro {paro_v}, PIB {pib_v}: modelo por tramos {extremo:.2%} (cae en el tramo extremo); "
          f"logit lineal {tasa(completo, paro_v, pib_v):.2%}")
