---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, santander, bbva, resultados, comparabilidad, f1]
---

# F1 · Datos públicos: Santander y BBVA en el EBA 2025

Consultado el 2026-10-16 y **validado ese mismo día contra fuentes primarias** (informe
`reports/Validación F1 stress test.md`, correcciones D1-D15). **Las tablas completas por país y
segmento (todas las carteras, hogares + empresas, minorista, empresas, hipotecas y resto
minorista) están en `research_notes/Validación F1 stress test/datos-publicos.md`, §2.** Scripts de
cálculo en `herramientas/validacion_f1/`.

Fuentes primarias: fichas de resultados por banco de la EBA del 1-ago-2025
(`fuentes/2025-08-01 EBA ST2025 resultados Santander.pdf` y `…BBVA.pdf`) y **base de datos CSV de
la EBA**, que trae el país codificado y los decimales. Para el anexo S4, usar el CSV y no el PDF:
<https://www.eba.europa.eu/assets/st25/full_database/763451/> (`TRA_CRE_IRB.csv`, `TRA_CRE_STA.csv`,
`TRA_OTH.csv`, `Metadata_TR.xlsx`, `Data_Dictionary.xlsx`). Comprobar la ruta `763451` y posibles
correcciones posteriores antes de publicar.

## 1. Resumen por grupo (millones de euros y %)

| | Santander | BBVA |
|---|---|---|
| CET1 *fully loaded* de partida (31-dic-2024, re-expresado CRR3) | 12,19 % | 12,88 % |
| Mínimo FL en el adverso | 10,46 % (2025 y 2027) | 10,70 % (2025) |
| **Caída máxima FL** | **173 pb** | **218 pb** |
| CET1 FL a fin de 2027, adverso | 10,46 % | 11,02 % |
| CET1 FL a fin de 2027, base | 14,65 % | 16,43 % |
| CET1 transitorio: partida y adverso 2025 / 2026 / 2027 | 12,78 % → 10,94 / 11,63 / 10,91 % (mínimo en 2027, −187 pb) | Igual que el FL |
| Deterioro acumulado de activos financieros, adverso 2025-2027 | 44.852 | 35.594 |
| Deterioro acumulado, base 2025-2027 | 25.013 | 22.708 |
| Beneficio del primer año adverso | −3.502 | −2.697 |
| APR (REA) totales re-expresados, con ajustes transitorios | 627.012 | 396.547 |

`[Certain]` Todas las cifras salen de la tabla resumen de cada ficha (p. 2) y de la tabla A1 del informe EBA.

- `[Certain]` **El deterioro se concentra en el primer año** en los dos bancos (Santander 21.120 de 44.852 M€; BBVA 14.481 de 35.594 M€). **En capital, no siempre:** BBVA toca suelo en 2025; Santander empata en 10,46 % FL en 2025 y 2027, y en transitorio su mínimo es 2027.
- `[Certain]` La EBA atribuye esa concentración al perfil del escenario y a la **previsión perfecta**, que lleva todo el escenario a la LGD y a la pérdida a vida desde el primer año (informe EBA, p. 39). `[Likely]` Hay que matizar el §39.2 del manual IRB: la concentración no se debe a la migración de etapas IFRS 9 en sí.
- `[Certain]` **La media de 228 pb que publicó BBVA** es la media simple de la caída FL a fin de 2027 de diez comparables elegidos por BBVA (BNP, Crédit Agricole, CaixaBank, Deutsche, ING, Intesa, Nordea, Santander, Société Générale, UniCredit). Se reproduce con la tabla A2 de la EBA (2.278 / 10 = 227,8 pb; ratio final medio 10,01 %). Sin Crédit Agricole (478 pb), la media de los otros nueve baja a 200 pb.
- `[Certain]` **Agregado EBA 2025** (informe de resultados, pp. 9-12, 21, 28 y 39-40): 64 bancos (51 de la zona del euro), ~75 % del activo; pérdidas de 547.000 M€ (crédito 394.000, mercado 98.000 netos, operacional 55.000); PIB de la UE −6,3 %, paro +5,8 pp; CET1 transitorio −370 pb (15,8 → 12,1 %), *fully loaded* −304 pb; las pérdidas de crédito son el 1,9 % de la exposición.

## 2. Desglose por país

Método: suma de los bloques IRB y estándar por país; "exposición" = S1 + S2 + S3 a 31-dic-2024;
"ΔProv" = stock de provisiones (S1+S2+S3) a fin de 2027 menos el de partida. Con balance estático,
sin *workout* ni liberación de provisiones de S3, ese aumento aproxima el deterioro acumulado.

