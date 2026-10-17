---
type: source
created: 2026-10-16
status: active
freshness: snapshot
tags: [stress-test, jers, escenario, f1]
---

# F1 · JERS: el escenario adverso y los países de fuera de la UE

Consultado el 2026-10-16 y **validado ese mismo día contra fuentes primarias** (informe
`reports/Validación F1 stress test.md`, correcciones J1-J11). **Las tablas completas por país
(IPC, tipos a largo, tipos de cambio, curvas swap e iTraxx), base para el anexo S3, están en
`research_notes/Validación F1 stress test/jers-escenario.md`, §2.**

Fuente primaria: escenario macrofinanciero de la JERS para el ejercicio 2025
(`fuentes/2025-02-26 ESRB escenario ST2025.pdf`). El escenario se publicó con el lanzamiento del
20-ene-2025; el PDF local es la versión corregida por la fe de erratas ESRB/2025/0014 (carta del
26-feb-2025, publicada por la EBA el 28-feb-2025), que **solo corrige algunos tramos de los swaps
en GBP**. No cambia ninguna cifra de PIB, paro, precios ni tipos de cambio `[Certain]`.

`[Likely]` El escenario del 2027 no está publicado a 2026-10-16. Por el precedente (la JERS lo
aprueba el 14-ene-2025, lo envía el 15-ene y la EBA lanza el 20-ene), saldría a finales de enero de
2027; la EBA prevé resultados "around summer".

## 1. Quién lo hace y cómo

- `[Certain]` El adverso 2025 lo diseñó la *Task Force on Stress Testing* de la JERS en estrecha colaboración con el BCE; la Junta General lo aprobó el 14-ene-2025. El escenario base de la UE son las proyecciones de dic-2024 de los bancos centrales nacionales; el base de la zona del euro lo aporta el BCE (NM27 párr. 42).
- `[Certain]` **Base de los países no UE: el WEO del FMI de octubre de 2024 y datos de la OCDE** (nota al pie 2, repetida en cada tabla). **En tipos de cambio, bolsa y materias primas el base es plano** (se mantiene el nivel de partida). **Para el manual:** el base de México en el EBA no es el de Banxico ni el de la filial, sino el del FMI. Es la primera pieza del puente del cap. 27.
- `[Certain]` Narrativa 2025: tensiones geopolíticas agravadas, barreras comerciales y repunte inflacionista por el lado de la oferta.

## 2. Resumen por país (anexo 4.1, pp. 13-24)

Desviaciones = nivel adverso frente a nivel base en 2027. Depreciación = cálculo sobre la media anual
de 2025 frente al punto de partida.

| País | PIB acumulado adverso | PIB desv. 2027 | Paro desv. 2027 | Vivienda desv. 2027 | CRE desv. 2027 | Depreciación frente al EUR (2025) | Bolsa (2025) |
|---|---|---|---|---|---|---|---|
| UE | −6,3 % | −10,4 % | — | — | — | — | −50 % |
| España | −4,1 % | −9,8 % | +5,7 pp | −30,1 % | −28,8 % | — | −50 % (UE) |
| México | −6,9 % | −11,9 % | +5,3 pp | −22,1 % | −42,1 % | +8,9 % | −66 % (RoW) |
| Brasil | −3,0 % | −9,2 % | +4,3 pp | −25,6 % | −39,8 % | +13,4 % | −66 % (RoW) |
| Chile | −3,3 % | −10,0 % | +4,4 pp | −22,1 % | −35,1 % | +15,5 % | −66 % (RoW) |
| Colombia | −2,7 % | −10,3 % | +4,8 pp | −22,1 % | −36,7 % | +8,7 % | −66 % (RoW) |
| Perú | −3,6 % | −10,3 % | +4,8 pp | −22,1 % | −36,3 % | +4,2 % | −66 % (RoW) |
| Türkiye | −6,6 % | −14,8 % | +6,1 pp | −19,3 % | −39,3 % | +36,5 % | −66 % (RoW) |
| Reino Unido | −10,0 % | −13,9 % | +6,2 pp | −30,8 % | −41,3 % | 0 % | −52 % |
| EE. UU. | −3,4 % (valle −7,4 %) | −9,3 % | +4,5 pp | −22,9 % | −46,3 % | 0 % | −61 % |

`[Certain]` Cifras del PDF. Por años, el PIB de México es −4,7 % / −2,2 % / −0,1 %, y el de España, −2,5 % / −3,5 % / +2,0 %.
`[Certain]` Paro en niveles, adverso frente a base en 2027: España 15,6 % frente a 9,9 %; México 8,8 % frente a 3,5 %; Brasil 11,7 % frente a 7,4 %.
`[Certain]` Vivienda en acumulado nominal: España −17,2 %, México −8,1 %, Brasil −19,4 %, Reino Unido −26,7 % (tabla 4.1.4, p. 16).
`[Certain]` Tipo de cambio, media anual 2025/2026/2027 frente al nivel de partida: EUR/MXN +8,9 / +7,3 / +6,0 %; EUR/BRL +13,4 / +11,0 / +8,9 %; EUR/TRY +36,5 / +30,0 / +24,6 %.

## 3. Qué variables hay y cuáles no

