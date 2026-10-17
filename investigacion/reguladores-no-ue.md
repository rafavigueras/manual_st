---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, reguladores, mexico, brasil, eeuu, reino-unido, f1]
---

# F1 · Reguladores de fuera de la UE de las filiales de Santander y BBVA

Consultado el 2026-10-16 y **validado ese mismo día contra fuentes primarias** (informe
`reports/Validación F1 stress test.md`, correcciones R1-R30; detalle en
`research_notes/Validación F1 stress test/reguladores-no-ue.md`). Cada ejercicio se describe por sus
rasgos, como pide el `PROCESO.md` §6.

## 1. Mapa de rasgos

| Rasgo | Fed | Banco de Inglaterra (BCST) | CNBV | Banxico | BCB | CMF (IAPE) | BDDK | BCRA |
|---|---|---|---|---|---|---|---|---|
| Filial | Santander Holdings USA | Santander UK | Santander México, BBVA México | Ídem (sistema) | Santander Brasil | Santander Chile | Garanti BBVA | BBVA y Santander Argentina |
| Quién proyecta | Supervisor | Mixto: banco y Banco de Inglaterra | Banco, con escenarios de la CNBV | Supervisor (sistema) | Supervisor, banco a banco | Banco, con parámetros de la CMF | Banco (ISEDES); la BDDK hace además macro stress `[Likely]` | Banco, con variables del BCRA `[Likely]` |
| Horizonte | 9 trimestres | 5 años | ≥ 9 trimestres | 3 años | 12 trimestres | ≥ 3 años | Falta contexto | Falta contexto |
| Balance | Supuestos de capital fijados por la norma | Dinámico (crédito +6,5 %) | Dinámico (plan de negocios) | Falta contexto | Dinámico | Dinámico; sin mitigación, trayectoria mantenida | Falta contexto | Falta contexto |
| Acciones de gestión | No | Sí, las aceptadas | Plan de Acción Preventivo si incumple | No | No (sí disparadores de AT1/Nivel II) | Escenario con y sin mitigación | Falta contexto | Correctivas `[Likely]` |
| Métrica y umbral | CET1 4,5 % + SCB | CET1 y apalancamiento frente a mínimos (2025) | Categoría I: ICAP ≥ 10,5 % + suplementos | ICAP frente a 10,5 % | IB/IPR1/ICP; 10,5 % y colchón de conservación | Mínimo legal en tensión | Falta contexto | Falta contexto |
| Provisiones | US GAAP (CECL) `[Likely]` | IFRS 9 sin transitorios | CUB: PI × SP × EI y NIF C-16 | Ídem CNBV `[Likely]` | CMN 4.966 con transición | Normas CMF `[Guessing]` | BDDK, sin NIC 29 en 2025 `[Likely]` | NIIF con NIC 29 |
| Publicación por banco | Sí | Sí | No consta | No (sistema) | No (sistema) | No | No consta | No consta |

`[Certain]` salvo donde se indica. Tipología de familias: (a) **el banco proyecta** con escenarios o parámetros del supervisor (EBA, CNBV, CMF/IAPE, BCRA/IAC, ISEDES, ICAAP); (b) **el supervisor proyecta** con sus modelos (Fed, Banxico, BCB, BCCh); (c) **mixto**, con acciones de gestión (Banco de Inglaterra, sin umbral sistémico en 2025).

`[Certain]` **El mismo "10,5 %" en México y en Brasil no es la misma cosa:** en México es el ICAP de categoría I (CUB art. 220); en Brasil, el IB más el colchón de conservación sobre el patrimonio de referencia brasileño. Mismo número, distinta métrica y distinta base de capital. Material para una TRAMPA del cap. 6.

## 2. Estados Unidos (Fed)

