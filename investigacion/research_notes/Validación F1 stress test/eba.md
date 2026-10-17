---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, eba, metodologia, f1, validacion]
---

# Validación F1 · EBA: metodología del ejercicio europeo (2025 final, 2027 borrador)

Validación de `investigacion/eba.md` a fecha de 2026-10-16. Fuentes primarias leídas en texto completo con pdftotext:

- **NM27**: nota metodológica 2027 en borrador, 11-jun-2026 (`fuentes/2026-06-11 EBA ST2027 draft methodological note.pdf`; [PDF EBA](https://www.eba.europa.eu/sites/default/files/2026-06/7185aac4-4a70-4d83-ae1b-1cfca979ae07/2027%20EU-wide%20stress%20test%20-%20Draft%20Methodological%20Note.pdf)).
- **NM25**: nota metodológica 2025 final, fechada en portada el 11-nov-2024 (`fuentes/2024-11 EBA ST2025 methodological note.pdf`).
- **CP-M4**: EBA/CP/2026/07, módulo 4 (*stress testing*), 10-abr-2026 ([PDF](https://eba.europa.eu/sites/default/files/2026-04/3bcb008b-2b61-4b86-8049-17c0c0aec85c/CP%20Module%204%20-%20Stress%20testing.pdf)).
- **CP-gen**: EBA/CP/2026/07, parte general ([PDF](https://www.eba.europa.eu/sites/default/files/2026-04/ec63db1e-39b5-4c78-9e20-71bdfb0eed85/EBA%20CP%202026%2007%20(Consultation%20paper%20on%20revised%20ITS%20on%20supervisory%20reporting).pdf)).
- **GL26**: informe final de EBA/GL/2026/06 ([PDF](https://www.eba.europa.eu/sites/default/files/2026-06/fd5fbfa1-2efb-4122-8e91-4831469d8150/Final%20Report%20on%20revised%20SREP%20and%20supervisory%20stress%20testing%20Guidelines.pdf)).
- **NP27**: nota de prensa de la EBA del 11-jun-2026 ([enlace](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-early-consultation-simplified-eu-wide-stress-test-climate-risk-integration)).

Los números de párrafo son del NM27 salvo que se indique otra cosa. Veredictos posibles: **Confirmado**, **Corregido**, **Refutado** y **No verificable**.

## P1. ¿Son correctas las referencias de párrafo y su contenido (sección 1 y 2 de eba.md)?

### Takeaway
Casi todas las referencias del capítulo 1 son correctas. Hay que matizar cuatro cosas: el pro-forma (párr. 15-20), la divisa (párr. 35, porque NII, NFCI y gastos sí recogen el efecto del tipo de cambio), los ratios que se reportan (párr. 26) y la base legal (el art. 32 del Reglamento 1093/2010 no aparece en el párr. 42).

### Cited Findings
- **Calendario 2025.** Veredicto: **Confirmado con matiz**, `[Certain]`. La NM25 lleva fecha de 11-nov-2024 en portada. El ejercicio 2025 se lanzó el 20-ene-2025 con un horizonte 2025-2027, y la EBA anunció resultados "a principios de agosto de 2025". No he verificado aquí ni la fecha exacta del 1-ago-2025 ni la existencia de una versión preliminar de julio de 2024: mantener `[Likely]` para esos dos puntos. Fuentes: [NM25, portada](file:fuentes/2024-11%20EBA%20ST2025%20methodological%20note.pdf); [EBA, nota de prensa del 20-ene-2025](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-its-2025-eu-wide-stress-test).
- **Publicación del borrador 2027.** Veredicto: **Confirmado**, `[Certain]`. El 11-jun-2026 se publicaron la nota, las plantillas y la guía en borrador, antes que en ciclos anteriores. La muestra es de 63 bancos (47 de la zona del euro) y cubre el 75 % del sector. — [NP27](https://www.eba.europa.eu/publications-and-media/publications-and-media/press-releases/eba-launches-early-consultation-simplified-eu-wide-stress-test-climate-risk-integration); [página EBA EU-wide stress testing](https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-stress-testing)
- **Horizonte y fecha de referencia.** Veredicto: **Confirmado**, `[Certain]`. El párr. 21 fija los escenarios 2027-2029 y el párr. 24 las cifras a cierre de 2026. Añadido: la muestra cubre "broadly 75%" del activo a cierre de 2025 en la zona del euro, en cada Estado miembro no euro y en Noruega, con un mínimo de 30.000 M€ de activo (párr. 7-8). Los bancos de menos de 50.000 M€ y los que entran por encima del 70 % de cobertura pueden aplicar la proporcionalidad del anexo VIII (párr. 9). — NM27 párr. 7-9, 21, 24
- **Bottom-up restringido (párr. 38).** Veredicto: **Confirmado**, `[Certain]`. Texto literal: "constrained bottom-up stress test with some top-down elements… For the projections of net fee and commission income and the credit loss path of sovereign exposures, banks are required to make use of prescribed parameters. Projections of interest rate margin components should follow the outcome of prescribed formulas." — NM27 párr. 38
- **Balance estático (párr. 33-34 y 36).** Veredicto: **Confirmado**, `[Certain]`. Rige en base individual, subconsolidada y consolidada. Lo que vence se sustituye por instrumentos similares en tipo, divisa, calidad crediticia y vencimiento original. No hay *workout* ni curas de S3. No se asumen medidas de capital posteriores al 31-dic-2026. Se mantienen el modelo de negocio y la presencia geográfica (párr. 33-34). No hay excepciones; las desinversiones no cerradas antes del 31-dic-2026 no se tienen en cuenta (párr. 36). Añadido: las medidas de capital completadas entre el 1-ene y el 31-mar-2027 se reportan "below the line" en CSV_CAPMEAS y no afectan a los ratios (párr. 37). — NM27 párr. 33-37
- **Divisa (párr. 35).** Veredicto: **Corregido**. La redacción del borrador es: "assets and liabilities remain fixed in the reporting currency, except for the items where stated explicitly. If the euro is not the reporting currency, all stock projections should be translated by applying the exchange rate as of 31 December 2026. In particular, FX effects should not have an impact on the projection of REA (with the exception of the market risk methodology)." La afirmación de eba.md de que "el peso mexicano no se deprecia" vale para los stocks y para el RWA. **No vale para la cuenta de resultados.** La tabla 1 dice que el NII "includes FX variations" y que la NFCI en adverso y los gastos administrativos incluyen variaciones del tipo de cambio. Redacción propuesta: «Los stocks de balance y el RWA de crédito no se mueven por el tipo de cambio; el NII, las comisiones (en adverso) y los gastos administrativos sí incorporan el efecto divisa del escenario». `[Certain]` — NM27 párr. 35; tabla 1 (filas NII y Non-interest income)
- **Sin umbral de aprobado/suspenso (párr. 30).** Veredicto: **Confirmado con matiz**, `[Certain]`. La nota 4 al pie del párr. 30 todavía remite a **EBA/GL/2022/03**: el borrador es anterior a EBA/GL/2026/06, publicada el 26-jun-2026. `[Likely]` La versión final lo actualizará a GL/2026/06. — NM27 párr. 30 y nota 4
- **Perímetro y pro-forma (párr. 13-20).** Veredicto: **Corregido (matiz)**, `[Certain]`. Los párr. 13-14 son correctos. Pro-forma:
  - solo para eventos únicos con impacto de **más del 12,5 % del activo total** (párr. 16);
  - lista cerrada de eventos: fusiones, adquisiciones, *spin-off* de unidades relevantes, desinversiones y transferencias de activos o pasivos (párr. 17);
  - solo para las partidas de resultados con *caps* o *floors* basados en datos históricos (párr. 15);
  - la autoridad competente presenta los casos a la EBA antes de la primera fecha de envío (párr. 18);
  - sin propuesta o sin reconocimiento no hay ajuste (párr. 20).
  
  La palabra "acquisitions" va en minúscula en la lista: no hay más eventos que esos cinco. — NM27 párr. 13-20
- **Modelos internos (párr. 28-29).** Veredicto: **Confirmado y completado**, `[Certain]`. Solo cuentan los modelos aprobados **e implantados** a 31-dic-2026. Excepción: un banco que cambie de enfoque regulatorio (IRB→STA o viceversa) con aprobación e implantación en el 1T 2027 puede recibir permiso para hacer el ejercicio con el nuevo régimen y reexpresar el REA de partida. — NM27 párr. 28-29
- **Tipo impositivo del 30 % (párr. 32).** Veredicto: **Confirmado**, `[Certain]`. — NM27 párr. 32
- **Resultado en CET1 (párr. 26-27).** Veredicto: **Corregido (completar)**, `[Certain]`. El impacto se reporta en CET1, y además se reportan cada año el ratio Tier 1, el ratio de capital total y la ratio de apalancamiento. Todos van en base transitoria y *fully loaded*, y los componentes transitorios se publican por separado. — NM27 párr. 26-27
- **Reparto de papeles y base legal (párr. 42).** Veredicto: **Corregido (atribución)**, `[Certain]`. El contenido del párr. 42 es correcto:
  - la JERS y el BCE elaboran el escenario adverso y el BCE aporta el base;
  - la EBA coordina, define la metodología y la guía mínima de QA, mantiene el Q&A y da estadísticas descriptivas;
  - las autoridades competentes hacen el QA, revisan los modelos, aplican la función de reacción supervisora y llevan los hallazgos al SREP.
  
  Lo que no está en el borrador es el art. 32 del Reglamento 1093/2010: el párr. 1 solo dice que la EBA está obligada a iniciar y coordinar los ejercicios en cooperación con la JERS. `[Likely]` La base legal es efectivamente el art. 32(2) de ese reglamento, pero hay que citarla del propio reglamento, no del párr. 42. El módulo climático sí cita el **art. 23** del mismo reglamento (párr. 565). — NM27 párr. 1, 42, 565

### Inferences
- `[Likely]` Para filiales en LatAm, el punto relevante del manual no es "el peso no se deprecia" sino la asimetría que deja el párr. 35. Los stocks y el RWA quedan congelados al tipo de cierre de 2026, mientras que el NII y los gastos incorporan la senda de divisa del escenario. El JST puede cuestionar la coherencia entre ambas partes.

### Gaps
- Fecha exacta de publicación de los resultados de 2025 y existencia de una versión preliminar de la NM25 en julio de 2024: no verificadas en esta pasada.

## P2. Capítulo de riesgo de crédito (párr. 45-59, 100-127, 147-156): ¿referencias y contenido correctos?

### Takeaway
El núcleo es correcto, pero hay errores de atribución:
- el suelo de titulizaciones está en el párr. 178, no en el 153;
- el "Recuadro 1" remite a los párr. 123-124 y 128;
- el criterio de país inmediato es una novedad de 2027 frente a 2025;
- la tabla de umbrales de divisa ya no usa clases regulatorias sino carteras tipo FINREP;
- la referencia normativa del umbral del 10 % es el art. 5(2) del Reglamento de Ejecución (UE) 2024/3117.

### Cited Findings
- **Tres pasos (párr. 45).** Veredicto: **Confirmado**, `[Certain]`. Parámetros de partida, impacto del escenario en los parámetros y variación del stock de provisiones que va a resultados. El párr. 45 es idéntico en NM25 y NM27. — NM27 párr. 45; NM25 párr. 45
- **Perímetro de pérdidas y de RWA (párr. 50-52).** Veredicto: **Confirmado**, `[Certain]`. Las pérdidas se calculan solo sobre coste amortizado; FVOCI, FVPL y CCR van por mercado. El REA sigue el perímetro CRR/CRD e incluye CCR y valor razonable. Añadido en la nota 7 al pie: los préstamos a FVPL financiados con cédulas a FVPL, al estilo del *balance principle* danés, entran en pérdidas de crédito. — NM27 párr. 50-52
- **Recuadro 1, supuestos IFRS 9.** Veredicto: **Confirmado con corrección de referencia**, `[Certain]`. Los supuestos son:
  - escenario único por escenario macro (párr. 128);
  - previsión perfecta (párr. 123);
  - reversión lineal en 6 años de los parámetros adversos de S1/S2 hacia los del escenario base de 2029 (párr. 124);
  - en el escenario base, los parámetros de S1/S2 se quedan planos después de 2029;
  - en S3, macro plana después de 2029 salvo el PIB, que crece constante a la tasa del último año del escenario base (párr. 123).
  
  El recuadro está en el párr. 46 y remite a los párr. 123, 124 y 128. — NM27 párr. 46 (recuadro 1), 123-124, 128
- **Recuadro 2, restricciones (párr. 49).** Veredicto: **Corregido (referencias)**, `[Certain]`. Las restricciones son:
  - no hay curas desde S3 (párr. 86);
  - no se liberan provisiones de S3, y la regla se aplica exposición a exposición (párr. 141);
  - el UTREA de crédito de cierre de 2026 hace de suelo, por separado para IRB y STA, y no se aplica al STREA (párr. 153);
  - las titulizaciones tienen un suelo análogo por método (SEC-IRBA, SEC-SA, SEC-ERBA, SEC-IAA) **en el párr. 178, no en el 153**.
  
  Fuente: NM27 párr. 49, 86, 141, 153, 178.
- **Parámetros PiT de partida (párr. 109-112).** Veredicto: **Confirmado**, `[Certain]`. Se extraen de los modelos de provisiones con los escenarios internos. Si se aproximan con datos históricos observados, solo se admiten ajustes que los hagan más conservadores (párr. 110). Hay que describir la metodología en la nota explicativa (párr. 111). Tras el envío se hace una comparación transversal entre bancos, con posible petición de revisión (párr. 112). — NM27 párr. 109-112
- **Jerarquía de enfoques (párr. 113-118).** Veredicto: **Confirmado**, `[Certain]`.
  - Los modelos propios van por delante de los *benchmarks* y se evalúan contra estándares mínimos de solidez econométrica y sensibilidad (párr. 113).
  - Sin modelo adecuado, se usan los *benchmarks* del BCE sin ajuste ni escalado, a nivel de cartera y no de grado (párr. 115).
  - La elección inicial solo cambia con permiso de la autoridad (párr. 116), que puede pedir la intención antes de publicarse el escenario (nota 20).
  - Regla del 10 %: si los satélites no cubren al menos el 10 % de la exposición de la "pivot asset class", se aplica el *benchmark* a toda la clase. Por encima del 10 %, se puede mezclar con media ponderada justificándolo (párr. 117). "Pivot asset class" es el nivel más bajo de agregación (nota 21).
  - Los *benchmarks* sirven siempre de referencia en ambos escenarios y son input obligatorio para soberanos. Si las cifras se consideran "overly optimistic" puede pedirse su revisión (párr. 118).
  
  **Sin cambios de fondo frente a 2025** (NM25 párr. 123-125). Fuente: NM27 párr. 113-118 y notas 20-21.
- **Sectores (párr. 114).** Veredicto: **Confirmado**, `[Certain]`. Hay que añadir el umbral de materialidad sectorial: una combinación de país y NACE de nivel 1 se reporta si pesa al menos el 0,5 % de la exposición total a sociedades no financieras (párr. 98). — NM27 párr. 98, 114
- **Desglose por país (párr. 100-107).** Veredicto: **Confirmado con corrección**, `[Certain]`.
  - El umbral del 10 % (exposición no doméstica ≥ 10 % del total, filas 0850/0860 de C 04.00) es el del **art. 5(2) del Reglamento de Ejecución (UE) 2024/3117**.
  - En CR_SCEN y CR_SECTOR se reportan como máximo **10 países**, y solo los no domésticos que superan el **1 %** del total.
  - En CR_REA_STA_DET y CR_REA_IRB_DET el máximo es de **5 países**, que son un subconjunto de los anteriores en el mismo orden (párr. 105-106).
  - Si la exposición doméstica supera el 90 %, todo lo no doméstico va a "Other" (párr. 100).
  - La fecha de corte para elegir los países es el 31-dic-2026, y la selección queda fija (párr. 102).
  
  Fuente: NM27 párr. 100-107.
- **Criterio de país (párr. 58-59).** Veredicto: **Confirmado, y además es una novedad no señalada en eba.md**, `[Certain]`. En CR_SCEN el país va en base **inmediata** y sin efectos de CRM (párr. 58); en el REA se aplica la base de **riesgo último** con CRM (párr. 59). En 2025, en cambio, el país era el de riesgo último para todas las plantillas (NM25 párr. 102). — NM27 párr. 58-59; NM25 párr. 102
- **Préstamos en divisa (párr. 147-148).** Veredicto: **Corregido (matiz)**, `[Certain]`. El umbral del 5 % se aplica por país de contraparte y cartera a la cuota de exposición en divisa distinta de la local del prestatario. Las TR se estresan con modelos satélite; las LR, con un *add-on* al LTV si hay garantía o un *add-on* de divisa basado en la historia si no la hay. En 2027 la tabla 10 se aplica a siete **carteras de impairment tipo FINREP**: tres de pymes (CRE, otros préstamos) y otras de sociedades no financieras, más vivienda, consumo y otros préstamos a hogares. En 2025 se aplicaba a **clases de exposición IRB y STA** (NM25 tablas 8-9). — NM27 párr. 147-148, tabla 10; NM25 párr. 154-155
- **REA bajo estrés (párr. 149-156).** Veredicto: **Confirmado**, `[Certain]`.
  - Se aplica el perímetro COREP con CCR y CRM, y la exposición en FVPL/FVOCI queda constante (párr. 149-150).
  - Hay que considerar la reestimación esperada de parámetros con datos de estrés y los suelos y escalares supervisores (párr. 152).
  - La migración de grados debe ser coherente con los flujos de *default*; el STA en *default* sin garantía pondera al 100 % o 150 % (párr. 155).
  - No hay migración entre clases de exposición (párr. 156).
  
  Añadido: el REA en *default* con LGD propia se calcula con la fórmula del recuadro 10, `MAX{0; (LGDreg − ELBE) × 12,5 × stock}` (párr. 157), y el exceso o déficit IRB se trata según el art. 159 de la CRR (párr. 161). — NM27 párr. 149-161
- **Exposición frente a la matriz (párr. 126).** Veredicto: **Confirmado**, `[Certain]`. Se trata en condiciones de mercado (*arm's length*). — NM27 párr. 126
- **Referencia del párr. 56 en eba.md.** Veredicto: **Corregido**. El párr. 56 define los stages y los POCI "in alignment with FINREP". La remisión al FINREP como fuente futura de los puntos de partida está en los **párr. 60 y 62**: este último cita la consulta EBA/CP/2026/07 del 10-abr-2026, que propone recoger en FINREP los puntos de partida de CR_SCEN. `[Certain]` — NM27 párr. 56, 60, 62

### Inferences
- `[Likely]` El paso al país inmediato y a un máximo de 10 países con umbral del 1 % reduce la granularidad para los grupos muy internacionales frente a la regla de 2025 (cobertura del 95 % o los 10 primeros países). Para Santander y BBVA probablemente no cambie la lista de países principales, pero sí cómo se asignan las exposiciones garantizadas o con riesgo transfronterizo.

### Gaps
- No he leído en detalle las secciones 2.3.3 a 2.3.8 (variables de CR_SCEN, clases de activo y *overlays* por stage). En el párr. 63 aparecen los "Overlays S1/S2/S3/POCI" tal como los define la consulta; no he comprobado si son una novedad frente a 2025.

## P3. NII y NFCI: ¿qué es nuevo en 2027 y qué dice exactamente la EBA sobre el NII "top-down"?

### Takeaway
**Corregido.** El párr. 38 de 2027 añade de forma explícita que los componentes del margen siguen "fórmulas prescritas", y la nota de prensa presenta NII y NFCI como "supervisory top-down elements". Pero las fórmulas de margen (pasivo con γ × max(Δ diferencial soberano, Δ idiosincrático); activo con λ × max(Δ diferencial soberano, 0)) y el "NII centralised approach" **ya existían en 2025**. Lo que cambia sobre todo es la etiqueta y algo más de centralización, no el mecanismo. Además, 2025 incluía las ponderaciones de titulizaciones entre lo prescrito y 2027 las saca.

### Cited Findings
- **Párr. 38 de 2025.** `[Certain]` Texto: "For the projections of net fee and commission income, risk weights of securitisations, and the credit loss path of sovereign exposures, banks are required to make use of prescribed parameters." No menciona el NII. — NM25 párr. 38
- **Párr. 38 de 2027.** `[Certain]` NFCI y senda de pérdidas soberanas con parámetros prescritos; "Projections of interest rate margin components should follow the outcome of prescribed formulas". — NM27 párr. 38
- **Nota de prensa.** `[Certain]` Habla de "supervisory top-down elements, including projections of net interest income and net fee and commission income". — [NP27](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-early-consultation-simplified-eu-wide-stress-test-climate-risk-integration)
- **Fórmulas de margen en 2025.** `[Certain]` Ya estaban en la NM25: margen de pasivos nuevos en el párr. 422 y recuadro 23, margen de activos nuevos en el párr. 425 y recuadro 24. En 2027 son idénticas: párr. 426 y recuadro 20, y párr. 429 y recuadro 21. Las γ por tipo de pasivo del recuadro 20 de 2027 son 0 para bancos centrales, 1 para entidades de crédito, 0,1 para la vista de hogares, 0,75 para valores emitidos, etc. — NM25 párr. 422, 425; NM27 párr. 423, 426, 429
- **"NII centralised approach".** `[Certain]` Existía en ambos ejercicios. En las carteras dentro de su alcance, las proyecciones se rellenan en CSV_NII_CALC con las fórmulas del anexo VII (2027) o del anexo VIII (2025). En derivados, el banco solo proyecta el margen. **Novedad 2027:** el reparto margen/tipo de referencia del *new business* de partida (2026) se hace de forma centralizada (párr. 382 y 384). — NM27 párr. 382, 384; NM25 párr. 378
- **Restricciones de NII que siguen.** `[Certain]` En adverso, el NII no puede subir frente a 2026 a nivel de grupo (párr. 408-409). Los ingresos de dudosos van netos de provisiones, con *cap* al EIR en adverso (párr. 411). Las cuentas a la vista repreciaban de inmediato según la metodología (párr. 397, 401). El NII de la cartera de negociación se fija en la media 2024-2026 (párr. 434). — NM27 recuadro 17 (párr. 351)
- **Titulizaciones.** `[Certain]` En 2025 se aplicaba "a fixed risk weight increase… to the different credit quality steps". En 2027 el banco proyecta él mismo la migración de grados y los KIRB/KSA del subyacente (párr. 175-176), con suelo en el REA de 2026 por método (párr. 178). — NM25 párr. 48 y recuadro 2; NM27 párr. 175-178
- **Fuente secundaria.** `[Likely]` Management Solutions resume 2027 como "top-down elements (NFCI projections and centralization of NII projections)". — [Management Solutions, EU-wide Stress Test 2027](https://www.managementsolutions.com/sites/default/files/publicaciones/eng/eu-wide-stress-test-2027.pdf)

### Inferences
- `[Likely]` La afirmación de eba.md de que "el NII entra en la lista de lo prescrito; la frontera se estrecha" sobrevalora el cambio. En 2025 el banco ya proyectaba volúmenes y repreciación, pero los márgenes nuevos seguían fórmulas prescritas y parte del cálculo estaba centralizado. Redacción propuesta: «En 2027 la EBA califica ya expresamente el NII como elemento top-down (párr. 38 y nota de prensa). En la práctica, las fórmulas de margen y el cálculo centralizado ya existían en 2025; el cambio es sobre todo de etiqueta y de centralización del punto de partida. En sentido contrario, las titulizaciones dejan de tener ponderaciones prescritas y pasan a proyección propia.» Con esta redacción, el crédito sigue siendo el gran bloque *bottom-up*, y ahora también lo son las titulizaciones.

### Gaps
- No he comparado los anexos VII (2027) y VIII (2025) fórmula a fórmula; puede haber cambios menores en el alcance del enfoque centralizado.

## P4. Hueco: sección 2.4.3 (cálculo de S3 y provisiones) y anexo IV (restricciones clave)

### Takeaway
No hay suelos de cobertura regulatorios explícitos (ni *backstop* de NPE ni *floors* de LGD) ni suelos derivados de los *benchmarks*. La disciplina viene de cuatro sitios:
1. fórmulas de provisiones prescritas para cada flujo entre stages;
2. no liberar provisiones de S3, exposición a exposición;
3. un suelo implícito de cobertura del S3 antiguo igual a su provisión de partida;
4. parámetros soberanos del BCE obligatorios, más la comparación con *benchmarks* y entre bancos en el QA.

### Cited Findings
- **Principio general.** `[Certain]` Se aplica un único escenario por escenario macro (párr. 128). Las pérdidas adicionales se contabilizan como "impairment of financial assets other than instruments designated at fair value through P&L" (párr. 129). Con previsión perfecta, el lifetime ECL de S2/S3 y de los flujos S1→S2/S3 incorpora todo el escenario. Ejemplo literal: una caída del 10 % del precio de la vivienda en el horizonte "should be reflected in the impairment loss for old S3 exposures already in 2027" (párr. 130). — NM27 párr. 128-130
- **Stock de provisiones (recuadro 3, párr. 131).** `[Certain]`
  - S1 = provisiones de S2→S1 + provisiones de S1→S1.
  - S2 = provisiones de S1→S2 + provisiones de S2→S2.
  - S3 = acumulado de S1→S3 + acumulado de S2→S3 + S3 antiguo.
  
  En POCI el banco rellena directamente el stock proyectado de provisiones (párr. 132); los POCI son estáticos y no migran (párr. 86). — NM27 párr. 86, 131-133
- **Fórmulas prescritas por flujo.** `[Certain]`
  - **Nuevos S1** (recuadro 4): `Exp S2(t) × TR2-1(t+1) × PD12M S1(t+2) × LGD S1(t+2)`.
  - **S1 existentes** (recuadro 5): `Exp S1(t) × [1 − TR1-2(t+1) − PD12M S1(t+1)] × PD12M S1(t+2) × LGD S1(t+2)`.
  - En 2029, el escenario base usa los parámetros de 2029 (planos). El adverso pondera **5/6 los parámetros adversos y 1/6 los del base de 2029** por la reversión a 6 años.
  - **Nuevos S2** (recuadro 6): `Exp S1(t) × TR1-2(t+1) × LRLT S2(t+1)`.
  - **S2 existentes** (recuadro 7): `Exp S2(t) × [1 − TR2-1(t+1) − PD12M S2(t+1)] × LRLT S2(t+1)`, con una LRLT *forward-looking*.
  - **Nuevos S3** (recuadro 8): `Exp S1(t) × PD12M S1(t+1) × LGD S1(t+1) + Exp S2(t) × PD12M S2(t+1) × LGD S2(t+1)`. Se acumulan a lo largo del horizonte porque no se pueden liberar.
  
  Fuente: NM27 párr. 134-142 y recuadros 4-8.
- **S3 antiguo (recuadro 9, párr. 143-144).** `[Certain]` `Prov Old S3(t+1) = MAX{Exp S3(t=0) × LGD S3(t=1); Prov S3(t=0)}`. Se calcula con el parámetro del primer año y previsión perfecta. **Para el manual: es un suelo de cobertura implícito**: la provisión del S3 de partida nunca baja de la de cierre de 2026, y cualquier deterioro de garantías del escenario se carga entero en 2027. — NM27 párr. 143-144
- **Sin liberación de provisiones de S3 (párr. 141).** `[Certain]` "No release of accumulated provisions for any given S3 exposure is permitted for any year or scenario and this restriction shall be applied at the exposure level." — NM27 párr. 141
- **Balance estático en crédito (párr. 86-87).** `[Certain]` Los S3 no se reponen: los nuevos S3 reducen S1/S2 manteniendo la exposición total. No hay curas ni bajas (fallidos, ventas de NPL) en los 3 años. El vencimiento residual se mantiene constante a efectos de REA. — NM27 párr. 86-87
- **Soberanos (párr. 145-146).** `[Certain]` Afecta solo a "General governments" a coste amortizado. **Los bancos centrales tienen tasa de pérdida cero** en ambos escenarios. Los parámetros estresados del BCE (PD/TR, LGD, LR) son **obligatorios para todos los bancos y todos los países** cubiertos, se reporte o no el país por separado. En los países sin parámetros del BCE, el banco estima con conservadurismo siguiendo la jerarquía de enfoques. Base: párr. 23 ("prescribed shocks to credit risk losses for sovereign exposures"). — NM27 párr. 23, 145-146
- **Anexo IV, tabla 29 (crédito sin titulizaciones).** `[Certain]`
  - no liberación de provisiones de S3 (párr. 141);
  - no reducción del stock de provisiones del S3 antiguo (recuadro 9, implementado en CSV_CR_SCEN);
  - sin *workout* ni curas (párr. 33);
  - el REA IRB y el REA STA para el UTREA no pueden bajar (párr. 153);
  - la exposición para el REA no se ve afectada por fluctuaciones de valor de mercado (párr. 89);
  - fórmulas prescritas de los recuadros 3 a 9 y del recuadro 10 (REA en *default*).
  
  El anexo aclara que solo resume lo que ya está en la nota y que **no añade requisitos** (párr. 594). La misma tabla se aplica al módulo climático "where relevant" (párr. 595). — NM27 anexo IV, párr. 594-595, tabla 29
- **Anexo IV, tabla 30 (titulizaciones).** `[Certain]` Los ajustes específicos se restan de la exposición (párr. 170). El REA antes de ajustes y reducciones de SEC-IRBA, SEC-SA, SEC-ERBA y SEC-IAA no puede bajar frente al punto de partida, y los ajustes no se ven afectados por el suelo (párr. 178). — NM27 anexo IV, tabla 30
- **Diferencia con el anexo IV de 2025.** `[Certain]` La tabla 27 de 2025 incluía además: "At the exposure level, funded collateral cannot be higher than the respective exposure (Paragraph 66)". Esa fila no aparece en la tabla 29 de 2027. — NM25 anexo IV, tabla 27
- **Suelos de cobertura.** `[Certain]` No hay suelos de cobertura por *vintage* ni *benchmark floors* en crédito. En el capítulo 2 de 2027, los únicos "floor" son los de REA (párr. 49, 153, 178). Lo único que recuerda a un suelo de LGD es que la LGD/LR en S3 debe recoger supuestos prudentes de cura implícita y costes de liquidación (párr. 122) y la caída del valor de las garantías (párr. 121). El párr. 152 menciona los "regulatory floors and/or parameter-level supervisory scalars" de los modelos IRB a efectos de REA. — NM27 párr. 121-122, 152; búsqueda de "floor" y "cap" en el capítulo 2

### Inferences
- `[Likely]` El conservadurismo de 2027 en crédito no se impone con números fijos en la nota. Se impone con la comparación con los *benchmarks* del BCE y entre bancos durante el QA (párr. 112, 118). Por eso el "*challenge*" del JST es el mecanismo real de suelo y el manual debe tratarlo como tal.

### Gaps
- La guía de plantillas y el Q&A pueden contener controles adicionales (por ejemplo, comprobaciones automáticas en CSV_CR_SCEN) que no he revisado.

## P5. Hueco: capítulo 7, módulo climático

### Takeaway
Es un módulo **solo de pérdidas por riesgo de crédito** (sin REA), aplicado como *overlay* sobre el escenario adverso. Tiene dos partes:
- **transición**: 2027-2029, sociedades no financieras de sectores NACE A-H y M e hipotecas por eficiencia energética;
- **física**: inundación fluvial con probabilidad del 1 %, solo en 2027, garantías inmobiliarias y sociedades no financieras del EEE, con resultados brutos y netos de seguros.

La nota de prensa dice que no afectará a los resultados principales; el capítulo 7 no lo dice con esas palabras, pero lo encaja al limitarse a la cuenta de resultados en plantillas propias.

### Cited Findings
- **Base legal y diseño.** `[Certain]` Se apoya en el art. 23 del Reglamento 1093/2010 (párr. 565). Los shocks de transición y de inundación se aplican "in conjunction with, and as complementary overlays to, the adverse macro financial scenario" (párr. 566). Los escenarios los elaboran la JERS y el BCE (párr. 567). El escenario base climático es el base macro (párr. 570). — NM27 párr. 565-567, 570
- **Escenarios.** `[Certain]` Transición: giro brusco y estricto de la política climática en un mundo dependiente de combustibles fósiles, durante 2027-2029. El banco elige uno de dos juegos de shocks: (1) variables climáticas (precio del carbono, sendas de GEI por país, precios de gas y petróleo) o (2) shocks de VAB por país en NACE 1 y NACE 2. Físico: inundación fluvial con 1 % de probabilidad, según los mapas del JRC, simultánea en todo el EEE, **solo en el año 1 (2027)** y sin efectos de segunda ronda sobre la macro. — NM27 párr. 568, 570, 589; recuadro 29
- **Perímetro (párr. 571-573).** `[Certain]`
  - Solo exposiciones en balance a coste amortizado (más los préstamos FVPL financiados con cédulas al estilo danés); en riesgo físico, solo "Loans and advances". Sin riesgo de mercado.
  - **Solo efecto en resultados, sin REA** (párr. 572).
  - Transición: préstamos y valores frente a sociedades no financieras de NACE 1 en los sectores A-H y M (los de alta contribución según el Reglamento 2020/852), más NACE 2 materiales (≥ 0,5 % de la exposición a sociedades no financieras del país); y préstamos para vivienda por tramo de eficiencia energética, sin umbral.
  - Física: préstamos con garantía inmobiliaria en el EEE y sociedades no financieras del EEE de todos los sectores.
  
  Fuente: NM27 párr. 571-573, 584 y notas 78-79.
- **Supuestos (párr. 576-577).** `[Certain]` Balance estático. No se suponen renovaciones energéticas, recuperación de inmuebles dañados ni acciones de gestión de mitigación. — NM27 párr. 576-577
- **Reporting (párr. 578-583).** `[Certain]` Plantillas CSV_CL_TR (transición) y CSV_CL_PR (física). Los países son los mismos que en CR_SCEN; en riesgo físico, limitados al EEE y con categorías de severidad de inundación. Las carteras físicas siguen la provisional FINREP F 49 (tabla 18). — NM27 párr. 578-583, tabla 18
- **Proyección de parámetros PiT (párr. 584-591).** `[Certain]`
  - **Partida:** coherente con el párr. 2.4.1; en transición, por NACE material y por intensidad energética; en física, por categoría de exposición a inundación (párr. 584).
  - **Proyección:** con modelos internos, PD/TR y LR/LGD estresados, transición en los 3 años y física en el año 1 (párr. 585-586).
  - **Riesgo físico:** se geolocaliza cada garantía (latitud y longitud) contra el mapa del JRC y se aplica una **función de daño** que se traduce en un shock adicional al precio del inmueble y en la LGD del año 1 (párr. 587). Las PD de las sociedades no financieras afectadas suben en el año 1, con posible migración inmediata a S2 o S3 (párr. 588). Hay que usar métricas de daño de cola, no daño medio anual (párr. 590). Los parámetros se reportan antes de seguros (párr. 591).
  - **Canales de transmisión (recuadro 30):** para transición, costes operativos, capex de descarbonización, sustitución tecnológica, demanda y, en vivienda, la asequibilidad por coste energético y el efecto de la eficiencia en el valor de la garantía. Los shocks climáticos "should not replace or offset the macro-financial stress".
  
  Fuente: NM27 párr. 584-591, recuadro 30.
- **Provisiones (párr. 592).** `[Certain]` Mismo mecanismo de transiciones entre stages que en crédito. Recuadro 31: deterioro bruto (sin seguro, con parámetros granulares) y neto de seguros (solo stock total, separando seguro privado y esquemas públicos), con tasa de cobertura de seguro privado, retrasos y conservadurismo. No se cuentan pérdidas soportadas por aseguradoras del grupo. — NM27 párr. 592, recuadro 31
- **Consulta abierta.** `[Certain]` El capítulo incluye una "Question for banks" sobre el alcance del riesgo físico y el tratamiento de las sociedades no financieras y la interrupción de negocio, lo que indica que esta parte puede cambiar en la versión final. — NM27, final del capítulo 7
- **Relación con los resultados principales.** `[Certain]` La nota de prensa dice que el módulo "will not affect the core stress test results". — [NP27](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-early-consultation-simplified-eu-wide-stress-test-climate-risk-integration). `[Likely]` En el NM27 lo apoyan el párr. 572 (sin REA), las plantillas separadas y el carácter de *overlay*, pero el capítulo 7 no lo dice textualmente.
- **Carácter de corto plazo.** `[Certain]` La EBA "intends to integrate a short-term climate risk component into the 2027 EU-wide stress test… a dedicated module covering both physical and transition risks". — [CP-M4, nota 1](https://eba.europa.eu/sites/default/files/2026-04/3bcb008b-2b61-4b86-8049-17c0c0aec85c/CP%20Module%204%20-%20Stress%20testing.pdf)

### Inferences
- `[Likely]` Para Santander y BBVA, el riesgo físico se limita al EEE: no capta inundaciones en México, Brasil o EE. UU. La transición, en cambio, sí sigue la lista de países de CR_SCEN, que puede incluir países no UE.

### Gaps
- Las cifras del escenario climático (precio del carbono, shocks de VAB) no están publicadas; se publicarán con el lanzamiento.
- No he revisado la tabla 7 de la guía de plantillas (criterios de exposición alta, moderada o no significativa).

## P6. ¿Hay nota final 2027, escenario o fecha de lanzamiento desde el 11-jun-2026? ¿Qué calendario?

### Takeaway
A 2026-10-16 no he encontrado nota final, escenario ni calendario oficial de la EBA; en su página del ejercicio solo figuran los documentos en borrador del 11-jun-2026. El calendario que circula (nota final a final de 2026, lanzamiento a final de enero de 2027, envíos de marzo a junio de 2027, resultados en agosto de 2027) es una **expectativa** de consultoras construida por analogía con 2025.

### Cited Findings
- **Estado de la página de la EBA.** `[Certain]` En la página de *stress testing* solo aparecen la nota, la guía y las plantillas en borrador del 11-06-2026. No figuran nota final, escenario ni fechas. — [EBA, EU-wide stress testing](https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-stress-testing)
- **Nota de prensa.** `[Certain]` Da fecha de cierre de la consulta de la nota metodológica y anuncia talleres con la industria. — [NP27](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-early-consultation-simplified-eu-wide-stress-test-climate-risk-integration)
- **Calendario esperado por KPMG (25-ago-2026), explícitamente "expected" y "similar to the 2025 exercise".** `[Likely]`
  - nota final a final de 2026;
  - final de enero de 2027: lanzamiento con escenarios y plantillas;
  - febrero de 2027: envío de COREP/FINREP;
  - marzo de 2027: primer envío (ADC);
  - abril de 2027: FDC 1;
  - junio de 2027: FDC 2;
  - agosto de 2027: publicación de resultados.
  
  Fuente: [KPMG Irlanda](https://kpmg.com/ie/en/insights/banking/eba-2027-stress-test.html).
- **Indicios en el propio borrador.** `[Certain]` Hay "three submission dates" y las medidas de capital se recogen hasta el 31-mar-2027 (párr. 37). La fecha de corte de la información de conducta aparece como "DD June 2027", un marcador pendiente de rellenar (párr. 464). `[Likely]` Esto encaja con un último envío en junio de 2027. — NM27 párr. 37, 464
- **Precedente 2025.** `[Certain]` El ejercicio 2025 se lanzó el 20-ene-2025 y la EBA anunció resultados para principios de agosto de 2025. — [EBA, 20-ene-2025](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-its-2025-eu-wide-stress-test)
- **Consulta del módulo de reporting.** Veredicto: **Confirmado y elevado a `[Certain]`** (eba.md lo tenía como `[Likely]`). La consulta EBA/CP/2026/07 cerró el 10-jul-2026 a las 23:59 CEST. — [CP-gen](https://www.eba.europa.eu/sites/default/files/2026-04/ec63db1e-39b5-4c78-9e20-71bdfb0eed85/EBA%20CP%202026%2007%20(Consultation%20paper%20on%20revised%20ITS%20on%20supervisory%20reporting).pdf)
- **Fecha de cierre de la consulta de la nota metodológica.** `[Guessing]` Un buscador devolvió "7 de agosto de 2026" sin que pudiera localizar la fuente; KPMG no la da. Tratar como no verificable.

### Inferences
- `[Likely]` La afirmación `[Guessing]` de eba.md (nota final a final de 2026, lanzamiento en enero de 2027, resultados a final de julio de 2027) debe ajustarse así: «resultados previsiblemente a principios de agosto de 2027 (precedente 2025; KPMG), sin fecha oficial de la EBA». Se mantiene la etiqueta `[Guessing]`/`[Likely]`.

### Gaps
- No hay confirmación primaria del calendario 2027. Hay que revisar la página de la EBA antes de redactar la Parte III, porque la nota final podría publicarse en noviembre o diciembre de 2026.

## P7. ¿Respalda una fuente primaria que la integración completa en FINREP/COREP llega en el ejercicio de 2029?

### Takeaway
**Sí. Veredicto: Confirmado, y se eleva de `[Likely]` a `[Certain]`** como propuesta en consulta. El módulo 4 de EBA/CP/2026/07 lo dice literalmente. Matiz: es una propuesta de ITS en consulta, aún no adoptada por la Comisión.

### Cited Findings
- **Texto del módulo 4.** `[Certain]` "This proposal would apply for the 2029 stress test and onwards (as FINREP/COREP amendments are planned to have as first reference as of September 2027). Still for the 2027 stress test, the stress test templates will mimic the FINREP/COREP/ESG reporting proposals included in the amended ITS on supervisory reporting." La integración cubre **solo los puntos de partida**; las proyecciones se quedan en plantillas ad hoc. — [CP-M4, párr. 6](https://eba.europa.eu/sites/default/files/2026-04/3bcb008b-2b61-4b86-8049-17c0c0aec85c/CP%20Module%204%20-%20Stress%20testing.pdf)
- **Calendario del ITS revisado.** `[Certain]` Primer reporting con fecha de referencia del 30-sep-2027; el reglamento "shall apply from 28 September 2027"; informe final a la Comisión a final de 2026. — [CP-gen, "Next steps" y art. 3 del borrador](https://www.eba.europa.eu/sites/default/files/2026-04/ec63db1e-39b5-4c78-9e20-71bdfb0eed85/EBA%20CP%202026%2007%20(Consultation%20paper%20on%20revised%20ITS%20on%20supervisory%20reporting).pdf)
- **Plantillas de crédito.** `[Certain]` Los datos de crédito para *stress test* entran en FINREP (nuevas F 49/F 50) y en ESG (D 01.00, sectorial y transición). — [CP-M4, párr. 8-9](https://eba.europa.eu/sites/default/files/2026-04/3bcb008b-2b61-4b86-8049-17c0c0aec85c/CP%20Module%204%20-%20Stress%20testing.pdf); NM27 párr. 62, 97, tabla 18
- **Crítica de la industria.** `[Certain]` AFME sostiene que los parámetros que pide F 49.01 (PD a 12 meses por stage, LGD, tasas de transición, LTV) no son datos contables y que FINREP no es el vehículo adecuado. — [AFME, respuesta al módulo 4](https://www.afme.eu/media/5jybqs2g/module-4-stress-testing.pdf) (vía resumen del buscador; no leído en directo)

### Inferences
- `[Likely]` La observación de eba.md para el manual (las diferencias de perímetro entre el FINREP consolidado y el reporting local aflorarán como errores de conciliación) sigue siendo válida, pero aplica de lleno al ejercicio de 2029, no al de 2027.

### Gaps
- No se sabe si el ITS final (previsto para final de 2026) mantiene la fecha de septiembre de 2027 ni la secuencia hasta 2029.

## P8. EBA/GL/2026/06 y estado de EBA/GL/2018/04

### Takeaway
GL/2026/06 queda **confirmada**: publicada el 26-jun-2026 y aplicable desde el 1-ene-2027. Deroga **EBA/GL/2022/03 y EBA/GL/2017/05** (las de evaluación TIC). Hay que corregir eba.md, que decía "las de TIC" sin número. El texto final **mantiene la opción de fijar la P2G cada dos años**, con revisión en el año intermedio. GL/2018/04 sigue citada como vigente en GL/2026/06; no he encontrado revisión en curso.

### Cited Findings
- **Identificación y vigencia.** `[Certain]` Referencia EBA/GL/2026/06. "The Guidelines will apply from 1 January 2027." Derogan y sustituyen EBA/GL/2022/03 y EBA/GL/2017/05. Integran ASG, resiliencia operativa y DORA, sucursales de terceros países (art. 48n(6)(a) de la CRD VI) y el *output floor* (art. 104a(7) de la CRD VI), con la interacción P1/P2. — [EBA, nota de prensa del 26-jun-2026](https://www.eba.europa.eu/publications-and-media/press-releases/eba-reaches-another-important-milestone-enhancing-supervisory-efficiency-its-revised-srep-guidelines); [GL26, portada y párr. de derogación](https://www.eba.europa.eu/sites/default/files/2026-06/fd5fbfa1-2efb-4122-8e91-4831469d8150/Final%20Report%20on%20revised%20SREP%20and%20supervisory%20stress%20testing%20Guidelines.pdf)
- **Frecuencia de la P2G.** `[Certain]` Las autoridades "may determine P2G and P2G-LR only every second year instead of annually, including for SREP Category 1 institutions. However, in the year that follows the year of determining P2G, competent authorities should assess whether P2G and P2G-LR are still relevant or need to be updated, on the basis of all relevant information, including outcomes of past supervisory stress tests, together with additional sensitivity analysis". Además, deben revisar la P2G cada vez que haya resultados de un nuevo *stress test* supervisor. La frecuencia mínima es la del modelo de mínima interacción del SREP. — GL26 párr. 346-347
- **Papel del *stress testing* supervisor.** `[Certain]`
  - La P2G se fija con el escenario adverso de los *stress tests* supervisores, "including the EU-wide stress tests performed by the EBA", con horizonte de al menos 2 años (párr. 344), y para proteger frente al incumplimiento del TSCR (párr. 343).
  - Se calibra con el **impacto máximo**: CET1 mínimo del escenario adverso frente al CET1 de partida (párr. 348); la P2G-LR, análogamente con la ratio de apalancamiento (párr. 349).
  - Se compensa con el colchón de conservación de capital y se puede ajustar por el balance estático o el desfase temporal (párr. 350).
  - Para entidades que no son de categoría 1 y filiales de grupos transfronterizos caben *stress tests* simplificados (párr. 345).
  
  Fuente: GL26 párr. 342-350.
- **Diseño de futuros ejercicios.** `[Certain]` Ante la petición de la industria de no introducir escenarios ASG antes del ejercicio de 2029, la EBA responde que el diseño de futuros EU-wide "is outside the scope of these guidelines". — GL26, tabla de comentarios recibidos
- **GL/2018/04.** `[Certain]` GL/2026/06 la cita en varias notas al pie como "EBA Guidelines on institutions' stress testing (EBA/GL/2018/04)", sin indicar su derogación. — GL26, notas 14, 32 y 55. `[Likely]` Sigue vigente. No he encontrado consulta de revisión en curso (búsqueda web sin resultados). Mantener `[Likely]` en vez de `[Guessing]`.

### Inferences
- `[Likely]` La P2G bienal encaja con la cadencia bienal del ejercicio europeo: el JST puede fijar la P2G de Santander y BBVA en 2027 con el EU-wide y revisarla en 2028 con sensibilidades.
- `[Likely]` El borrador NM27 (párr. 30, nota 4) cita todavía GL/2022/03 porque es anterior al 26-jun-2026.

### Gaps
- No he confirmado si la EBA tiene en su programa de trabajo una revisión de GL/2018/04.

## P9. Diferencias 2025 vs 2027 en riesgo de crédito que eba.md no recoge, y otras afirmaciones

### Takeaway
eba.md omite varios cambios relevantes:
1. 2027 elimina el *backstop* de SICR (triplicar la PD lifetime) y el umbral de bajo riesgo del 0,30 %, y deja de equiparar S3 a NPE: se usa el S3 contable IFRS 9.
2. El desglose por país pasa de "95 % o 10 primeros países, riesgo último" a "art. 5(2) del ITS, 10 países, 1 %, base inmediata".
3. Las titulizaciones pasan de un aumento fijo de ponderaciones a proyección propia.
4. Las carteras de los umbrales de divisa pasan de clases regulatorias a carteras de tipo FINREP.
5. Los puntos de partida se piden a cierre de 2025 y de 2026, con POCI aparte.

### Cited Findings
- **SICR.** `[Certain]` En 2025 se exigía que las exposiciones S1 con una PD lifetime tres veces mayor que la inicial pasaran a S2 (con TR1-3 como aproximación), y había bajo riesgo de crédito si la TR1-3 era menor del 0,30 %. En 2027 hay que "project significant increase in credit risk in line with their accounting approaches"; el término "threefold" y el 0,30 % no aparecen en el NM27. — NM25 párr. 56; NM27 párr. 56
- **S3 y NPE.** `[Certain]` El recuadro 1 de 2025 incluía "A common definition of S3 assets as non-performing exposures is applied for the starting point and for the projections". El recuadro 1 de 2027 no lo incluye: S3 se define como "credit-impaired" según el apéndice A de IFRS 9, y POCI se reporta aparte "in alignment with FINREP". — NM25 recuadro 1, párr. 46; NM27 párr. 56
- **Puntos de partida.** `[Certain]` 2027 pide cierre de 2025 y de 2026 (párr. 56). 2025 pedía 2024 real y "restated" por la CRR3. — NM27 párr. 56; NM25 párr. 56
- **País.** `[Certain]` En 2025 se pedía cobertura mínima del 95 % de la exposición y los 10 primeros países, en base de riesgo último. 2027 aplica las reglas de los párr. 58-59 y 100-107 descritas en P2. — NM25 párr. 102-105
- **Titulizaciones y divisa.** `[Certain]` Ver P3 (titulizaciones) y P2 (divisa). — NM25 párr. 48, tablas 8-9; NM27 párr. 148, 175-178
- **Lo que no cambia.** `[Certain]` Reversión lineal a 6 años, previsión perfecta, regla del 10 % de la "pivot class", no liberación de provisiones de S3, suelos de REA de crédito y titulizaciones. — NM25 recuadros 1-2, párr. 124; NM27 recuadros 1-2, párr. 117
- **Reducción del 55 % de datos.** `[Certain]` "Cuts required data points by 55%" frente al ejercicio anterior. — [NP27](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-early-consultation-simplified-eu-wide-stress-test-climate-risk-integration)
- **Antecedentes (EBA/DP/2020/01 y comisiones top-down desde 2023).** Veredicto: **No verificable con las fuentes de esta pasada**: ni la NM25 ni la NM27 citan el DP/2020/01 ni el ejercicio de 2023. `[Likely]` por conocimiento previo; si el manual lo afirma, hay que bajarlo de `[Certain]` a `[Likely]` hasta contrastarlo con el DP/2020/01 y la nota metodológica de 2023.

### Inferences
- `[Likely]` Quitar el *backstop* de triplicar la PD y la equiparación S3 = NPE acerca el ejercicio a la contabilidad del banco (coherente con la integración FINREP). Pero desplaza el *challenge* del JST hacia los criterios de SICR propios de cada banco, que pasan a ser una fuente de dispersión entre entidades.

### Gaps
- No he comparado fórmula a fórmula los recuadros 3 a 10 de 2025 y 2027; la lectura cruzada sugiere que son idénticos salvo fechas.
- DP/2020/01 y la nota metodológica de 2023 están pendientes de lectura primaria.
