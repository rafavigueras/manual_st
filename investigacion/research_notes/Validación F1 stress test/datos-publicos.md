---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, santander, bbva, eba-2025, validacion, f1]
---

# Validación de `investigacion/datos-publicos.md`: Santander y BBVA en el stress test EBA 2025

Consultado el 2026-10-16. Datos de partida a 31-dic-2024 (re-expresados CRR3) y proyecciones 2025-2027.

**Fuentes primarias usadas:**

- Fichas EBA por banco (copia local en `investigacion/fuentes/`):
  - Santander: [EBA_ST_ES_5493006QMFDDMYWIAM13.pdf](https://www.eba.europa.eu/assets/st25/bank_individual_results/763451/EBA_ST_ES_5493006QMFDDMYWIAM13.pdf)
  - BBVA: [EBA_ST_ES_K8MS7FD7N5Z2WQ51AZ71.pdf](https://www.eba.europa.eu/assets/st25/bank_individual_results/763451/EBA_ST_ES_K8MS7FD7N5Z2WQ51AZ71.pdf)
  - Las dos tienen la misma paginación: p. 2, resumen; pp. 3-11, IRB (3-5 dato re-expresado, 6-8 base, 9-11 adverso); pp. 12-20, estándar (STA).
- Base de datos completa de la EBA en CSV: [TRA_CRE_IRB.csv](https://www.eba.europa.eu/assets/st25/full_database/763451/TRA_CRE_IRB.csv) y [TRA_CRE_STA.csv](https://www.eba.europa.eu/assets/st25/full_database/763451/TRA_CRE_STA.csv), con [Metadata_TR.xlsx](https://www.eba.europa.eu/assets/st25/full_database/763451/Metadata_TR.xlsx) para los códigos.
- Informe agregado de la EBA: [2025 EU-wide stress test – Results](https://www.eba.europa.eu/sites/default/files/2025-08/0178b9c5-2f0d-42ee-8226-6fa0a87c0d6c/2025%20EU-wide%20stress%20test%20-%20Results.pdf). Las páginas que cito son las del PDF.

**Scripts** (en un directorio temporal, fuera del proyecto; el sistema puede borrarlo):

- `/var/folders/ng/8k377x1x6k3f3z3tsk01nwn40000gp/T/st25val.6Moz/work/parse_bbox.py`: parser alternativo. Lee `pdftotext -bbox` y reconstruye cada fila por su coordenada vertical.
- `.../work/compute.py`: desglose por país y por cartera. Comprueba además que la suma de las clases cuadre con el TOTAL y que el balance sea estático.
- `.../work/csv_check.py`: recalcula todo desde el CSV de la EBA, que trae el país codificado, y lo compara con los PDF.
- `.../work/retail_split.py`: separa hipotecas y resto minorista.
- `.../work/shift_share.py`: descompone la diferencia entre bancos en mezcla e intensidad.
- `.../work/labels.py` y `bbox.py`: localizan las etiquetas de país.

Si el directorio desaparece, el método está descrito en la sección 2 y se reproduce con el CSV de la EBA en unas 30 líneas.

**Leyenda de veredictos:**

- **Confirmado:** la cifra o afirmación es correcta tal como está.
- **Corregido:** hay que cambiar la cifra, el matiz o la etiqueta de confianza.
- **Refutado:** la afirmación no se sostiene.
- **Inverificable:** no se ha podido comprobar en esta pasada.

---

## 1. Tabla resumen por grupo (§1 de la nota)

### Takeaway
Las nueve cifras de la tabla resumen son correctas en los dos bancos. Hay que corregir dos cosas del texto:
- "El peor año es el primero" vale para el deterioro, pero no del todo para el capital de Santander.
- La "comprobación" de que el aumento de provisiones coincide con el deterioro solo se cumple en BBVA. En Santander hay 762 M€ de diferencia.

### Cited Findings

**Veredicto por cifra.** Fuente: ficha EBA, p. 2 ("Summary"); "fila" es el `RowNum` de esa tabla.

| Afirmación de la nota | Santander | BBVA | Veredicto | Fuente / aritmética | Confianza |
|---|---|---|---|---|---|
| CET1 *fully loaded* de partida (re-expresado CRR3) | 12,19 % | 12,88 % | Confirmado | Fila 9, columna "Restatement CRR3" | `[Certain]` |
| Mínimo en el adverso | 10,46 % (2025 y 2027) | 10,70 % (2025) | Confirmado | Fila 9. Santander: 10,46 / 11,12 / 10,46. BBVA: 10,70 / 10,99 / 11,02 | `[Certain]` |
| Caída máxima | 173 pb | 218 pb | Confirmado | 12,19 − 10,46 = 1,73 pp; 12,88 − 10,70 = 2,18 pp. Coincide con el *peak-to-trough* de la tabla A2 del informe EBA (p. 62) | `[Certain]` |
| CET1 FL a fin de 2027, adverso | 10,46 % | 11,02 % | Confirmado | Fila 9. Caída a fin de horizonte: 173 pb y 186 pb (tabla A2, "Delta") | `[Certain]` |
| CET1 FL a fin de 2027, base | 14,65 % | 16,43 % | Confirmado | Fila 9 | `[Certain]` |
| Deterioro acumulado, adverso 2025-27 (M€) | 44.852 | 35.594 | Confirmado | Fila 3. Santander: 21.120 + 10.342 + 13.390 = 44.852. BBVA: 14.481 + 11.154 + 9.959 = 35.594 | `[Certain]` |
| Deterioro acumulado, base 2025-27 (M€) | 25.013 | 22.708 | Confirmado | Fila 3. Santander: 9.025 + 6.675 + 9.313 = 25.013. BBVA: 10.035 + 6.662 + 6.011 = 22.708 | `[Certain]` |
| Beneficio del primer año adverso (M€) | −3.502 | −2.697 | Confirmado | Fila 4, adverso 2025 | `[Certain]` |
| "RWA de partida (transitorio, re-expresado)" (M€) | 627.012 | 396.547 | Confirmado, con matiz de nombre | Fila 7: es el *Total Risk exposure amount (all transitional adjustments included)* re-expresado. Mejor llamarlo "APR (REA) totales re-expresados, con ajustes transitorios" | `[Certain]` |

**Dato que falta en la nota: el CET1 transitorio de Santander.** Ficha EBA de Santander, p. 2, fila 8.
- En BBVA el transitorio y el *fully loaded* son iguales: 12,88 % de partida, 11,02 % en 2027.
- En Santander no. Parte de 12,78 % y pasa a 10,94 / 11,63 / 10,91 %.
- En transitorio, el mínimo de Santander es **2027** (10,91 %), con una caída de 187 pb. Coincide con la tabla A1 del informe EBA ("−187 / −187"). `[Certain]`

**"El peor año es el primero".** Veredicto: **Corregido**.
- **Deterioro: se cumple en los dos bancos.**
  - Santander: 21.120 en 2025, frente a 10.342 y 13.390 después.
  - BBVA: 14.481 en 2025, frente a 11.154 y 9.959. `[Certain]`
- **Capital: se cumple en BBVA, no claramente en Santander.**
  - BBVA toca suelo en 2025.
  - Santander empata en 10,46 % en 2025 y 2027 en *fully loaded* (con dos decimales), y en transitorio el suelo es 2027. `[Certain]`
- **Por qué la pérdida se concentra en el primer año.** La EBA lo atribuye al perfil temporal del escenario (el golpe más duro cae en el primer año) y a un supuesto del método: los bancos conocen de antemano la senda macro, así que reflejan todo el escenario en la LGD y en la pérdida esperada a vida desde el principio ([informe EBA, p. 39](https://www.eba.europa.eu/sites/default/files/2025-08/0178b9c5-2f0d-42ee-8226-6fa0a87c0d6c/2025%20EU-wide%20stress%20test%20-%20Results.pdf)). `[Certain]`
- La tesis de que "la migración de etapas IFRS 9 adelanta la pérdida" es compatible con eso, pero la EBA destaca el supuesto de previsión perfecta, no la migración en sí. Recomiendo matizar el §39.2 en ese sentido. `[Likely]` No he leído el §39.2 del manual IRB.

**La comprobación de grupo de la §2 ("coincide").** Veredicto: **Corregido**.
- BBVA: aumento de provisiones 47.647 − 12.054 = 35.593, frente a 35.594 de deterioro. Diferencia de 1 M€. `[Certain]`
- Santander: 65.983 − 21.893 = 44.090, frente a 44.852. Diferencia de **762 M€**, un 1,70 % (762 / 44.852). `[Certain]`
- Redacción propuesta: "En BBVA el aumento de provisiones de las tablas de crédito coincide al millón con el deterioro de la cuenta de resultados. En Santander queda 762 M€ por debajo (−1,7 %), probablemente por deterioro de partidas que no están en las tablas de crédito." Esa última parte es `[Guessing]`: no he identificado la partida.

### Inferences
- `[Likely]` La tabla resumen puede usarse tal cual. El matiz transitorio / *fully loaded* importa en Santander (59 pb de diferencia de partida) y no en BBVA. El manual debería decir siempre qué métrica usa.

### Gaps
- Qué partida explica los 762 M€ de Santander. Habría que cruzar la p. 25 (P&L) y la p. 21 (titulizaciones) de la ficha.
- No he consultado el §39.2 del manual IRB.

---

## 2. Bloques IRB sin etiqueta y desglose por país recalculado (§2 de la nota)

### Takeaway
La asignación de los tres bloques IRB sin etiqueta **era correcta**. La confirman dos vías independientes:
1. Las coordenadas del PDF.
2. La base CSV de la EBA, que trae el país codificado.

Las dos tablas por país de la nota se reproducen exactamente. Su confianza sube de `[Likely]` a `[Certain]`.

### Cited Findings

**Qué falló en el parser original.**
- La etiqueta de país está dibujada a media altura de cada bloque, en la fila 11 de 21 del IRB ("Retail – Secured by residential real estate").
- En los bloques 4, 5 y 6 de los dos bancos, esa fila sale de `pdftotext -layout` partida en celdas verticales. La etiqueta queda en una línea sin número de fila y la expresión regular no la encontraba. `[Certain]`
- Lo mismo pasa en el bloque STA 2 (España): el número 37 sale en una línea aparte. El parser lo resolvía con el valor por defecto `home='SPAIN'`. `[Certain]`

**Primera vía: coordenadas (`pdftotext -bbox`).** Ficha EBA, pp. 3-11.
- Cada palabra de país se asigna a la fila cuyo número tiene la coordenada vertical más cercana (diferencia de 0,4 a 4,2 puntos).
- Santander:
  - UNITED STATES cae en la fila 74 (bloque 4).
  - BRAZIL en la 95 (bloque 5).
  - CHILE en la 116 (bloque 6).
- BBVA:
  - TURKEY cae en la fila 74 (bloque 4).
  - UNITED STATES en la 95 (bloque 5).
  - PERU en la 116 (bloque 6).
- La asignación es idéntica en las páginas de dato re-expresado, base y adverso. `[Certain]`

**Segunda vía: el CSV de la EBA**, columnas `Country` y `Country_rank` ([TRA_CRE_IRB.csv](https://www.eba.europa.eu/assets/st25/full_database/763451/TRA_CRE_IRB.csv)).

| Rango | Santander | BBVA |
|---|---|---|
| 1 | España | España |
| 2 | Reino Unido | México |
| 3 | EE. UU. | Türkiye |
| 4 | Brasil | EE. UU. |
| 5 | Chile | Perú |
| 6 | Portugal | Colombia |
| 7 | Alemania | Italia |
| 8 | Polonia | Francia |
| 9 | México | Reino Unido |
| 10 | Francia | Argentina |

El orden es igual en IRB y en STA. `[Certain]`

**Cuadre entre PDF y CSV.**
- He comparado 88 combinaciones (2 bancos × 11 bloques × 4 carteras). La exposición y el ratio de provisiones coinciden.
- Las únicas diferencias salen en carteras diminutas de BBVA, porque el PDF redondea a millones y el CSV trae decimales. La mayor es la cartera minorista de BBVA en EE. UU. (141 M€): 14,18 % frente a 14,53 %. `[Certain]`

**Controles internos del recálculo.** En los dos bancos, los tres escenarios y los once bloques:
- La suma de las clases de exposición de primer nivel cuadra con la fila TOTAL (0 descuadres de más de 3 M€).
- En STA, las filas 14 + 15 + 16 suman la 13.
- La exposición total a 2027 es igual a la de partida (balance estático). `[Certain]`

**Afirmación "el denominador incluye bancos centrales, soberanos e instituciones".** Veredicto: **Confirmado**, y ahora cuantificado.

| Banco / país | Peso de hogares + empresas en la exposición total | Aritmética |
|---|---|---|
| Santander, grupo | 66,0 % | 913.531 / 1.384.138 |
| BBVA, grupo | 68,9 % | 443.684 / 643.928 |
| Santander España | 50,8 % | 157.612 / 309.960 |
| BBVA España | 64,3 % | 160.804 / 250.029 |
| Santander México | 63,2 % | 41.495 / 65.678 |
| BBVA México | 82,3 % | 89.244 / 108.478 |

`[Certain]`

**Referencia de la nota a la nota metodológica (párr. 106).** Veredicto: **Inverificable**. No la he abierto; con la verificación directa ya no hace falta.

**Método del recálculo.**
- Exposición inicial: suma de stage 1 + stage 2 + stage 3 a 31-dic-2024 re-expresado.
- Aumento de provisiones (ΔProv): stock de provisiones S1 + S2 + S3 a 31-dic-2027 menos el de partida.
- Ratio: ΔProv dividido por la exposición inicial.
- S3 2027: exposición en stage 3 a 2027 sobre la exposición de 2027, que con balance estático es igual a la inicial.
- Peso IRB: exposición IRB sobre el total.

**Carteras** (clases de exposición de las plantillas EBA):

| Cartera | IRB | STA |
|---|---|---|
| **Todo** | TOTAL (fila 21) | TOTAL (fila 24) |
| **Hogares + empresas** | Corporates (fila 6) + Retail (fila 10) | Corporates (8) + Retail (11) + Secured by mortgages on immovable property and ADC (13) |
| **Minorista** | Retail | Retail (11) + Residential immovable property (14) |
| **Empresas** | Corporates | Corporates (8) + Commercial immovable property (15) + ADC (16) |

Se excluyen bancos centrales, administraciones públicas, entes públicos, bancos multilaterales, organismos internacionales, instituciones, bonos garantizados, deuda subordinada, CIU, renta variable, titulizaciones y otras exposiciones.

Límites de la definición:
- La clase "Corporates" incluye las sociedades financieras que no son entidades de crédito, porque la plantilla no separa las no financieras. El cubo "hogares + empresas" es una aproximación de "hogares y sociedades no financieras". `[Likely]`
- "Minorista" incluye las pymes minoristas. `[Certain]`

#### Tablas recalculadas: Santander (M€ y %)

**Todas las carteras.** Reproduce exactamente la tabla de la nota.

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 1.384.138 | 21.893 | 65.983 | 46.875 | 2,58 % | 3,19 % | 1,80 % | 1,38 pp | 8,58 % | 43 % |
| España | 309.960 | 4.166 | 9.907 | 7.659 | 2,18 % | 1,85 % | 1,13 % | 0,73 pp | 5,37 % | 47 % |
| Reino Unido | 324.063 | 1.039 | 6.091 | 2.874 | 1,28 % | 1,56 % | 0,57 % | 0,99 pp | 5,74 % | 75 % |
| EE. UU. | 179.578 | 4.351 | 11.057 | 8.746 | 4,25 % | 3,73 % | 2,45 % | 1,29 pp | 15,21 % | 17 % |
| Brasil | 148.751 | 5.412 | 17.191 | 12.906 | 5,28 % | 7,92 % | 5,04 % | 2,88 pp | 13,88 % | 18 % |
| Chile | 51.730 | 1.214 | 2.491 | 1.567 | 4,88 % | 2,47 % | 0,68 % | 1,79 pp | 12,23 % | 7 % |
| Portugal | 41.110 | 701 | 1.645 | 1.168 | 2,01 % | 2,30 % | 1,14 % | 1,16 pp | 5,50 % | 74 % |
| Alemania | 44.490 | 512 | 2.133 | 1.360 | 1,71 % | 3,64 % | 1,91 % | 1,74 pp | 7,80 % | 63 % |
| Polonia | 52.704 | 1.215 | 3.018 | 2.113 | 2,75 % | 3,42 % | 1,70 % | 1,72 pp | 8,02 % | 4 % |
| México | 65.678 | 1.316 | 5.255 | 3.558 | 2,27 % | 6,00 % | 3,41 % | 2,58 pp | 14,04 % | 26 % |
| Francia | 30.187 | 281 | 993 | 648 | 1,12 % | 2,36 % | 1,22 % | 1,14 pp | 4,14 % | 67 % |

**Solo hogares + empresas.**

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 913.531 | 21.741 | 63.972 | 45.649 | 3,89 % | 4,62 % | 2,62 % | 2,01 pp | 12,55 % | 63 % |
| España | 157.612 | 4.151 | 9.594 | 7.470 | 4,29 % | 3,45 % | 2,11 % | 1,35 pp | 9,89 % | 89 % |
| Reino Unido | 258.965 | 1.037 | 5.957 | 2.801 | 1,60 % | 1,90 % | 0,68 % | 1,22 pp | 7,08 % | 93 % |
| EE. UU. | 91.594 | 4.346 | 11.017 | 8.722 | 8,32 % | 7,28 % | 4,78 % | 2,51 pp | 29,63 % | 29 % |
| Brasil | 109.664 | 5.407 | 17.048 | 12.834 | 7,16 % | 10,62 % | 6,77 % | 3,84 pp | 18,58 % | 24 % |
| Chile | 40.557 | 1.207 | 2.461 | 1.550 | 6,23 % | 3,09 % | 0,85 % | 2,25 pp | 15,43 % | 8 % |
| Portugal | 34.008 | 671 | 1.594 | 1.132 | 2,42 % | 2,71 % | 1,36 % | 1,36 pp | 6,19 % | 88 % |
| Alemania | 35.224 | 510 | 2.118 | 1.355 | 2,16 % | 4,57 % | 2,40 % | 2,17 pp | 9,67 % | 75 % |
| Polonia | 33.814 | 1.213 | 2.938 | 2.073 | 4,28 % | 5,10 % | 2,54 % | 2,56 pp | 11,91 % | 5 % |
| México | 41.495 | 1.307 | 5.103 | 3.480 | 3,60 % | 9,15 % | 5,24 % | 3,91 pp | 21,44 % | 36 % |
| Francia | 22.438 | 281 | 987 | 644 | 1,49 % | 3,15 % | 1,62 % | 1,53 pp | 5,53 % | 87 % |

**Minorista** (incluye pymes minoristas e hipotecas STA).

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 620.606 | 16.692 | 52.926 | 38.023 | 4,43 % | 5,84 % | 3,44 % | 2,40 pp | 15,17 % | 58 % |
| España | 96.962 | 2.349 | 6.373 | 4.887 | 4,01 % | 4,15 % | 2,62 % | 1,53 pp | 10,68 % | 88 % |
| Reino Unido | 223.104 | 614 | 4.584 | 2.025 | 1,52 % | 1,78 % | 0,63 % | 1,15 pp | 6,58 % | 96 % |
| EE. UU. | 51.098 | 4.006 | 10.272 | 8.309 | 14,14 % | 12,26 % | 8,42 % | 3,84 pp | 49,32 % | 1 % |
| Brasil | 70.525 | 4.676 | 15.361 | 11.695 | 9,28 % | 15,15 % | 9,95 % | 5,20 pp | 25,05 % | 0 % |
| Chile | 28.446 | 773 | 1.632 | 1.011 | 6,18 % | 3,02 % | 0,84 % | 2,18 pp | 16,98 % | 0 % |
| Portugal | 25.601 | 372 | 910 | 654 | 1,63 % | 2,10 % | 1,10 % | 1,00 pp | 5,19 % | 87 % |
| Alemania | 24.946 | 412 | 1.651 | 1.010 | 2,40 % | 4,97 % | 2,40 % | 2,57 pp | 10,98 % | 80 % |
| Polonia | 21.354 | 865 | 1.993 | 1.500 | 4,39 % | 5,28 % | 2,97 % | 2,31 pp | 11,98 % | 0 % |
| México | 25.773 | 1.167 | 4.898 | 3.297 | 4,96 % | 14,48 % | 8,26 % | 6,21 pp | 31,91 % | 0 % |
| Francia | 11.879 | 220 | 909 | 589 | 2,11 % | 5,80 % | 3,11 % | 2,69 pp | 8,51 % | 91 % |

**Empresas** (corporates + inmobiliario comercial y ADC del STA).

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 292.924 | 5.050 | 11.046 | 7.625 | 2,75 % | 2,05 % | 0,88 % | 1,17 pp | 6,99 % | 72 % |
| España | 60.650 | 1.802 | 3.221 | 2.583 | 4,75 % | 2,34 % | 1,29 % | 1,05 pp | 8,62 % | 90 % |
| Reino Unido | 35.861 | 423 | 1.373 | 776 | 2,10 % | 2,65 % | 0,98 % | 1,66 pp | 10,18 % | 75 % |
| EE. UU. | 40.499 | 339 | 747 | 415 | 0,99 % | 1,01 % | 0,19 % | 0,82 pp | 4,77 % | 64 % |
| Brasil | 39.140 | 731 | 1.687 | 1.139 | 3,34 % | 2,44 % | 1,04 % | 1,40 pp | 6,94 % | 67 % |
| Chile | 12.110 | 435 | 829 | 540 | 6,34 % | 3,25 % | 0,87 % | 2,39 pp | 11,77 % | 26 % |
| Portugal | 8.407 | 298 | 684 | 478 | 4,83 % | 4,59 % | 2,14 % | 2,45 pp | 9,25 % | 90 % |
| Alemania | 10.280 | 98 | 467 | 345 | 1,58 % | 3,59 % | 2,40 % | 1,19 pp | 6,49 % | 64 % |
| Polonia | 12.459 | 347 | 945 | 575 | 4,10 % | 4,80 % | 1,83 % | 2,97 pp | 11,78 % | 12 % |
| México | 15.722 | 140 | 205 | 183 | 1,37 % | 0,41 % | 0,27 % | 0,14 pp | 4,28 % | 94 % |
| Francia | 10.558 | 61 | 78 | 55 | 0,80 % | 0,16 % | −0,06 % | 0,22 pp | 2,17 % | 83 % |

#### Tablas recalculadas: BBVA (M€ y %)

**Todas las carteras.** Reproduce exactamente la tabla de la nota.

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 643.928 | 12.054 | 47.647 | 34.762 | 2,28 % | 5,53 % | 3,53 % | 2,00 pp | 10,14 % | 48 % |
| España | 250.029 | 4.268 | 15.026 | 9.664 | 2,96 % | 4,30 % | 2,16 % | 2,14 pp | 9,22 % | 60 % |
| México | 108.478 | 3.219 | 18.047 | 14.195 | 2,32 % | 13,67 % | 10,12 % | 3,55 pp | 17,99 % | 42 % |
| Türkiye | 72.964 | 1.895 | 4.101 | 3.091 | 2,61 % | 3,02 % | 1,64 % | 1,38 pp | 9,15 % | 0 % |
| EE. UU. | 54.528 | 20 | 841 | 457 | 0,01 % | 1,51 % | 0,80 % | 0,70 pp | 3,32 % | 78 % |
| Perú | 23.735 | 1.064 | 2.887 | 2.411 | 4,82 % | 7,68 % | 5,68 % | 2,01 pp | 16,92 % | 3 % |
| Colombia | 20.333 | 847 | 2.004 | 1.628 | 4,80 % | 5,69 % | 3,84 % | 1,85 pp | 16,15 % | 6 % |
| Italia | 11.951 | 15 | 129 | 75 | 0,07 % | 0,95 % | 0,50 % | 0,45 pp | 1,59 % | 58 % |
| Francia | 12.952 | 21 | 150 | 117 | 0,29 % | 1,00 % | 0,74 % | 0,25 pp | 2,08 % | 74 % |
| Reino Unido | 10.981 | 42 | 559 | 412 | 0,33 % | 4,71 % | 3,37 % | 1,34 pp | 10,54 % | 87 % |
| Argentina | 9.399 | 178 | 982 | 702 | 1,13 % | 8,55 % | 5,58 % | 2,98 pp | 13,93 % | 0 % |

**Solo hogares + empresas.**

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 443.684 | 11.949 | 45.990 | 33.602 | 3,13 % | 7,67 % | 4,88 % | 2,79 pp | 13,95 % | 61 % |
| España | 160.804 | 4.248 | 14.514 | 9.177 | 4,15 % | 6,38 % | 3,07 % | 3,32 pp | 13,63 % | 91 % |
| México | 89.244 | 3.215 | 17.971 | 14.146 | 2,82 % | 16,53 % | 12,25 % | 4,29 pp | 21,71 % | 51 % |
| Türkiye | 53.371 | 1.852 | 3.668 | 2.909 | 3,57 % | 3,40 % | 1,98 % | 1,42 pp | 11,02 % | 0 % |
| EE. UU. | 28.356 | 16 | 810 | 432 | 0,02 % | 2,80 % | 1,47 % | 1,33 pp | 6,19 % | 98 % |
| Perú | 21.370 | 1.064 | 2.883 | 2.407 | 5,31 % | 8,51 % | 6,28 % | 2,23 pp | 18,72 % | 3 % |
| Colombia | 17.007 | 843 | 1.954 | 1.609 | 5,64 % | 6,53 % | 4,50 % | 2,03 pp | 18,76 % | 4 % |
| Italia | 5.372 | 8 | 95 | 54 | 0,15 % | 1,62 % | 0,86 % | 0,76 pp | 2,12 % | 97 % |
| Francia | 6.069 | 18 | 127 | 100 | 0,61 % | 1,80 % | 1,35 % | 0,44 pp | 3,74 % | 94 % |
| Reino Unido | 8.837 | 41 | 549 | 406 | 0,41 % | 5,75 % | 4,13 % | 1,62 pp | 12,93 % | 85 % |
| Argentina | 7.329 | 164 | 809 | 560 | 1,45 % | 8,80 % | 5,40 % | 3,40 pp | 12,31 % | 0 % |

**Minorista.**

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 205.919 | 8.344 | 30.464 | 23.810 | 4,76 % | 10,74 % | 7,51 % | 3,23 pp | 19,65 % | 50 % |
| España | 100.055 | 2.994 | 8.198 | 5.667 | 5,18 % | 5,20 % | 2,67 % | 2,53 pp | 14,26 % | 91 % |
| México | 50.098 | 2.872 | 16.213 | 12.900 | 4,35 % | 26,63 % | 20,02 % | 6,61 pp | 34,34 % | 24 % |
| Türkiye | 27.728 | 913 | 1.710 | 1.447 | 3,00 % | 2,87 % | 1,93 % | 0,95 pp | 10,27 % | 0 % |
| EE. UU. | 141 | 5 | 25 | 24 | 4,26 % | 14,18 % | 13,48 % | 0,71 pp | 20,71 % | 22 % |
| Perú | 8.999 | 470 | 1.621 | 1.358 | 4,91 % | 12,79 % | 9,87 % | 2,92 pp | 22,72 % | 0 % |
| Colombia | 9.530 | 750 | 1.476 | 1.306 | 8,97 % | 7,62 % | 5,83 % | 1,78 pp | 26,33 % | 0 % |
| Italia | 62 | 1 | 11 | 9 | 11,29 % | 16,13 % | 12,90 % | 3,23 pp | 27,42 % | 26 % |
| Francia | 119 | 1 | 12 | 10 | 11,76 % | 9,24 % | 7,56 % | 1,68 pp | 19,17 % | 37 % |
| Reino Unido | 92 | 1 | 4 | 3 | 2,17 % | 3,26 % | 2,17 % | 1,09 pp | 12,09 % | 86 % |
| Argentina | 3.490 | 114 | 358 | 320 | 1,26 % | 6,99 % | 5,90 % | 1,09 pp | 12,32 % | 0 % |

**Empresas.**

| País | Exposición inicial | Prov. iniciales | Prov. 2027 adv | Prov. 2027 base | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |
|---|---|---|---|---|---|---|---|---|---|---|
| Grupo | 237.766 | 3.604 | 15.526 | 9.791 | 1,73 % | 5,01 % | 2,60 % | 2,41 pp | 9,01 % | 71 % |
| España | 60.747 | 1.254 | 6.315 | 3.511 | 2,45 % | 8,33 % | 3,72 % | 4,62 pp | 12,60 % | 90 % |
| México | 39.145 | 342 | 1.757 | 1.246 | 0,87 % | 3,61 % | 2,31 % | 1,31 pp | 5,55 % | 84 % |
| Türkiye | 25.642 | 939 | 1.958 | 1.462 | 4,18 % | 3,97 % | 2,04 % | 1,93 pp | 11,83 % | 0 % |
| EE. UU. | 28.215 | 11 | 785 | 408 | 0,00 % | 2,74 % | 1,41 % | 1,34 pp | 6,11 % | 98 % |
| Perú | 12.372 | 594 | 1.263 | 1.051 | 5,60 % | 5,41 % | 3,69 % | 1,71 pp | 15,81 % | 5 % |
| Colombia | 7.476 | 93 | 478 | 301 | 1,39 % | 5,15 % | 2,78 % | 2,37 pp | 9,12 % | 10 % |
| Italia | 5.310 | 7 | 84 | 45 | 0,02 % | 1,45 % | 0,72 % | 0,73 pp | 1,83 % | 98 % |
| Francia | 5.948 | 17 | 115 | 90 | 0,37 % | 1,65 % | 1,23 % | 0,42 pp | 3,43 % | 95 % |
| Reino Unido | 8.745 | 40 | 545 | 403 | 0,39 % | 5,77 % | 4,15 % | 1,62 pp | 12,93 % | 85 % |
| Argentina | 3.838 | 50 | 449 | 239 | 1,62 % | 10,40 % | 4,92 % | 5,47 pp | 12,30 % | 1 % |

**Minorista partido en hipotecas y resto** (calculado sobre el CSV de la EBA).
- Hipotecas: IRB "Retail – Secured by residential real estate" (código 4150) + STA "Residential immovable property" (5300).
- Resto minorista: consumo, tarjetas, auto y pymes minoristas. Se calcula como IRB Retail (4000) menos IRB hipotecas, más STA Retail (4000).
- Las dos partes suman exactamente la tabla "Minorista": Santander México 10.125 + 15.648 = 25.773; BBVA México 16.786 + 33.313 = 50.099 (50.098 en el PDF, por redondeo).

| Banco | País | Segmento | Exposición inicial (M€) | ΔProv adv / exp. | ΔProv base / exp. |
|---|---|---|---|---|---|
| Santander | Grupo | Hipotecas | 368.077 | 1,36 % | 0,62 % |
| Santander | Grupo | Resto minorista | 252.529 | 12,37 % | 7,55 % |
| Santander | España | Hipotecas | 64.414 | 1,55 % | 0,83 % |
| Santander | España | Resto minorista | 32.548 | 9,29 % | 6,15 % |
| Santander | México | Hipotecas | 10.125 | 3,53 % | 2,73 % |
| Santander | México | Resto minorista | 15.648 | 21,55 % | 11,84 % |
| Santander | EE. UU. | Hipotecas | 14.884 | 1,38 % | 0,50 % |
| Santander | EE. UU. | Resto minorista | 36.213 | 16,73 % | 11,67 % |
| Santander | Brasil | Hipotecas | 10.829 | 2,51 % | 1,37 % |
| Santander | Brasil | Resto minorista | 59.694 | 17,44 % | 11,51 % |
| BBVA | Grupo | Hipotecas | 97.634 | 2,39 % | 1,23 % |
| BBVA | Grupo | Resto minorista | 108.283 | 18,27 % | 13,17 % |
| BBVA | España | Hipotecas | 71.704 | 1,80 % | 0,68 % |
| BBVA | España | Resto minorista | 28.352 | 13,79 % | 7,71 % |
| BBVA | México | Hipotecas | 16.786 | 4,71 % | 3,08 % |
| BBVA | México | Resto minorista | 33.313 | 37,67 % | 28,56 % |
| BBVA | Türkiye | Hipotecas | 1.360 | 1,87 % | 1,57 % |
| BBVA | Türkiye | Resto minorista | 26.368 | 2,93 % | 1,95 % |

Países pedidos que no aparecen en una de las dos fichas:
- Santander no tiene bloque de Türkiye, Perú ni Colombia.
- BBVA no tiene bloque de Brasil ni de Chile.

Cada ficha solo trae los diez primeros países por exposición. `[Certain]`

### Inferences
- `[Certain]` Las tablas de la nota original se pueden publicar en S4 sin cambios en las cifras. Solo hay que cambiar la etiqueta de confianza y la explicación del método.
- `[Likely]` El S3 a fin de 2027 en Santander EE. UU. minorista (49,32 %) y Santander México minorista (31,91 %) parece extremo. Es coherente con dos cosas: carteras de consumo y auto de alta PD, y un balance estático sin fallidos, en el que el stage 3 se acumula durante tres años. Conviene explicarlo en el manual para que no se lea como una tasa de mora real.
- `[Likely]` Para el capítulo 27 conviene usar como métrica principal la cartera "hogares + empresas" o los segmentos (hipotecas, resto minorista, empresas). El total por país mezcla el peso de la deuda pública, que varía mucho: España pesa un 50,8 % en hogares + empresas en Santander frente a un 64,3 % en BBVA.

### Gaps
- La plantilla no separa las sociedades financieras no bancarias dentro de "Corporates".
- El STA minorista no separa tarjetas de consumo o auto. Solo trae "of which SME".

---

## 3. Los dos cocientes del capítulo 27 (§3 de la nota)

### Takeaway
Los dos cocientes son aritméticamente correctos. Pero no resisten el cambio de cartera ni de escenario:
- **México / España ≈ 3,2x en los dos bancos**: sale 3,24 y 3,18. Con hogares + empresas baja a 2,65 y 2,59. En base y en adverso menos base los dos bancos divergen (3,03 frente a 4,69; 3,56 frente a 1,66).
- **Mismo país ≈ 2,3x más caro en BBVA**: se cumple en España (2,32) y México (2,28). No es general: en EE. UU. y Francia BBVA sale 0,40x y 0,42x. Con hogares + empresas queda en ~1,8x.
- **La lectura "la composición de cartera explica la diferencia entre bancos" queda refutada** al nivel de detalle de las plantillas EBA. Casi toda la diferencia es de intensidad dentro de cada segmento, no de mezcla.

### Cited Findings

Todas las cifras salen de las tablas de la sección 2, que a su vez salen de las fichas EBA y del CSV. Los cocientes están calculados con más decimales de los que se ven en las tablas.

**Cociente México / España dentro de cada banco.** Veredicto: **Confirmado** el 3,2x en el adverso con todas las carteras, **con matices** en el resto.

| Cartera y escenario | Santander | BBVA |
|---|---|---|
| Todas, adverso (lo que dice la nota) | 5,9974 / 1,8522 = **3,24** | 13,6691 / 4,3027 = **3,18** |
| Hogares + empresas, adverso | 9,1481 / 3,4534 = **2,65** | 16,5344 / 6,3842 = **2,59** |
| Todas, base | 3,4136 / 1,1269 = 3,03 | 10,1182 / 2,1581 = 4,69 |
| Todas, adverso menos base | 2,58 / 0,73 = 3,56 | 3,55 / 2,14 = 1,66 |
| Hogares + empresas, adverso menos base | 3,91 / 1,35 = 2,90 | 4,29 / 3,32 = 1,29 |
| Minorista, adverso | 14,48 / 4,15 = 3,49 | 26,63 / 5,20 = 5,12 |
| Empresas, adverso | 0,41 / 2,34 = 0,18 | 3,61 / 8,33 = 0,43 |

`[Certain]` toda la aritmética. Fuente: tablas de la sección 2.

**Cociente BBVA / Santander en el mismo país.** Veredicto: **Corregido**. Es cierto en España y México, pero no es una regularidad.

| País | Todas, adverso | Hogares + empresas, adverso | Minorista | Empresas | Todas, base | Todas, adverso menos base |
|---|---|---|---|---|---|---|
| España | 4,3027 / 1,8522 = **2,32** | 6,3842 / 3,4534 = **1,85** | 1,25 | 3,56 | 1,92 | 2,96 |
| México | 13,6691 / 5,9974 = **2,28** | 16,5344 / 9,1481 = **1,81** | 1,84 | 8,74 | 2,96 | 1,37 |
| EE. UU. | 1,5056 / 3,7343 = 0,40 | 0,38 | 1,16 | 2,72 | 0,33 | 0,55 |
| Reino Unido | 4,7081 / 1,5590 = 3,02 | 3,03 | 1,83 | 2,18 | 5,95 | 1,35 |
| Francia | 0,9960 / 2,3586 = 0,42 | 0,57 | 1,59 | 10,23 | 0,61 | 0,22 |
| Grupo | 5,5275 / 3,1854 = 1,74 | 1,66 | 1,84 | 2,45 | 1,95 | 1,45 |

`[Certain]` la aritmética. En EE. UU., Reino Unido y Francia una de las dos carteras es pequeña o muy distinta: BBVA EE. UU. minorista son 141 M€ y BBVA Reino Unido 10.981 M€. Por eso esos cocientes no comparan negocios equivalentes. `[Likely]`

**Descomposición mezcla / intensidad de la diferencia BBVA − Santander** (hogares + empresas, adverso). Tres segmentos: hipotecas, resto minorista y empresas.
- Efecto mezcla: Σ (peso BBVA − peso Santander) × tasa Santander.
- Efecto intensidad: Σ peso BBVA × (tasa BBVA − tasa Santander).
- Fuente: CSV EBA, script `shift_share.py`.

| País | Pesos Santander (hip. / resto min. / empresas) | Pesos BBVA | Tasas Santander | Tasas BBVA | Diferencia total | Mezcla | Intensidad |
|---|---|---|---|---|---|---|---|
| España, adverso | 40,9 / 20,7 / 38,5 % | 44,6 / 17,6 / 37,8 % | 1,55 / 9,29 / 2,34 % | 1,80 / 13,79 / 8,34 % | 6,38 − 3,45 = 2,93 pp | −0,24 pp | +3,17 pp |
| España, base | igual | igual | 0,83 / 6,15 / 1,29 % | 0,68 / 7,71 / 3,72 % | 0,96 pp | −0,16 pp | +1,13 pp |
| México, adverso | 24,4 / 37,7 / 37,9 % | 18,8 / 37,3 / 43,9 % | 3,53 / 21,55 / 0,41 % | 4,71 / 37,67 / 3,61 % | 16,53 − 9,15 = 7,39 pp | −0,26 pp | +7,64 pp |
| México, base | igual | igual | 2,73 / 11,84 / 0,27 % | 3,08 / 28,56 / 2,30 % | 7,02 pp | −0,18 pp | +7,20 pp |
| Grupo, adverso | 40,3 / 27,6 / 32,1 % | 22,0 / 24,4 / 53,6 % | 1,36 / 12,37 / 2,05 % | 2,39 / 18,27 / 5,01 % | 3,05 pp | −0,21 pp | +3,26 pp |

`[Certain]` la aritmética. Comprobación con México adverso: −0,26 + 7,64 = 7,38, frente a 7,39 de diferencia; la desviación es redondeo.

Veredictos sobre las lecturas de la §3:
- **"La composición de la cartera explica la relación entre bancos (más consumo y tarjetas en BBVA México, más hipotecas y empresas grandes en Santander España)": Refutado** al nivel de las plantillas EBA.
  - La mezcla entre hipotecas, resto minorista y empresas aporta −0,26 pp de los 7,39 pp de diferencia en México, y −0,24 pp de 2,93 pp en España.
  - El peso del resto minorista es casi igual en México: 37,7 % en Santander y 37,3 % en BBVA.
  - Lo que difiere es la tasa dentro de cada segmento. En México, el resto minorista cuesta 37,67 % en BBVA frente a 21,55 % en Santander (1,75x), y las empresas 3,61 % frente a 0,41 %.
  - Nueva confianza: `[Likely]`. Dentro del "resto minorista" puede haber todavía mezcla de producto (tarjetas frente a nómina o auto) que la plantilla STA no separa.
- **"El escenario explica la relación entre países": Corregido.**
  - La coincidencia de 3,2x solo aparece en el adverso con todas las carteras.
  - En el escenario base los dos bancos dan 3,03 y 4,69, y en el incremento adverso menos base 3,56 y 1,66. Si el escenario explicara solo la relación entre países, esos cocientes también deberían parecerse.
  - Nueva confianza: `[Likely]` que la coincidencia sea en parte casual.
- **"[Guessing] Parte de la diferencia puede venir del método o de los modelos": se mantiene como `[Guessing]`. Inverificable** con datos públicos.
  - La descomposición de arriba refuerza que la diferencia está en las tasas por segmento: perfil de riesgo, producto dentro del segmento, parámetros de los modelos o *overlays*.
  - Los datos públicos no permiten separar esas causas.
- **"[Certain] El escenario base ya consume mucho en México (BBVA 10,12 %; Santander 3,41 %)": Confirmado.**
  - Adverso menos base: BBVA México 3,55 pp y Santander México 2,58 pp.
  - En España: BBVA 2,14 pp y Santander 0,73 pp.
  - Con hogares + empresas: BBVA México 4,29 pp, Santander México 3,91 pp, BBVA España 3,32 pp, Santander España 1,35 pp. `[Certain]`

### Inferences
- `[Likely]` Para el capítulo 27, el "puente" país → banco no debería apoyarse en la coincidencia del 3,2x. Es más sólido así:
  - Medir la severidad del país como adverso menos base, por segmento.
  - Medir la diferencia entre bancos con la descomposición mezcla / intensidad. Muestra que en los dos países casi todo es intensidad.
- `[Likely]` Que en México las empresas de Santander salgan casi sin coste (0,41 % en adverso, 0,14 pp sobre base, 94 % IRB) es un caso didáctico. Ilustra cómo la exposición a grandes corporativos con PD baja, modelizada por IRB, amortigua el estrés país.

### Gaps
- No hay forma pública de separar tarjetas, consumo y auto dentro del minorista STA de México.

---

## 4. Agregado EBA 2025 y la media de 228 pb de BBVA (§1 de la nota)

### Takeaway
- Las cifras agregadas están en el informe de la EBA, que es fuente primaria: 547.000 M€ de pérdidas y −6,3 % de PIB.
  - Caída del CET1: 370 pb en transitorio (de 15,8 % a 12,1 %) y 304 pb en *fully loaded*.
  - Pérdidas de crédito: 394.000 M€.
  - Muestra: 64 bancos.
- La media de 228 pb que cita BBVA es la **media simple** de la caída *fully loaded* a fin de 2027 de diez competidores. La he reproducido exactamente con la tabla A2 de la EBA.

### Cited Findings

**Agregado de la EBA.** Veredicto: **Confirmado**. La etiqueta de la nota debe pasar de "fuente secundaria" a primaria. `[Certain]`
- **Muestra:** 64 bancos de 17 países de la UE y el EEE, 51 de ellos de la zona euro, con ~75 % de los activos bancarios de la UE ([informe EBA, p. 12](https://www.eba.europa.eu/sites/default/files/2025-08/0178b9c5-2f0d-42ee-8226-6fa0a87c0d6c/2025%20EU-wide%20stress%20test%20-%20Results.pdf); [nota de prensa EBA, 1-ago-2025](https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-results-its-2025-eu-wide-stress-test)). `[Certain]`
- **Pérdidas combinadas** de crédito, mercado y operacional: 547.000 M€ en tres años, frente a 496.000 M€ en 2023. El PIB de la UE cae un 6,3 % y el paro sube 5,8 pp (informe EBA, p. 9). `[Certain]`
- **Desglose de las pérdidas** (tabla 1, p. 28):
  - Crédito: 394.000 M€.
  - Mercado: 98.000 M€ netos. Las pérdidas iniciales de mercado son 187.000 M€ (p. 10).
  - Operacional: 55.000 M€.
  - Aritmética: 394 + 98 + 55 = 547. `[Certain]`
- **Caída del CET1 en transitorio:** 370 pb, de un 15,8 % de partida con CRR3 a un 12,1 % a fin de 2027 (p. 21). En 2023 había sido de 479 pb (p. 21). `[Certain]`
- **Caída del CET1 *fully loaded*:** 304 pb (p. 21, nota 17). `[Certain]`
- **CET1 *fully loaded* agregado:** a fin del adverso queda "por encima del 11 %" (p. 10). El *fully loaded* re-expresado CRR3 es 129 pb más bajo en partida que el transitorio (p. 10).
  - Deduzco un CET1 *fully loaded* de partida de ~14,5 % (15,8 − 1,29) y de fin de horizonte de ~11,5 % (14,5 − 3,04). La EBA no publica esas dos cifras exactas en el texto. `[Likely]`
- **Pérdidas de crédito en detalle** (pp. 39-40):
  - Las 394.000 M€ son el 1,9 % de la exposición total a fin de 2024. Restan 437 pb de CET1, con un rango por banco de 10 a 828 pb. En 2023 fueron 347.000 M€.
  - El minorista es menos del 10 % de la exposición, pero concentra casi el 30 % de las pérdidas de crédito.
  - Stage 2 pasa del 8,2 % al 13,7 % y stage 3 del 1,7 % al 6,0 %. `[Certain]`
- **Escenario base agregado:** el CET1 llega al 16,9 % en 2027 (p. 10). `[Certain]`

**Comparación de orden de magnitud con el agregado.**
- La EBA define la tasa de pérdida como pérdida acumulada sobre la exposición de partida (p. 41, nota de la figura 22). Es casi la misma métrica que el ΔProv / exposición de la nota.
- Resultados:
  - Agregado UE: 1,9 %.
  - Santander: 3,19 % (44.090 / 1.384.138).
  - BBVA: 5,53 % (35.593 / 643.928).
- Las definiciones del denominador pueden no ser idénticas: la EBA habla de "total exposures". `[Likely]`

**La media de 228 pb de BBVA.** Veredicto: **Confirmado**, y ahora reproducido.
- La nota de BBVA del 1-ago-2025 dice que su caída de 186 pb "stands out very favorably with the average of BBVA's comparable European banks (228 basis points down to 10.01 percent)" ([BBVA, 1-ago-2025](https://www.bbva.com/en/economy-and-finance/bbva-one-of-europes-most-resilient-banks-in-the-2025-stress-tests/)).
- El grupo de comparables está en la nota al pie: BNP, Crédit Agricole, CaixaBank, Deutsche Bank, ING, Intesa, Nordea, Santander, Société Générale y UniCredit. `[Certain]`
- Reproducción con la tabla A2 del informe EBA (pp. 61-63), columna "Delta" (*fully loaded*, fin de 2027):

| Banco | Caída (pb) | CET1 FL 2027 adverso |
|---|---|---|
| Deutsche Bank | 226 | 7,4 % |
| CaixaBank | 162 | 10,8 % |
| Santander | 173 | 10,5 % |
| Nordea | 225 | 10,5 % |
| BNP | 213 | 8,9 % |
| Crédit Agricole | 478 | 9,5 % |
| Société Générale | 337 | 8,6 % |
| Intesa | 62 | 11,8 % |
| UniCredit | 215 | 11,7 % |
| ING | 187 | 10,4 % |
| **Suma** | **2.278** | **100,1 %** |
| **Media simple** | **227,8 ≈ 228** | **10,01 %** |

`[Certain]`

- Redacción propuesta: "BBVA cifró en 228 pb la caída media de diez comparables europeos que eligió él. Es la media simple, sin ponderar, de los datos *fully loaded* publicados por la EBA, y se puede reproducir con la tabla A2 del informe."

### Inferences
- `[Likely]` Para el manual, la referencia neutral es el agregado de la EBA: 304 pb en *fully loaded* y 370 pb en transitorio. El 228 pb de BBVA depende de los comparables que elige el banco y de no ponderar. Por ejemplo, el 478 pb de Crédit Agricole sube la media; sin él, la media de los otros nueve es (2.278 − 478) / 9 = 200 pb.

### Gaps
- No he consultado la nota de prensa de Santander del 1-ago-2025. Las cifras de Santander se apoyan en la ficha EBA y en la tabla A2.

---

## 5. Santander México, BBVA México y los ejercicios locales (§4 de la nota)

### Takeaway
- **Santander México dejó de cotizar en 2023: confirmado y fechado.**
  - Salida de NYSE: Form 25 presentado el 24-abr-2023.
  - Cancelación de la inscripción en el RNV mexicano: 12-may-2023.
  - Tras la venta forzosa (*statutory sell-out*), Santander tiene ~99,97 %.
- No he encontrado resultados del ejercicio local publicados por banco, ni de Santander México ni de BBVA México.
- Banxico publica su prueba de estrés de sistema con resultados agregados.
- La filial de BBVA México que he revisado (la casa de bolsa) solo publica una frase cualitativa sobre su Evaluación de Suficiencia de Capital.

### Cited Findings

**Santander México.** Veredicto: **Confirmado**. Pasa de `[Likely]` a `[Certain]`.
- La asamblea extraordinaria del 30-nov-2022 aprobó cancelar la inscripción en la BMV y en NYSE, condicionada a las OPA ([El CEO, 1-dic-2022](https://elceo.com/mercados/accionistas-de-santander-aprueban-desliste-de-la-bmv-y-wall-street/)). `[Certain]`
- Banco Santander lanzó la OPA en EE. UU. el 7-feb-2023 (Schedule TO-T, [índice EDGAR CIK 1698287](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001698287&type=SC+TO-T)). `[Certain]`
- Al cierre de la oferta se presentó ~95,73 % de las acciones serie B a las que se dirigía. La participación de Santander pasaba de ~96,2 % a ~99 % ([SC TO-T/A n.º 2, 11-abr-2023](https://www.sec.gov/Archives/edgar/data/1698287/000095010323005586/0000950103-23-005586-index.htm)). `[Certain]`
- Form 25 de exclusión de NYSE presentado el 24-abr-2023 ([EDGAR](https://www.sec.gov/Archives/edgar/data/1698287/000095010323006070/0000950103-23-006070-index.htm)). Bloomberg Línea esperaba la exclusión efectiva el 4-may-2023 ([Bloomberg Línea, 13-abr-2023](https://www.bloomberglinea.com/latinoamerica/mexico/banco-santander-solicita-cancelacion-de-ads-en-la-bolsa-de-valores-de-nueva-york/)). `[Certain]`
- "On May 12, 2023, the registration of the Company's Series B Shares with the Mexican National Securities Registry of the CNBV was cancelled" ([SC TO-T/A n.º 4, 15-may-2023](https://www.sec.gov/Archives/edgar/data/1698287/000095010323007299/0000950103-23-007299-index.htm)). `[Certain]`
- El *statutory sell-out* venció el 15-nov-2023. Después, la participación de Santander es de ~99,97 % ([SC TO-T/A n.º 5, 16-nov-2023](https://www.sec.gov/Archives/edgar/data/1698287/000095010323016368/0000950103-23-016368-index.htm)). `[Certain]`
- Redacción propuesta: "Santander México dejó de cotizar en 2023. Salió de NYSE en abril-mayo y la CNBV canceló su inscripción en el RNV el 12 de mayo. Banco Santander controla ~99,97 % desde noviembre de 2023."

**BBVA México.**
- "BBVA México no cotiza": veredicto **Inverificable** en esta pasada. Mantener `[Likely]` hasta comprobarlo con la BMV.
- La casa de bolsa de BBVA México describe la ESC de la CNBV así:
  > "A solicitud de la Comisión Nacional Bancaria y de Valores, anualmente se realiza el Ejercicio de Evaluación de Suficiencia de Capital (ESC) [...] en el cual se evalúa su capacidad para seguir realizando operaciones ante los escenarios macroeconómicos propuestos por el regulador."

  Del resultado solo dice que los ratios de solvencia "cumplen durante todo el periodo de proyección con niveles superiores a los mínimos regulatorios", sin cifras ([Estados financieros 2023 de Casa de Bolsa BBVA México](https://investors.bbva.mx/wp-content/uploads/2024/02/Edos-Financieros-CB-2023-R%C3%BAbrica.pdf)). `[Certain]` para la casa de bolsa.
- Que el banco BBVA México publique algo parecido es `[Likely]`. No lo he comprobado.

**Los "tres números de estrés" de la nota.** Veredicto: **Confirmado en lo esencial**, con un matiz inverificable.
- **EBA:** confirmado por las fichas. `[Certain]`
- **Banxico:** su *Reporte de Estabilidad Financiera* de junio de 2026, sección 4 "Pruebas de estrés":
  - Simula a tres años desde marzo de 2026 tres escenarios macro (A, B y C) y tres históricos (H1 a H3).
  - Presenta la distribución del ICAP del sistema.
  - Supone que "no se consideran las reacciones de los bancos ni de los reguladores": los bancos no cambian estrategia, aportaciones de capital ni posiciones.
  - Lo describe como "simulación contrafactual y de equilibrio parcial".
  - Fuente: Banxico, REF junio 2026 (copia local leída; listado en [banxico.org.mx, reportes sobre el sistema financiero](https://www.banxico.org.mx/publicaciones-y-prensa/reportes-sobre-el-sistema-financiero/reportes-sistema-financiero-ta.html); no he resuelto la URL exacta del PDF). `[Certain]` para el contenido.
  - Que los resultados no se den por banco nombrado es `[Likely]`: los gráficos son distribuciones (cajas y bigotes).
- **CNBV (ESC):** ejercicio anual con escenarios del regulador, confirmado por la cita anterior. `[Certain]`
  - "Con metodología local de reservas": **Inverificable**.
- La nota fechaba Banxico en "2025-2026". El ejercicio más reciente que he visto es el de junio de 2026.

**"Las filiales no publican su resultado del ejercicio local".** Veredicto: **Confirmado parcialmente.** `[Likely]`
- Lo único publicado que he encontrado es la frase cualitativa de la casa de bolsa de BBVA México.
- Una búsqueda sobre la ESC de la CNBV no devolvió resultados por banco ([búsqueda web, 16-oct-2026]; sin fuente positiva).

### Inferences
- `[Likely]` La conclusión de la nota sigue en pie: la comparación cuantitativa entre el ejercicio local y la EBA tendrá que hacerse en S4 con datos sintéticos.
- `[Likely]` Ahora se puede calibrar mejor con datos reales del EBA por segmento. Por ejemplo, México resto minorista en adverso: 21,55 % en Santander y 37,67 % en BBVA.

### Gaps
- El estado de cotización de BBVA México y de su grupo financiero en la BMV.
- Si el banco BBVA México o Santander México publican en sus estados financieros una frase sobre la ESC parecida a la de la casa de bolsa.
- La URL exacta del PDF del REF de junio de 2026.
- Si Santander México conserva deuda listada en la BMV. No afecta a la tesis.

---

## 6. Datos interactivos y CSV de la EBA para el anexo

### Takeaway
Sí, la EBA publica en abierto la base completa del ejercicio 2025 en CSV, con diccionario y metadatos, y dos páginas interactivas en Power BI. Es la fuente recomendable para el anexo S4: trae el país codificado y evita los problemas de extraer texto del PDF.

### Cited Findings
- **Página del ejercicio:** [https://www.eba.europa.eu/eu-wide-stress-test-2025](https://www.eba.europa.eu/eu-wide-stress-test-2025). `[Certain]`
- **Ficheros CSV** (cada uno con la descripción del [CSV guide](https://www.eba.europa.eu/assets/st25/full_database/763451/CSV_guide.pdf)):
  - [TRA_CRE_IRB.csv](https://www.eba.europa.eu/assets/st25/full_database/763451/TRA_CRE_IRB.csv): ~62 MB, riesgo de crédito IRB.
  - [TRA_CRE_STA.csv](https://www.eba.europa.eu/assets/st25/full_database/763451/TRA_CRE_STA.csv): ~70 MB, riesgo de crédito estándar y titulizaciones.
  - [TRA_OTH.csv](https://www.eba.europa.eu/assets/st25/full_database/763451/TRA_OTH.csv): ~6 MB, resumen, capital, APR y P&L.

  `[Certain]`
- **Metadatos y diccionario:** [Metadata_TR.xlsx](https://www.eba.europa.eu/assets/st25/full_database/763451/Metadata_TR.xlsx) y [Data_Dictionary.xlsx](https://www.eba.europa.eu/assets/st25/full_database/763451/Data_Dictionary.xlsx). `[Certain]`
- **Estructura de los CSV de crédito:**
  - Columnas: `Country_code, LEI_Code, Bank_name, Period, Item, Scenario, Portfolio, IFRS9_Stages, Exposure, Country, Country_rank, Perf_status, Amount`.
  - Escenarios: 11 = re-expresado, 2 = base, 3 = adverso.
  - Partidas: 2532003 y 2532004 = exposición y provisiones por stage en IRB; 2533003 y 2533004 = lo mismo en STA.
  - Exposición: 0 total, 3000 corporates, 4000 retail, 4150 retail hipotecario IRB, 5000, 5300, 5400 y 5600 inmobiliario STA.
  - Países: 28 España, 38 México, 43 EE. UU., 31 Brasil, 42 Türkiye.
  - El CSV usa formato numérico del Reino Unido (punto decimal).
  - Fuente: Metadata_TR.xlsx y CSV guide. `[Certain]`
- **LEI:** Santander 5493006QMFDDMYWIAM13; BBVA K8MS7FD7N5Z2WQ51AZ71 (Metadata_TR.xlsx, hoja ListOfBanks). `[Certain]`
- **Herramientas interactivas** (Power BI):
  - [st25_visualisation_page_2.html](https://tools.eba.europa.eu/interactive-tools/2025/powerbi/763451/st25_visualisation_page_2.html)
  - [st25_visualisation_page_3.html](https://tools.eba.europa.eu/interactive-tools/2025/powerbi/763451/st25_visualisation_page_3.html)
  - Están enlazadas desde la página del ejercicio. No las he abierto, porque requieren JavaScript. `[Certain]` que existen y están enlazadas.
- **Fichas por banco:** `https://www.eba.europa.eu/assets/st25/bank_individual_results/763451/EBA_ST_<país>_<LEI>.pdf`. `[Certain]`

### Inferences
- `[Likely]` Para S4 conviene sustituir el parser de texto por una consulta al CSV:
  - Filtrar por LEI, Item, Scenario y Period (202412 y 202712), con `Perf_status = 0` e `IFRS9_Stages` de 1 a 3.
  - Agrupar por `Country` y `Exposure`.
  - Es más robusto y trae decimales. Las diferencias con el PDF son de redondeo: como máximo 0,35 pp, en una cartera de 141 M€.
- `[Likely]` Citar en el anexo la URL del CSV con fecha de consulta, como snapshot.

### Gaps
- No he comprobado si la EBA ha publicado correcciones de los CSV después del 1-ago-2025. La ruta lleva el identificador `763451`; si cambia, habrá una versión nueva.
