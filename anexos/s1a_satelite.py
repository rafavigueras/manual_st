"""Anexo S1, primera parte: un modelo satelite estimado sobre datos sinteticos.

Genera veinte anos de datos trimestrales de una cartera de consumo mexicana
(tasa de default observada, paro y crecimiento del PIB), estima un satelite
sobre el logit de la tasa y muestra como se lee: coeficientes, ajuste,
elasticidades y que pasa si se olvida un retardo.

Los datos son sinteticos: el "modelo verdadero" esta escrito abajo y sirve
para comprobar que la estimacion lo recupera.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm

rng = np.random.default_rng(2026)

# ------------------------------------------------------------------
# 1. Historia macro sintetica: 80 trimestres (20 anos) con dos recesiones
# ------------------------------------------------------------------
T = 80
pib = np.full(T, 2.4)           # crecimiento interanual del PIB, %
pib += rng.normal(0, 0.8, T)
pib[28:34] -= np.array([2.0, 4.5, 6.5, 6.0, 4.0, 1.5])     # recesion 1 (anos 8-9)
pib[60:64] -= np.array([3.0, 9.0, 6.0, 2.0])               # recesion 2 (anos 15-16)

paro = np.empty(T)
paro[0] = 4.0
for t in range(1, T):
    # el paro sube cuando el PIB crece por debajo de ~2,5 % (ley de Okun simplificada)
    paro[t] = paro[t - 1] + 0.12 * (2.5 - pib[t]) * 0.5 - 0.04 * (paro[t - 1] - 4.0)
paro += rng.normal(0, 0.08, T)

# ------------------------------------------------------------------
# 2. Modelo verdadero de la tasa de default anual (en logit)
#    logit(TD_t) = a + b * paro_{t-1} + c * pib_t + ruido
# ------------------------------------------------------------------
#    En recesion la tasa responde mas: termino extra d * max(0, -PIB)
a_true, b_true, c_true, d_true = -3.60, 0.22, -0.06, 0.05
paro_l1 = np.r_[paro[0], paro[:-1]]
logit_td = (a_true + b_true * paro_l1 + c_true * pib + d_true * np.maximum(0, -pib)
            + rng.normal(0, 0.06, T))
td = 1 / (1 + np.exp(-logit_td))

df = pd.DataFrame({"pib": pib, "paro": paro, "paro_l1": paro_l1, "td": td})
df["logit_td"] = np.log(df.td / (1 - df.td))
df = df.iloc[1:]   # se pierde el primer trimestre por el retardo

print("Resumen de los datos sinteticos (80 trimestres)")
print(df[["pib", "paro", "td"]].describe().loc[["mean", "min", "max"]].round(3).to_string())

# ------------------------------------------------------------------
# 3. Estimacion: MCO sobre el logit de la tasa
# ------------------------------------------------------------------
X = sm.add_constant(df[["paro_l1", "pib"]])
modelo = sm.OLS(df.logit_td, X).fit(cov_type="HAC", cov_kwds={"maxlags": 4})
print("\nSatelite estimado: logit(TD) = a + b*paro(t-1) + c*PIB(t)")
print(modelo.summary2().tables[1][["Coef.", "Std.Err.", "P>|z|"]].round(4).to_string())
print(f"R2 = {modelo.rsquared:.3f}   (verdadero: a={a_true}, b={b_true}, c={c_true})")

# ------------------------------------------------------------------
# 4. Como se lee: efecto de un punto de paro sobre la tasa
# ------------------------------------------------------------------
a, b, c = modelo.params
def tasa(paro_val, pib_val):
    z = a + b * paro_val + c * pib_val
    return 1 / (1 + np.exp(-z))

for paro_ref in (3.5, 8.0):
    t0 = tasa(paro_ref, 2.0)
    t1 = tasa(paro_ref + 1, 2.0)
    print(f"Con paro {paro_ref:.1f} %: TD {t0:.2%} -> {t1:.2%} si el paro sube 1 punto "
          f"(+{(t1 - t0) * 100:.2f} pp, +{t1 / t0 - 1:.0%})")

# ------------------------------------------------------------------
# 5. Lo que sale mal: olvidar el retardo del paro
# ------------------------------------------------------------------
X2 = sm.add_constant(df[["paro", "pib"]])
m2 = sm.OLS(df.logit_td, X2).fit()
print("\nSin retardo (paro contemporaneo):")
print(m2.params.round(4).to_string(), f"\nR2 = {m2.rsquared:.3f}")

# ------------------------------------------------------------------
# 6. Lo que sale mal: estimar solo con anos buenos (sin recesiones)
# ------------------------------------------------------------------
buenos = df.drop(index=list(range(28, 38)) + list(range(60, 68)), errors="ignore")
m3 = sm.OLS(buenos.logit_td, sm.add_constant(buenos[["paro_l1", "pib"]])).fit(
    cov_type="HAC", cov_kwds={"maxlags": 4})
print("\nSolo trimestres sin recesion:")
print(pd.DataFrame({"coef": m3.params, "error": m3.bse}).round(4).to_string(), f"\nR2 = {m3.rsquared:.3f}")
print(f"Rango de paro en esa muestra: {buenos.paro_l1.min():.1f} % - {buenos.paro_l1.max():.1f} %")

# Proyeccion en un punto adverso: paro 8,8 % (retardado) y PIB -4,7 %
def pred(params, paro_v, pib_v, d=0.0):
    z = params.iloc[0] + params.iloc[1] * paro_v + params.iloc[2] * pib_v + d * max(0, -pib_v)
    return 1 / (1 + np.exp(-z))
verdad = pred(pd.Series([a_true, b_true, c_true]), 8.8, -4.7, d_true)
print(f"\nTasa en un punto adverso (paro 8,8 %, PIB -4,7 %):")
print(f"  modelo verdadero          {verdad:.2%}")
print(f"  satelite con recesiones   {pred(modelo.params, 8.8, -4.7):.2%}")
print(f"  satelite sin recesiones   {pred(m3.params, 8.8, -4.7):.2%}")

print("\nCoeficientes para el anexo S0:", {k: round(v, 4) for k, v in modelo.params.items()})

# ------------------------------------------------------------------
# 7. Validacion: backtest fuera de muestra
#    Se estima con los 15 primeros anos y se proyecta los 5 ultimos,
#    que contienen la segunda recesion, con la macro observada.
# ------------------------------------------------------------------
corte = 60
ent = df.loc[:corte - 1]
pru = df.loc[corte:]
m_ent = sm.OLS(ent.logit_td, sm.add_constant(ent[["paro_l1", "pib"]])).fit()
pred_pru = 1 / (1 + np.exp(-(m_ent.params["const"] + m_ent.params["paro_l1"] * pru.paro_l1
                             + m_ent.params["pib"] * pru.pib)))
err = pred_pru - pru.td
print("\nBacktest fuera de muestra (estimado con anos 1-15, proyectado en anos 16-20):")
print(f"  coeficientes estimados: " + ", ".join(f"{k} {v:.4f}" for k, v in m_ent.params.items()))
print(f"  error medio {err.mean() * 100:+.2f} pp; error absoluto medio {err.abs().mean() * 100:.2f} pp")
pico = pru.td.idxmax()
print(f"  en el pico de la recesion: observado {pru.td[pico]:.2%}, proyectado {pred_pru[pico]:.2%}")

# ------------------------------------------------------------------
# 8. Validacion: estabilidad de los coeficientes por ventanas
# ------------------------------------------------------------------
print("\nEstabilidad: coeficiente del paro con ventanas moviles de 10 anos")
for ini in (1, 21, 41):
    v = df.loc[ini:ini + 39]
    mv = sm.OLS(v.logit_td, sm.add_constant(v[["paro_l1", "pib"]])).fit()
    print(f"  trimestres {ini:2d}-{ini + 39:2d}: paro {mv.params['paro_l1']:.3f}, PIB {mv.params['pib']:.3f}")

# ------------------------------------------------------------------
# 9. Validacion: sensibilidad a choques de una desviacion tipica
# ------------------------------------------------------------------
base_paro, base_pib = df.paro_l1.mean(), df.pib.mean()
t0 = tasa(base_paro, base_pib)
print(f"\nSensibilidad en la media (TD {t0:.2%}):")
for nombre, dp, dg in (("paro +1 desv. tipica", df.paro_l1.std(), 0), ("PIB -1 desv. tipica", 0, -df.pib.std())):
    t1 = tasa(base_paro + dp, base_pib + dg)
    print(f"  {nombre:22} ({dp:+.2f} / {dg:+.2f}): TD {t1:.2%} ({(t1 - t0) * 100:+.2f} pp)")
