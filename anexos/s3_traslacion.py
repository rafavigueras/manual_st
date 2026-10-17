"""Anexo S3: traslacion del escenario de la JERS a las geografias de fuera de la UE.

Datos: escenario macrofinanciero de la JERS para el ejercicio europeo de 2025 (tablas 4.1.1,
4.1.2 y 4.1.4 y tipos de cambio), transcritos y validados en investigacion/jers-escenario.md.

Cuatro piezas:
  1. Severidad: acumulado frente a desviacion sobre el base, por pais.
  2. Turkiye: por que una variable nominal engana con inflacion alta.
  3. Argentina, que no tiene fila: la fila "Rest of the world" frente a aplicar la desviacion
     regional a un base propio (ilustrativo).
  4. La asimetria del tipo de cambio en la filial del juguete (anexo S0): los saldos se quedan
     al tipo de cierre, el margen se convierte con la senda del escenario.
"""
# PIB (tasa anual, %) y paro (media anual, %): base 25-27 y adverso 25-27
ESC = {
    "Espana":  {"pib_b": [2.5, 1.9, 1.7], "pib_a": [-2.5, -3.5, 2.0], "paro_b": [10.8, 10.4, 9.9], "paro_a": [14.1, 16.8, 15.6], "paro0": 11.5},
    "Mexico":  {"pib_b": [1.3, 2.0, 2.3], "pib_a": [-4.7, -2.2, -0.1], "paro_b": [3.3, 3.4, 3.5], "paro_a": [5.2, 7.6, 8.8], "paro0": 3.0},
    "Brasil":  {"pib_b": [2.2, 2.3, 2.4], "pib_a": [-3.3, -0.6, 1.0], "paro_b": [7.2, 7.3, 7.4], "paro_a": [11.6, 12.1, 11.7], "paro0": 7.2},
    "Chile":   {"pib_b": [2.4, 2.5, 2.4], "pib_a": [-5.1, -0.2, 2.1], "paro_b": [8.0, 7.8, 7.7], "paro_a": [11.8, 12.5, 12.1], "paro0": 8.5},
    "Turkiye": {"pib_b": [2.7, 3.2, 3.4], "pib_a": [-4.9, -2.7, 1.0], "paro_b": [9.9, 9.6, 9.5], "paro_a": [15.6, 16.2, 15.6], "paro0": 9.3},
    "EE. UU.": {"pib_b": [2.2, 2.0, 2.1], "pib_a": [-5.1, -2.5, 4.3], "paro_b": [4.4, 4.3, 4.2], "paro_a": [8.9, 10.0, 8.6], "paro0": 4.1},
    "Resto del mundo": {"pib_b": [3.9, 4.2, 3.9], "pib_a": [-3.2, -1.5, 1.5], "paro_b": [9.9, 9.6, 9.5], "paro_a": [15.6, 16.1, 15.4], "paro0": 9.3},
    "America Latina": {"pib_b": [2.3, 2.5, 2.6], "pib_a": [-2.7, -0.6, 0.9], "paro_b": [6.2, 6.3, 6.3], "paro_a": [9.2, 10.5, 10.7], "paro0": 6.2},
}
FX_MXN = [8.9, 7.3, 6.0]          # depreciacion media anual EUR/MXN frente al punto de partida, %


def nivel(tasas):
    n = 1.0
    for x in tasas:
        n *= 1 + x / 100
    return n


def severidad():
    print("1. Severidad del adverso: acumulado frente a desviacion sobre el base en el ano 3")
    for pais, e in ESC.items():
        acum = (nivel(e["pib_a"]) - 1) * 100
        desv = (nivel(e["pib_a"]) / nivel(e["pib_b"]) - 1) * 100
        dparo = e["paro_a"][2] - e["paro_b"][2]
        print(f"  {pais:16} PIB acumulado {acum:6.1f} %  desviacion {desv:6.1f} %  paro +{dparo:.1f} pp sobre el base")


def turkiye():
    print("\n2. Turkiye: vivienda nominal frente a desviacion (escenario de 2025)")
    nominal, desviacion = 128.7, -19.3
    base_implicito = (1 + nominal / 100) / (1 + desviacion / 100) - 1
    print(f"  Adverso: +{nominal} % nominal acumulado; desviacion frente al base {desviacion} %")
    print(f"  Base implicito: +{base_implicito * 100:.1f} % nominal en tres anos")
    print("  Un satelite que lea la variable nominal 've' una subida del 129 %: senal de signo equivocado")


def argentina():
    print("\n3. Argentina sin fila: dos traslaciones (base argentino supuesto, ilustrativo)")
    base_ar_pib, base_ar_paro = [3.0, 3.0, 3.0], [7.0, 7.0, 7.0]
    for fuente in ("Resto del mundo", "America Latina"):
        e = ESC[fuente]
        dpib = [a - b for a, b in zip(e["pib_a"], e["pib_b"])]
        dparo = [a - b for a, b in zip(e["paro_a"], e["paro_b"])]
        pib = [b + d for b, d in zip(base_ar_pib, dpib)]
        paro = [b + d for b, d in zip(base_ar_paro, dparo)]
        print(f"  Desviacion de '{fuente}': PIB {' / '.join(f'{x:.1f}' for x in pib)} %; "
              f"paro {' / '.join(f'{x:.1f}' for x in paro)} %")
    e = ESC["Resto del mundo"]
    print(f"  Fila 'Resto del mundo' tal cual: PIB {' / '.join(f'{x:.1f}' for x in e['pib_a'])} %; "
          f"paro {' / '.join(f'{x:.1f}' for x in e['paro_a'])} % (el paro replica el de Turkiye)")


def tipo_cambio():
    print("\n4. Asimetria del tipo de cambio en la filial del juguete (anexo S0)")
    margen_eur = 1000 * 0.075 + 1000 * 0.012           # margen adverso dado, al tipo de cierre
    rwa0, impuesto = 1722.0, 0.30                       # RWA de partida de la filial (anexo S0)
    perdido = 0.0
    for t, dep in enumerate(FX_MXN, start=1):
        convertido = margen_eur / (1 + dep / 100)
        perdido += margen_eur - convertido
        print(f"  Ano {t}: EUR/MXN +{dep:.1f} %: margen {margen_eur:.1f} -> {convertido:.1f} M EUR")
    print(f"  Margen perdido en tres anos: {perdido:.1f} M EUR = {perdido * (1 - impuesto) / rwa0 * 1e4:.0f} pb "
          f"de CET1 de la filial sobre sus RWA de partida, que no se mueven")


if __name__ == "__main__":
    severidad()
    turkiye()
    argentina()
    tipo_cambio()
