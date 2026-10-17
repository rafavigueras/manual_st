# Investigación (F1) — índice

Research de fuentes del 2026-10-16, **validado ese mismo día contra fuentes primarias**
(`reports/Validación F1 stress test.md`; notas de detalle en `research_notes/Validación F1 stress test/`).
Cada afirmación lleva `[Certain]` (evidencia dura), `[Likely]` (inferencia fuerte) o `[Guessing]`
(hueco rellenado con criterio).

| Nota | Qué cubre | Alimenta |
|---|---|---|
| `eba.md` | Metodología EBA 2025 y borrador 2027 (11-jun-2026): crédito, provisiones, cambios 2025→2027, módulo climático; GL/2026/06 | Partes II y III, cap. 29 |
| `bce-mus.md` | Tramos de P2G, SREP 2025, QA del BCE (+88 pb), ejercicio geopolítico 2026, prioridades 2026-2028, Guía ICAAP 2026, RDARR | Caps. 3, 11, 13, 14, 21-24, 26 |
| `jers-escenario.md` | Escenario adverso 2025 por país, variables disponibles y huecos, vías del tipo de cambio | Caps. 4, 25, 27; anexo S3 |
| `reguladores-no-ue.md` | Fed, Banco de Inglaterra (BCST), CNBV, Banxico, BCB, CMF, BDDK, BCRA; venta de Santander Polska | Caps. 6, 25, 27, 29 |
| `datos-publicos.md` | Resultados EBA 2025 de Santander y BBVA por país y segmento; mezcla frente a intensidad | Cap. 27; anexo S4 |

`fuentes/` guarda los PDF públicos consultados (fuera de git por tamaño).
`../herramientas/validacion_f1/` guarda los scripts de la validación (CSV de la EBA, coordenadas del PDF,
descomposición mezcla/intensidad). `../herramientas/parse_eba_resultados.py` queda obsoleto: usar el CSV.

## Hallazgos que cambian el plan

1. **El EBA 2027 está a medio publicar** (borrador del 11-jun-2026; nota final y escenario previstos entre
   diciembre de 2026 y finales de enero de 2027). El manual se escribe sobre el 2027 como referencia y el
   2025 como último cerrado; los caps. 5 y 7-12 se redactan como mecanismo y se revisan cuando salga la final.
2. **La EBA etiqueta ahora el NII como *top-down*, pero el mecanismo ya existía en 2025**, y las
   titulizaciones hacen el camino contrario (pasan a proyección propia). El crédito sigue siendo el gran
   bloque *bottom-up*. La decisión de perímetro no cambia.
3. **Los *benchmarks* del BCE son el eje del diálogo con el JST** en crédito. En 2025 los bancos enviaron
   el crédito antes de recibirlos, y el QA sumó 88 pb a la caída del sistema. **El EBA 2027 no tiene suelos
   de cobertura** (solo de REA), así que el cap. 11 trata de *benchmarks*, pares y QA.
4. **Asimetría del tipo de cambio:** stocks y RWA quedan al tipo de cierre, pero NII, comisiones y gastos
   recogen la senda de divisa del escenario. EUR/USD y EUR/GBP no se mueven. Pieza central del puente
   España–México y fuente de incoherencias del cap. 18.
5. **El cap. 27 pasa del cociente al puente.** El "México cuesta 3,2 veces lo que España" solo sale con una
   métrica y un escenario. Medido frente a la base, el escenario no es mucho más severo para México; la
   diferencia viene del riesgo de partida y de la intensidad por segmento, no de la mezcla de cartera.
   Puente en cuatro pasos: severidad neta de la base, denominador hogares + empresas, mezcla frente a
   intensidad, y mecánica EBA frente a local. Anexo S4 sintético, calibrado con tasas reales por segmento.
6. **Polonia sale casi entera del perímetro de Santander** (venta a Erste cerrada el 9-ene-2026), salvo
   Santander Consumer Bank Polonia `[Likely]`: ejemplo real de cambio de perímetro entre ejercicios.
7. **La Fed promediará el SCB a dos años** (primer SCB promediado el 1-ene-2029) y someterá escenarios y
   modelos a comentario público (escenarios 2027 propuestos antes del 10-ene-2027). Material del cap. 29.
8. **La P2G puede fijarse cada dos años** (EBA/GL/2026/06, aplicables desde el 1-ene-2027).
9. **La referencia del cap. 13 es la Guía ICAAP del BCE de julio de 2026**; la de 2018 está obsoleta.
10. **El EBA 2027 quita el *backstop* de SICR y la equivalencia S3 = NPE**, y cambia el criterio de país
    (inmediato en pérdidas, riesgo último en RWA). El SICR de cada banco pasa a ser fuente de dispersión.

## Lección de método

Las cifras transcritas aguantaron la validación; fallaron las inferencias apoyadas en una sola métrica, en
un párrafo leído de forma literal o en la etiqueta de una nota de prensa. Y dos huecos "solo en el gráfico"
estaban en SVG con las cifras trazadas: **renderizar las imágenes de las páginas oficiales antes de dar un
dato por no publicado.**
