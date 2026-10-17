---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, jers, escenario, validacion, f1]
---

# Validación F1 · Escenario adverso JERS/ESRB (ejercicio EBA 2025) y estado del escenario 2027

Validación de `investigacion/jers-escenario.md` (a fecha de 2026-10-16). Fuente primaria: `fuentes/2025-02-26 ESRB escenario ST2025.pdf` (28 páginas; metadatos de creación 28-feb-2025), que es la versión corregida que aloja la EBA: [ESRB, Macro-financial scenario for the 2025 EU-wide banking sector stress test (updated 26 February 2025)](https://www.eba.europa.eu/sites/default/files/2025-02/f23c8470-a2e1-410f-b752-55aff8f8e8f4/2025-02-26%20-%20ESRB%20-%20Macrofinancial%20scenario%20for%20the%202025%20EU-wide%20banking%20sector%20stress%20test%20%28updated%2026%20February%202025%29.pdf). En adelante, "PDF ESRB" con su número de página impreso ("Page X of 28").

Convenciones de unidades (las del propio documento): PIB, IPCA/IPC y precios inmobiliarios en **tasa de variación media anual (%)**; "acumulado" = crecimiento acumulado del nivel desde el punto de partida 2024 hasta 2027 (%); "desv. 2027" = desviación del nivel adverso frente al nivel base en 2027 (%); paro en **tasa media anual (%)**, y sus acumulados y desviaciones en **puntos porcentuales (p.p.)**; tipos en **% medio anual**; tipos de cambio en **unidades de divisa por euro, media anual**. Separador decimal: coma.

## 1. Veredicto, afirmación por afirmación, sobre jers-escenario.md

### Takeaway
Todas las cifras de la nota original son correctas. Hay tres correcciones de matiz: la fecha y la naturaleza de la versión del 26-feb-2025, que es una fe de erratas limitada a los swaps en GBP; que la bolsa **no** viene país a país para LatAm, Türkiye ni España; y que el efecto del tipo de cambio no llega solo por los satélites. Argentina queda confirmada como ausente del documento.

### Cited Findings

| # | Afirmación original (resumen) | Veredicto | Redacción corregida | Etiqueta | Fuente / página |
|---|---|---|---|---|---|
| 1 | Fuente: "versión actualizada del 26-feb-2025" | **Corregida (matiz)** | El escenario original se publicó con el lanzamiento del ejercicio el 20-ene-2025. El 26-feb-2025 la JERS envió a la EBA una fe de erratas (ESRB/2025/0014) que **solo corrige "certain tenors of the GBP swap rates"**, y la EBA la publicó como *corrigendum* el 28-feb-2025. El PDF local es la versión corregida. Ninguna cifra de PIB, paro, precios ni tipos de cambio cambió. | `[Certain]` | [Carta ESRB 26-feb-2025](https://www.esrb.europa.eu/mppa/stress/shared/pdf/esrb.stress_test250228_letter~54efbffa63.en.pdf); [página EBA ST 2025](https://www.eba.europa.eu/eu-wide-stress-test-2025); [nota de prensa EBA 20-ene-2025](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-its-2025-eu-wide-stress-test) |
| 2 | El escenario 2027 aún no está publicado | **Confirmada** | A 16-oct-2026 la página de la EBA solo lista los documentos *draft* del 11-jun-2026 (nota metodológica, plantillas y su guía). No hay escenario macro 2027. | `[Likely]` (no se puede probar una ausencia; sí que no figura en las páginas oficiales) | [EBA, EU-wide stress testing](https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-stress-testing) |
| 3 | Saldrá hacia enero de 2027 | **Confirmada como inferencia; sube de nivel** | Precedente de 2025: la Junta General de la JERS aprobó el escenario el 14-ene-2025, la JERS lo envió el 15-ene y la EBA lanzó el ejercicio el 20-ene-2025. El *draft* 2027 fija como fecha de referencia el cierre de 2026 y como horizonte 2027-2029. La EBA prevé publicar los resultados "around summer" de 2027. | `[Likely]` | PDF ESRB p. 1; [EBA 20-ene-2025](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-its-2025-eu-wide-stress-test); draft note 2027 párr. 21 y 24; [EBA Work Programme 2027, §1.2.3.1](https://www.eba.europa.eu/sites/default/files/2026-09/f6561915-4192-4d73-88ac-10f8bc09abca/EBA%20Work%20programme%202027.pdf) |
| 4 | El adverso lo diseñan JERS y BCE con las autoridades competentes, la EBA y los BCN; la base la aporta el BCE (nota EBA 2027, párr. 42) | **Confirmada** | Literal en el párr. 42 de la *draft note* 2027, y también en el párr. 42 de la nota de 2025. Para 2025, el PDF ESRB precisa que el adverso lo diseñó la *Task Force on Stress Testing* de la JERS "in close collaboration with" el BCE, y que la base UE son las proyecciones de diciembre de 2024 de los bancos centrales nacionales. | `[Certain]` | [Draft note 2027](https://www.eba.europa.eu/sites/default/files/2026-06/7185aac4-4a70-4d83-ae1b-1cfca979ae07/2027%20EU-wide%20stress%20test%20-%20Draft%20Methodological%20Note.pdf), párr. 42; PDF ESRB p. 1 |
| 5 | La Junta General aprobó el escenario 2025 el 14-ene-2025 | **Confirmada** | Aprobado el 14-ene-2025 y enviado a la EBA el 15-ene-2025. | `[Certain]` | PDF ESRB p. 1 |
| 6 | Base no UE: sobre todo el WEO del FMI de octubre de 2024 y datos de la OCDE (nota al pie 2) | **Confirmada** | Nota al pie 2 (p. 1). Las notas de cada tabla (PIB, paro, IPC, vivienda, tipos largos, swaps) repiten que la base no UE sale del WEO de octubre de 2024. | `[Certain]` | PDF ESRB pp. 1, 13-18, 24 |
| 7 | La base de México en el EBA es la del FMI, no la de Banxico ni la de la filial | **Confirmada** | Se sigue de lo anterior. Añadido: en tipos de cambio, bolsa y materias primas la base es **plana** (sin cambios desde el punto de partida o la fecha de corte), no la del FMI. | `[Certain]` | PDF ESRB pp. 13, 19, 20 |
| 8 | Narrativa: geopolítica, barreras comerciales, repunte inflacionista de oferta | **Confirmada** | Sección 2, "Aggravation of geopolitical tensions leading to depressed global growth". | `[Certain]` | PDF ESRB pp. 2-4 |
| 9 | Tabla de PIB (10 filas) | **Confirmada, cifra a cifra** | Tabla 4.1.1. Las diez filas coinciden. "Crecimiento acumulado" = nivel 2027 frente a 2024. Ver el aviso sobre EE. UU. en la sección 2. | `[Certain]` | PDF ESRB p. 13 |
| 10 | México por años −4,7 / −2,2 / −0,1; España −2,5 / −3,5 / +2,0 | **Confirmada** | Son tasas medias anuales del adverso 2025/2026/2027. | `[Certain]` | PDF ESRB p. 13 |
| 11 | Paro adverso frente a base en 2027: ES 15,6 frente a 9,9; MX 8,8 frente a 3,5; BR 11,7 frente a 7,4 | **Confirmada** | Tabla 4.1.2. Desviación 2027: ES +5,7 p.p., MX +5,3 p.p., BR +4,3 p.p. | `[Certain]` | PDF ESRB p. 14 |
| 12 | Vivienda: ES −17,2 % (−30,1 %), MX −8,1 % (−22,1 %), BR −19,4 % (−25,6 %), UK −26,7 % (−30,8 %) | **Confirmada** | Tabla 4.1.4 (*residential real estate prices*): acumulado 2024-2027 y desviación frente a la base en 2027. | `[Certain]` | PDF ESRB p. 16 |
| 13 | El documento incluye inflación, tipos, tipos de cambio y bolsa "por país" | **Corregida** | Hay series por país de PIB, paro, IPCA/IPC, vivienda, inmobiliario comercial (CRE) y tipos a largo para ES, UK, US, TR, BR, MX, CL, CO, PE. Los tipos de cambio van por par EUR/xxx: hay MXN, BRL, TRY, CLP, COP y PEN; EUR/GBP y EUR/USD **no se mueven** en el adverso. Hay curvas swap para EUR, GBP, USD, TRY, BRL, MXN, CLP y COP, pero **no para PEN**. La **bolsa no viene por país** salvo UE, NO, UK, US, JP, CA, CH y AU&NZ; LatAm y Türkiye caen en "Rest of the world" (−66 / −61 / −57 %), y España usa el choque UE. | `[Certain]` | PDF ESRB pp. 13-24 |
| 14 | El escenario cubre las geografías de Santander y BBVA | **Confirmada con matiz** | Cubierto en PIB, paro, IPC, vivienda, CRE y tipos largos para MX, BR, CL, CO, PE, TR, UK y US. Huecos: bolsa (solo "resto del mundo"), swap PEN (se usa la curva RoW, idéntica a la USD) y Argentina (nada). | `[Certain]` | PDF ESRB pp. 13-24 |
| 15 | Argentina no aparece en el PIB y cae en "Resto del mundo" `[Likely]` | **Confirmada; sube a [Certain] la ausencia** | La palabra "Argentina" no aparece en todo el documento, tampoco como par EUR/ARS ni como curva swap. Que deba tratarse con las filas "Rest of the world" es explícito solo para swaps y tipos de cambio (ver sección 3). | `[Certain]` (ausencia) / `[Likely]` (tratamiento en PIB y paro) | PDF ESRB pp. 13-24; nota EBA 2025 párr. 375-376 |
| 16 | La severidad relativa no es homogénea (MX y TR sufren más que ES en PIB; ES más en vivienda) | **Confirmada, con precisión** | Medida por acumulado: MX −6,9 y TR −6,6 frente a ES −4,1. Medida por desviación frente a la base, la distancia se estrecha: MX −11,9, TR −14,8, ES −9,8. En vivienda, ES −17,2 % acumulado y −30,1 % de desviación frente a MX −8,1 % y −22,1 %. | Cifras `[Certain]`; lectura `[Likely]` | PDF ESRB pp. 13, 16 |
| 17 | Balance estático (párr. 35): la depreciación no reduce el tamaño de la filial en euros; el efecto llega por los satélites | **Corregida (incompleta)** | El párr. 35 (idéntico en la nota de 2025 y en el *draft* 2027) fija los saldos en la divisa de reporte al tipo de cambio de cierre (31-dic-2024 en 2025; 31-dic-2026 en 2027) y excluye el efecto FX en los APR salvo en riesgo de mercado. El tipo de cambio sí entra: (a) en **FX lending** (párr. 147-148 del *draft* 2027), con satélites sobre las tasas de transición y *add-on* de LTV en LR para carteras con más del 5 % en divisa por país de contraparte; (b) en el margen de intereses (NII), con un factor corrector (párr. 380 del 2027 y 376 del 2025); (c) en las comisiones (NFCI), que "includes FX variations to the starting point"; (d) en riesgo de mercado. | `[Certain]` | Nota EBA 2025 párr. 35, 375-376; draft note 2027 párr. 35, 147-148, 379-380 y cuadro resumen |
| 18 | Las variables que no da el escenario las deriva el banco con modelos auxiliares | **Confirmada en crédito; refutada en mercado** | En riesgo de crédito el banco traslada el escenario con sus satélites. En riesgo de mercado la EBA **prohíbe** extrapolar o ampliar factores: se aplica el choque más cercano, y por ejemplo el choque bursátil UE se usa igual para todos los países UE (*draft* 2027, párr. 260). | `[Likely]` (crédito) / `[Certain]` (mercado) | Draft note 2027 párr. 113-118, 147 y 260 |
| 19 | El gráfico 14 compara la severidad con el CCAR 2024 y los dos escenarios del BoE de 2024 | **Confirmada; añadido aviso de medida** | Texto literal en p. 11 y gráfico en p. 12. Ver sección 4: la métrica no es de pico a valle. | `[Certain]` | PDF ESRB pp. 11-12 |
| 20 | Argentina no tiene fila en las tablas del anexo ni en tipos de cambio | **Confirmada** | Tampoco tiene curva swap. | `[Certain]` | PDF ESRB pp. 13-24 |

### Inferences
- La nota original es fiable en cifras. Sus errores son de alcance (cree que hay bolsa por país) y de mecanismo FX (lo reduce a los satélites). `[Likely]`

### Gaps
- No se ha descargado la tabla de erratas (Excel del 28-feb-2025). La carta dice que afecta solo a tramos del swap GBP; no se ha comprobado qué tramos ni cuánto.

## 2. Sendas base y adversa por país (para el anexo S3)

### Takeaway
El escenario da sendas completas para las nueve geografías de los grupos, salvo Argentina. Hay tres rarezas que el manual debe explicar. EUR/USD y EUR/GBP no se mueven en el adverso. La bolsa de LatAm y Türkiye es el choque "Rest of the world". Las variables nominales de Türkiye (vivienda +128,7 % acumulado) solo se entienden en desviación frente a la base (−19,3 %).

### Cited Findings
Todas las tablas proceden del PDF ESRB, anexo 4.1, páginas indicadas. EA = zona del euro; LA = agregado Latin America; WR = Rest of the world.

**2.1 PIB real (tabla 4.1.1, p. 13). Tasa media anual (%), acumulado (%), mínimo desde el punto de partida (%), desviación del nivel en 2027 (%)**

| País | 2024 hist. | Base 25 | Base 26 | Base 27 | Adv 25 | Adv 26 | Adv 27 | Acumulado | Mínimo | Desv. 2027 |
|---|---|---|---|---|---|---|---|---|---|---|
| EA | 0,7 | 1,1 | 1,4 | 1,3 | −2,3 | −4,0 | 0,0 | −6,2 | −6,2 | −9,8 |
| UE | 0,9 | 1,4 | 1,6 | 1,5 | −2,3 | −4,2 | 0,0 | −6,3 | −6,3 | −10,4 |
| España | 3,1 | 2,5 | 1,9 | 1,7 | −2,5 | −3,5 | 2,0 | −4,1 | −5,9 | −9,8 |
| Reino Unido | 1,1 | 1,5 | 1,5 | 1,5 | −4,5 | −4,5 | −1,3 | −10,0 | −10,0 | −13,9 |
| EE. UU. | 2,8 | 2,2 | 2,0 | 2,1 | −5,1 | −2,5 | 4,3 | −3,4 | −7,4 | −9,3 |
| Türkiye | 3,0 | 2,7 | 3,2 | 3,4 | −4,9 | −2,7 | 1,0 | −6,6 | −7,5 | −14,8 |
| Latin America | 1,7 | 2,3 | 2,5 | 2,6 | −2,7 | −0,6 | 0,9 | −2,4 | −3,3 | −9,3 |
| Brasil | 3,0 | 2,2 | 2,3 | 2,4 | −3,3 | −0,6 | 1,0 | −3,0 | −3,9 | −9,2 |
| México | 1,5 | 1,3 | 2,0 | 2,3 | −4,7 | −2,2 | −0,1 | −6,9 | −6,9 | −11,9 |
| Chile | 2,5 | 2,4 | 2,5 | 2,4 | −5,1 | −0,2 | 2,1 | −3,3 | −5,3 | −10,0 |
| Colombia | 1,6 | 2,5 | 2,8 | 3,0 | −4,1 | −0,1 | 1,6 | −2,7 | −4,2 | −10,3 |
| Perú | 3,0 | 2,6 | 2,3 | 2,3 | −3,9 | −0,6 | 0,9 | −3,6 | −4,5 | −10,3 |
| Rest of the world | 2,1 | 3,9 | 4,2 | 3,9 | −3,2 | −1,5 | 1,5 | −3,2 | −4,7 | −13,9 |

**2.2 Tasa de paro (tabla 4.1.2, p. 14). Media anual (%); variaciones en p.p.**

| País | 2024 | Base 25 | Base 26 | Base 27 | Adv 25 | Adv 26 | Adv 27 | Acum. (p.p.) | Máx. (p.p.) | Desv. 2027 (p.p.) |
|---|---|---|---|---|---|---|---|---|---|---|
| EA | 6,4 | 6,4 | 6,2 | 6,0 | 8,1 | 10,6 | 11,9 | 5,6 | 5,6 | 5,9 |
| UE | 5,8 | 5,9 | 5,7 | 5,5 | 7,7 | 10,3 | 11,6 | 5,8 | 5,8 | 6,1 |
| España | 11,5 | 10,8 | 10,4 | 9,9 | 14,1 | 16,8 | 15,6 | 4,1 | 5,3 | 5,7 |
| Reino Unido | 4,3 | 4,1 | 4,0 | 4,0 | 7,2 | 9,6 | 10,2 | 5,9 | 5,9 | 6,2 |
| EE. UU. | 4,1 | 4,4 | 4,3 | 4,2 | 8,9 | 10,0 | 8,6 | 4,6 | 6,0 | 4,5 |
| Türkiye | 9,3 | 9,9 | 9,6 | 9,5 | 15,6 | 16,2 | 15,6 | 6,3 | 6,9 | 6,1 |
| Latin America | 6,2 | 6,2 | 6,3 | 6,3 | 9,2 | 10,5 | 10,7 | 4,6 | 4,6 | 4,5 |
| Brasil | 7,2 | 7,2 | 7,3 | 7,4 | 11,6 | 12,1 | 11,7 | 4,5 | 5,0 | 4,3 |
| México | 3,0 | 3,3 | 3,4 | 3,5 | 5,2 | 7,6 | 8,8 | 5,9 | 5,9 | 5,3 |
| Chile | 8,5 | 8,0 | 7,8 | 7,7 | 11,8 | 12,5 | 12,1 | 3,6 | 4,0 | 4,4 |
| Colombia | 10,2 | 10,0 | 9,8 | 9,6 | 13,4 | 14,4 | 14,4 | 4,2 | 4,2 | 4,8 |
| Perú | 6,8 | 6,5 | 6,5 | 6,5 | 9,9 | 11,1 | 11,3 | 4,6 | 4,6 | 4,8 |
| Rest of the world | 9,3 | 9,9 | 9,6 | 9,5 | 15,6 | 16,1 | 15,4 | 6,2 | 6,8 | 6,0 |

**2.3 IPCA / IPC (tabla 4.1.3, p. 15). Tasa media anual (%); acumulado (%); desviación del nivel de precios en 2027 (%)**

| País | 2024 | Base 25 | Base 26 | Base 27 | Adv 25 | Adv 26 | Adv 27 | Acumulado | Desv. 2027 |
|---|---|---|---|---|---|---|---|---|---|
| EA | 2,4 | 2,1 | 1,9 | 2,1 | 4,5 | 3,3 | 2,0 | 10,1 | 3,7 |
| UE | 2,5 | 2,4 | 2,0 | 2,1 | 5,0 | 3,5 | 1,9 | 10,7 | 3,9 |
| España | 2,9 | 2,1 | 1,7 | 2,4 | 4,9 | 2,9 | 1,1 | 9,1 | 2,6 |
| Reino Unido | 2,5 | 2,0 | 2,0 | 2,0 | 4,6 | 2,5 | 1,5 | 8,8 | 2,6 |
| EE. UU. | 2,3 | 1,9 | 2,1 | 2,4 | 5,7 | 3,4 | 1,8 | 11,3 | 4,4 |
| Türkiye | 43,0 | 24,0 | 17,2 | 15,3 | 29,6 | 18,2 | 12,6 | 72,5 | 2,9 |
| Latin America | 19,4 | 7,9 | 5,4 | 3,9 | 10,6 | 6,8 | 3,5 | 22,1 | 3,3 |
| Brasil | 4,3 | 3,3 | 3,0 | 3,0 | 4,1 | 4,0 | 3,5 | 12,0 | 2,2 |
| México | 4,5 | 3,2 | 3,0 | 3,0 | 7,3 | 3,7 | −0,5 | 10,7 | 1,1 |
| Chile | 4,5 | 3,5 | 3,0 | 3,0 | 4,9 | 3,7 | 3,4 | 12,5 | 2,5 |
| Colombia | 5,7 | 3,5 | 3,0 | 3,0 | 6,1 | 4,6 | 3,5 | 14,8 | 4,5 |
| Perú | 2,4 | 2,0 | 2,0 | 2,0 | 4,5 | 3,6 | 2,5 | 10,9 | 4,5 |
| Rest of the world | 13,6 | 9,8 | 8,2 | 7,2 | 13,8 | 8,6 | 4,9 | 29,6 | 1,8 |

(La tabla trae una columna "minimum growth from the starting point" que en el IPC replica la tasa adversa de 2025. Se omite por no ser informativa.)

**2.4 Precio de la vivienda (RRE) (tabla 4.1.4, p. 16). Tasa media anual (%); acumulado (%); mínimo (%); desviación 2027 (%)**

| País | 2024 | Base 25 | Base 26 | Base 27 | Adv 25 | Adv 26 | Adv 27 | Acumulado | Mínimo | Desv. 2027 |
|---|---|---|---|---|---|---|---|---|---|---|
| EA | 1,6 | 3,3 | 2,7 | 2,4 | −3,1 | −7,9 | −4,5 | −14,8 | −14,8 | −21,6 |
| UE | 1,8 | 3,0 | 2,7 | 2,3 | −3,5 | −8,4 | −4,7 | −15,7 | −15,7 | −22,2 |
| España | 7,9 | 7,0 | 6,1 | 4,3 | −2,3 | −9,8 | −6,2 | −17,2 | −17,2 | −30,1 |
| Reino Unido | 2,4 | 1,9 | 1,9 | 1,9 | −4,0 | −13,0 | −12,2 | −26,7 | −26,7 | −30,8 |
| EE. UU. | 7,8 | 7,4 | 7,6 | 7,9 | −6,5 | −3,5 | 6,6 | −3,9 | −9,8 | −22,9 |
| Türkiye | 65,7 | 46,7 | 40,0 | 38,0 | 37,3 | 30,3 | 27,8 | 128,7 | 37,3 | −19,3 |
| Latin America | 20,2 | 8,7 | 6,2 | 4,7 | −4,4 | −3,5 | −2,6 | −10,1 | −10,1 | −25,6 |
| Brasil | 3,9 | 2,9 | 2,6 | 2,6 | −9,4 | −6,7 | −4,6 | −19,4 | −19,4 | −25,6 |
| México | 7,1 | 5,8 | 5,6 | 5,6 | −0,5 | −3,4 | −4,3 | −8,1 | −8,1 | −22,1 |
| Chile | 6,2 | 5,2 | 4,7 | 4,7 | −1,1 | −4,2 | −5,1 | −10,1 | −10,1 | −22,1 |
| Colombia | 4,3 | 2,2 | 1,6 | 1,7 | −3,9 | −7,0 | −7,9 | −17,7 | −17,7 | −22,1 |
| Perú | 3,2 | 2,8 | 2,8 | 2,8 | −3,4 | −6,0 | −6,9 | −15,4 | −15,4 | −22,1 |
| Rest of the world | 13,0 | 9,2 | 7,6 | 6,6 | −3,9 | −2,2 | −0,9 | −6,8 | −6,8 | −25,6 |

**2.5 Inmobiliario comercial (CRE) (tabla 4.1.5, p. 17). Sin dato histórico 2024: "for almost all countries, public data are not available"**

| País | Base 25 | Base 26 | Base 27 | Adv 25 | Adv 26 | Adv 27 | Acumulado | Mínimo | Desv. 2027 |
|---|---|---|---|---|---|---|---|---|---|
| EA | 1,4 | 1,2 | 1,2 | −9,1 | −13,6 | −9,1 | −28,6 | −28,6 | −31,3 |
| UE | 1,5 | 1,3 | 1,3 | −9,4 | −14,3 | −9,3 | −29,5 | −29,5 | −32,3 |
| España | 2,9 | 3,0 | 1,6 | −5,8 | −12,1 | −7,3 | −23,2 | −23,2 | −28,8 |
| Reino Unido | 1,8 | 0,7 | 1,2 | −7,9 | −20,1 | −17,2 | −39,1 | −39,1 | −41,3 |
| EE. UU. | 3,8 | 4,0 | 4,7 | −18,8 | −19,9 | −6,7 | −39,3 | −39,3 | −46,3 |
| Türkiye | 4,3 | 2,7 | 8,0 | −5,9 | −18,5 | −8,5 | −29,8 | −29,8 | −39,3 |
| Latin America | 2,1 | 0,0 | 1,3 | −15,2 | −15,7 | −8,5 | −34,6 | −34,6 | −36,7 |
| Brasil | 3,0 | 0,9 | 1,3 | −15,6 | −15,8 | −10,9 | −36,7 | −36,7 | −39,8 |
| México | 3,3 | 2,4 | 4,0 | −12,9 | −17,5 | −11,5 | −36,4 | −36,4 | −42,1 |
| Chile | 3,1 | 1,8 | 2,4 | −8,8 | −13,7 | −11,4 | −30,3 | −30,3 | −35,1 |
| Colombia | 0,9 | −0,3 | 0,9 | −11,3 | −16,4 | −13,2 | −35,7 | −35,7 | −36,7 |
| Perú | 2,4 | 1,2 | 1,9 | −10,1 | −14,9 | −12,2 | −32,8 | −32,8 | −36,3 |
| Rest of the world | 4,1 | 1,5 | 2,4 | −17,9 | −17,4 | −9,5 | −38,6 | −38,6 | −43,3 |

**2.6 Tipos a largo plazo (deuda soberana a 10 años) (tabla 4.1.6, p. 18). % medio anual; "media 2024" y "último 2024" (media de diciembre de 2024)**

| País | Media 2024 | Último 2024 | Base 25 | Base 26 | Base 27 | Adv 25 | Adv 26 | Adv 27 |
|---|---|---|---|---|---|---|---|---|
| EA | 2,88 | 2,73 | 2,93 | 3,07 | 3,21 | 4,63 | 4,45 | 4,34 |
| UE | 3,08 | 2,96 | 3,12 | 3,22 | 3,35 | 4,80 | 4,60 | 4,47 |
| España | 3,15 | 2,91 | 3,16 | 3,33 | 3,50 | 5,74 | 5,33 | 5,06 |
| Reino Unido | 4,1 | 4,4 | 4,2 | 4,2 | 4,2 | 6,0 | 5,9 | 5,7 |
| EE. UU. | 4,2 | 4,4 | 4,5 | 4,6 | 4,7 | 5,7 | 5,7 | 5,7 |
| Türkiye | 41,6 | 29,9 | 33,9 | 20,1 | 16,9 | 36,7 | 22,8 | 19,3 |
| Latin America | 8,9 | 9,6 | 8,6 | 8,1 | 7,6 | 11,4 | 10,7 | 10,0 |
| Brasil | 11,9 | 14,2 | 11,5 | 10,8 | 10,1 | 14,3 | 13,4 | 12,5 |
| México | 9,7 | 10,2 | 9,3 | 8,8 | 8,2 | 12,1 | 11,4 | 10,6 |
| Chile | 5,8 | 5,8 | 5,6 | 5,3 | 4,9 | 8,4 | 7,9 | 7,4 |
| Colombia | 10,5 | 11,2 | 10,1 | 9,5 | 8,9 | 12,9 | 12,1 | 11,3 |
| Perú | 6,8 | 6,6 | 6,6 | 6,2 | 5,8 | 9,4 | 8,8 | 8,2 |
| Rest of the world | 4,2 | 4,4 | 4,5 | 4,6 | 4,7 | 7,4 | 7,2 | 7,2 |

**2.7 Bolsa (tabla 4.1.7, p. 19). Desviación frente al punto de partida (%). En la base, la bolsa no se mueve**

| Área | 2025 | 2026 | 2027 |
|---|---|---|---|
| Unión Europea (se aplica a España) | −50 | −46 | −42 |
| Reino Unido | −52 | −48 | −45 |
| EE. UU. | −61 | −56 | −52 |
| Rest of the world (MX, BR, CL, CO, PE, TR, AR) | −66 | −61 | −57 |

(Otras filas: Noruega −42 / −39 / −36; Japón −35 / −32 / −30; Canadá −35 / −33 / −30; Suiza −43 / −40 / −37; Australia y Nueva Zelanda −40 / −37 / −34.)

**2.8 Tipos de cambio (tabla 4.1.10, p. 20). Unidades de divisa por euro, media anual. Base constante en el nivel de 2024. Un aumento es una apreciación del euro. La depreciación de la divisa local frente al EUR (%) es cálculo propio a partir de la tabla**

| Par | 2024 = base 25-27 | Adv 25 | Adv 26 | Adv 27 | Deprec. frente al EUR 25 / 26 / 27 (cálc.) |
|---|---|---|---|---|---|
| EUR/USD | 1,08 | 1,08 | 1,08 | 1,08 | 0 / 0 / 0 |
| EUR/GBP | 0,85 | 0,85 | 0,85 | 0,85 | 0 / 0 / 0 |
| EUR/MXN | 19,82 | 21,59 | 21,27 | 21,01 | +8,9 / +7,3 / +6,0 |
| EUR/BRL | 5,84 | 6,62 | 6,48 | 6,36 | +13,4 / +11,0 / +8,9 |
| EUR/TRY | 35,59 | 48,57 | 46,25 | 44,34 | +36,5 / +30,0 / +24,6 |
| EUR/CLP | 1020,95 | 1179,32 | 1150,94 | 1127,65 | +15,5 / +12,7 / +10,5 |
| EUR/COP | 4406,72 | 4792,01 | 4722,98 | 4666,33 | +8,7 / +7,2 / +5,9 |
| EUR/PEN | 4,06 | 4,23 | 4,20 | 4,18 | +4,2 / +3,4 / +3,0 |
| EUR-rest of the world | 1,08 | 1,18 | 1,16 | 1,15 | +9,3 / +7,4 / +6,5 |

No existe el par EUR/ARS.

**2.9 Swaps (tabla 4.1.11, pp. 21-24). % medio anual. Tramos 3M, 1A, 5A y 10A (el documento da 1M, 3M, 1A, 2A, 3A, 5A, 7A, 10A, 20A y 30A)**

| Divisa | Tramo | Media 2024 | Último 2024 | Base 25 | Base 26 | Base 27 | Adv 25 | Adv 26 | Adv 27 |
|---|---|---|---|---|---|---|---|---|---|
| EUR | 3M | 3,57 | 2,81 | 2,13 | 2,03 | 2,18 | 3,40 | 3,08 | 3,04 |
| EUR | 1A | 3,22 | 2,35 | 2,14 | 2,06 | 2,20 | 3,29 | 3,00 | 2,97 |
| EUR | 5A | 2,58 | 2,15 | 2,25 | 2,31 | 2,37 | 3,22 | 3,10 | 3,03 |
| EUR | 10A | 2,58 | 2,24 | 2,34 | 2,37 | 2,42 | 3,13 | 3,03 | 2,96 |
| GBP | 3M | 5,00 | 4,64 | 4,13 | 3,19 | 3,00 | 5,31 | 4,28 | 4,02 |
| GBP | 1A | 4,69 | 4,42 | 4,10 | 3,24 | 3,07 | 4,87 | 3,95 | 3,72 |
| GBP | 5A | 3,88 | 3,97 | 3,99 | 3,53 | 3,42 | 4,83 | 4,31 | 4,14 |
| GBP | 10A | 3,80 | 3,95 | 3,85 | 3,88 | 3,85 | 4,59 | 4,57 | 4,49 |
| USD (= RoW) | 3M | 5,06 | 4,37 | 4,45 | 4,19 | 4,09 | 6,01 | 5,63 | 5,43 |
| USD (= RoW) | 1A | 4,64 | 4,17 | 4,42 | 4,18 | 4,11 | 5,63 | 5,30 | 5,15 |
| USD (= RoW) | 5A | 3,80 | 3,88 | 4,26 | 4,16 | 4,18 | 5,15 | 4,98 | 4,94 |
| USD (= RoW) | 10A | 3,74 | 3,86 | 4,07 | 4,13 | 4,26 | 4,93 | 4,93 | 5,01 |
| TRY | 3M | 51,30 | 49,41 | 43,55 | 29,82 | 26,54 | 46,26 | 32,33 | 28,87 |
| TRY | 1A | 52,97 | 48,61 | 45,23 | 31,49 | 28,22 | 46,77 | 34,74 | 31,29 |
| TRY | 5A | 34,96 | 35,68 | 27,22 | 13,48 | 10,21 | 30,36 | 17,53 | 14,11 |
| TRY | 10A | 30,73 | 31,90 | 22,98 | 9,24 | 5,97 | 24,58 | 10,73 | 7,35 |
| BRL | 3M | 10,94 | 12,73 | 11,03 | 9,54 | 8,06 | 12,78 | 11,16 | 9,56 |
| BRL | 1A | 11,32 | 14,71 | 11,41 | 9,92 | 8,44 | 12,83 | 11,21 | 9,62 |
| BRL | 5A | 11,84 | 14,54 | 11,92 | 10,43 | 8,96 | 13,11 | 11,50 | 9,91 |
| BRL | 10A | 11,86 | 13,98 | 11,95 | 10,46 | 8,98 | 13,46 | 11,86 | 10,28 |
| MXN | 3M | 11,00 | 10,18 | 9,15 | 7,00 | 6,44 | 10,90 | 8,62 | 7,94 |
| MXN | 1A | 10,44 | 9,56 | 8,59 | 6,44 | 5,87 | 10,73 | 8,45 | 7,77 |
| MXN | 5A | 9,12 | 9,15 | 7,27 | 5,12 | 4,56 | 9,84 | 7,57 | 6,90 |
| MXN | 10A | 9,06 | 9,26 | 7,22 | 5,06 | 4,50 | 8,73 | 6,47 | 5,80 |
| CLP | 3M | 5,86 | 5,07 | 5,39 | 4,42 | 3,87 | 7,26 | 6,16 | 5,48 |
| CLP | 1A | 5,27 | 4,98 | 4,80 | 3,83 | 3,29 | 7,18 | 6,08 | 5,41 |
| CLP | 5A | 4,90 | 5,10 | 4,44 | 3,46 | 2,92 | 6,76 | 5,66 | 5,00 |
| CLP | 10A | 5,11 | 5,34 | 4,65 | 3,67 | 3,13 | 6,22 | 5,13 | 4,48 |
| COP | 3M | 10,28 | 8,81 | 9,46 | 7,75 | 6,80 | 11,67 | 9,81 | 8,70 |
| COP | 1A | 9,23 | 8,36 | 8,41 | 6,70 | 5,74 | 11,45 | 9,59 | 8,49 |
| COP | 5A | 7,75 | 8,23 | 6,93 | 5,22 | 4,26 | 10,29 | 8,44 | 7,36 |
| COP | 10A | 8,06 | 8,70 | 7,24 | 5,53 | 4,57 | 8,83 | 7,01 | 5,94 |

No hay curva PEN ni ARS. La curva "RoW" del documento repite cifra a cifra la curva USD en todos los tramos (p. 24 frente a p. 22).

**2.10 Otros datos del documento**
- iTraxx 5A, nivel en p.b. (tabla 4.1.9, p. 19). Overall: 56 en 2024; base 71 / 76 / 81; adverso 240 / 198 / 168. Sub-financials: 115; base 130 / 135 / 140; adverso 544 / 434 / 355. — PDF ESRB p. 19
- Medianas UE: paro +6,0 p.p. acumulado y +6,2 p.p. frente a la base. Vivienda: −3,2 % (2025), −10,4 % (2026) y −6,1 % (2027). CRE: −8,0 %, −15,6 % y −9,9 %. — PDF ESRB pp. 9-10
- La tabla 4.1.8 (demanda exterior y materias primas) sale en el PDF como imagen y no se extrae como texto. Nota de la tabla: en la base, las materias primas se mantienen al nivel de la fecha de corte. — PDF ESRB p. 19

### Inferences
- **EE. UU. no es un caso de "acumulado bajo, choque bajo".** El acumulado (−3,4 %) esconde un valle del −7,4 % y un rebote del +4,3 % en 2027. Para PD/LGD que dependen del nivel, la variable relevante es el mínimo o la desviación (−9,3 %), no el acumulado. `[Likely]`
- **Las filiales en UK y US no sufren choque de tipo de cambio frente al euro** (EUR/GBP y EUR/USD planos). Las de LatAm y Türkiye sí: de +4,2 % (PEN) a +36,5 % (TRY) en 2025. Como EUR/USD no se mueve, la depreciación frente al USD es la misma que frente al EUR; por ejemplo, el BRL/USD implícito pasa de 5,41 a 6,13 (cálculo propio). `[Certain]` en las cifras; `[Likely]` en la lectura.
- **Desviación común en vivienda para LatAm.** MX, CL, CO y PE comparten −22,1 % de desviación en 2027, y BR comparte con LA y WR el −25,6 %. Apunta a una calibración regional de la desviación más que a una calibración país a país. `[Guessing]` sobre el método; `[Certain]` sobre la coincidencia de cifras.
- **"Rest of the world" es un proxy muy burdo.** Su paro reproduce casi exactamente el de Türkiye (base idéntica: 9,3 / 9,9 / 9,6 / 9,5), sus tipos largos base son los de EE. UU. y su curva swap es la USD. Aplicarlo a Argentina, con tipos y una inflación de otro orden, dejaría el riesgo de tipo de interés y de inflación muy por debajo de la realidad. `[Likely]`
- **Türkiye exige leer desviaciones, no tasas.** Vivienda +128,7 % nominal acumulado en el adverso, pero −19,3 % frente a la base. El IPC adverso de 2025 (29,6 %) es mayor que el de la base (24,0 %). Un satélite en términos nominales daría señales erróneas. `[Likely]`
- En México el IPC adverso de 2027 es −0,5 %: una deflación de un año, rara en los escenarios del manual. `[Certain]` (cifra)

### Gaps
- Las sendas de demanda exterior y materias primas (tabla 4.1.8) y la descomposición sectorial del VAB solo están en el Excel del escenario, que no se ha descargado.
- Los tramos swap 1M, 2A, 3A, 7A, 20A y 30A están en el PDF (pp. 21-24) pero no se han transcrito aquí.

## 3. Construcción de la base y del adverso fuera de la UE; países sin senda

### Takeaway
La base no UE sale del WEO del FMI de octubre de 2024 (con datos de la OCDE). Tipos de cambio, bolsa y materias primas se mantienen planos en la base. Para divisas sin senda, la metodología EBA manda usar la curva swap y el choque cambiario "Rest of the world". Para PIB, paro o vivienda de un país sin fila (Argentina) no hay regla explícita en las notas revisadas.

### Cited Findings
- Base no UE: "based mainly on the projections from the October 2024 IMF World Economic Outlook and data from the OECD" (nota al pie 2). Base UE: proyecciones de diciembre de 2024 de los bancos centrales nacionales. — PDF ESRB p. 1
- Tipos largos: la base no UE sale del WEO de octubre de 2024. Para Türkiye, Macao y Ucrania, el punto de partida medio también sale del WEO. — PDF ESRB p. 18
- Swaps: la base de la zona euro (3M) son cálculos del personal del BCE. Para los países UE fuera del euro y Noruega, sus bancos centrales dieron el 3M y el 10A. "The baseline for other countries is based on projections from the October 2024 IMF World Economic Outlook". Los demás tramos se obtienen por interpolación y extrapolación. — PDF ESRB p. 24
- En la base, los tipos de cambio no cambian (p. 20), la bolsa no cambia (p. 19) y las materias primas se quedan al nivel de la fecha de corte (p. 19). — PDF ESRB
- Diseño del adverso: lo hizo la *Task Force on Stress Testing* de la JERS con el BCE. El documento remite la metodología al anexo 3 del escenario de 2020 y la descomposición sectorial al anexo 4.3 del de 2023 (nota al pie 3). — PDF ESRB p. 1
- Convenio *no policy change*: no se suponen medidas monetarias ni fiscales distintas de las de la base. Los tipos sin riesgo y las primas del adverso son coherentes con las expectativas de mercado. — PDF ESRB p. 2
- En la UE, la mitad de la caída del PIB frente a la base se debe a choques exteriores (materias primas y comercio). — PDF ESRB p. 5
- Regla EBA 2025 para divisas sin senda: "If a currency's swap rate curve is not provided in the macroeconomic scenario, the swap rate curve for 'rest of the world' is used… For currencies where no stress is provided, the 'rest of the world' currency shock shall be used". — [Nota metodológica EBA 2025](https://www.eba.europa.eu/eu-wide-stress-test-2025), párr. 375-376 (fichero local `2024-11 EBA ST2025 methodological note.pdf`). Se repite en los párr. 379-380 del [draft 2027](https://www.eba.europa.eu/sites/default/files/2026-06/7185aac4-4a70-4d83-ae1b-1cfca979ae07/2027%20EU-wide%20stress%20test%20-%20Draft%20Methodological%20Note.pdf).
- Riesgo de mercado: "no statistical extrapolation or expansion of risk factors is permitted. The closest applicable shock from the MR scenario should be used". — Draft note 2027, párr. 260
- *FX lending*: la regla se aplica por país de la contraparte cuando las exposiciones en divisa superan el 5 % de cada cartera. — Draft note 2027, párr. 147-148 y tabla 10

### Inferences
- **Argentina** (fuera de la UE y sin fila): en FX y tipos, la regla es explícita y se usa RoW (EUR-RoW +9,3 % en 2025; curva USD). En PIB, paro, IPC y vivienda la opción natural son las filas "Rest of the world", pero no se ha encontrado una regla escrita. Lo razonable es que el banco documente su traslación ante la autoridad competente. `[Likely]`
- Que el adverso no UE salga de un modelo global del BCE con efectos de contagio es lo habitual en la JERS, pero este documento no lo describe. `[Guessing]`, pendiente de verificar en el anexo 3 del escenario 2020.

### Gaps
- No se ha leído el anexo 3 del escenario JERS 2020 (metodología del diseño, modelo global y contagio). Una búsqueda falló por el límite de uso de la herramienta web. Ahí está la respuesta a cómo se construye el adverso fuera de la UE.
- No se ha encontrado en las notas EBA una regla para las variables macro (no financieras) de países sin fila. Habría que buscar en las FAQ (Q&A) de la EBA 2025.

## 4. Gráfico 14: severidad frente a Fed CCAR 2024 y BoE 2024

### Takeaway
Confirmado el texto. El gráfico compara la caída **acumulada del PIB doméstico desde el punto de partida hasta el final del horizonte**, no de pico a valle. Con esa métrica el CCAR 2024 sale en torno a −1,5 %, aunque su caída de pico a valle es del −8,5 %. El manual debe decirlo, o la comparación engaña.

### Cited Findings
- "The scenario is more severe than the 2024 scenario of the Bank of England and of the Federal Reserve System in terms of cumulated domestic real GDP losses"; "notably more pronounced than in the Federal Reserve's 2024 CCAR… sharper than in both adverse scenarios of Bank of England's 2024 desk-based stress test exercise". Lo atribuye a "the varying dates of the respective risk assessments, the different starting dates, and the distinct cyclical and structural characteristics". — PDF ESRB p. 11
- Valores del gráfico 14, leídos de las barras (sin tabla): EBA 2025 ≈ −6,3; BoE 2024 *supply shock* ≈ −3,5; BoE 2024 *demand shock* ≈ −2,6; Fed CCAR 2024 *severely adverse* ≈ −1,5. — PDF ESRB p. 12 (lectura visual: `[Likely]` ±0,2)
- En el escenario *severely adverse* de 2024 de la Fed, el PIB real cae un 8,5 % del 4T-2023 a su valle en el 1T-2025 y luego se recupera. El paro llega al 10 %. — [Fed, 2024 Stress Test Scenarios](https://www.federalreserve.gov/publications/2024-stress-test-scenarios.htm); [nota de prensa Fed 15-feb-2024](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20240215a.htm) (vía resumen de búsqueda; página no abierta)
- Severidad frente a ejercicios EBA anteriores: mediana por país del acumulado −5,8 % (0,3 p.p. por debajo de 2023). Desviación mediana en 2027: −12,2 % (−10,9 % en 2023). — PDF ESRB p. 8

### Inferences
- El EBA mide el acumulado desde el punto de partida hasta el final de un horizonte de tres años en medias anuales; la Fed, en datos trimestrales de pico a valle. El gráfico 14 es, por tanto, una prueba de que la severidad depende de la métrica tanto como del escenario, además de lo que dice la JERS (fechas y ciclo). `[Likely]`

### Gaps
- Las cifras exactas de las barras no están tabuladas en el PDF. No se ha comprobado el −8,5 % de la Fed en su documento original (solo vía resultado de búsqueda).

## 5. Escenario adverso 2027: ¿publicado?

### Takeaway
No. A 16-oct-2026 solo existen los documentos *draft* de la EBA del 11-jun-2026 (horizonte 2027-2029, datos a cierre de 2026, 63 bancos). Por el precedente, el escenario saldría con el lanzamiento, hacia la segunda quincena de enero de 2027, y los resultados "around summer" de 2027.

### Cited Findings
- La página de la EBA solo lista el *Draft Methodological Note*, el *Draft Template Guidance* y las *Draft Templates*, todos del 11-jun-2026. La consulta "is being launched at an earlier stage than for previous EBA stress tests". — [EBA](https://www.eba.europa.eu/risk-and-data-analysis/risk-analysis/eu-wide-stress-testing)
- Escenarios base y adverso comunes, periodo 2027-2029; cifras a cierre de 2026. — Draft note 2027, párr. 21 y 24
- Participan 63 bancos (47 de la zona del euro), un 75 % del sector bancario de la UE. Primera inclusión de riesgos climáticos (transición y físico) en un módulo separado. — [Regulation Tomorrow, jun-2026](https://www.regulationtomorrow.com/2026/06/eba-issues-draft-methodology-and-templates-for-2027-eu-wide-stress-test/)
- "The EBA will run the 2027 EU-wide stress test and publish results around summer"; reducción del 55 % de los datos frente a 2025; módulo climático (transición y riesgo físico por inundación fluvial); entregable "2027 EU-wide stress test exercise" en el 3T. — [EBA Work Programme 2027 (sep-2026)](https://www.eba.europa.eu/sites/default/files/2026-09/f6561915-4192-4d73-88ac-10f8bc09abca/EBA%20Work%20programme%202027.pdf), §1.2.3.1
- Precedente: escenario 2025 aprobado por la JERS el 14-ene-2025, enviado a la EBA el 15-ene y ejercicio lanzado el 20-ene-2025. — PDF ESRB p. 1; [EBA](https://www.eba.europa.eu/publications-and-media/press-releases/eba-launches-its-2025-eu-wide-stress-test)
- Las cartas de la JERS de 2026 que aparecen en su web (ESRB/2026/0056 y otra de dic-2025/ene-2026) van dirigidas a la presidenta de ESMA y tratan del escenario del ejercicio de ESMA de 2026 sobre entidades de contrapartida central. No son el escenario EBA 2027. — [ESRB, carta ESRB/2026/0056](https://www.esrb.europa.eu/mppa/stress/shared/pdf/esrb.stress_test260430_letter~31ee188b35.en.pdf)

### Inferences
- Lanzamiento con escenario hacia finales de enero de 2027. `[Likely]` (precedente de 2025 y calendario del *draft*). KPMG estima metodología final a finales de 2026, escenarios y plantillas a finales de enero de 2027 y envíos de marzo a junio de 2027. — [KPMG Irlanda](https://kpmg.com/ie/en/insights/banking/eba-2027-stress-test.html) (solo resumen de búsqueda; estimación de terceros, `[Guessing]`)

### Gaps
- No hay escenario 2027, así que no se pueden extraer sus variables. Habrá que repetir esta extracción cuando salga.
- La fecha de cierre de la consulta del *draft* (un resumen de búsqueda decía el 7-ago-2026) no está verificada en fuente primaria.

## 6. Comparación de severidad con Banxico (REF jun-2026) y BCB

### Takeaway
No se puede comparar nivel con nivel. Banxico publica sus choques en **desviaciones típicas**, no en niveles. El BCB los publica en **gráficos sin tabla**. Leído de los gráficos, el escenario "Crise de Confiança" del BCB (REF abril 2025) es mucho más duro que la JERS en tipo de cambio y en Selic. "Recessão Aguda" es más duro en paro. En PIB, ambos son del mismo orden.

### Cited Findings
**Banxico, REF junio de 2026** ([PDF Banxico](https://www.banxico.org.mx/publicaciones-y-prensa/reportes-sobre-el-sistema-financiero/%7B86FBB07E-F883-0A38-2110-3C736DB0760E%7D.pdf), §V.1, pp. 136-137 impresas; cifras a marzo de 2026, horizonte de tres años):
- Tres escenarios macro (A: debilitamiento del consumo y la inversión nacionales; B: desaceleración global con recesión en EE. UU.; C: rebaja de la calificación soberana y de Pemex) y tres históricos (H1 crisis de 1995, H2 crisis de 2008, H3 COVID-19). Generados con un VAR a 36 meses. Es un ejercicio de equilibrio parcial y contrafactual.
- Nota al pie 134, literal. **A:** choques entre −1,52 y 2,63 desviaciones típicas (d.t.); "una disminución de 1,04 d.t. en el desempleo, un incremento de 2,63 d.t. en el tipo de cambio y una contracción de 1,52 d.t. en el crecimiento del IGAE". **B:** entre −1,70 y 2,71 d.t.; desempleo +0,70 d.t., tipo de cambio +2,71 d.t., IGAE −1,70 d.t. **C:** entre −1,45 y 1,77 d.t.; tipo de cambio +1,77 d.t., IGAE −1,45 d.t.
- Resultado: el ICAP del sistema se mantiene por encima del mínimo más los suplementos (10,5 %) en todos los escenarios, también en los históricos.

**BCB, Relatório de Estabilidade Financeira, vol. 24 n.º 1, abril 2025** (fichero local `fuentes/2025-04 BCB REF.pdf`, recuadro "Descrição dos cenários…" y gráficos 1.2.5.1-1.2.5.5, pp. 43-44):
- "Recessão Aguda": fuerte caída de la demanda interna y de la economía mundial desde el 2T-2025; el PIB no vuelve al nivel de mediados de 2024 hasta mediados de 2027; sube el paro; baja la inflación y la Selic baja (regla de Taylor). "Crise de Confiança": deterioro fiscal y monetario (referencia: 2014-2016), con depreciación acusada (máximo en el 3T-2025), más inflación y subida de la Selic. Punto de partida: Focus a 31-ene-2025; último trimestre previo a la crisis, 1T-2025.
- Lectura visual de los gráficos, aproximada (`[Guessing]` ±0,3-0,5):
  - PIB (variación acumulada en cuatro trimestres): valle de −3,5 % a −4 % en el 1T-2026 en ambos escenarios.
  - Paro: pico ≈14,3 % ("Recessão Aguda", 3T-4T 2025) y ≈12,3 % ("Crise", 2026), frente a ≈7-8 % en la base.
  - BRL/USD: pico ≈9,4 ("Crise", 3T-2025) y ≈7,4 ("Recessão"), frente a ≈6,0 en la base.
  - Selic: pico ≈24,5 % ("Crise") y valle ≈6 % ("Recessão").

**JERS 2025, a efectos de comparación** (PDF ESRB pp. 13-24):
- Brasil: PIB −3,3 % (2025, media anual) y desviación de −9,2 % en 2027; paro máximo 12,1 % (2026); EUR/BRL +13,4 % en 2025 (BRL/USD implícito de 5,41 a 6,13); swap BRL 3M adverso de 12,78 % en 2025, frente a 11,03 % en la base.
- México: PIB −4,7 % (2025) y acumulado −6,9 %; paro de 3,0 % a 8,8 % (+5,9 p.p.); EUR/MXN +8,9 % en 2025; swap MXN 3M adverso de 10,90 % en 2025, frente a 9,15 % en la base.

### Inferences
- **Brasil.** Contra el escenario "Crise de Confiança" del BCB, la JERS es mucho más suave en tipo de cambio (≈+13 % de media anual frente a ≈+55 % en el pico trimestral) y en tipos (swap 3M ≈12,8 % frente a una Selic ≈24,5 %). En PIB es comparable. En paro (12,1 %) queda entre los dos escenarios del BCB. Parte de la diferencia es de medida: medias anuales frente a picos trimestrales. `[Guessing]` en magnitudes, `[Likely]` en el sentido.
- **México.** En PIB, la JERS (−4,7 % en 2025, acumulado −6,9 %) es severa para un adverso no histórico. Banxico no permite comparar porque expresa los choques en d.t. de sus variables. Incluso su escenario más duro en tipo de cambio (+2,71 d.t.) no se puede pasar a porcentaje sin las desviaciones típicas, que el REF no publica. `[Likely]`
- La "disminución de 1,04 d.t. en el desempleo" del escenario A de Banxico va contra la narrativa del propio escenario (impacto negativo en el empleo). Puede ser una errata del REF o un convenio de signo. **Falta contexto**; no se debe citar sin aclarar.

### Gaps
- No se han revisado los REF del BCB posteriores (noviembre de 2025 y el de 2026). El de abril de 2025 se eligió por ser contemporáneo del escenario JERS 2025, pero no es el último publicado.
- Las cifras de los gráficos del BCB pueden estar en el anexo estadístico o en ficheros de datos del REF; no se han buscado.
- Banxico no publica las desviaciones típicas ni las sendas en niveles de los escenarios A, B y C en el REF. Haría falta otra fuente (presentaciones técnicas, *working papers*) o preguntar a Banxico.