- `[Certain]` SHUSA es uno de los 32 bancos del *stress test* supervisor de 2026. La Fed publicó el 4-feb-2026 una nota de prensa con los escenarios y la congelación de los SCB. Lo de una "carta" de la Fed, que decía la versión anterior de esta nota, no está verificado.
- `[Certain]` **Resultados de SHUSA en 2026** (tabla 6): CET1 del 12,6 % al 11,7 % (al final y en el mínimo); Tier 1 de 14,4 a 13,5; capital total de 16,5 a 15,7; apalancamiento Tier 1 de 9,2 a 8,7. Agregado: 708.000 M$ de pérdidas, 625.000 de ellas en préstamos; CET1 del 12,8 % al 11,2 % en el mínimo. <https://www.federalreserve.gov/publications/2026-june-dodd-frank-act-stress-test-results.htm>.
- `[Certain]` **SCB de SHUSA: 3,4 %** (4,5 % + 3,4 % = 7,9 % de CET1). SHUSA no participó en el test de 2025, así que su SCB se basa en los resultados de 2024. La Fed votó en febrero de 2026 mantener los SCB hasta 2027. <https://www.federalreserve.gov/publications/files/large-bank-capital-requirements-20260624.pdf>. `[Likely]` El 3,5 % del año anterior no está verificado en fuente primaria.
- `[Certain]` **Reglas finales del 30-sep-2026** (<https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260930a.htm>):
  - El SCB será la media de las caídas máximas de CET1 de los dos últimos tests con igual peso, más cuatro trimestres de dividendos previstos y un suelo del 2,5 %. **No se aplica si hay un cambio material del plan de negocio.** El texto no tiene ninguna regla asimétrica.
  - El SCB del test de 2027 entra en vigor el 1-ene-2028; el primer SCB promediado (tests de 2027 y 2028), el 1-ene-2029. La Fed estima que la volatilidad interanual baja en torno al 50 %.
  - **Escenarios y modelos sometidos a comentario público cada año.** Para 2027: escenarios propuestos antes del 10-ene-2027, finales antes del 28-feb-2027, documentación de modelos antes del 15-may-2027 y resultados antes del 30-jun-2027. Dos *global market shocks*, de los que se aplica el peor.
- `[Certain]` Diferencia de fondo con el EBA: en la Fed **el supervisor proyecta con sus propios modelos** y el resultado es un requerimiento vinculante (SCB). En el EBA proyecta el banco y el resultado orienta una guía (P2G).
- `[Certain]` BBVA vendió BBVA USA a PNC el 1-jun-2021 por ~11.600 M$ en efectivo: **BBVA no tiene entidad en el test de la Fed**. Su exposición a EE. UU. en el EBA es sobre todo mayorista.

## 3. Reino Unido (Banco de Inglaterra)

- `[Certain]` Desde 2025 el ejercicio se llama **Bank Capital Stress Test (BCST)**. El ACS era el ejercicio anual del marco anterior; el último fue el de 2022/23. El BCST es **bienal**: en los años intermedios hay ejercicios exploratorios publicados solo en agregado (en 2026, el de mercados privados, publicado el 19-jun). `[Likely]` Por la cadencia, el siguiente BCST sería en 2027; no hay anuncio a 2026-10-16.
- `[Certain]` BCST 2025, publicado el 2-dic-2025: siete participantes (Barclays, HSBC, Lloyds, Nationwide, NatWest, Santander UK y Standard Chartered), que **en conjunto** suman ~75 % del crédito a la economía real. Horizonte de **cinco años** desde dic-2024. Balance dinámico (crédito +6,5 %).
- `[Certain]` **Santander UK:** CET1 del 14,8 % a un mínimo del 9,7 % antes de acciones de gestión y del 10,3 % después, frente a un mínimo del 6,9 %; apalancamiento del 4,9 % al 3,5 % antes de acciones y al 3,9 % después (umbral 3,25 %). El mínimo cae en el **año 2** (en el año 1 para los demás bancos). Sin acciones de capital adicionales.
- `[Certain]` El Banco solo acepta las acciones de gestión que considera realistas. **En 2025 no hubo aprobado o suspenso frente a mínimos más colchones sistémicos:** se publicaron los mínimos de cada banco junto a sus requerimientos mínimos, para recalibrar la referencia tras IFRS 9. En los próximos tests volverá a evaluar contra mínimos más colchones sistémicos (FSR dic-2025, cap. 5.1).
- `[Certain]` La rebaja del ~14 % al ~13 % de APR (≈11 % de CET1) **no es el umbral del test**: es la referencia del FPC para los requerimientos de Tier 1 del sistema (FSR dic-2025, cap. 4).

## 4. México

- `[Certain]` **CNBV:** CUB (Disposiciones de carácter general aplicables a las instituciones de crédito), **Capítulo VI Bis, Sección Tercera, arts. 2 Bis 117 e a 2 Bis 117 i**. No existe un "2 Bis 117" sin letra. <https://www.cnbv.gob.mx/Normatividad/Disposiciones%20de%20car%C3%A1cter%20general%20aplicables%20a%20las%20instituciones%20de%20cr%C3%A9dito.pdf> (compilada a 1-sep-2026).
  - Cada año, la banca múltiple comprueba que su Capital Neto cubre las pérdidas, que **sigue en la categoría I** (art. 220) y que cumple el capital mínimo **en cada trimestre**.
  - Los escenarios los fija la CNBV **por oficio**, con calendario publicado en enero. Se proyectan **al menos 9 trimestres** con el plan de negocios (incluidos los dividendos).
  - El informe lo firma el director general y lo aprueba el Consejo. Si hay incumplimiento, **Plan de Acción Preventivo** a 12 meses como máximo.
  - Los lineamientos están en el **anexo 12-D** (sin leer). `[Guessing]` Que sean escenarios "base y adverso" no consta en el articulado.
