---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, reguladores, validacion, f1, eeuu, reino-unido, mexico, brasil, chile, turquia, argentina, polonia]
---

# Validación F1 · Reguladores de fuera de la UE (filiales de Santander y BBVA)

Validación de `investigacion/reguladores-no-ue.md` a fecha de 2026-10-16. Veredictos posibles: **Confirmado**, **Corregido**, **Refutado** y **No verificable**. Cada fila da la redacción corregida en español, la etiqueta de confianza que merece ahora y la fuente exacta. Las fuentes locales están en `investigacion/fuentes/`. El resto se consultó en la web el 2026-10-16.

Nota de método: tres fuentes no se pudieron leer directamente. bcentral.cl está detrás de un muro anti-bots (Incapsula). La guía de la BDDK está tras un muro de pago. El texto ordenado de la BCRA sobre gestión de riesgos da 404. En esos casos se indica qué se leyó en su lugar.

## 0. Mapa comparable (perfil por jurisdicción)

### Takeaway
`[Certain]` Hay tres familias de ejercicio: (a) **el supervisor proyecta** con sus modelos (Fed, Banxico, BCB, BCCh); (b) **el banco proyecta** escenarios que da el supervisor (CNBV con escenarios supervisores; CMF dentro del IAPE con parámetros de la CMF; BCRA dentro del IAC con variables del BCRA); (c) **mixto** (Banco de Inglaterra: el banco proyecta y el Banco ajusta, con acciones de gestión). Las métricas de salida, los umbrales y la base contable de las provisiones difieren en cada país. Por eso la comparación con el número del grupo en el EBA necesita un puente explícito.

### Cited Findings

