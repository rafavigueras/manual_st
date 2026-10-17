"""Anexo S4: puente de comparabilidad Espana-Mexico con los datos publicos del EBA 2025.

Datos: base de datos de transparencia del ejercicio europeo de 2025 (EBA, 1-ago-2025),
recalculada por pais y segmento en la validacion de la F1
(investigacion/research_notes/Validacion F1 stress test/datos-publicos.md, seccion 2).
Metrica: aumento del stock de provisiones (S1+S2+S3) entre el punto de partida (31-dic-2024)
y el final de 2027, sobre la exposicion de partida. Con balance estatico, sin workout ni
liberacion de provisiones de S3, aproxima el deterioro acumulado.

Para regenerar las cifras desde los CSV de la EBA (TRA_CRE_IRB.csv, TRA_CRE_STA.csv), ver
herramientas/validacion_f1/ (csv_check.py, retail_split.py, shift_share.py).

Puente en cuatro pasos:
  1. Severidad neta: adverso menos base.
  2. Denominador: hogares + empresas, sin soberanos, bancos centrales ni entidades.
  3. Mezcla frente a intensidad entre segmentos (hipotecas, resto minorista, empresas).
  4. Mecanica EBA frente a local: no se puede hacer con datos publicos; ver anexo S6.
"""
# exposicion (M EUR) y tasa (%) adversa y base, por banco y pais
TODO = {  # todas las carteras
    ("Santander", "Espana"): (309_960, 1.8522, 1.1269),
    ("Santander", "Mexico"): (65_678, 5.9974, 3.4136),
    ("BBVA", "Espana"): (250_029, 4.3027, 2.1581),
    ("BBVA", "Mexico"): (108_478, 13.6691, 10.1182),
}
HE = {  # hogares + empresas
    ("Santander", "Espana"): (157_612, 3.4534, 2.11),
    ("Santander", "Mexico"): (41_495, 9.1481, 5.24),
    ("BBVA", "Espana"): (160_804, 6.3842, 3.07),
    ("BBVA", "Mexico"): (89_244, 16.5344, 12.25),
}
SEG = {  # segmento: (exposicion, adverso, base)
    ("Santander", "Espana"): {"hipotecas": (64_414, 1.55, 0.83), "resto minorista": (32_548, 9.29, 6.15), "empresas": (60_650, 2.34, 1.29)},
    ("Santander", "Mexico"): {"hipotecas": (10_125, 3.53, 2.73), "resto minorista": (15_648, 21.55, 11.84), "empresas": (15_722, 0.41, 0.27)},
    ("BBVA", "Espana"): {"hipotecas": (71_704, 1.80, 0.68), "resto minorista": (28_352, 13.79, 7.71), "empresas": (60_747, 8.33, 3.72)},
    ("BBVA", "Mexico"): {"hipotecas": (16_786, 4.71, 3.08), "resto minorista": (33_313, 37.67, 28.56), "empresas": (39_145, 3.61, 2.31)},
}
JERS = {  # desviacion frente al base en 2027 (escenario JERS 2025)
    "Espana": {"PIB": -9.8, "paro (pp)": 5.7, "vivienda": -30.1, "inmobiliario comercial": -28.8},
    "Mexico": {"PIB": -11.9, "paro (pp)": 5.3, "vivienda": -22.1, "inmobiliario comercial": -42.1},
}


def cociente(tabla, banco, idx):
    return tabla[(banco, "Mexico")][idx] / tabla[(banco, "Espana")][idx]


def paso0():
    print("0. El cociente de partida: Mexico / Espana, todas las carteras, adverso")
    for b in ("Santander", "BBVA"):
        print(f"  {b:9} {TODO[(b, 'Mexico')][1]:.2f} % / {TODO[(b, 'Espana')][1]:.2f} % = {cociente(TODO, b, 1):.2f}")


def paso1():
    print("\n1. Severidad neta: el escenario no es mucho mas duro para Mexico")
    for p, v in JERS.items():
        print(f"  JERS {p:7}: " + ", ".join(f"{k} {x:+.1f}" for k, x in v.items()))
    for b in ("Santander", "BBVA"):
        print(f"  {b:9} base: Mexico {TODO[(b, 'Mexico')][2]:.2f} %, Espana {TODO[(b, 'Espana')][2]:.2f} % "
              f"(cociente {cociente(TODO, b, 2):.2f})")
        am = TODO[(b, "Mexico")][1] - TODO[(b, "Mexico")][2]
        ae = TODO[(b, "Espana")][1] - TODO[(b, "Espana")][2]
        print(f"  {b:9} adverso menos base: Mexico {am:.2f} pp, Espana {ae:.2f} pp (cociente {am / ae:.2f})")


def paso2():
    print("\n2. Denominador: hogares + empresas")
    for b in ("Santander", "BBVA"):
        for p in ("Espana", "Mexico"):
            peso = HE[(b, p)][0] / TODO[(b, p)][0]
            print(f"  {b:9} {p:7} peso de hogares + empresas {peso:.1%}; tasa adversa {HE[(b, p)][1]:.2f} %")
        print(f"  {b:9} cociente Mexico / Espana con hogares + empresas: {cociente(HE, b, 1):.2f}")


def paso3():
    print("\n3. Mezcla frente a intensidad (BBVA - Santander, hogares + empresas, adverso)")
    for p in ("Espana", "Mexico"):
        s, bb = SEG[("Santander", p)], SEG[("BBVA", p)]
        ts, tb = sum(v[0] for v in s.values()), sum(v[0] for v in bb.values())
        mezcla = intensidad = 0.0
        for seg in s:
            ws, wb = s[seg][0] / ts, bb[seg][0] / tb
            mezcla += (wb - ws) * s[seg][1]
            intensidad += wb * (bb[seg][1] - s[seg][1])
            print(f"  {p:7} {seg:16} peso S {ws:5.1%} / B {wb:5.1%}   tasa S {s[seg][1]:5.2f} % / B {bb[seg][1]:5.2f} %")
        tasa_s = sum(v[0] * v[1] for v in s.values()) / ts
        tasa_b = sum(v[0] * v[1] for v in bb.values()) / tb
        print(f"  {p:7} diferencia {tasa_b - tasa_s:+.2f} pp = mezcla {mezcla:+.2f} + intensidad {intensidad:+.2f}")


def pesos():
    print("\nPeso de Mexico en exposicion y en perdidas (todas las carteras, adverso)")
    datos = {"Santander": (65_678, 3_939, 1_384_138, 44_090), "BBVA": (108_478, 14_828, 643_928, 35_593)}
    for b, (e_mx, d_mx, e_g, d_g) in datos.items():
        print(f"  {b:9} exposicion {e_mx / e_g:.1%}; aumento de provisiones {d_mx / d_g:.1%}")


if __name__ == "__main__":
    paso0()
    paso1()
    paso2()
    paso3()
    pesos()
