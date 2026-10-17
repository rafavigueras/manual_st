"""Cifras del capitulo 28 (Parte IV): una primera estimacion antes de tener el escenario.

Usa el agregado publico del ejercicio de 2025 (informe de resultados de la EBA, pp. 39-40):
perdidas de credito del 1,9 % de la exposicion, 437 pb de CET1 de media, rango 10-828 pb.
"""
exposicion, rwa, impuesto = 100_000, 35_000, 0.30     # banco de referencia de la seccion 2.1.4
for tasa in (0.019, 0.025, 0.030):
    perdida = exposicion * tasa
    pb = perdida * (1 - impuesto) / rwa * 1e4
    print(f"Tasa de perdida {tasa:.1%}: {perdida:,.0f} M EUR antes de impuestos = {pb:.0f} pb de CET1")