- `[Certain]` **Comprobación de grupo:** en BBVA el aumento de provisiones (35.593 M€) coincide con el deterioro de resultados (35.594 M€). **En Santander queda 762 M€ por debajo** (44.090 frente a 44.852 M€; −1,7 %). `[Guessing]` Probablemente por deterioro de partidas que no están en las tablas de crédito (titulizaciones u otras).
- `[Certain]` **Asignación de países verificada.** Los tres bloques IRB por banco sin etiqueta en la extracción de texto (Santander: EE. UU., Brasil, Chile; BBVA: Türkiye, EE. UU., Perú) estaban bien asignados. Se confirmó por dos vías: coordenadas del PDF (`pdftotext -bbox`) y columnas `Country` del CSV, que coinciden en 88 de 88 combinaciones salvo redondeos (el mayor, 0,35 pp en una cartera de 141 M€). Cada ficha solo trae los diez primeros países: Santander no tiene bloque de Türkiye, Perú ni Colombia, y BBVA no tiene Brasil ni Chile.

### 2.1 Todas las carteras (ΔProv / exposición)

| Banco y país | Exposición inicial (M€) | Adverso | Base | Adv. − base | S3 2027 adv. | Peso IRB |
|---|---|---|---|---|---|---|
| Santander grupo | 1.384.138 | 3,19 % | 1,80 % | 1,38 pp | 8,58 % | 43 % |
| Santander España | 309.960 | 1,85 % | 1,13 % | 0,73 pp | 5,37 % | 47 % |
| Santander Reino Unido | 324.063 | 1,56 % | 0,57 % | 0,99 pp | 5,74 % | 75 % |
| Santander EE. UU. | 179.578 | 3,73 % | 2,45 % | 1,29 pp | 15,21 % | 17 % |
| Santander Brasil | 148.751 | 7,92 % | 5,04 % | 2,88 pp | 13,88 % | 18 % |
| Santander México | 65.678 | 6,00 % | 3,41 % | 2,58 pp | 14,04 % | 26 % |
| BBVA grupo | 643.928 | 5,53 % | 3,53 % | 2,00 pp | 10,14 % | 48 % |
| BBVA España | 250.029 | 4,30 % | 2,16 % | 2,14 pp | 9,22 % | 60 % |
| BBVA México | 108.478 | 13,67 % | 10,12 % | 3,55 pp | 17,99 % | 42 % |
| BBVA Türkiye | 72.964 | 3,02 % | 1,64 % | 1,38 pp | 9,15 % | 0 % |
| BBVA EE. UU. | 54.528 | 1,51 % | 0,80 % | 0,70 pp | 3,32 % | 78 % |

Resto de países (Chile, Polonia, Alemania, Portugal, Francia, Perú, Colombia, Italia, Reino Unido de
BBVA, Argentina) en la nota de validación.

### 2.2 Solo hogares y empresas no financieras (sin bancos centrales, soberanos ni instituciones)

`[Certain]` El peso de hogares + empresas varía mucho: 66,0 % en Santander, 68,9 % en BBVA, **50,8 % en
Santander España**, 64,3 % en BBVA España, 63,2 % en Santander México y **82,3 % en BBVA México**. Con
todas las carteras, el denominador mezcla deuda pública en proporciones distintas, y el cociente
entre países o entre bancos sale distorsionado.

| Banco y país | Exposición (M€) | Adverso | Base | Adv. − base | S3 2027 adv. |
|---|---|---|---|---|---|
| Santander España | 157.612 | 3,45 % | 2,11 % | 1,35 pp | 9,89 % |
| Santander México | 41.495 | 9,15 % | 5,24 % | 3,91 pp | 21,44 % |
| Santander Brasil | 109.664 | 10,62 % | 6,77 % | 3,84 pp | 18,58 % |
| Santander EE. UU. | 91.594 | 7,28 % | 4,78 % | 2,51 pp | 29,63 % |
| BBVA España | 160.804 | 6,38 % | 3,07 % | 3,32 pp | 13,63 % |
| BBVA México | 89.244 | 16,53 % | 12,25 % | 4,29 pp | 21,71 % |
| BBVA Türkiye | 53.371 | 3,40 % | 1,98 % | 1,42 pp | 11,02 % |

### 2.3 Por segmento, adverso (ΔProv / exposición)

| Banco y país | Hipotecas | Resto minorista (consumo, tarjetas, auto, pymes minoristas) | Empresas |
|---|---|---|---|
| Santander España | 1,55 % | 9,29 % | 2,34 % |
| BBVA España | 1,80 % | 13,79 % | 8,33 % |
| Santander México | 3,53 % | 21,55 % | 0,41 % |
| BBVA México | 4,71 % | 37,67 % | 3,61 % |

`[Certain]` La empresa mexicana de Santander es el caso didáctico del hilo conductor: **0,41 % en el
adverso, 0,14 pp sobre la base y 94 % IRB**, frente al 3,61 % de BBVA México.
`[Likely]` Los S3 a fin de 2027 de Santander EE. UU. minorista (49,32 %) y México minorista (31,91 %)
parecen extremos, pero salen de carteras de consumo y auto de PD alta bajo balance estático sin
fallidos. No son tasas de mora: hay que explicarlo en el manual.

