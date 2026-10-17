---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, eba, metodologia, f1]
---

# F1 · EBA: metodología del ejercicio europeo (2025 cerrado, 2027 en borrador)

Consultado el 2026-10-16 y **validado ese mismo día contra fuentes primarias** (informe
`reports/Validación F1 stress test.md`, correcciones E1-E26; detalle en
`research_notes/Validación F1 stress test/eba.md`). Fuentes principales: nota metodológica 2027 en
borrador (`fuentes/2026-06-11 EBA ST2027 draft methodological note.pdf`, "NM27") y nota final 2025
(`fuentes/2024-11 EBA ST2025 methodological note.pdf`, "NM25"). Los párrafos son de la NM27 salvo
que se diga otra cosa.

## 1. Calendario y estado

- `[Certain]` 2025: nota final fechada el 11-nov-2024, ejercicio lanzado el 20-ene-2025, cifras a 31-dic-2024, horizonte 2025-2027, resultados el 1-ago-2025. `[Likely]` Hubo una versión preliminar de la nota en julio de 2024.
- `[Certain]` El 11-jun-2026 la EBA publicó **en borrador** la nota, las plantillas y la guía del 2027, antes que en ciclos anteriores. <https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-early-consultation-simplified-eu-wide-stress-test-climate-risk-integration>.
- `[Certain]` 2027: fecha de referencia 31-dic-2026, horizonte 2027-2029 (párr. 21 y 24). 63 bancos de la UE y Noruega, 47 de la zona del euro, ~75 % del sector. Activo mínimo de 30.000 M€; los bancos de menos de 50.000 M€ y los que entran por encima del 70 % de cobertura pueden aplicar la proporcionalidad del anexo VIII (párr. 7-9).
- `[Certain]` La consulta del módulo de reporting asociado (EBA/CP/2026/07) cerró el 10-jul-2026 a las 23:59 CEST. `[Guessing]` La fecha de cierre de la consulta de la propia nota (un buscador decía 7-ago-2026) no está verificada.
- `[Certain]` No hay calendario oficial a 2026-10-16: la EBA solo dice que publicará resultados "around summer" de 2027 (Programa de trabajo EBA 2027, §1.2.3.1). `[Likely]` Por analogía con 2025 (KPMG): nota final a final de 2026, lanzamiento con escenarios a final de enero de 2027, primer envío en marzo, segundo en abril, último en junio y resultados en agosto. Encaja con los calendarios que manejan los bancos para el ejercicio (ejecución de enero a junio de 2027, con el pico entre febrero y abril).

## 2. Rasgos estructurales

- `[Certain]` **Bottom-up restringido** con elementos top-down: el banco proyecta con sus modelos bajo restricciones estrictas y revisión de la autoridad competente (párr. 38).
- `[Certain]` **Elementos top-down del 2027:** comisiones (NFCI) con parámetros prescritos, senda de pérdidas de soberanos prescrita y componentes del margen de intereses según fórmulas prescritas (párr. 38). La nota de prensa califica ya el NII de *top-down*. **Pero no es una novedad de fondo:** las fórmulas de margen (NM25 párr. 422 y 425; NM27 párr. 426 y 429) y el cálculo centralizado del NII ya existían en 2025. El cambio es sobre todo de etiqueta y de centralización del punto de partida (párr. 382 y 384). En sentido contrario, **las titulizaciones dejan de tener ponderaciones prescritas y pasan a proyección propia** (párr. 175-178). En 2025 lo prescrito eran las comisiones, las ponderaciones de titulizaciones y la senda de pérdidas de soberanos (NM25 párr. 38). `[Likely]` Para el manual: el crédito sigue siendo el gran bloque *bottom-up*, ahora junto con las titulizaciones.
- `[Certain]` **Balance estático**, en base individual, subconsolidada y consolidada. Lo que vence se sustituye por instrumentos similares; **sin *workout* ni curas de stage 3**; mismo modelo de negocio y misma presencia geográfica (párr. 33-34). Sin excepciones (párr. 36). Las desinversiones no cerradas antes del 31-dic-2026 no se tienen en cuenta (párr. 36). Las medidas de capital completadas entre el 1-ene y el 31-mar-2027 se reportan aparte en CSV_CAPMEAS y no afectan a los ratios (párr. 37).
- `[Certain]` **Tipo de cambio: asimetría entre balance y resultados.** Los stocks de balance y el RWA de crédito no se mueven por el tipo de cambio: se convierten al tipo del 31-dic-2026 (párr. 35). **El NII** (factor corrector, párr. 380), **las comisiones** en el adverso y **los gastos administrativos** sí incorporan la senda de divisa del escenario (tabla 1). En crédito, el tipo de cambio entra por los satélites y por la regla de préstamos en divisa (párr. 147-148). **Para el manual:** la filial mexicana no encoge en euros en el balance, pero sus ingresos y gastos sí se convierten con el peso depreciado.
- `[Certain]` **Sin umbral de aprobado o suspenso**; el resultado alimenta el SREP (párr. 30). La nota 4 al pie del borrador aún remite a EBA/GL/2022/03; `[Likely]` la versión final citará la GL/2026/06.
- `[Certain]` **Perímetro:** máximo nivel de consolidación prudencial CRR/CRD; seguros fuera (párr. 13-14). **Datos pro forma** solo para eventos únicos de más del 12,5 % del activo (párr. 16), con una **lista cerrada** de cinco eventos: fusiones, adquisiciones, escisiones de unidades relevantes, desinversiones y transferencias de activos o pasivos (párr. 17). Solo afectan a las partidas con *caps* o *floors* basados en datos históricos (párr. 15). La autoridad presenta el caso a la EBA antes del primer envío (párr. 18); sin reconocimiento no hay ajuste (párr. 20).
- `[Certain]` **Modelos:** solo cuentan los modelos internos aprobados e implantados a 31-dic-2026. Excepción: un banco que cambie de enfoque (IRB a estándar o al revés) con aprobación e implantación en el 1T 2027 puede hacer el ejercicio con el nuevo régimen y reexpresar el REA de partida (párr. 28-29).
- `[Certain]` Tipo impositivo común simplificado del 30 % (párr. 32).
- `[Certain]` Se reportan cada año el CET1, el Tier 1, el capital total y la ratio de apalancamiento, en base transitoria y *fully loaded* (párr. 26-27).