- `[Certain]` Hay series por país de PIB, paro, IPC, vivienda, inmobiliario comercial y tipos a largo para ES, UK, US, TR, BR, MX, CL, CO y PE.
- `[Certain]` Los tipos de cambio van por par EUR/xxx (MXN, BRL, TRY, CLP, COP, PEN). **EUR/USD y EUR/GBP no se mueven en el adverso.**
- `[Certain]` Hay curvas swap para EUR, GBP, USD, TRY, BRL, MXN, CLP y COP. **No hay para PEN**: se usa la curva RoW, idéntica a la USD.
- `[Certain]` **La bolsa solo viene** para UE, NO, UK, US, JP, CA, CH y AU&NZ. LatAm y Türkiye usan "Rest of the world" (−66 / −61 / −57 %) y España, el choque UE.
- `[Certain]` **Argentina no aparece en el documento**: ni fila, ni par EUR/ARS, ni curva swap. La metodología EBA obliga a usar "Rest of the world" solo para swaps y tipos de cambio (NM25 párr. 375-376; NM27 párr. 379-380). `[Likely]` Para PIB, paro o vivienda no hay regla escrita: el banco documenta su traslación ante la autoridad. `[Likely]` "Rest of the world" es un proxy burdo (su paro replica el de Türkiye, sus tipos son los de EE. UU.) y subestima el riesgo de tipos e inflación de Argentina.

## 4. Lo que importa para el manual

- `[Certain]` El escenario cubre las geografías de Santander y BBVA (México, Brasil, Chile, Colombia, Perú, Türkiye, Reino Unido, EE. UU.) en las variables macro, con los huecos anteriores.
- `[Certain]` / `[Likely]` **Severidad relativa: depende de cómo se mida.** En acumulado, México (−6,9 %) y Türkiye (−6,6 %) sufren más que España (−4,1 %). En desviación frente a la base, la distancia se estrecha: México −11,9 %, Türkiye −14,8 %, España −9,8 %. En paro, México y España son parecidos (+5,3 frente a +5,7 pp), y **en vivienda España sufre más** (−30,1 frente a −22,1 %). Solo en inmobiliario comercial México es claramente peor (−42,1 frente a −28,8 %). EE. UU. (−3,4 % acumulado) esconde un valle del −7,4 % y un rebote del +4,3 % en 2027. **Consecuencia para el cap. 27:** el escenario no explica por sí solo que la pérdida mexicana triplique la española (ver `datos-publicos.md`).
- `[Certain]` **El tipo de cambio entra por cuatro vías**, no solo por los satélites: el párr. 35 fija los saldos al tipo de cierre y excluye el FX del RWA salvo en mercado, pero el FX llega por los préstamos en divisa (párr. 147-148), el NII con factor corrector (NM27 párr. 380; NM25 párr. 376), las comisiones ("includes FX variations to the starting point") y el riesgo de mercado. Como EUR/USD y EUR/GBP no se mueven, las filiales de EE. UU. y Reino Unido no tienen choque cambiario frente al euro.
- `[Likely]` / `[Certain]` **Variables que faltan:** en crédito, el banco las deriva con satélites o modelos auxiliares (anexo S3). **En mercado está prohibido**: "no statistical extrapolation or expansion of risk factors is permitted"; se aplica el choque más cercano (NM27 párr. 260).
- `[Certain]` **Türkiye solo se entiende en desviación:** la vivienda sube un 128,7 % nominal acumulado en el adverso, pero cae un 19,3 % frente a la base. Un satélite en términos nominales daría señales erróneas.
- `[Certain]` En México el IPC adverso de 2027 es **−0,5 %**: un año de deflación.
- `[Guessing]` México, Chile, Colombia y Perú comparten el mismo −22,1 % de desviación en vivienda, lo que sugiere una calibración regional común.
- `[Certain]` El propio documento compara la severidad con otros supervisores (gráfico 14, pp. 11-12): la caída del PIB doméstico del EBA 2025 es "notablemente más pronunciada" que la del CCAR 2024 de la Fed y más fuerte que los dos escenarios del ejercicio de escritorio de 2024 del Banco de Inglaterra; lo atribuye a fechas, puntos de partida y rasgos cíclicos distintos. **Aviso de métrica:** el gráfico mide la caída acumulada **desde el punto de partida hasta el final del horizonte**, no de pico a valle. `[Likely]` Con esa métrica el CCAR 2024 sale en torno a −1,5 %, aunque su caída de pico a valle es del −8,5 %. **Para el manual:** prueba de que dos escenarios "severos" no son comparables sin fijar antes la métrica. Arranque natural del cap. 27.

## 5. Comparación con los escenarios locales

- `[Likely]` Brasil: frente al escenario "Crise de Confiança" del BCB, la JERS es mucho más suave en tipo de cambio (≈+13 % de media anual frente a ≈+55 % en el pico trimestral) y en tipos (swap 3M ≈12,8 % frente a una Selic ≈24,5 %); comparable en PIB. Parte de la diferencia es de medida (medias anuales frente a picos trimestrales). `[Guessing]` las magnitudes.
- `[Certain]` Banxico no publica en su informe las sendas en niveles ni las desviaciones típicas de sus escenarios A, B y C, así que la comparación con México es cualitativa.

## Huecos que siguen abiertos

- Escenario 2027 (no publicado).
- Anexo 3 del escenario JERS 2020 (cómo se construye el adverso no UE) y regla para variables macro de países sin fila en las Q&A de la EBA.
- Tramos swap 1M, 2A, 3A, 7A, 20A y 30A, y tabla de erratas de los swaps GBP (Excel del 28-feb-2025).
- Sendas de Banxico en niveles; ficheros de datos del informe del BCB.