| Rasgo | EE. UU. (Fed) | Reino Unido (BoE, BCST 2025) | México: CNBV (escenarios supervisores) | México: Banxico (REF) | Brasil (BCB, REF) | Chile: CMF (IAPE) | Chile: BCCh (IEF) | Türkiye (BDDK) | Argentina (BCRA) |
|---|---|---|---|---|---|---|---|---|---|
| Quién proyecta | Supervisor, con modelos propios [Certain] ([Fed 2026](https://www.federalreserve.gov/publications/2026-june-dodd-frank-act-stress-test-results.htm)) | Bancos y Banco; el Banco ajusta lo que envían los bancos [Certain] ([FSR dic-2025](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025)) | Banco, con escenarios de la CNBV [Certain] ([CUB art. 2 Bis 117 e-g](https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf)) | Banxico, top-down [Certain] (REF jun-2026, local) | BCB, top-down banco a banco [Certain] (REF abr-2025, anexo "Conceitos e Metodologias") | Banco, con parámetros agregados de la CMF y estimaciones propias [Certain] ([RAN 21-13](https://www.cmfchile.cl/portal/normativa/624/articles-29808_doc_pdf.pdf)) | BCCh, para el sistema [Likely] ([DT 801](https://ideas.repec.org/p/chb/bcchwp/801.html)) | Banco en su ISEDES; la BDDK además hace macro stress [Likely] | Banco, dentro del IAC, con variables del BCRA [Likely] ([Com. A 6646](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6646.pdf)) |
| Escenarios | Fed: base y *severely adverse*, más el *global market shock* para los bancos con mucha cartera de negociación [Certain] | Un escenario adverso del Banco, más análisis de sensibilidad [Certain] | Fijados por la CNBV mediante oficio [Certain] (art. 2 Bis 117 f) | 3 hipotéticos (A, B, C) y 3 históricos (H1 1995, H2 2008, H3 COVID-19) [Certain] | Base (Focus), Recessão Aguda y Crise de Confiança, más sensibilidades [Certain] | Base, tensión sin mitigación y tensión con mitigación [Certain] | Escenario severo, en el IEF semestral [Likely] | Los diseña el banco (guía BDDK 2016) [Likely] | Variables de estrés del BCRA más las del banco [Likely] |
| Horizonte | 9 trimestres (2026:T1-2028:T1) [Certain] | 5 años [Certain] ([Key elements](https://www.bankofengland.co.uk/stress-testing/2025/key-elements-bank-capital)) | Al menos 9 trimestres [Certain] (art. 2 Bis 117 g) | 3 años [Certain] | 12 trimestres [Certain] | 3 años [Certain] | Falta contexto | Falta contexto | Falta contexto (plan de negocios a 2 años en 2019/2020) |
| Balance | Supuestos de capital fijados por la norma (12 CFR 252.44(c)); balance: falta contexto | Dinámico: el banco atiende la demanda de crédito (crédito +6,5 % en el horizonte) [Certain] | Dinámico: plan de negocios del banco [Certain] (art. 2 Bis 117 g.II) | Falta contexto | Dinámico ("exercício dinâmico") [Certain] (REF may-2026) | Dinámico (plan de negocios); en tensión sin mitigación se mantiene la trayectoria de la cartera [Certain] | Falta contexto | Falta contexto | Falta contexto |
| Acciones de gestión | No; acciones de capital supuestas por la norma [Certain] | Sí, las que el Banco acepta [Certain] | Plan de Acción Preventivo si no se cumple el umbral [Certain] (art. 2 Bis 117 h) | No ("no considera las posibles acciones de mitigación") [Certain] | No como tales; sí se computan los disparadores de deuda Nivel II/AT1 [Certain] | Escenario con y sin mitigación [Certain] | Falta contexto | Falta contexto | Acciones correctivas exigidas en el informe [Likely] |
| Métrica y umbral | CET1 mínimo 4,5 % más SCB; SHUSA 3,4 %, total 7,9 % [Certain] | CET1 y apalancamiento Tier 1 frente a mínimos; Santander UK 6,9 % y 3,25 % [Certain] | ICAP, Capital Neto, APSR; seguir en categoría I del art. 220 (ICAP ≥ 10,5 % + suplementos) [Certain] | ICAP frente a "mínimo regulatorio + suplementos = 10,5" [Certain] | IB, IPR1 e ICP ("desenquadramento"); 10,5 % y restricción por ACP [Certain] | Mínimo regulatorio en tensión; objetivo interno en escenario normal [Certain] | Falta contexto | Falta contexto | Falta contexto |
| Base contable de las provisiones | US GAAP (CECL) [Likely]; tratamiento de CECL en el test: falta contexto | IFRS 9; transitorios ya expirados [Certain] | Criterios contables CNBV: PI×SP×EI por etapas y NIF C-16 [Certain] | Igual que CNBV [Likely] | Res. CMN 4.966/2021, en vigor desde ene-2025 con transición [Certain] | Normas CMF (Compendio de Normas Contables) [Guessing] | Igual [Guessing] | BDDK; sin NIC 29 en 2025 [Likely] | NIIF con NIC 29 desde 2020 [Certain] ([Com. A 6849](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6849.pdf)) |
| Publicación | Por banco [Certain] | Por banco y agregada [Certain] | No consta publicación [Likely] | Sistema [Certain] | Sistema [Certain] | No se publica [Likely] | Sistema [Likely] | No consta [Likely] | No consta [Likely] |
| Entidad del grupo | Santander Holdings USA (SHUSA). BBVA: ninguna | Santander UK Group Holdings | Santander México, BBVA México | Las mismas | Santander Brasil | Santander Chile | Santander Chile | Garanti BBVA | BBVA Argentina, Santander Argentina |

### Inferences
- `[Likely]` Para el puente del cap. 27 conviene ordenar los ejercicios por quién proyecta, no por país. México tiene dos ejercicios con lógica opuesta (CNBV: proyecta el banco; Banxico: proyecta el supervisor) y Chile también (CMF frente a BCCh).
- `[Likely]` Solo la Fed y el Banco de Inglaterra publican resultados por banco. En el resto, el único número local comparable con el del grupo en el EBA es agregado del sistema, o es confidencial (CNBV, CMF, BDDK, BCRA).

### Gaps
- Horizonte y métrica del ejercicio del BCCh: falta contexto (bcentral.cl bloqueado).
- Supuesto de balance de la Fed para 2026: no verificado en la fuente primaria.
- Base contable chilena: no verificada.

## 1. EE. UU. (Fed): SHUSA en 2026, SCB y reforma del 30-sep-2026

### Takeaway
`[Certain]` SHUSA estuvo en el test de 2026: su CET1 pasa del 12,6 % (2025:T4) a un mínimo del 11,7 %. Su SCB sigue en el 3,4 % (CET1 total del 7,9 %), porque en febrero de 2026 la Fed congeló los SCB hasta 2027. La reforma final del 30-sep-2026 promedia los dos últimos tests con igual peso desde el SCB efectivo el 1-ene-2029 y traslada la fecha de efecto al 1 de enero, ya desde 2028.

### Cited Findings

**Validación de afirmaciones**

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| SHUSA está en el test de 2026 ("carta de la Fed del 4-feb-2026") | Confirmado (participación); fuente corregida | SHUSA es uno de los 32 bancos del test de 2026 y figura en las tablas 5 y 6 de resultados. El 4-feb-2026 la Fed publicó una **nota de prensa** que fijaba los escenarios y congelaba los SCB; no se ha verificado ninguna "carta". | [Certain] | [Fed, resultados 2026](https://www.federalreserve.gov/publications/2026-june-dodd-frank-act-stress-test-results.htm); [Fed, Large Bank Capital Requirements, jun-2026, nota 3](https://www.federalreserve.gov/publications/files/large-bank-capital-requirements-20260624.pdf) |
| SCB 3,4 % y CET1 total 7,9 % | Confirmado | SHUSA: mínimo 4,5 % + SCB 3,4 % = **7,9 %** de CET1. La marca "†" indica que no participó en el test de 2025, así que su SCB **se basa en los resultados de 2024**. | [Certain] | [Fed, Large Bank Capital Requirements, jun-2026, tabla y nota †](https://www.federalreserve.gov/publications/files/large-bank-capital-requirements-20260624.pdf) |
| Vigente desde el 1-oct-2025; 3,5 % el año anterior | Fecha confirmada; 3,5 % no verificado | Efectivo desde el 1-oct-2025 según el anuncio de SHUSA de 2025. El 3,5 % previo no se ha comprobado en la fuente primaria. | [Likely] | [SHUSA, 2025 SCB (Business Wire)](https://www.businesswire.com/news/home/20250701456768/en/Santander-Holdings-USA-Inc.-Announces-2025-Stress-Capital-Buffer/) |
| La Fed votó en feb-2026 mantener los SCB hasta 2027 | Confirmado | "In February 2026, the Board voted to maintain the current stress capital buffer requirements until 2027". | [Certain] | [Fed, Large Bank Capital Requirements](https://www.federalreserve.gov/publications/files/large-bank-capital-requirements-20260624.pdf) |
| 32 bancos, ~708.000 M$ de pérdidas, CET1 agregado 12,8 % → 11,2 % | Confirmado | 32 bancos; pérdidas de **708.000 M$** (625.000 M$ en préstamos, el 89 %); CET1 agregado 12,8 % → mínimo 11,2 % (12,7 % al final de los 9 trimestres). | [Certain] | [Fed, resultados 2026](https://www.federalreserve.gov/publications/2026-june-dodd-frank-act-stress-test-results.htm) |
| SHUSA 12,6 % → 11,7 % (prensa) | Confirmado en fuente primaria | CET1 12,6 % real → 11,7 % al final y en el mínimo. Tier 1: 14,4 → 13,5. Capital total: 16,5 → 15,7. Apalancamiento Tier 1: 9,2 → 8,7 (mínimo). | [Certain] (antes [Likely]) | [Fed, resultados 2026, tabla 6](https://www.federalreserve.gov/publications/2026-june-dodd-frank-act-stress-test-results.htm) |
| SCB como media de los dos últimos tests, con igual peso "también cuando baja" | Corregido (matiz) | Media de las caídas máximas de CET1 de los dos últimos tests, **con igual peso**; a eso se suman cuatro trimestres de dividendos previstos y se aplica el suelo del 2,5 %. La media **no se aplica en general si hay un cambio material del plan de negocio**. El texto no menciona ninguna regla asimétrica para subidas o bajadas. | [Certain] | [Fed, memo al Consejo, 30-sep-2026, nota 18](https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20260930a1.pdf) |
| Reducción de ~50 % de la volatilidad interanual | Confirmado | "likely to reduce year-over-year volatility in capital requirements by approximately 50 percent". Sin efecto material en el agregado. | [Certain] | [Fed, nota de prensa 30-sep-2026](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm) |
| Media desde 2028, efectiva el 1-ene-2029; fecha de efecto al 1 de enero | Confirmado | El SCB del test de 2027 entra en vigor el **1-ene-2028** (antes, el 1 de octubre). El primer SCB promediado (tests de 2027 y 2028) entra en vigor el **1-ene-2029**. | [Certain] | [Fed, "Stress Test Changes and Effective Dates"](https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20260930a5.pdf); [memo](https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20260930a1.pdf) |
| Modelos y escenarios a comentario público | Confirmado | La Fed debe someter **cada año** a comentario público los escenarios y cualquier cambio material de modelo. Para el test de 2027: escenarios propuestos antes del 10-ene-2027, finales antes del 28-feb-2027, documentación final de modelos antes del 15-may-2027, resultados antes del 30-jun-2027. Habrá dos *global market shocks* y se aplicará el peor. | [Certain] | [Fed, nota de prensa](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm); [calendario](https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20260930a5.pdf) |
| En la Fed proyecta el supervisor y el resultado es vinculante (SCB) | Confirmado | Proyecciones "Federal Reserve estimates"; las acciones de capital las supone la norma (12 CFR 238.132(d); 252.44(c)). | [Certain] | [Fed, resultados 2026, nota a tabla 4](https://www.federalreserve.gov/publications/2026-june-dodd-frank-act-stress-test-results.htm) |
| BBVA vendió BBVA USA a PNC en 2021 | Confirmado | Cierre el **1-jun-2021**, ~11.600 M$ en efectivo. BBVA no tiene ningún holding estadounidense en el test de la Fed. | [Certain] | [PNC, nota de prensa 1-jun-2021](https://investor.pnc.com/news-events/financial-press-releases/detail/44/pnc-completes-acquisition-of-bbva-usa) |
| Exposición de BBVA a EE. UU. en el EBA ~54.500 M€ | No verificable aquí | Depende de `datos-publicos.md`; fuera del alcance de esta validación. | Sin cambio | n/a |

### Inferences
- `[Likely]` Para el manual, SHUSA es el mejor caso de "mismo grupo, dos números": su caída de CET1 en la Fed fue de solo 0,9 pp (12,6 → 11,7), con modelos de la Fed y US GAAP, mientras el grupo publica su caída en el EBA con proyecciones propias e IFRS 9.
- `[Likely]` La congelación de los SCB hace que el test de 2026 **no** mueva el requerimiento de SHUSA. Es un buen ejemplo de resultado publicado sin consecuencia de capital inmediata.

### Gaps
- SCB de SHUSA anterior (3,5 %): no leído en la fuente primaria.
- Si el test de 2026 ya incorpora CECL en las provisiones: no verificado.

## 2. Reino Unido (Banco de Inglaterra): Bank Capital Stress Test 2025

### Takeaway
`[Certain]` El *Bank Capital Stress Test* 2025 (resultados el 2-dic-2025) cubrió a siete bancos con un horizonte de 5 años. Santander UK baja del 14,8 % al 9,7 % de CET1 antes de acciones de gestión y al 10,3 % después, frente a un mínimo del 6,9 %. El ejercicio es ahora **bienal** (fuente primaria) y en 2025 se evaluó contra mínimos, no contra mínimos más colchones sistémicos.

### Cited Findings

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| El ejercicio del mapa se llama "ACS" | Corregido | Desde 2025 se llama **Bank Capital Stress Test (BCST)**. El ACS era el ejercicio anual del marco anterior; el último fue el de 2022/23. | [Certain] | [FSR dic-2025, cap. 5](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025) |
| BCST 2025 publicado el 2-dic-2025 con siete participantes; ~75 % del crédito | Corregido (matiz) | Siete participantes: Barclays, HSBC, Lloyds, Nationwide, NatWest, Santander UK y Standard Chartered. El ~75 % del crédito a la economía real del Reino Unido corresponde **al conjunto** de participantes, no a Santander UK. | [Certain] | [FSR dic-2025](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025); [Santander UK, 2-dic-2025](https://www.santander.co.uk/about-santander/investor-relations/stock-exchange-announcements/santander-uk-group-holdings-plc-statement-on-the-outcome-of-the-2025-bank-of-england-capital-stress-test/) |
| Santander UK: 14,8 % → 9,7 % antes de acciones y 10,3 % después; umbral 6,9 %; apalancamiento 4,9 % → 3,9 % (umbral 3,25 %); sin acciones de capital adicionales | Confirmado y ampliado | Además: apalancamiento **3,5 % antes de acciones**. El punto mínimo de Santander UK cae en el **año 2** (en el año 1 para el resto). El banco dice que supera los mínimos en los 5 años incluso sin acciones estratégicas. | [Certain] | [Santander UK](https://www.santander.co.uk/about-santander/investor-relations/stock-exchange-announcements/santander-uk-group-holdings-plc-statement-on-the-outcome-of-the-2025-bank-of-england-capital-stress-test/); [FSR dic-2025, anexo 2 y nota f](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025) |
| Horizonte de 5 años [Likely] | Confirmado | Cinco años, con punto de partida a fin de diciembre de 2024. | [Certain] | [Key elements 2025](https://www.bankofengland.co.uk/stress-testing/2025/key-elements-bank-capital) |
| El BoE admite acciones de gestión y fija un umbral de aprobado | Corregido (matiz) | Los bancos proponen acciones de gestión (dividendos, retribución variable, costes) y el Banco acepta solo las realistas. En 2025 **no hubo aprobado o suspenso frente a mínimos más colchón sistémico**: se publicaron los mínimos de cada banco junto a sus requerimientos mínimos, para recalibrar la referencia tras IFRS 9. En los próximos tests el Banco **volverá a evaluar contra mínimos más colchones de riesgo sistémico**. | [Certain] | [FSR dic-2025, cap. 5.1](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025) |
| Ciclo bienal [Likely] | Confirmado | "the Bank expects to carry out a Bank Capital Stress Test every other year". En los años intermedios: ejercicios de escritorio, focalizados o exploratorios, publicados solo en agregado. El FSR de dic-2025 lo cita como medida ya adoptada. | [Certain] | [BoE, approach to stress testing (2024)](https://www.bankofengland.co.uk/stress-testing/2024/boes-approach-to-stress-testing-the-uk-banking-system); [FSR dic-2025](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025) |
| Referencia de Tier 1 del 14 % a ~13 % [Guessing] | Confirmado y recalificado | No es el umbral del test. Es la **referencia del FPC para el nivel de requerimientos de Tier 1 del sistema**, rebajada del ~14 % al **~13 % de APR** (≈11 % de CET1). | [Certain] | [FSR dic-2025, cap. 4 y recuadro](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025) |
| Próximo ejercicio | Nuevo | Por el ciclo bienal tocaría un BCST en 2027. En la página de stress testing (vista el 2026-10-16) no hay anuncio. En 2026 el Banco publicó (19-jun-2026) un ejercicio exploratorio de mercados privados para todo el sistema. | [Likely] | [BoE, stress testing](https://www.bankofengland.co.uk/stress-testing) |

Datos de contexto del BCST 2025 `[Certain]` ([FSR dic-2025](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025)):
- Escenario: shock global de oferta. PIB del Reino Unido −5 %, paro máximo 8,5 %, Bank Rate 8 %, vivienda −28 %.
- Agregado: CET1 14,5 % → 11,0 % (−3,5 pp, mínimo en el año 1). Apalancamiento 5,3 % → 4,7 %.
- Balance dinámico: el crédito a la economía real crece más del 6,5 % en el horizonte.
- IFRS 9 sin transitorios: el alivio transitorio ha expirado.

### Inferences
- `[Likely]` En el puente del grupo, Santander UK es el ejemplo de balance dinámico con acciones de gestión y 5 años, frente al EBA (estático, sin acciones de gestión, 3 años). La diferencia de 0,6 pp entre antes y después de acciones (9,7 frente a 10,3) mide de forma directa el efecto de las acciones de gestión.

### Gaps
- Anuncio oficial del BCST 2027: no encontrado.

## 3. México: CNBV (escenarios supervisores) y Banxico (REF)

### Takeaway
`[Certain]` El ejercicio de la CNBV está en la CUB, **Capítulo VI Bis, arts. 2 Bis 117 a-i** (texto compilado con reformas hasta el 1-sep-2026). Es anual, con escenarios que fija la CNBV por oficio y al menos 9 trimestres de proyección. El banco debe seguir en la **categoría I** de alertas tempranas (art. 220). Lo de Banxico se confirma entero. Las reservas se calculan con PI×SP×EI por etapas (CUB arts. 110 Bis, 111 y 129) y con metodologías internas basadas en la NIF C-16.

### Cited Findings

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| Banxico: pruebas de crédito, liquidez y climáticas en el REF de junio de 2026, pp. 28-31 | Confirmado; páginas corregidas | El fichero local es la **presentación** del REF (10-jun-2026). Pruebas de estrés en pp. 29-33: introducción en la 29, escenarios en la 30, crédito en la 31, liquidez a 90 días en la 32 y climáticas (C1/C2) en la 33. | [Certain] | `fuentes/2026-06-10 Banxico REF.pdf` |
| Escenarios A, B, C y tres históricos (1995, 2008, COVID-19) | Confirmado | A: debilitamiento prolongado de consumo e inversión. B: recesión en EE. UU., más volatilidad y tipo de cambio, posible rebaja de la calificación soberana y de Pemex. C: volatilidad, depreciación, primas de riesgo y tipos al alza. H1 = 1995, H2 = 2008, H3 = COVID-19. | [Certain] | ídem, pp. 30-31 |
| Cifras a marzo de 2026 y simulación a 3 años | Confirmado | "Cifras a marzo de 2026 y simulaciones a 3 años a partir de entonces". | [Certain] | ídem, p. 31 |
| Escenario común, sin problemas idiosincrásicos, sin mitigación, equilibrio parcial | Confirmado | "El ejercicio es común para todas las instituciones y no considera problemas idiosincrásicos en la originación crediticia"; "no considera las posibles acciones de mitigación… (es un ejercicio contrafactual de equilibrio parcial y no general)". | [Certain] | ídem, p. 30 |
| Umbral = 10,5 % de ICAP | Confirmado | "Mínimo regulatorio + suplementos de capital = 10.5"; la métrica es el índice de capitalización (ICAP). | [Certain] | ídem, p. 31 |
| El sistema queda por encima del umbral en todos los escenarios | Confirmado | Incluidos los históricos, "aunque muestran niveles de capitalización menores". | [Certain] | ídem, p. 31 |
| CNBV: sección sobre suficiencia de capital bajo escenarios supervisores; al menos anual; escenarios base y adverso [Likely] | Corregido y elevado | **Capítulo VI Bis "De la Evaluación de la Suficiencia de Capital"**. Sección Primera (art. 2 Bis 117 a): autoevaluación anual con escenarios propios, el ICAAP mexicano. **Sección Tercera (arts. 2 Bis 117 e-i)**: "Evaluación de la Suficiencia de Capital bajo Escenarios Supervisores". Las instituciones de banca múltiple deben determinar **anualmente** si su Capital Neto cubre las pérdidas, si **se mantienen en la categoría I** (art. 220) y si cumplen el capital mínimo, **para cada trimestre** de la evaluación (117 e). La CNBV comunica los escenarios por **oficio** y publica el calendario en enero (117 f). El informe proyecta **al menos 9 trimestres**: estado de situación financiera y de resultados, ICAP, Capital Neto, APSR y desviaciones de límites, con los supuestos del plan de negocios (colocación, pasivos, dividendos, gastos), firmado por el director general y aprobado por el Consejo (117 g). Si se incumple, se presenta un **Plan de Acción Preventivo** con acciones de 12 meses como máximo (117 h). La CNBV puede pedir más frecuencia (117 i). Los lineamientos están en el **Anexo 12-D**. Que los escenarios sean "base y adverso" **no consta** en el articulado leído. | [Certain] (el "base y adverso", [Guessing]) | [CUB compilada, CNBV, reformas hasta 1-sep-2026](https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf), art. 1 fr. LIX y LXIV y arts. 2 Bis 117 a-i |
| "El art. 2 Bis 117 se cita en documentos del BIS" | Corregido | Los artículos correctos son **2 Bis 117 a** a **2 Bis 117 i**. No existe un "2 Bis 117" sin letra en ese capítulo. | [Certain] | ídem |
| Umbral de categoría I | Nuevo | Art. 220: categoría I si ICAP ≥ 10,5 % + SCCS + SCCI, CCB ≥ 8,5 % + SCCS + SCCI y CCF ≥ 7 % + SCCS + SCCI. Es coherente con el 10,5 % de Banxico. | [Certain] | ídem, art. 220 |
| Reservas: pérdida esperada regulatoria (PI × SP × EI) desde 2011, categorías A-1…E; etapas alineadas con IFRS 9 desde 2022 | Confirmado en lo esencial; "desde 2011" no verificado | Art. 111: reservas de etapas 1 y 3 = **PI × SP × EI**; etapa 2, **vida completa**. Las etapas se asignan por el art. 110 Bis y el criterio contable B-6 "Cartera de Crédito". Art. 129: reservas por métodos estándar o **internos basados en la NIF C-16** (Capítulo V Bis 1), clasificadas en grados **A-1, A-2, B-1, B-2, B-3, C-1, C-2, D y E**. Entrada en vigor del esquema por etapas (NIF C-16) el **1-ene-2022**, según el informe de criterios contables de un emisor. | [Certain] (CUB); [Likely] (fecha de 2022) | [CUB, arts. 110 Bis, 111 y 129](https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf); [BanBajío, criterios contables 2022 (BMV)](https://bmv.com.mx/docs-dig/fina/BBAJIO/2022/1276477-BBAJIO-Informe_de_Principales_Politicas_y_Criterios_Contables_del_2022.pdf) |
| El grupo consolida en IFRS 9; el ejercicio local parte de la provisión local | Confirmado (inferencia) | La base local son los criterios contables de la CNBV (NIF más reglas propias), no IFRS. La misma cartera tiene una reserva local (fórmula regulatoria o NIF C-16) y otra en IFRS 9 en el consolidado del grupo. | [Likely] | ídem |
| ICAP del sistema del 20,00 % en jun-2025 (ABM citando a la CNBV) | No verificable | No se ha comprobado en esta pasada. | [Likely] (sin cambio) | Sin fuente primaria |
| ¿Santander México salió de bolsa en 2023? | Confirmado (nuevo) | Ofertas públicas concluidas el **10-abr-2023**: la participación de Banco Santander sube del ~96,2 % al **~99,8 %**. La CNBV emitió el oficio de **cancelación de la inscripción en el RNV el 12-may-2023**, con fideicomiso de cancelación para los minoritarios. También se retiraron los ADS de la NYSE. | [Certain] | [BMV, evento relevante 13-abr-2023](https://www.bmv.com.mx/docs-pub/eventemi/eventemi_1270456_1.pdf); [BMV, 15-may-2023](https://www.bmv.com.mx/docs-pub/eventemi/eventemi_1281501_1.pdf) |
| ¿BBVA México publica sus propios resultados de estrés? | Nuevo | No se ha encontrado ninguna publicación por banco. La CUB no exige publicar el informe del art. 2 Bis 117 g, que se entrega a la CNBV. | [Likely] | [CUB](https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf); búsqueda sin resultados |

Ojo con un dato que corrige la búsqueda secundaria: el oficio de la CNBV del 27-nov-2023 (cancelación en el RNV y listado en el SIC) es de **Banco Santander, S.A.**, la matriz española, **no** de Santander México ([BMV, aviso](https://www.bmv.com.mx/docs-pub/8kmateri/8kmateri_1333503_1.pdf)). `[Certain]`

Banxico, otros detalles `[Certain]` (presentación del REF, pp. 32-33):
- Liquidez a 90 días con datos al 30-abr-2026, en escenarios base, medio y severo.
- Climático: C1 (PIB −1 %, ICAP −1,02 pp) y C2 (PIB −2 %, ICAP −0,45 pp). Las cifras se transcriben tal cual: que el escenario más severo en PIB tenga menos impacto parece contraintuitivo y conviene revisarlo en el REF completo.

### Inferences
- `[Likely]` México es el caso más útil para el cap. 6. El mismo banco (Santander México o BBVA México) aparece en un ejercicio *bottom-up* con escenarios del supervisor y acciones de gestión vía plan preventivo (CNBV, confidencial) y en uno *top-down* sin mitigación (Banxico, agregado). Ninguno de los dos da un número público por banco.
- `[Likely]` Con Santander México fuera de bolsa desde 2023, no hay obligación bursátil local que fuerce a publicar sus métricas: el número público es el del grupo.

### Gaps
- Contenido del Anexo 12-D (número de escenarios, balance dinámico o estático): no leído, va en anexo aparte de la CUB compilada.
- Fecha exacta de la resolución de la CNBV que introdujo las etapas (reforma "274" en las marcas de la CUB): no verificada.

## 4. Brasil (BCB)

### Takeaway
`[Certain]` El BCB hace un test macro *top-down* banco a banco, dinámico y a 12 trimestres, con escenarios Base, Recessão Aguda y Crise de Confiança, más sensibilidades, contagio y liquidez. El último REF es el de **mayo de 2026** (datos de dic-2025): 97 instituciones, el 96,72 % del activo. En la Crise de Confiança, entidades con el 68,7 % del activo siguen por encima del 10,5 %, y la necesidad de capital es el 3,1 % del PR. Además, los bancos del S1 hacen su propio ICAAP (Res. CMN 4.557, art. 40).

### Cited Findings

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| REF semestral con test macro, sensibilidades, contagio y liquidez (abr-2025) | Confirmado | Componentes: test macroeconómico, análisis de sensibilidad (tipos de interés, tipo de cambio, activos problemáticos, precios de vivienda), contagio interfinanceiro directo y estrés de liquidez. | [Certain] | `fuentes/2025-04 BCB REF.pdf`, anexo "Conceitos e Metodologias" |
| Escenario de "crisis de confianza" | Confirmado y ampliado | Tres escenarios: **Base** (medianas Focus), **Recessão Aguda** y **Crise de Confiança** (referencia: deterioro fiscal de 2014-2016). Cinco variables: PIB, BRL/USD, Selic, IPCA y paro. | [Certain] | REF abr-2025, recuadro de escenarios y anexo; [REF may-2026, recuadro 4](https://www.bcb.gov.br/content/publicacoes/ref/202605/RELESTAB202605-refPub.pdf) |
| Horizonte "varios trimestres" [Guessing] | Corregido | **12 trimestres** ("os três cenários macroeconômicos para os doze trimestres seguintes à data de referência"). En may-2026: de dic-2025 a dic-2028. | [Certain] | REF abr-2025, anexo; REF may-2026, gráfico 1.2.5.6 |
| "Desenquadramento" = incumplir al menos uno de IB, IPR1 o ICP | Confirmado | Literal. Además, "insolvente" significa pérdida total del capital principal. | [Certain] | REF abr-2025, nota 79 y anexo; REF may-2026, nota 50 |
| Restricción de dividendos por no cubrir el ACPConservação del 2,5 % (Res. BCB 200/2022) | Confirmado | La insuficiencia del ACPConservação del 2,5 % restringe dividendos, JCP, recompras, retribución variable y reducciones de capital. | [Certain] | REF abr-2025, nota 78; REF may-2026, nota 52 |
| Más del 40 % del sistema con restricciones en Crise de Confiança (abr-2025) | Confirmado y precisado | Resumen ejecutivo: "mais de 40%". Cuerpo: **44 % del activo** con restricciones y 46 % por encima del 10,5 %. Mínimo del índice: **13,5 % en mar-2026**. Necesidad de capital: **9,9 % del PR** en el trimestre 12 (Crise de Confiança) y 2,7 % (Recessão Aguda). | [Certain] | REF abr-2025, pp. 7 y 46 |
| Escenarios desde datos observados más Focus hasta el trimestre anterior a la "crisis" | Confirmado | En abr-2025: Focus hasta el 31-ene-2025; último trimestre previo a la crisis, el 1T2025. | [Certain] | REF abr-2025, recuadro |
| Res. CMN 4.966/2021 en vigor el 1-ene-2025 | Confirmado y ampliado | En vigor en enero de 2025. Transición de la **Res. CMN 5.199/2024**: 25 % del impacto al año desde el 1T2025, y el test aplica el 75 % dentro del horizonte. El test también incorpora la Ley 14.467/2022 y el RWAOPAD (Res. BCB 356/2023). | [Certain] | REF abr-2025, notas 82-83; REF may-2026, nota 54 |
| El BCB hace un estrés de riesgo climático físico (la sequía como principal riesgo) | Corregido | Lo que hay es un análisis de **exposiciones de crédito a riesgos climáticos físicos** (sección 2.2) y una **encuesta** a entidades en la que la **sequía** es el evento con mayor impacto esperado. No es un test de capital al estilo del macro. | [Certain] | REF abr-2025, sección 2.2 y resumen ejecutivo |
| Último REF (nov-2025 o may-2026) | Nuevo | **REF may-2026** (vol. 25, n.º 1): datos de dic-2025, 97 instituciones (96,72 % del activo). En Crise de Confiança, el **68,7 % del activo** sigue por encima del 10,5 % y la necesidad máxima de capital es el **3,1 % del PR** en el último trimestre (frente al 5,3 % del REF anterior). En Recessão Aguda, el 1,6 % (frente al 2 %). Sensibilidad a tipos (mayor variación en 27 años): necesidad del 3,2 % del PR. Lo describe como "exercício dinâmico". | [Certain] | [REF may-2026](https://www.bcb.gov.br/content/publicacoes/ref/202605/RELESTAB202605-refPub.pdf), sección 1.2.5 |
| ¿Hacen los bancos su propio ICAAP? | Nuevo | La Res. CMN 4.557/2017 exige un **programa de pruebas de estrés** (arts. 7.VII y 11: sensibilidad, escenarios y estrés inverso) y, en la gestión de capital, plan de capital a **≥3 años**, plan de contingencia y evaluación de la adecuación de capital (arts. 40-41). **ICAAP para el S1** e ICAAP simplificado para el S2 (art. 40 §2). Los segmentos se definen en la Res. 4.553/2017. | [Certain] | [Res. CMN 4.557/2017 (BCB)](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o&numero=4557) |

### Inferences
- `[Likely]` Santander Brasil está en el S1 y por tanto hace ICAAP, pero no se ha verificado en la lista de segmentos del BCB.
- `[Likely]` El umbral práctico que reportan los REF es el **10,5 %** (IB mínimo más ACPConservação). Coincide en número con el de México, pero aquí sobre el PR brasileño. Es un buen ejemplo de "mismo número, distinta base".
- `[Likely]` La caída de la necesidad de capital del 9,9 % del PR (abr-2025) al 3,1 % (may-2026) muestra lo mucho que dependen estos resultados de la severidad y del punto de partida de cada edición.

### Gaps
- Si el BCB tiene además un ejercicio *bottom-up* en el que los bancos proyectan con escenarios del BCB: no verificado.
- Cifras del REF de nov-2025: no leídas (el de may-2026 lo sustituye).

## 5. Chile (CMF y Banco Central de Chile)

### Takeaway
`[Certain]` La CMF exige a los bancos, dentro del **IAPE** (RAN cap. 21-13, versión de la Circular 2.365 de 8-jul-2025), pruebas de tensión a **3 años** con escenario base, tensión **sin** mitigación y tensión **con** mitigación, usando **parámetros agregados que da la CMF**. El BCCh publica sus pruebas en el IEF semestral (1S2026: 19-may-2026). El 18-may-2026 subió el **requerimiento de capital contracíclico (RCC) del 0,5 % al 1 % de los APR, con 24 meses de plazo**.

### Cited Findings

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| IEF 1S2026 (19-may-2026): con contracción y alza del coste de financiación, los bancos mantienen el CET1 por encima de los requerimientos | Fecha confirmada; contenido corregido | La nota de prensa dice que "los niveles de rentabilidad, capital y liquidez" permitirían a los bancos **mantenerse solventes en un escenario de tensión severo**. El principal riesgo citado es un **endurecimiento abrupto de las condiciones de financiamiento**. No se ha podido comprobar que la métrica sea CET1. | [Likely] (texto leído vía buscador; bcentral.cl bloqueado) | [BCCh, nota de prensa IEF 1S2026](https://www.bcentral.cl/contenido/-/detalle/prensa/nota-de-prensa/bcch-publica-ief-primer-semestre-2026) |
| La CMF exige un IAPE con pruebas de tensión [Likely] | Confirmado y elevado | RAN 21-13: horizonte de **≥3 años**. El objetivo interno de patrimonio incluye un **colchón voluntario de capital básico** para absorber un escenario de tensión severo sin incumplir el mínimo legal. En tensión, el banco debe cumplir **al menos el mínimo regulatorio**; en escenario normal, su objetivo interno. Debe hacer ejercicios "en base a los parámetros agregados que le entregue la Comisión y a sus propias estimaciones internas" y reportar los resultados a la CMF. Proyecta base, tensión sin mitigación ("manteniendo las trayectorias de la cartera") y tensión con mitigación. El impacto entra por PD y LGD. Ratios: patrimonio efectivo/APR, capital básico/APR y capital básico/activos totales. | [Certain] | [CMF, RAN cap. 21-13, sección 5.3](https://www.cmfchile.cl/portal/normativa/624/articles-29808_doc_pdf.pdf) |
| La subida a 1 % de los APR parece ser el colchón contracíclico [Guessing] | Confirmado | Es el **RCC**: del 0,5 % al **1 % de los APR**, en un plazo de **24 meses**, por unanimidad, con informe previo favorable de la CMF, en la Reunión de Política Financiera del 1S2026 (comunicado del 18-may-2026). Próxima RPF: comunicado el 16-nov-2026. | [Certain] | [BCCh, comunicado RPF 1S2026](https://www.bcentral.cl/contenido/-/detalle/prensa/comunicados-rpf/reunion-de-politica-financiera-primer-semestre-2026); [CNN Chile](https://www.cnnchile.com/negocios/banco-central-endurece-requisitos-capital-para-bancos-1-riesgos-elevados-guerra-medio-oriente/) |
| Método del BCCh | Nuevo, parcial | Pruebas de tensión de riesgo de crédito y de mercado para el sistema bancario; actualización metodológica en el Documento de Trabajo 801 (2017). | [Likely] | [BCCh DT 801 (RePEc)](https://ideas.repec.org/p/chb/bcchwp/801.html) |
| Cargos de Pilar 2 de la CMF | Nuevo | La CMF ha aplicado cargos de Pilar 2 por resolución en enero de 2024 y de 2025. | [Likely] (vía buscador) | [CMF, prensa](https://www.cmfchile.cl/portal/prensa/625/w4-article-89700.html) |

### Inferences
- `[Likely]` Santander Chile es el caso de "ICAAP con escenario del supervisor": se parece más al EBA (proyecta el banco con parámetros comunes) que al BCCh, pero con mitigación permitida en uno de los escenarios y un horizonte de 3 años.

### Gaps
- Horizonte, métrica y umbral de las pruebas del BCCh en el IEF 1S2026: falta contexto (bcentral.cl bloqueado).
- Base contable de las provisiones en Chile (normas CMF frente a IFRS 9): no verificada.

## 6. Türkiye (BDDK, Garanti BBVA)

### Takeaway
`[Certain]` La base normativa se confirma: art. 43 ("programa de stress test") del Reglamento de Sistemas Internos e ISEDES (RG 29057, 11-jul-2014) y la guía de la BDDK del **31-mar-2016**. BBVA aplica la **NIC 29** a sus entidades turcas **desde el 1-ene-2022** en la consolidación. Los estados locales de los bancos turcos (normas BDDK) **no** aplican contabilidad de inflación en 2025, por decisión de la BDDK.

### Cited Findings

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| Base normativa: ISEDES art. 43 y guía BDDK (31-mar-2016) | Confirmado | Guía "Bankaların Sermaye ve Likidite Planlamasında Kullanacakları Stres Testlerine İlişkin Rehber", adoptada y vigente desde el **31-03-2016**, que desarrolla el **art. 43** del Reglamento de Sistemas Internos e ISEDES (RG 11-07-2014, n.º 29057). Su estado vigente en 2026 no se ha podido leer (muro de pago). | [Certain] (base); [Likely] (vigencia) | [Lexpera, ficha de la guía](https://www.lexpera.com.tr/mevzuat/kilavuzlar/bankalarin-sermaye-ve-likidite-planlamasinda-kullanacaklari-stres-testlerine-iliskin-rehber-1) |
| La BDDK hace macro stress al menos dos veces al año; los bancos presentan escenarios cada año en su ISEDES | Sin cambio (fuente solo secundaria) | Lo dice la prensa turca citando a la BDDK, sin fecha clara ni documento primario. | [Likely] | [Dünya](https://www.dunya.com/finans/haberler/bankalar-saglikli-ve-guclu-haberi-435897) |
| Türkiye aplica la NIC 29 en la consolidación del grupo [Guessing] | Confirmado | BBVA aplica la NIC 29 "to its Group entities in Turkey" **desde el 1-ene-2022**, con reflejo en las cuentas del 2T2022. No se aplica a las filiales de Garanti fuera de Türkiye (Rumanía, Países Bajos). Impacto estimado sobre datos a mar-2022: **−324 M€** de beneficio atribuido y **+19 pb** de CET1 *fully loaded*. | [Certain] | [BBVA, comunicado al mercado 29-jun-2022 (réplica de RNS)](https://www.ticker.app/lse/BVA/rns/2022-06-29/Implementation-of-IAS-29-to-BBVA-Turkey/5460Q) |
| Diferencia entre el número local y el del grupo | Nuevo | La BDDK decidió que bancos y entidades financieras **no apliquen contabilidad de inflación** en sus estados de 2025 (decisión n.º 11340 del 18-dic-2025, que deroga la n.º 10825 de 11-ene-2024; antes, la n.º 11021 de 5-dic-2024). | [Likely] (prensa) | [Bloomberg HT](https://www.bloomberght.com/bddk-bankalar-ve-finans-kurumlari-icin-enflasyon-muhasebesi-uygulanmayacak-3764574); [Alomaliye](https://www.alomaliye.com/2025/12/23/enflasyon-muhasebesi-uygulamasi-banka-ve-finans-sirketlerinde-kaldirildi/) |

### Inferences
- `[Likely]` Garanti BBVA da la diferencia de base contable más grande de todo el grupo. Local: normas BDDK **sin** NIC 29. Grupo: NIIF **con** NIC 29 (pérdida por posición monetaria neta y reexpresión). El estrés local y la contribución de Türkiye al EBA parten, por tanto, de capitales y resultados distintos.

### Gaps
- Si la BDDK fija escenarios comunes a los bancos para el ISEDES, el horizonte y la métrica: no verificado.
- Pruebas de estrés del banco central turco (CBRT) en su informe de estabilidad: no investigadas.

## 7. Argentina (BCRA)

### Takeaway
`[Likely]` Los bancos argentinos hacen pruebas de estrés dentro del régimen informativo "Plan de negocios y proyecciones e Informe de Autoevaluación del Capital" (apartado IV, "Pruebas de estrés"), con supuestos macro del REM y **variables de estrés que fija el BCRA**. `[Certain]` La NIC 29 es obligatoria para las entidades financieras desde los ejercicios que empiezan el 1-ene-2020.

### Cited Findings

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| Argentina: no investigado [Guessing] | Cubierto en parte | Com. "A" 6646 (8-feb-2019), régimen informativo para el período 2019/2020: supuestos macro según la mediana del REM; apartado IV de pruebas de estrés con políticas, metodología, modelos, planes de contingencia y acciones correctivas, y resultados sobre activos, resultados y capital; "Variables para pruebas de estrés" que da el BCRA; versión simplificada para las entidades del Grupo B que usan sensibilidad. La versión vigente en 2026 no se ha leído. | [Certain] (2019); [Likely] (vigencia) | [BCRA, Com. "A" 6646](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6646.pdf) |
| NIC 29 en Argentina | Nuevo | Com. "A" 6849 (27-dic-2019): reexpresión por NIC 29 para los ejercicios iniciados desde el **01-01-2020** (fecha de transición, 31-12-2018), según lo anunciado en las "A" 6651 y "A" 6778. | [Certain] | [BCRA, Com. "A" 6849](https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A6849.pdf) |
| Lineamientos de gestión de riesgos | Nuevo | La Com. "A" 8249 (jun-2025, vigente desde el 1-sep-2025) modificó los lineamientos para la gestión de riesgos (tres líneas de defensa, resiliencia operacional). No se ha leído el texto. | [Likely] (vía buscador) | Sin fuente primaria leída |

### Inferences
- `[Likely]` En Argentina las dos bases aplican la NIC 29 (local por norma del BCRA y grupo por NIIF), así que la diferencia contable con el grupo es menor que en Türkiye. Esto se infiere y no se ha comprobado con BBVA ni con Santander.

### Gaps
- Texto ordenado vigente de "Lineamientos para la gestión de riesgos" y del régimen IAC (el enlace del BCRA da 404).
- Si el BCRA publica pruebas de estrés del sistema en su IEF: no verificado.
- Fecha desde la que BBVA y Santander aplican la NIC 29 a Argentina en la consolidación: no verificada en la fuente primaria.

## 8. Polonia (cambio de perímetro)

### Takeaway
`[Certain]` Erste cerró el **9-ene-2026** la compra del **49 %** de Santander Bank Polska (y del 50 % de Santander TFI) por ~7.000 M€. Santander se queda con el **9,7 %** tras haber colocado ~3,5 % en diciembre de 2025.

### Cited Findings

| Afirmación de la nota | Veredicto | Redacción corregida | Confianza | Fuente |
|---|---|---|---|---|
| Erste cerró la compra del 49 % el 9-ene-2026; a Santander le queda el 9,7 % | Confirmado | Precio de 584 zł por acción, ~7.000 M€ en efectivo (2,2 veces el valor contable tangible del 1T2025). Plusvalía neta de ~1.900 M€ y **+~95 pb de CET1**. Colocación acelerada de ~3,5 % en diciembre de 2025. "Santander now holds a 9.7% stake". | [Certain] | [Santander, nota de prensa 9-ene-2026](https://www.santander.com/en/press-room/press-releases/2026/01/santander-completes-the-sale-of-49-of-santander-bank-polska-to-erste-group); [Erste, 9-ene-2026](https://www.erstegroup.com/en/news-media/press-releases/2026/01/09/erste-group-completes-acquisition-of-controlling-stake-in-santander-bank-polska) |
| Polonia sale del perímetro de Santander en el EBA 2027 | Sin cambio (inferencia) | Con un 9,7 % deja de ser filial consolidada; el punto de partida de 2027 (dic-2026) ya no la incluye. | [Likely] | Inferencia sobre las fuentes anteriores |

### Inferences
- `[Likely]` Además, Santander mantiene el 100 % de Santander Consumer Bank Polonia (lo cita la prensa), así que Polonia no sale del todo del perímetro. Conviene precisarlo en el manual.

### Gaps
- Tratamiento contable del 9,7 % restante (participación financiera o asociada): no verificado.
- Propiedad del 100 % de Santander Consumer Bank Polonia: falta la fuente primaria.

## 9. Sección 8 de la nota ("Lo que esto significa para el manual")

### Takeaway
`[Certain]` La tipología de tres familias se sostiene con dos ajustes: Chile (CMF) y Argentina (BCRA) entran en "el banco proyecta, con parámetros del supervisor", y el Banco de Inglaterra no tuvo en 2025 un umbral de aprobado frente a colchones sistémicos.

### Cited Findings
- Tipología (a) el banco proyecta, (b) el supervisor proyecta, (c) mixto: **Confirmado**, `[Certain]`. Añadir la CMF y el BCRA al grupo (a). La Fed, Banxico y el BCB son (b) según sus propios documentos ([Fed](https://www.federalreserve.gov/publications/2026-june-dodd-frank-act-stress-test-results.htm); Banxico REF, p. 30; BCB REF, anexo). El Banco de Inglaterra es (c) ([FSR dic-2025](https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025)).
- Métricas de salida: **Confirmado y ampliado**. Fed: CET1 frente a 4,5 % + SCB. Banco de Inglaterra: CET1 y apalancamiento Tier 1 frente a mínimos (en 2025). México: ICAP frente a categoría I (10,5 % + suplementos). Brasil: IB, IPR1 e ICP con desenquadramento y restricción por ACP. Chile (CMF): patrimonio efectivo/APR, capital básico/APR y capital básico/activos. Fuentes en las secciones 1 a 5.

### Inferences
- `[Likely]` El "10,5 %" aparece a la vez en México (ICAP) y en Brasil (IB más conservación). Hay que avisar en el manual de que no son la misma métrica ni la misma base de capital.

### Gaps
- Ninguno adicional.
