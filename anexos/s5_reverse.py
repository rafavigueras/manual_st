"""Anexo S5: reverse stress test sobre la filial del hilo conductor.

Pregunta inversa: en lugar de "cuanto cae el CET1 con este escenario", "que escenario hace
caer el CET1 tanto". Usa el stress test de juguete del anexo S0 (filial mexicana, consumo y
empresas, margen dado) y dos herramientas:

1. Escalar el escenario: el adverso se escribe como base + k * (adverso - base) y se busca la
   k que produce la caida objetivo. k = 1 es el adverso de la JERS.
2. El escenario mas plausible: se mueven por separado el choque de paro y el de PIB, se
   trazan las combinaciones que producen la misma caida y se elige la que esta mas cerca del
   base en distancia de Mahalanobis (desviaciones tipicas y correlacion supuestas, ilustrativas).
"""
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import s0_juguete as s0  # noqa: E402

BASE = {k: list(v) for k, v in s0.ESC["base"].items()}
ADV = {k: list(v) for k, v in s0.ESC["adverso"].items()}


def caida_maxima(k_paro, k_pib):
    """Caida maxima de CET1 (pb) de la filial con el adverso escalado, margen adverso dado."""
    s0.ESC["adverso"] = {
        "paro": [b + k_paro * (a - b) for a, b in zip(ADV["paro"], BASE["paro"])],
        "pib": [b + k_pib * (a - b) for a, b in zip(ADV["pib"], BASE["pib"])],
    }
    tot = None
    for nombre in s0.CARTERAS:
        df, _ = s0.proyectar(nombre, "adverso")
        cols = df[["deterioro", "rwa", "margen"]]
        tot = cols if tot is None else tot + cols
    rwa0 = tot.rwa.iloc[0]
    cet1 = s0.CET1_INICIAL_SOBRE_RWA * rwa0
    ratios = [cet1 / rwa0]
    for t in (1, 2, 3):
        cet1 += (-tot.deterioro.iloc[t] + tot.margen.iloc[t]) * (1 - s0.TIPO_FISCAL)
        ratios.append(cet1 / max(tot.rwa.iloc[t], rwa0))
    s0.ESC["adverso"] = {k: list(v) for k, v in ADV.items()}
    return (ratios[0] - min(ratios)) * 1e4


def main():
    ref = caida_maxima(1.0, 1.0)
    print(f"Adverso JERS (k = 1): caida maxima {ref:.0f} pb")
    print("\n1. Escalar el escenario entero")
    for objetivo in (300, 600, 800):
        k = brentq(lambda x: caida_maxima(x, x) - objetivo, 0.0, 3.0)
        paro3 = BASE["paro"][2] + k * (ADV["paro"][2] - BASE["paro"][2])
        pib1 = BASE["pib"][0] + k * (ADV["pib"][0] - BASE["pib"][0])
        print(f"  Caida de {objetivo} pb: k = {k:.2f} (paro del ano 3 {paro3:.1f} %, PIB del ano 1 {pib1:.1f} %)")

    print("\n2. El escenario mas plausible para una caida de 600 pb")
    # desviaciones tipicas del choque (en unidades de k) y correlacion, supuestas
    sd_paro, sd_pib, rho = 1.0, 1.0, 0.6
    cov = np.array([[sd_paro ** 2, rho * sd_paro * sd_pib], [rho * sd_paro * sd_pib, sd_pib ** 2]])
    inv = np.linalg.inv(cov)
    mejor = None
    for kp in np.linspace(0.0, 3.0, 61):
        f = lambda kg: caida_maxima(kp, kg) - 600  # noqa: E731
        if f(-1.0) * f(6.0) > 0:
            continue
        kg = brentq(f, -1.0, 6.0)
        d = float(np.sqrt(np.array([kp, kg]) @ inv @ np.array([kp, kg])))
        if mejor is None or d < mejor[2]:
            mejor = (kp, kg, d)
        if abs(kp - round(kp * 2) / 2) < 1e-9:
            print(f"  choque de paro x{kp:.1f} -> hace falta choque de PIB x{kg:.2f}  (distancia {d:.2f})")
    kp, kg, d = mejor
    print(f"  Mas plausible: paro x{kp:.2f}, PIB x{kg:.2f} (distancia {d:.2f}); "
          f"escalado uniforme: x{brentq(lambda x: caida_maxima(x, x) - 600, 0, 3):.2f}")


if __name__ == "__main__":
    main()
