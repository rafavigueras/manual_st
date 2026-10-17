"""Cifras de los ejemplos NUMEROS y PALANCA de los capitulos 9 a 13 (Parte II).

Los datos de entrada son publicos y salen de las notas validadas de investigacion/
(fichas EBA 2025, resultados de la Fed 2026, BCST 2025 del Banco de Inglaterra,
informe del BCE sobre el ST 2025, paginas del BCE sobre la P2G). El script solo hace
las cuentas. Si cambia una cifra aqui, cambia en el texto.
"""

print("== Cap. 9: el mismo grupo, tres ejercicios ==")
ejercicios = [
    # nombre, partida, minimo antes de acciones, minimo despues de acciones, referencia
    ("Santander, EBA 2025 (CET1 FL)", 12.19, 10.46, None, None),
    ("Santander, EBA 2025 (CET1 transitorio)", 12.78, 10.91, None, None),
    ("SHUSA, Fed 2026 (CET1)", 12.6, 11.7, None, 4.5 + 3.4),
    ("Santander UK, BCST 2025 (CET1)", 14.8, 9.7, 10.3, 6.9),
]
for nombre, ini, mn, mn_acc, ref in ejercicios:
    linea = f"{nombre}: {ini:.2f} -> {mn:.2f} %  caida {round((ini - mn) * 100):.0f} pb"
    if mn_acc is not None:
        linea += f"; con acciones {mn_acc:.2f} % (caida {round((ini - mn_acc) * 100):.0f} pb)"
    if ref is not None:
        linea += f"; referencia {ref:.1f} %, holgura en el minimo {round((mn - ref) * 100):.0f} pb"
    print(linea)
print("SCB de SHUSA: 4,5 % + 3,4 % =", f"{4.5 + 3.4:.1f} % de CET1")

print("\n== Cap. 11: comprobacion de grupo con la base de datos de la EBA ==")
for banco, d_prov, deterioro in [("Santander", 44_090, 44_852), ("BBVA", 35_593, 35_594)]:
    dif = deterioro - d_prov
    print(f"{banco}: aumento de provisiones {d_prov:,} frente a deterioro {deterioro:,} M EUR; "
          f"diferencia {dif:,} M EUR ({dif / deterioro:.1%})")

print("\n== Cap. 12: tramos de la P2G (BCE) ==")
TRAMOS = [  # (limite superior de la caida en pp, tramo, rango de P2G)
    (3.0, 1, "hasta 1,00 %"),
    (6.0, 2, "0,50-2,00 %"),
    (9.0, 3, "1,00-2,75 %"),
    (float("inf"), 4, "desde 1,75 %, sin tope"),
]


def tramo(caida_pp):
    for limite, n, rango in TRAMOS:
        if caida_pp <= limite:
            return n, rango


for nombre, caida in [("Santander EBA 2025", 1.73), ("BBVA EBA 2025", 2.18),
                      ("Ejemplo del BCE", 8.0), ("Muestra BCE 2025 (FL, maximo)", 3.5)]:
    n, rango = tramo(caida)
    print(f"{nombre}: caida {caida:.2f} pp -> tramo {n}, P2G {rango}")

print("\n-- PALANCA: 50 pb a cada lado del corte de 3 pp --")
rwa, impuesto = 35_000, 0.30          # banco de referencia de la Parte I
pb = 50
perdida_neta = pb / 1e4 * rwa
perdida_bruta = perdida_neta / (1 - impuesto)
print(f"Banco de referencia (RWA {rwa:,}): {pb} pb de CET1 = {perdida_neta:,.0f} M EUR despues de "
      f"impuestos = {perdida_bruta:,.0f} M EUR antes de impuestos")
for caida in (2.0, 2.5, 3.0 - 0.01, 3.0 + 0.01, 3.5, 4.0):
    n, rango = tramo(caida)
    print(f"  caida {caida:.2f} pp -> tramo {n} ({rango})")

print("\n-- Caida maxima frente a caida a fin de horizonte (EBA 2025, FL) --")
for banco, ini, minimo, fin in [("Santander", 12.19, 10.46, 10.46), ("BBVA", 12.88, 10.70, 11.02)]:
    print(f"{banco}: maxima {round((ini - minimo) * 100):.0f} pb; a fin de 2027 {round((ini - fin) * 100):.0f} pb")

print("\n-- Lo que no dice el tramo: la media de comparables de BBVA --")
suma_10, ca = 2_278, 478
print(f"Media de 10 comparables: {suma_10 / 10:.1f} pb; sin el que mas cae ({ca} pb): "
      f"{(suma_10 - ca) / 9:.1f} pb")

print("\n-- QA del BCE de 2025 --")
antes, despues = 308, 396
print(f"Caida del sistema antes del QA {antes} pb, despues {despues} pb: +{despues - antes} pb "
      f"({(despues - antes) / antes:.1%} sobre la cifra inicial)")

print("\n-- Contraste: SCB de la Fed, anual frente a promediado (ilustrativo) --")
suelo, dividendos = 2.5, 0.6          # pp; dividendos de cuatro trimestres, supuesto
caidas = [2.4, 4.6, 3.1, 4.2]         # caidas maximas de CET1 de cuatro tests consecutivos, supuestas
anual = [max(suelo, c + dividendos) for c in caidas]
prom = [max(suelo, (caidas[i - 1] + caidas[i]) / 2 + dividendos) for i in range(1, len(caidas))]
print("Caidas supuestas:", " / ".join(f"{c:.1f}" for c in caidas))
print("SCB anual:       ", " / ".join(f"{s:.1f}" for s in anual))
print("SCB promediado:  ", "  -  / " + " / ".join(f"{s:.2f}" for s in prom))
salto_anual = [abs(anual[i] - anual[i - 1]) for i in range(2, len(anual))]
salto_prom = [abs(prom[i] - prom[i - 1]) for i in range(1, len(prom))]
print(f"Salto medio de un ano a otro (tests 3 y 4): anual {sum(salto_anual) / len(salto_anual):.2f} pp, "
      f"promediado {sum(salto_prom) / len(salto_prom):.2f} pp")

print("\n== Cap. 13: Brasil, la misma prueba en dos ediciones ==")
print("REF abr-2025, Crise de Confianca: 44 % del activo con restricciones; necesidad 9,9 % del PR")
print("REF may-2026, Crise de Confianca: 68,7 % del activo por encima del 10,5 %; necesidad 3,1 % del PR")
print(f"Necesidad de capital: {9.9 / 3.1:.1f} veces mayor en la edicion de 2025")
