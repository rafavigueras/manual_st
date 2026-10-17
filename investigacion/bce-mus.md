---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, bce, mus, p2g, icaap, f1]
---

# F1 · BCE y MUS: uso del resultado, QA, ejercicios temáticos y expectativas

Consultado el 2026-10-16 y **validado ese mismo día contra fuentes primarias** (informe
`reports/Validación F1 stress test.md`, correcciones B1-B15; detalle en
`research_notes/Validación F1 stress test/bce-mus.md`).

## 1. De la caída de capital a la P2G

- `[Certain]` El BCE fija la P2G en **dos pasos** desde 2021 (<https://www.bankingsupervision.europa.eu/activities/srep/html/p2g.en.html>):
  1. Asigna el banco a uno de cuatro tramos según la **máxima caída del CET1 *fully loaded*** en el adverso. Se usa *fully loaded* para quitar el efecto de la reexpresión CRR3, que no es "inesperado" (informe BCE ST 2025, §4.2, p. 60 y nota 76).
  2. El JST fija la P2G dentro del rango, o excepcionalmente fuera, según el perfil de riesgo, los **cambios materiales del perfil desde la fecha de referencia**, el año del mínimo y las **acciones mitigadoras relevantes** (ventas de activos, reestructuraciones).
- `[Certain]` **Tramos** (gráficos SVG de las páginas del BCE; sin cambios desde 2021):

| Tramo | Caída del CET1 FL | Rango de P2G | Caída de la ratio de apalancamiento | Rango de P2G-LR |
|---|---|---|---|---|
| 1 | 0-3 pp | Hasta 1,00 % | 0-1,10 pp | Hasta 0,35 % |
| 2 | 3-6 pp | 0,50-2,00 % | 1,10-2,20 pp | 0,20-0,70 % |
| 3 | 6-9 pp | 1,00-2,75 % | 2,20-3,30 pp | 0,40-1,05 % |
| 4 | Más de 9 pp | Desde 1,75 %, sin tope | Más de 3,30 pp | Desde 0,60 %, sin tope |

  `[Guessing]` El punto exacto de corte (si 3,00 pp es tramo 1 o 2) no está publicado.
- `[Certain]` La P2G no es igual a la caída de capital. Ejemplo oficial: una caída de 8 pp sitúa al banco en el tercer tramo, con P2G probablemente no superior al 2,75 %.
- `[Certain]` **P2G-LR:** misma lógica de cuatro tramos sobre la máxima caída de la ratio de apalancamiento, pero **solo para algunos bancos** (por ejemplo, si la ratio proyectada cae por debajo del requisito global: 3 % + P2R-LR + colchón G-SII-LR). En el SREP 2025 se aplicó a 5 bancos.
- `[Certain]` Para los bancos que no participan en el ejercicio, la P2G sale de una evaluación prospectiva propia del supervisor.
- `[Certain]` **La P2G no es jurídicamente vinculante.** La Guía ICAAP de 2026 pide integrarla en el marco de riesgos y avisar al supervisor, con un plan de capital revisado, si los fondos propios caen por debajo de ella (art. 104b CRD).
- `[Certain]` **Evaluación cualitativa:** los JST valoran la puntualidad y exactitud de los datos, la cooperación y la calidad de la información, con métricas automáticas de calidad. Alimenta la evaluación RDAR del Elemento 2 del SREP, y las deficiencias cualitativas pueden influir en la **P2R**, no solo en la P2G (informe BCE ST 2025, §4.1 y p. 17, <https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.Report_2025_Stress_Test_202508.en.pdf>).
- `[Certain]` **Tras el EU-wide 2025**, la P2G media bajó del 1,3 % al 1,1 %, porque los beneficios amortiguaron la caída (SREP 2025 agregado, <https://www.bankingsupervision.europa.eu/activities/srep/2025/html/ssm.srep202511_aggregatedresults2025.en.html>). La muestra del BCE cayó 4,0 pp en transitorio (16,0 → 12,0 %) y 3,5 pp de máximo en *fully loaded*. La caída bruta de 8,1 pp (5,0 de provisiones, 1,1 de APR, 1,3 de mercado y ~0,6 de operacional) se compensó con 4,8 pp de ingresos.
- `[Likely]` Con sus caídas FL máximas de 2025, Santander (173 pb) y BBVA (218 pb) caen los dos en el tramo 1; como el JST puede salirse del rango, eso no da su P2G real.
- `[Certain]` Directrices de SREP revisadas: EBA/GL/2026/06, aplicables desde el 1-ene-2027, con posibilidad de P2G bienal (detalle en `eba.md`).

## 2. Ejercicio temático 2026: *reverse stress test* geopolítico

Fuentes: nota de prensa del 31-jul-2026 (<https://www.bankingsupervision.europa.eu/press/pr/date/2026/html/ssm.pr260731~93964644b0.en.html>) e informe completo de 16 págs. (<https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.geopolstresstest202608.en.pdf>).

- `[Certain]` 110 bancos de supervisión directa. Cada banco diseña escenarios geopolíticos plausibles con una **caída mínima de CET1 de 300 pb**; ~20 % eligió más. El objetivo se calibró con la mediana histórica de caídas anuales en sectores bancarios de la UE con pérdida de capital (~225-250 pb en 15-20 años). No es comparable con la caída del EU-wide.
- `[Certain]` Sin apoyo fiscal más allá del ya aprobado y con política monetaria libre.
- `[Certain]` Se hizo **dentro del ICAAP**, **sustituyó** la simulación de *reverse stress test* del ICAAP 2026 y cubre además el test supervisor anual del art. 100 CRD. **No ajusta la P2G ni la P2G-LR**; las deficiencias pueden ir a la parte de gobierno del SREP y afectar a la P2R.
- `[Certain]` Tres canales de transmisión: mercados financieros, economía real y seguridad (física, ciber, híbrida). La economía real es el principal y el de mercados el segundo; el de seguridad pesa en los escenarios de conflicto militar y ciberataque.
- `[Certain]` **Crédito:** los aumentos de NPL se concentran en agricultura, construcción, manufacturas, transporte y hostelería (tabla 2). El otro gran canal es el **margen de intereses**, en escenarios con tipos a la baja y curva invertida.
- `[Certain]` **Debilidades señaladas:** granularidad y sensibilidad de las evaluaciones; coherencia entre la narrativa y su traducción a solvencia y liquidez; realismo de las acciones de gestión en crisis sistémicas; interacción solvencia-liquidez; proyecciones de **balance dinámico** demasiado optimistas (crecer en plena crisis); y la importancia de usar **varios escenarios**.
- `[Certain]` **Incoherencias concretas:** el peso de los *drivers* no casa con la narrativa; hay sensibilidades de NII o de crédito anormalmente grandes, pequeñas o **de signo contrario** (pérdidas de préstamos que bajan en el adverso); la simulación no conecta con las carteras más vulnerables. Una severidad "beyond what is statistically plausible" para llegar a 300 pb se lee como síntoma de **modelos insensibles al escenario**. **Para el manual:** catálogo directo de bloques CASO JST.
- `[Certain]` **Acciones de gestión** más citadas: suspender dividendos (59 %), gestionar exposiciones (57 %), frenar nuevo negocio (50 %), endurecer la admisión (47 %), vender carteras (40 %), *repricing* (39 %) y ampliar capital (22 %). Algunas eran demasiado optimistas (vender carteras o ampliar capital a precios ambiciosos en mercados estresados). El BCE señala el **efecto manada**: si todos actúan a la vez, cada acción pierde eficacia. Hará seguimiento en el diálogo sobre planificación de capital y de recuperación.
- `[Certain]` **Liquidez:** la mediana del LCR baja del 186 % al 163 % en un año; el LCR en divisa cae por debajo del 100 % en algunos bancos; varios bancos dieron una respuesta de liquidez muy plana pese a una caída de capital grande.

## 3. Otros ejercicios temáticos

- `[Certain]` **Climático del BCE de 2022:** 104 bancos, *bottom-up* solo en 41, ~70.000 M€ de pérdidas que el BCE considera subestimadas; entrada cualitativa en el SREP, sin efecto en la P2G (<https://www.bankingsupervision.europa.eu/press/pr/date/2022/html/ssm.pr220708~565c38d18a.en.html>). El manual IRB lo cubre en §39.4.1.
- `[Certain]` **Análisis *Fit-for-55* (resultados el 19-nov-2024):** encargado por la Comisión a las **tres ESA, el BCE y la JERS**, no coordinado por la EBA. Escenarios de la JERS con apoyo del BCE; modelos *top-down*; bancos, aseguradoras, fondos de pensiones de empleo y fondos de inversión; horizonte 2022-2030; no fija requisitos (<https://www.ecb.europa.eu/press/pr/date/2024/html/ecb.pr241119~10b6083ce0.en.html>). No es el módulo climático del EBA 2027.
- `[Certain]` **Ciberresiliencia 2024:** 109 bancos, 28 con pruebas ampliadas; alimenta el SREP 2024; no es un ejercicio de capital. `[Likely]` Sin efecto en la P2G. Fuera del perímetro del manual.

## 4. Prioridades supervisoras 2026-2028 y guías

- `[Certain]` Dos prioridades (<https://www.bankingsupervision.europa.eu/framework/priorities/html/ssm.supervisory_priorities202511.en.html>):
  1. Riesgo geopolítico, con el temático 2026 como herramienta.
  2. Resiliencia operativa y TIC, donde está **RDARR**: progreso "remains slow" y la subpuntuación media no mejoró. Estrategia sistémica desde dic-2024, "clearly defined remediation and escalation process" e inspecciones *in situ* específicas.
- `[Certain]` Consecuencias en el SREP por deficiencias de datos en el ejercicio (informe BCE ST 2025): P2R adicional, *enforcement* y sanciones.
- `[Certain]` **Guía RDARR (mayo de 2024)**, <https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.supervisory_guides240503_riskreporting.en.pdf>: su perímetro incluye expresamente los envíos al EU-wide y a los tests del SREP (§3.2); un informe mensual o trimestral que tarda más de 20 días hábiles no permite reaccionar a tiempo (§3.6). Referencia del cap. 26.
- `[Certain]` **Guía ICAAP vigente: julio de 2026** (<https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.supervisory_guides202607_icaap.en.pdf>). La de noviembre de 2018 está marcada como "outdated". Mantiene los siete principios, las dos perspectivas (normativa y económica) y el horizonte mínimo de tres años; aclara que el *management buffer* no es un requisito ni "headroom" y añade expectativas sobre la P2G. Publicada dentro de la revisión de unas 130 guías del BCE anunciada el 26-jun-2026. `[Likely]` Fecha exacta: 15-jul-2026. Referencia del cap. 13.

## 5. El QA del ejercicio europeo

- `[Certain]` Las autoridades competentes validan datos y resultados, revisan modelos y aplican la "función de reacción supervisora"; la EBA da estadísticas descriptivas comunes; hay comparación transversal de parámetros de partida y proyectados con posible petición de revisión (NM27 párr. 42, 112 y 118).
- `[Certain]` El BCE describe su QA como "using top-down stress test models, peer benchmarking and supervisory scrutiny" (blog del 20-ene-2025, <https://www.bankingsupervision.europa.eu/press/blog/2025/html/ssm.blog20250120~424509dc36.en.html>). Usa *credit risk benchmarks* propios. **En 2025 los bancos tuvieron que enviar el crédito antes de recibir esos *benchmarks***, para que no pudieran anticipar el *challenge*. Quien envíe proyecciones demasiado optimistas recibe más escrutinio, posibles visitas *in situ* durante el QA e inspecciones posteriores.
- `[Certain]` **El QA de 2025 sumó 88 pb netos** a la caída del sistema (de 308 a 396 pb) (informe BCE ST 2025, p. 17). Es la cifra que mide el peso del *challenge*.
- `[Certain]` La puntuación cualitativa combina métricas automáticas de calidad de datos y el juicio del JST sobre el comportamiento en los ciclos de QA (§4.1).
- `[Guessing]` No se publican los *flags*, el número de rondas ni los plazos de respuesta. Para los caps. 21-23 hace falta experiencia de proyecto anonimizada. No existe ningún "*Stress test manual* del BCE de 2018" localizable: referencia retirada.

## Huecos que siguen abiertos

- Comparación línea a línea entre las Guías ICAAP de 2018 y 2026, y fecha exacta de la de 2026.
- Tablas 1-2 y gráfico 2 del informe geopolítico, que solo están en gráficos.
- Confirmar la frase literal sobre el efecto del ciber 2024 en la P2G.