- `[Certain]` **Banxico** publica pruebas de estrés en cada *Reporte de Estabilidad Financiera* (junio y diciembre). El fichero local (`fuentes/2026-06-10 Banxico REF.pdf`) es la **presentación** del informe del 10-jun-2026: estrés en las pp. 29-33 (escenarios en la 30, crédito en la 31, liquidez a 90 días en la 32 y clima en la 33). El texto completo está en el REF, §V.1 (<https://www.banxico.org.mx/publicaciones-y-prensa/reportes-sobre-el-sistema-financiero/%7B86FBB07E-F883-0A38-2110-3C736DB0760E%7D.pdf>).
  - Pruebas de crédito, liquidez y climáticas (eventos extremos).
  - Tres escenarios hipotéticos (A, B y C) y tres históricos (crisis de 1995, de 2008 y de la COVID-19). `[Certain]` La presentación y el REF completo describen B y C de forma distinta: citar el REF completo.
  - Cifras a marzo de 2026 y simulación a 3 años. Escenario común para todos los bancos, sin problemas idiosincrásicos de originación, sin acciones de mitigación ni reacción del regulador, en equilibrio parcial.
  - Umbral: mínimo regulatorio más suplementos = **10,5 % de ICAP** (no CET1). Resultado presentado como distribución del sistema; todo el sistema queda por encima del umbral, incluidos los escenarios históricos.
  - `[Guessing]` Las cifras climáticas parecen invertidas (el escenario de −2 % de PIB muestra menos impacto que el de −1 %): comprobar contra el REF completo.
- `[Certain]` **Provisiones (CUB):** art. 111, etapas 1 y 3 = PI × SP × EI; etapa 2, pérdida a **vida completa**; etapas asignadas por el art. 110 Bis y el criterio contable B-6. Art. 129: métodos estándar o internos **basados en la NIF C-16**, grados A-1 a E. `[Likely]` Esquema por etapas desde el 1-ene-2022 (informe de un emisor). **Para el manual:** la misma cartera tiene una provisión local y otra IFRS 9 del grupo; `[Likely]` el ejercicio de la CNBV parte de la local.
- `[Likely]` El ICAP del sistema llegó al 20,00 % en jun-2025, frente a un mínimo del 10,5 % (prensa citando a la CNBV; sin fuente primaria).
- `[Certain]` **Santander México** salió de NYSE (Form 25 del 24-abr-2023) y la CNBV canceló su inscripción en el RNV el 12-may-2023 (detalle en `datos-publicos.md`). No publica resultados de su ejercicio local. Tampoco BBVA México, salvo una frase cualitativa de su casa de bolsa.

## 5. Brasil

- `[Certain]` El BCB incluye en su *Relatório de Estabilidade Financeira* (semestral) un **test de estrés macroeconómico** de **12 trimestres** con balance dinámico y tres escenarios: Base (Focus), Recessão Aguda y Crise de Confiança, con cinco variables (PIB, BRL/USD, Selic, IPCA, paro). Incluye además análisis de sensibilidad, contagio interbancario y estrés de liquidez.
- `[Certain]` El resultado se expresa en **"desenquadramentos"** (incumplir al menos uno de IB, IPR1 o ICP) y en bancos con **restricciones para distribuir beneficios** por no cubrir el colchón de conservación del 2,5 % (Resolución BCB 200/2022).
- `[Certain]` REF de abril de 2025 (`fuentes/2025-04 BCB REF.pdf`): en Crise de Confiança, **el 44 % del activo** quedaría con restricciones y el 46 % por encima del 10,5 %; necesidad de capital del 9,9 % del PR en el trimestre 12.
- `[Certain]` REF de **mayo de 2026** (datos de dic-2025, 97 entidades, 96,72 % del activo): en Crise de Confiança, el 68,7 % del activo sigue por encima del 10,5 % y la necesidad de capital es el **3,1 % del PR**. La comparación con abril de 2025 muestra lo mucho que depende el resultado de la edición. <https://www.bcb.gov.br/content/publicacoes/ref/202605/RELESTAB202605-refPub.pdf>.
- `[Certain]` **Resolución CMN 4.966/2021**, en vigor desde el 1-ene-2025: pérdida esperada por etapas, cercana a IFRS 9. Transición de la **Res. CMN 5.199/2024**: 25 % del impacto al año, y el test aplica el 75 % dentro del horizonte.
- `[Certain]` El trabajo climático del BCB **no es un test de capital**: es un análisis de exposiciones de crédito a riesgos físicos y una encuesta en la que la sequía es el evento de mayor impacto esperado.
- `[Certain]` Los bancos grandes (segmento S1) hacen además su propio ICAAP con programa de *stress test* y plan de capital a al menos tres años (Res. CMN 4.557, art. 40 §2).

## 6. Chile

- `[Likely]` El Banco Central de Chile (IEF del primer semestre de 2026, 19-may-2026) concluye que rentabilidad, capital y liquidez permitirían a los bancos **mantenerse solventes en un escenario de tensión severo**, con el endurecimiento de la financiación como riesgo principal. No se ha comprobado que la métrica sea CET1.
- `[Certain]` **CMF, IAPE (RAN 21-13):** horizonte de **al menos 3 años**; escenarios base, tensión **sin** mitigación y tensión **con** mitigación, con **parámetros agregados de la CMF** y estimaciones propias. En tensión hay que cumplir al menos el mínimo regulatorio; en escenario normal, el objetivo interno. Ratios: patrimonio efectivo/APR, capital básico/APR y capital básico/activos. <https://www.cmfchile.cl/portal/normativa/624/articles-29808_doc_pdf.pdf>.
- `[Certain]` **Requerimiento de capital contracíclico:** del 0,5 % al **1 % de los APR**, con un plazo de 24 meses (reunión de política financiera del primer semestre de 2026, comunicado del 18-may-2026).

## 7. Türkiye

- `[Certain]` Base normativa: reglamento de sistemas internos y proceso de autoevaluación de capital (ISEDES), art. 43 (programa de *stress test*), publicado en el Boletín Oficial n.º 29057 del 11-jul-2014, y guía de la BDDK sobre *stress tests* en la planificación de capital y liquidez del 31-mar-2016. `[Likely]` Vigentes en 2026 (texto tras muro de pago).
- `[Likely]` La BDDK hace macro *stress tests* al menos dos veces al año, y los bancos presentan cada año escenarios detallados en su informe ISEDES.
- `[Certain]` **NIC 29:** BBVA aplica contabilidad de hiperinflación a sus entidades turcas **desde el 1-ene-2022** (impacto estimado sobre datos de mar-2022: −324 M€ de beneficio atribuido y +19 pb de CET1 *fully loaded*). `[Likely]` Localmente, la BDDK decidió que los bancos **no apliquen** contabilidad de inflación en 2025 (decisión 11340 del 18-dic-2025, según prensa). **Para el manual:** es probablemente la mayor diferencia de base contable entre el número del grupo y el local.

## 8. Argentina

- `[Certain]` Régimen "Plan de negocios y proyecciones e Informe de Autoevaluación del Capital", apartado IV, "Pruebas de estrés": supuestos macro del REM y **variables de estrés fijadas por el BCRA** (Com. "A" 6646, 2019). `[Likely]` Sigue vigente en 2026 (el texto ordenado actual no se pudo descargar).
- `[Certain]` NIC 29 obligatoria para las entidades financieras desde los ejercicios iniciados el 1-ene-2020 (Com. "A" 6849).

## 9. Cambio de perímetro: Polonia

- `[Certain]` Erste cerró la compra del 49 % de Santander Bank Polska el **9-ene-2026** por ~7.000 M€ en efectivo; Santander se queda con el 9,7 % tras esa venta y una colocación de ~3,5 % en dic-2025; la operación sumó ~95 pb de CET1. <https://www.santander.com/en/press-room/press-releases/2026/01/santander-completes-the-sale-of-49-of-santander-bank-polska-to-erste-group>.
- `[Likely]` Santander conserva el 100 % de Santander Consumer Bank Polonia (prensa): **Polonia no sale del todo del perímetro** del EBA 2027. Es un ejemplo real de cambio de perímetro entre ejercicios, y de por qué la comparación 2025 frente a 2027 de un mismo grupo hay que hacerla con el perímetro ajustado.

## Huecos que siguen abiertos

- Anexo 12-D de la CUB (número de escenarios, supuestos de balance).
- BCCh: horizonte, métrica y umbral de sus pruebas (bcentral.cl bloquea el acceso automatizado).
- BDDK: escenarios comunes, horizonte y métrica; vigencia de la guía de 2016.
- BCRA: régimen IAC vigente (enlace caído).
- Banxico: sendas de los escenarios A-C, cifras climáticas y descripciones de B y C en el REF completo.
- Fed: supuesto de balance de 2026 y tratamiento de CECL.
- BBVA México: estado de cotización. Tratamiento contable del 9,7 % de Santander Bank Polska y propiedad de Santander Consumer Bank Polonia.