## 3. Lo que dicen (y no dicen) los cocientes

- `[Certain]` **México frente a España:** 3,24 (Santander) y 3,18 (BBVA) en el adverso con todas las carteras. Pero con hogares + empresas da 2,65 y 2,59; en el base, 3,03 y 4,69; en adverso menos base, 3,56 y 1,66. `[Likely]` **La coincidencia de los dos bancos solo aparece con una métrica y un escenario concretos, y es en parte casual.** No sirve como tesis del cap. 27.
- `[Certain]` **BBVA frente a Santander en el mismo país:** 2,32 en España y 2,28 en México con todas las carteras; con hogares + empresas, 1,85 y 1,81. **No es una regularidad:** EE. UU. 0,40, Francia 0,42, Reino Unido 3,02 y grupo 1,74, aunque en esos países una de las dos carteras es pequeña o muy distinta.
- `[Certain]` **El escenario no explica la distancia entre países.** Si la explicara, los cocientes en base y en adverso menos base coincidirían, y no coinciden. Además, medido en desviación frente a la base, el escenario no es mucho más severo para México que para España (ver `jers-escenario.md`).
- `[Likely]` **La composición de cartera no explica la distancia entre bancos** (refutado al nivel de detalle de las plantillas EBA). Descomposición de la diferencia BBVA − Santander en hogares + empresas: en México, −0,26 pp de mezcla y +7,64 pp de intensidad (de 7,39 pp); en España, −0,24 y +3,17; en el grupo, −0,21 y +3,26. El peso del resto minorista en México es casi idéntico (37,7 % frente a 37,3 %). Lo que difiere es la tasa dentro de cada segmento: resto minorista 37,67 % en BBVA frente a 21,55 % en Santander; empresas 3,61 % frente a 0,41 %. Sigue siendo `[Likely]` porque dentro del "resto minorista" puede quedar mezcla de producto que la plantilla estándar no separa.
- `[Certain]` **El base ya consume mucho en México.** Adverso menos base con todas las carteras: BBVA México 3,55 pp, Santander México 2,58 pp, BBVA España 2,14 pp, Santander España 0,73 pp. Con hogares + empresas: 4,29 / 3,91 / 3,32 / 1,35 pp. Para comparar severidad hay que mirar adverso menos base.
- `[Likely]` **Tesis nueva para el cap. 27:** la pérdida mexicana triplica la española por el nivel de riesgo de partida y por la intensidad dentro de cada segmento, no por el escenario ni por la mezcla. Lo que pregunta el JST es por qué la tasa del mismo segmento difiere. `[Guessing]` Una parte puede venir del método (satélites propios frente a *benchmarks* del BCE, *overlays*); con datos públicos no se puede separar y se plantea como CASO JST.

## 4. Comparación con los ejercicios locales

- `[Certain]` La misma cartera mexicana tiene al menos tres "números de estrés": el del EBA del grupo (escenario JERS con base FMI, balance estático, CET1 FL del grupo, IFRS 9), el de Banxico (REF de junio de 2026: distribución del ICAP del sistema con escenarios propios e históricos, sin acciones ni resultados por banco) y el de la CNBV (cada banco proyecta con escenarios del regulador, al menos 9 trimestres, plan de negocios). `[Likely]` El de la CNBV parte de la provisión local (inferencia sobre la CUB).
- `[Certain]` **Ningún banco publica su número local.** Santander México salió de NYSE (Form 25 del 24-abr-2023) y la CNBV canceló su inscripción en el RNV el **12-may-2023**; Banco Santander pasó del ~96,2 % a algo más del 99 % con las OPA de abril de 2023 y al **~99,97 %** tras la venta forzosa de noviembre de 2023 (las fuentes dan 99 % o 99,8 % tras las OPA según cuenten una oferta o las dos). El oficio de la CNBV del 27-nov-2023 que circula en búsquedas es de la matriz española, no de Santander México. De BBVA México solo hay una frase cualitativa de su casa de bolsa ("niveles superiores a los mínimos regulatorios", sin cifras).
- `[Likely]` BBVA México no cotiza (sin verificar).
- `[Certain]` Consecuencia: la comparación local frente a EBA del anexo S4 tiene que ser sintética, calibrada con las tasas reales por segmento de §2.3, y dejando claro que es ilustrativa.

## Huecos que siguen abiertos

- Origen de los 762 M€ de Santander (cruzar las pp. 21, titulizaciones, y 25, resultados, de la ficha).
- Estado de cotización de BBVA México.
- Sustituir `herramientas/parse_eba_resultados.py` por una consulta al CSV de la EBA.