## 3. Riesgo de crédito (capítulo 2 de la NM27)

- `[Certain]` **Perímetro de pérdidas:** coste amortizado. Valor razonable (FVOCI, FVPL) y riesgo de contraparte (CCR) van por mercado. El RWA sigue el perímetro CRR/COREP e incluye CCR y valor razonable (párr. 50-52).
- `[Certain]` **Tres pasos:** parámetros de partida, impacto del escenario en los parámetros y variación del stock de provisiones que va a resultados (párr. 45).
- `[Certain]` **Recuadro 1 (párr. 46)**, que remite a los párr. 123, 124 y 128: un único escenario por escenario macro (128); **previsión perfecta** de la senda macro y tratamiento de S3 con variables planas tras 2029, salvo el PIB, que crece a la tasa del último año del base (123); reversión lineal en 6 años de los parámetros adversos de S1/S2 al nivel base de 2029 (124). En el base, los parámetros de S1/S2 quedan planos después de 2029.
- `[Certain]` **Restricciones del recuadro 2:** no hay curas desde S3 (párr. 86); no se liberan provisiones de S3, exposición a exposición (párr. 141); el UTREA de fin de 2026 es suelo metodológico del RWA de crédito, por separado para IRB y estándar, sin aplicarse al STREA del *output floor* (párr. 153); **el suelo de titulizaciones por método está en el párr. 178**.
- `[Certain]` **Parámetros de partida PiT:** salen de los modelos de provisiones; si se aproximan con observados históricos, solo se admiten ajustes que los hagan más conservadores; comparación transversal entre bancos tras el envío, con posible petición de revisión (párr. 109-112).
- `[Certain]` **Jerarquía de enfoques para proyectar:** modelos satélite propios por delante de los *benchmarks*, contrastados contra estándares mínimos de solidez econométrica y sensibilidad (párr. 113). Sin modelo adecuado, **benchmarks del BCE sin ajuste** y a nivel de cartera (párr. 115). La elección inicial no se cambia sin permiso (párr. 116), y la autoridad puede pedirla antes de que se publique el escenario (nota 20). Si los satélites no cubren al menos el 10 % de la clase pivote (el nivel más bajo de agregación, nota 21), *benchmark* para toda la clase; por encima del 10 %, mezcla justificada (párr. 117). **Los *benchmarks* del BCE sirven siempre de vara de medir**, y quien sale "demasiado optimista" puede tener que revisar (párr. 118). Son input obligatorio para soberanos. Sin cambios de fondo frente a 2025 (NM25 párr. 123-125). **Para el manual:** es el mecanismo detrás de la mitad de los bloques CASO JST.
- `[Certain]` Matrices de transición por grado si el modelo trabaja a ese nivel; si no, parámetros agregados por cartera documentados (párr. 119-120). La LGD refleja la caída del valor de las garantías y supuestos prudentes de cura implícita y costes (párr. 121-122).
- `[Certain]` **Sectores:** modelos o sensibilidades sectoriales; si no hay, reparto de las pérdidas del país entre sectores por sensibilidad al VAB o por tamaño, explicado en la nota explicativa; coherencia en dirección y magnitud con los choques de VAB (párr. 114). Una combinación de país y NACE 1 se reporta si pesa al menos el 0,5 % de la exposición a sociedades no financieras (párr. 98).
- `[Certain]` **Desglose por país de contraparte** (umbral del art. 5(2) del Reglamento de Ejecución (UE) 2024/3117, filas 0850/0860 de C 04.00): en CR_SCEN y CR_SECTOR, como máximo **10 países** no domésticos de más del 1 %; en CR_REA_STA_DET y CR_REA_IRB_DET, como máximo **5**, subconjunto de los anteriores en el mismo orden. Si lo doméstico supera el 90 %, todo lo demás va a "Other". Selección fijada a 31-dic-2026 (párr. 100-107).
- `[Certain]` **Criterio de país, novedad de 2027:** país inmediato en las plantillas de pérdidas (FINREP) y país de riesgo último en las de RWA (COREP) (párr. 58-59). **En 2025 todas usaban riesgo último**, con cobertura mínima del 95 % o los 10 primeros países (NM25 párr. 102-105). **Para el manual:** la ventana por la que el JST ve México o Brasil cambia de criterio entre ejercicios, y los dos criterios conviviendo en 2027 son una fuente de diferencias de conciliación.
- `[Certain]` **Préstamos en divisa:** si el peso en moneda distinta de la del prestatario supera el 5 % por país y cartera, las tasas de transición se estresan con satélites y la LR con un *add-on* al LTV (con garantía) o un *add-on* histórico de divisa (sin garantía). En 2027 la tabla 10 se aplica a siete **carteras de deterioro tipo FINREP**; en 2025, a clases de exposición IRB y estándar (NM25 tablas 8-9) (párr. 147-148). Relevante para la dolarización parcial (Perú, Argentina, Türkiye).
- `[Certain]` **RWA bajo estrés:** migración de grados coherente con los flujos de *default*; las exposiciones en *default* pasan a su ponderación (por ejemplo, 100 % o 150 % en estándar); hay que tener en cuenta la reestimación esperada de parámetros regulatorios con los nuevos datos de estrés y los suelos y escalares de supervisión; sin migración entre clases (párr. 152-156). El REA en *default* con LGD propia es `MAX{0; (LGDreg − ELBE) × 12,5 × stock}` (recuadro 10, párr. 157). El exceso o déficit IRB va por el art. 159 de la CRR (párr. 161).
- `[Certain]` Una exposición frente a la matriz se trata en condiciones de mercado (*arm's length*) (párr. 126).

### 3.1 Cálculo de provisiones: fórmulas prescritas y ningún suelo de cobertura (sección 2.4.3 y anexo IV)

- `[Certain]` **El EBA 2027 no tiene suelos de cobertura en crédito**: ni *backstop* de NPE ni *floors* de LGD. Los únicos "floors" del capítulo de crédito son de REA (párr. 49, 153 y 178). El anexo IV "no añade requisitos" (párr. 594): solo resume.
- `[Certain]` La disciplina sale de cuatro sitios:
  1. **Fórmulas prescritas** para cada flujo entre stages (recuadros 3 a 8). Por ejemplo, los S3 nuevos son `Exp S1(t) × PD12M S1(t+1) × LGD S1(t+1) + Exp S2(t) × PD12M S2(t+1) × LGD S2(t+1)` y se acumulan. En 2029, el adverso pondera 5/6 los parámetros adversos y 1/6 los del base, por la reversión a seis años.
  2. **No se liberan provisiones de S3**, exposición a exposición (párr. 141).
  3. **Suelo implícito sobre el S3 antiguo:** `Prov Old S3(t+1) = MAX{Exp S3(t=0) × LGD S3(t=1); Prov S3(t=0)}` (recuadro 9). Con previsión perfecta, cualquier caída de garantías del escenario se carga entera en el primer año (el párr. 130 pone el ejemplo de una caída del 10 % de la vivienda).
  4. **Parámetros soberanos del BCE**, obligatorios para todos los bancos y países, con tasa de pérdida cero para bancos centrales (párr. 145-146), más la comparación con *benchmarks* y entre bancos en el QA (párr. 112 y 118).
- `[Likely]` Consecuencia para el manual: el cap. 11 trata sobre *benchmarks*, comparación entre pares y QA, no sobre *caps* y *floors* de cobertura.

## 4. Qué cambia en 2027

- `[Certain]` **Un 55 % menos de datos** que en 2025, apoyándose en el reporting supervisor ordinario (nota de prensa).
- `[Certain]` **Cinco cambios de 2025 a 2027 en crédito:**
  1. Desaparece el *backstop* de SICR (PD *lifetime* triplicada) y el umbral de bajo riesgo del 0,30 %: el SICR sigue el criterio contable de cada banco. `[Likely]` El SICR propio de cada banco pasa a ser fuente de dispersión que el JST querrá explicar.
  2. S3 deja de equivaler a NPE y pasa a ser el *credit-impaired* de IFRS 9, con POCI aparte (párr. 56).
  3. Se piden puntos de partida a cierre de 2025 y de 2026.
  4. Las titulizaciones pasan de un aumento fijo de ponderaciones a proyección propia (párr. 175-178).
  5. Desaparece del anexo IV la fila "la garantía financiada no puede superar la exposición" (NM25 tabla 27; NM27 tabla 29).
- `[Certain]` **Integración con FINREP/COREP, como propuesta en consulta:** la EBA propone que los puntos de partida de crédito se tomen de FINREP/COREP a partir del **ejercicio de 2029**, porque los FINREP y COREP modificados tienen su primera referencia en septiembre de 2027. En 2027 las plantillas solo los imitan, y las proyecciones siguen en plantillas *ad hoc*. Es una propuesta de ITS aún no adoptada por la Comisión (CP módulo 4, párr. 6 y 8-9; NM27 párr. 60 y 62). **Para el manual:** cuando el punto de partida sea FINREP, cada diferencia de perímetro entre el FINREP consolidado y el reporting local de una filial no UE aflorará como error de conciliación, de lleno en 2029.
- `[Certain]` **Módulo climático (cap. 7):** solo pérdidas de crédito, **sin REA** (párr. 572), aplicado como *overlay* sobre el adverso (párr. 566). La nota de prensa dice textualmente que no afecta a los resultados principales.
  - Transición: 2027-2029, sociedades no financieras de los sectores NACE A-H y M, más los NACE 2 materiales (≥ 0,5 %), e hipotecas por tramo de eficiencia energética. El banco elige entre recibir variables climáticas o choques de VAB.
  - Físico: inundación fluvial de probabilidad 1 %, **solo en 2027**, simultánea en todo el EEE; geolocalización de cada garantía contra los mapas del JRC, función de daño, métricas de cola, resultados brutos y netos de seguros.
  - `[Likely]` Para Santander y BBVA, el riesgo físico no capta México, Brasil ni EE. UU.; la transición sí sigue la lista de países de CR_SCEN.
  - El capítulo deja abierta una "Question for banks" sobre el alcance físico: puede cambiar en la versión final.

## 5. Marco más amplio

- `[Certain]` El reparto de papeles está en el párr. 42: la JERS y el BCE hacen el adverso; el BCE, el base; la EBA, la metodología, el QA mínimo, las Q&A y las estadísticas para comprobar consistencia; las autoridades competentes, el QA, la revisión de modelos y el traslado al SREP. `[Likely]` La base legal es el art. 32(2) del Reglamento (UE) 1093/2010 (citarlo del reglamento; el párr. 1 solo dice que la EBA inicia y coordina con la JERS). El módulo climático se apoya en el art. 23 (párr. 565).
- `[Certain]` **EBA/GL/2026/06** (SREP y *stress testing* supervisor), publicadas el 26-jun-2026, aplicables desde el 1-ene-2027. Derogan y sustituyen las EBA/GL/2022/03 y EBA/GL/2017/05 (TIC). Añaden ASG, resiliencia operativa, sucursales de terceros países y la interacción Pilar 1/Pilar 2 con el *output floor*. **Mantienen la posibilidad de fijar la P2G y la P2G-LR cada dos años**, con revisión en el año intermedio y revisión obligada cuando hay resultados de un nuevo test supervisor (párr. 346-347). La P2G se calibra con el impacto máximo: CET1 mínimo del adverso frente al de partida (párr. 348).
- `[Likely]` **EBA/GL/2018/04** (*stress testing* de las entidades) siguen vigentes: la GL/2026/06 las cita (notas 14, 32 y 55) sin derogarlas y no hay consulta de revisión localizada.
- `[Certain]` Las comisiones se centralizaron en 2023 y el NII en 2025 (informe del BCE sobre el ST 2025, p. 17). `[Likely]` El antecedente es el documento de discusión EBA/DP/2020/01, con un enfoque de "dos patas" (banco y supervisor) que la industria rechazó; falta leerlo en fuente primaria.

## Huecos que siguen abiertos

- Nota final y escenario del 2027 (no publicados a 2026-10-16). Revisar en nov-dic 2026 y a final de enero de 2027.
- Fecha de cierre de la consulta de la nota 2027.
- Guía de plantillas 2027 y Q&A: controles automáticos de CSV_CR_SCEN y *overlays* por stage (párr. 63).
- DP/2020/01 y nota metodológica 2023 en fuente primaria (cap. 29).
- Comparación fórmula a fórmula de los recuadros 3 a 10 entre 2025 y 2027 (la lectura cruzada sugiere que son idénticos salvo fechas).
