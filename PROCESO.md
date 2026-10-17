# PROCESO — Manual de Stress Test de riesgo de crédito

> **Léeme primero.** Este archivo existe para que cualquier sesión nueva (con o sin contexto previo)
> pueda retomar el trabajo con el mismo enfoque, la misma voz y las mismas convenciones.
> Si estás empezando una sesión, lee este archivo entero antes de escribir nada.
>
> Es el hermano del *Manual de Capital y Provisiones* (`../manual_irb/`). Hereda de él voz,
> formato y método; donde este archivo no diga otra cosa, manda `../manual_irb/PROCESO.md`.

---

## 1. Qué estamos construyendo

Un **manual de estudio y referencia sobre *stress testing* de riesgo de crédito** para consultores
que entran en proyectos de *stress test* en grandes grupos bancarios. Formato final: **AZW3/EPUB**
construido desde HTML, como el del IRB.

**No es** una guía de la metodología EBA de un año concreto ni un resumen normativo. Es el manual de
**cómo se vive el ejercicio en un grupo con filiales en varios continentes frente al JST**: qué se
proyecta, cómo, qué pregunta el supervisor, dónde se rompe la coherencia y cómo se defiende un número.

### Encargo original (Rafa, 2026-10-16)

> - Para el procedimiento de cómo hacerlo, a quién enfocarlo, etc., fíjate en cómo lo hice para IRB.
> - Me gustaría que estuviese orientado a situaciones prácticas que viven los grandes bancos (piensa
>   en Santander o BBVA, que son españoles pero operan en múltiples países y geografías fuera de
>   Europa) con el regulador (por ejemplo, el JST).
> - Me gustaría que en la parte avanzada del manual se centrase en los retos de los próximos años con
>   el regulador, con su situación de datos en diferentes sitios y con comparables que resultan
>   modelos de ST realizados en diferentes países (¿cómo se compara el número que sale de Santander
>   España con el de Santander México?).
> - Me gustaría que incluyese una sección de metodología: desde la que hay que aplicar hoy a los retos
>   metodológicos que se plantean y cómo abordarlos.

Ese texto es el criterio de aceptación de todo lo que se escriba.

---

## 2. Decisiones cerradas (no reabrir sin que Rafa lo pida)

| Decisión | Valor |
|---|---|
| **Perímetro** | **Solo riesgo de crédito.** Del capital, lo justo para llevar pérdidas y RWA de crédito al CET1 |
| **Fuera de perímetro** | NII, mercado y CCR, operacional y conducta, comisiones, liquidez. Solo ganchos de remisión |
| **Perfil del lector** | **Cambiado el 2026-10-16:** persona que conoce la banca y el IRB en lo básico (PD, LGD, EAD, RWA, CET1), y poco más, a la que el manual lleva hasta experto. **No** se asumen IFRS 9, escenarios, econometría ni el propio *stress test*: se construyen en la Parte I |
| **Progresión** | Tres niveles (N1 fundamentos, N2 practicante, N3 experto), con objetivos al final de cada parte y autoevaluación. Lo que manda es el contenido, no el número de capítulos |
| **Autocontenido** | El manual se entiende sin el IRB; las remisiones al IRB son para profundizar |
| **Metodología** | Una sola parte con dos bloques: A, lo que se aplica hoy (N2); B, retos y cómo abordarlos (N3) |
| **Jurisdicción** | MUS/EBA como columna vertebral; reguladores de fuera de la UE de los grupos españoles como segunda capa |
| **Bancos reales** | **Con nombre real** (Santander, BBVA y sus filiales), **solo con datos públicos, fuente y fecha** |
| **Experiencia de encargos** | Entra **anonimizada**, como patrón, en los bloques CASO. Nunca con nombre del cliente |
| **Anexos ejecutables** | Sí, seis (S1-S6), en Python, **ejecutados antes de publicar** |
| **Fuentes** | Fase de research (F1) antes de cerrar el índice |
| **Formato** | Multi-archivo HTML (una parte por fichero) + CSS compartido → Calibre (AZW3 + EPUB) |
| **Repositorio** | **Público en GitHub** (`rafavigueras/manual_st`), por decisión de Rafa del 2026-10-17, que sustituye a la de «privado si se publica». Sin GitHub Pages. Los PDF de `investigacion/fuentes/` no se suben |
| **Idioma y voz** | Los del IRB (§6 de su `PROCESO.md`): español de España, director de riesgos con quince años de proyecto |
| **Máquina** | Mac. Python con `python3 -m venv .venv` (no hay `uv`). Calibre en `/Applications/calibre.app/Contents/MacOS/` |

---

## 3. Estructura de archivos

```
manual_st/
├── PROCESO.md                     ← este archivo
├── 00-indice-manual-st.md         ← plan de trabajo: índice a 3 niveles (F2)
├── investigacion/                 ← notas de research fechadas, con [Certain]/[Likely]/[Guessing] (F1)
├── herramientas/
│   └── revision.py                ← revisión automática (enlaces, anclas, bloques, HTML). Vive en el repo
└── manual/
    ├── estilo.css                 ← copia del IRB + bloque b-caso
    ├── index.html                 ← portada, sistema de bloques, índice a 2 niveles
    ├── parte-00.html … parte-06.html  ← la Parte III va partida en parte-03a.html (bloque A) y parte-03b.html (bloque B)
    ├── anexos-codigo.html         ← S1-S6
    ├── anexos-referencia.html
    ├── construir_kindle.py        ← copia del IRB, por adaptar a rutas de Mac
    ├── kindle-eink.css
    └── generar_portada.py         ← copia del IRB, por rehacer con motivo propio
```

**Regla heredada:** el `.md` del índice es el plan de trabajo (3 niveles); `index.html` es el índice
del libro (2 niveles). Si cambia la estructura, se actualizan ambos.

---

## 4. Estado actual

| Fase | Entregable | Estado |
|---|---|---|
| F0 · Arranque | Carpeta, repo, este archivo, nota de seguimiento | ✅ 2026-10-16 |
| F1 · Research | `investigacion/` (5 notas + `README.md` + PDFs en `fuentes/`) | ✅ 2026-10-16, **validada** contra fuentes primarias el mismo día (`investigacion/reports/`); huecos restantes al final de cada nota |
| F2 · Índice a 3 niveles | `00-indice-manual-st.md` v0.2 | ✅ Aprobado por Rafa el 2026-10-16 |
| F3 · Base | `estilo.css` (+`b-caso`, niveles, objetivos), `index.html`, `parte-00.html`, `herramientas/revision.py` | ✅ 2026-10-16 |
| F4 · Redacción | `parte-01.html` (Parte I, caps. 1-8, ~12.400 palabras tras la ampliación) | ✅ 2026-10-16, ampliada a petición de Rafa |
| F4 · Redacción | `parte-02.html` (Parte II, caps. 9-13, ~14.100 palabras) | ✅ 2026-10-17, pendiente de lectura de Rafa |
| F4 · Redacción | `parte-03a.html` (Parte III-A, caps. 14-21, ~14.900 palabras) | ✅ 2026-10-17, pendiente de lectura de Rafa |
| F4 · Redacción | `parte-03b.html`, `parte-04.html`, `parte-05.html`, `parte-06.html` (caps. 22-36) | ✅ 2026-10-17 |
| F5 · Anexos de código | S0-S6 ejecutados; `anexos-codigo.html` generado por `herramientas/generar_anexos_codigo.py`; `anexos-referencia.html` (R1-R7) | ✅ 2026-10-17 |
| F6 · Revisión | QUÉ VIENE inventariados, `revision.py` en OK, fugas revisadas | ✅ 2026-10-17 |
| F7 · Publicación | `manual-completo.html`, AZW3, EPUB, portada nueva; repo público en GitHub | ✅ 2026-10-17 |

---

## 5. Sistema de bloques

Los nueve del IRB, con la misma clase CSS y el mismo marcado (`<div class="bloque b-x"><span
class="etiqueta">…</span>…</div>`): NORMA, POR QUÉ, MARGEN, PALANCA, TRAMPA, NÚMEROS, CÓDIGO,
DEFENSA, QUÉ VIENE. Dos ajustes:

- **PALANCA** se lee aquí como impacto en el consumo de CET1 del escenario adverso (*depletion*) o en
  la P2G, con orden de magnitud en puntos básicos.
- **Bloque nuevo, CASO JST** (`b-caso`): una situación con el supervisor. Estructura fija en cuatro
  frases o párrafos cortos: **qué llega** (pregunta, *flag*, carta), **qué hay detrás** (lo que el
  supervisor está comprobando de verdad), **la respuesta que funciona**, **la que empeora las
  cosas**. Objetivo: al menos uno por capítulo en las Partes III a VI. Es el bloque que responde a
  la petición de "situaciones prácticas".

### Marcado propio de este manual (F3)

```html
<!-- Bloque CASO JST: siempre los cuatro tiempos, en este orden -->
<div class="bloque b-caso">
<span class="etiqueta">Caso JST</span>
<dl>
<dt>Qué llega</dt><dd>…</dd>
<dt>Qué hay detrás</dt><dd>…</dd>
<dt>La respuesta que funciona</dt><dd>…</dd>
<dt>La que empeora las cosas</dt><dd>…</dd>
</dl>
</div>

<!-- Nivel del capítulo, en el h2 -->
<h2 id="cap15">15. Modelos satélite en el ejercicio real <span class="nivel n2">N2</span></h2>

<!-- Cierre de cada parte -->
<div class="objetivos">
<span class="etiqueta">Qué deberías saber hacer ahora</span>
<ul><li>…</li></ul>
</div>
```

**Anclas:** `capN` en cada capítulo, `sN-M` en secciones y `sN-M-K` en subsecciones (la Parte 0 usa
`s0-1`, `s0-1-1`…). Deben coincidir con los `href` de `index.html`. **Etiquetas vacías siempre
autocerradas** (`<hr/>`, `<br/>`): el convertidor de Calibre se rompe sin ellas (lección del IRB).

**Revisión:** `python3 herramientas/revision.py` desde la raíz, tras cada parte. Lista aparte los
ficheros enlazados que aún no existen. **Verificación visual:** capturas con Chrome sin ancla en la
URL (con ancla salen en blanco), en claro y en oscuro (`--blink-settings=preferredColorScheme=1/0`),
en `.capturas/` (fuera de git).

Las reglas del bloque QUÉ VIENE son las del IRB (§5 de su `PROCESO.md`): sin fechas de aplicación
firmes, sin números de norma en negociación, madurez explícita, cerrar con el proyecto que genera.
En este manual pesan más: la metodología del *stress test* cambia en cada ejercicio.

---

## 6. Voz y precisión

Remisión íntegra a §6 del `PROCESO.md` del IRB. Añadidos propios de este manual:

- **Bancos reales:** cada cifra de Santander, BBVA o sus filiales lleva fuente pública y sello
  "(a fecha de…)" en el texto o en nota. Si el dato no es público, no se da.
- **Metodología de un ejercicio concreto:** decir siempre de qué ejercicio se habla (EBA 2025,
  borrador 2027…). Lo que cambia entre ejercicios se escribe como mecanismo, no como regla eterna.
- **Reguladores de fuera de la UE:** describir el ejercicio por sus rasgos (escenario, balance,
  horizonte, marco contable, publicación) antes que por su nombre oficial.
- **Niveles de confianza:** obligatorios en `investigacion/`. En el texto del manual no se ponen
  etiquetas; se aplica la regla de prudencia del IRB (lo no verificado, cualitativo).

---

## 7. Índice provisional (2 niveles)

Pendiente de bajar a 3 niveles en F2 con lo que salga del research.

- **Parte 0 · Cómo usar este manual**
- **Parte I · El mapa** — 1 Qué pregunta responde un *stress test* · 2 Un banco, seis números · 3 Qué hace el supervisor con el resultado
- **Parte II · Marco y actores** — 4 Quién decide qué · 5 Anatomía de un ejercicio EBA · 6 El grupo multi-regulador
- **Parte III · Metodología (I): lo que se aplica hoy** — 7 Punto de partida · 8 Modelos satélite · 9 Transiciones entre etapas · 10 Pérdidas bajo balance estático · 11 *Caps*, *floors* y *challengers* · 12 RWA y CET1 · 13 El *stress test* del ICAAP · 14 *Reverse* y temáticos
- **Parte IV · Metodología (II): retos** — 15 Series cortas y rupturas · 16 No linealidad y colas · 17 *Overlays* · 18 Coherencia entre ejercicios · 19 Climático · 20 *Machine learning*
- **Parte V · Frente al JST** — 21 El ejercicio como proyecto · 22 El ciclo de QA · 23 Situaciones recurrentes · 24 Después del resultado
- **Parte VI · Avanzada** — 25 Arquitectura de grupo · 26 Datos repartidos · 27 Comparabilidad (España vs México) · 28 Cómo compara el supervisor · 29 Lo que viene
- **Parte VII · El oficio** — 30 Tipologías de encargo · 31 Árbol de diagnóstico
- **Anexos de código** — S1 satélite PD/LGD · S2 migración de etapas · S3 traslación de escenario a geografías no UE · S4 puente de comparabilidad · S5 *reverse stress test* · S6 coherencia ICAAP vs EBA
- **Anexos de referencia** — glosario, fuentes y cómo seguir lo que viene, mapa de reguladores por país, calendario tipo, remisiones al manual IRB

**Hilo conductor:** las carteras de consumo y de empresas de una filial mexicana, proyectadas a la
vez en el EBA del grupo y en el ejercicio local. Se reutiliza en caps. 8, 9, 18, 25 y 27 y en S1, S3
y S4, como la hipoteca de 200.000 € en el IRB.

**Relación con el manual IRB:** su cap. 39 es el resumen; este manual es el desarrollo. No se repite
nada de la fórmula IRB, la definición de *default* ni IFRS 9 básico: se remite al capítulo del IRB.

---

## 8. F1 · Plan de research

Una nota por bloque en `investigacion/`, con fecha de consulta y nivel de confianza por afirmación:

1. `eba.md` — nota metodológica 2025; borrador o consulta del 2027 y calendario; reforma del marco del *stress test* europeo; GL de *stress testing* de entidades; GL de SREP.
2. `bce-mus.md` — Guía del ICAAP; Guía de RDARR (2024); metodología de P2G; QA; ejercicios temáticos (climático 2022, *Fit-for-55*, geopolítico).
3. `jers-escenario.md` — escenario adverso y su cobertura de países no UE.
4. `reguladores-no-ue.md` — Fed, BoE/PRA, CNBV/Banxico, BCB, CMF, BDDK, BCRA: tipo de ejercicio, escenario, balance, horizonte, marco contable, publicación, qué filial de Santander/BBVA afecta.
5. `datos-publicos.md` — resultados EBA 2025 de Santander y BBVA, desglose por país del ejercicio de transparencia, resultados publicados por reguladores locales. Materia prima del cap. 27 y de S4.

---

## 9-10. Flujo por parte, anexos y publicación

Mismo método que §8-§10 del `PROCESO.md` del IRB. **Regla heredada: ningún número se publica sin
haberse ejecutado.** Los scripts viven en `anexos/` (dentro del repo) y se ejecutan con
`.venv/bin/python -I anexos/<script>.py` (numpy, pandas, scipy, statsmodels). Las cifras de los
bloques NÚMEROS de la Parte I salen de `anexos/cifras_parte01.py`, `anexos/s1a_satelite.py` y
`anexos/s0_juguete.py`; las de la Parte II, de `anexos/cifras_parte02.py` (solo aritmética sobre datos
públicos de las notas de `investigacion/`, más un ejemplo ilustrativo del SCB promediado); las de la
Parte III-A, de `anexos/s1b_satelite.py` (S1, segunda parte), `anexos/s2_migracion.py` (S2, fórmulas de
los recuadros 3-9), `anexos/s5_reverse.py` (S5) y `anexos/cifras_parte03a.py`. Si se toca un
script, hay que revisar el texto que cita sus cifras.

## 11. Registro de reparto de contenido

> Cuando un capítulo **no** desarrolla algo porque le toca a otro, se anota aquí y se deja remisión
> explícita en el texto.

| Tema | Se menciona en | Se desarrolla en | Nota |
|---|---|---|---|
| P2G: tramos y uso del resultado | §1.1.2, §1.3.3, §2.1.2 | **Cap. 12** | La tabla de tramos vive solo en cap. 12 |
| Previsión perfecta y concentración del primer año | §4.1.3, §8.2.1 | **Cap. 16** | El juguete (§8.2.1) da la intuición y la cifra; cap. 16, la mecánica EBA y los datos reales de 2025 |
| Suelo del REA de partida | §7.1.2, §8.1.3 | **Cap. 19** | El juguete lo aplica |
| Exceso y déficit de provisiones en el ejercicio | §2.2.2 | **Cap. 19** (+ IRB cap. 32) | |
| *Benchmarks* del BCE y +88 pb del QA | §7.2.2 | **Cap. 18** | |
| Variables que faltan en el escenario | §5.2.3 | **Cap. 31** (y anexo S3) | |
| Severidad: acumulado frente a desviación | §5.2, §8.2.2 | **Cap. 32** | Los datos reales de España y México, solo en cap. 32 |
| No linealidad y escenarios fuera de la muestra | §6.1.4, §6.2.1 | **Cap. 23** | El 24,10 / 22,36 / 21,37 % del anexo S1 se puede reutilizar en cap. 23 |
| Signos sin sentido económico | §6.2.2 | **Caps. 15 y 23** | |
| Balance estático frente a dinámico | §7.1.3 | **Caps. 11 y 20** | |
| Fully loaded frente a transitorio | §2.1.3 | **Cap. 12** (uso en la P2G) | Ejemplo de Santander 2025 (12,78 / 12,19 %) ya usado en §2.1.3 |
| Activos fiscales diferidos y fiscalidad del ejercicio | §2.1.6 | **Cap. 19** | |
| SICR sin *backstop* en 2027 | §4.1.4 | **Cap. 16** | |
| Validación de satélites (*backtest*, estabilidad, sensibilidad) | §6.3 | **Caps. 15, 22 y 23** | Las cifras del S1 se pueden reutilizar |
| Ficha de resultados de la EBA | §1.3.4 (Santander) | **Caps. 11.4 y 32** | La base de datos CSV, en cap. 11.4 |
| Organización del ejercicio | §7.2.3 (tabla de dueños) | **Cap. 28** | No repetir la tabla |
| Sensibilidad de supuestos | §8.2.3 | **Caps. 15 y 18** | El "triple que la LGD" es una pieza reutilizable |
| Asimetría del tipo de cambio | §11.1.2 | **Caps. 25 y 31** | En la Parte II solo el mecanismo (párr. 35 y tabla 1) |
| Cambio de perímetro de Polonia | §11.1.3 | **Cap. 31.3.2** | Solo mencionado |
| Criterio de país (inmediato frente a riesgo último) | §11.3.3 | **Caps. 14 y 31** | Ejemplo del préstamo garantizado por la matriz ya usado |
| Comprobación de cuadre ΔProv frente a deterioro (762 M€) | §11.4.2 | **Cap. 32 y S4** | El hueco de los 762 M€ sigue abierto |
| Módulo climático | §11.3.4 | **Caps. 21 y 26** | |
| Comentario público de escenarios y modelos de la Fed | §13.2.1 | **Cap. 34** | |
| Colegios de supervisores; lo que ve el JST | §13.3.3 | **Cap. 33** | |
| Variables nominales en Türkiye (vivienda +128,7 % / −19,3 %) | §13.2.6 | **Cap. 31.2.3** | |
| Provisión local mexicana frente a IFRS 9 | §13.2.3 | **Cap. 32.5.2** | Que la CNBV parte de la provisión local sigue sin verificar |
| Sensibilidad baja del satélite y cómo corregirla | §15.4.3, §21.1.4 | **Cap. 23** | Sensibilidad relativa 0,64 frente al *benchmark* ilustrativo (S1b) reutilizable |
| *Overlays* por stage en el punto de partida | §14.1.2 | **Cap. 24** | |
| Puente ICAAP frente a EBA | §20.3.2 | **Cap. 25 y S6** | |
| Retos del módulo climático | §21.2.2 | **Cap. 26** | |
| Organización y calibración previa frente a pares | §18.2.2 | **Cap. 28** | |
| Ciclo de QA, rondas y nota explicativa | §11.2.3, §18.2.3 | **Cap. 29** | |

### Piezas reutilizables de la Parte I

- **Banco de referencia** (§2.1.4): activo 100.000 M€, RWA 35.000, CET1 4.550 (13,00 %); 1.000 M€ de
  pérdida → −200 pb, −252 pb con RWA +5 %; regla rápida 100 M€ = 20 pb.
- **Satélite del anexo S1**: logit(TD) = −3,514 + 0,215 × paro(t−1) − 0,080 × PIB; elasticidad +1,15 pp
  con paro 3,5 % y +2,53 pp con paro 8 %.
- **Anexo S2 (fórmulas EBA sobre el consumo del juguete)**: adverso 33,83 % (141,5 / 110,0 / 86,8), base
  12,33 %; sin previsión perfecta, primer año 132,6 y total 34,66 %; LRLT S2 54,33 % frente a 48,03 %;
  SICR 1,0 / 1,5 / 2,5 × PD: 30,49 / 33,83 / 39,38 %; S1 del año 3 con 5/6–1/6 37,51 frente a 42,14.
- **Anexo S1b**: PD de consumo México 4,86 → 7,64 / 9,80 / 13,33 %; España (constante recalibrada al
  3,0 %) → 4,41 / 8,05 / 9,14 %; *benchmark* ilustrativo 18,95 % en el año 3; sensibilidad relativa 0,64.
- **Anexo S5**: caída de 300 / 600 / 800 pb con k = 0,83 / 1,06 / 1,19; más plausible para 600 pb:
  paro ×1,10, PIB ×0,96. Suelo del REA: le cuesta 107 pb a la filial (−416 pb sin suelo).
- **Juguete del anexo S0 (hilo conductor)**: consumo 880/70/50 y empresas 950/36/14 M€; adverso
  consumo 34,31 % (base 12,34 %), empresas 4,65 % (base 1,74 %); CET1 de la filial con margen dado
  13,00 → 9,68 → 8,19 → 7,77 % (−523 pb, segundo tramo de P2G si fuera un banco del ejercicio);
  primer año de consumo 141,0 con previsión perfecta y 132,6 sin ella.

### Inventario de bloques QUÉ VIENE

| # | Ubicación | Tema | Revisar |
|---|---|---|---|
| 1 | §0.3.3 | Metaexplicación y dirección del ejercicio europeo | No caduca |
| 2 | §11.2.2 | Ciclo de 2027: borrador, nota final y calendario | Cuando salgan la nota final y el escenario (nov-2026 a ene-2027) |
| 3 | §11.3.5 | Puntos de partida desde FINREP/COREP | Cuando la Comisión adopte la norma técnica |
| 4 | §12.3.3 | P2G bienal (EBA/GL/2026/06) | Tras el primer SREP con las directrices aplicadas |
| 5 | §21.2.3 | Más clima en los próximos ciclos | Con la nota final de 2027 (alcance físico) |
| 6 | §26.4 | Alcance físico del clima fuera del EEE | Con la nota final de 2027 |
| 7 | §27.3 | Reglamento de IA y riesgo de modelo | Calendario de obligaciones de alto riesgo |
| 8 | §31.4.5 | FINREP/COREP como punto de partida, visto desde las filiales | Adopción de la norma técnica |
| 9 | §34.1 | UE: simplificación, integración, clima, P2G bienal | Cada nota final y cada SREP |
| 10 | §34.2 | Fed (SCB promediado, comentario público) y Banco de Inglaterra | Escenarios de la Fed de 2027; anuncio del BCST |

---

## 12. Notas de sesión

- **2026-10-16** — F0. Plan aprobado por Rafa. Creados carpeta, repo (sin remoto), `.gitignore`,
  este archivo y una nota de seguimiento personal. Copiados del IRB
  `estilo.css`, `kindle-eink.css`, `construir_kindle.py` y `generar_portada.py`, **sin adaptar
  todavía** (rutas de Windows). Siguiente: F1.

- **2026-10-16 (cont.)** — F1 hecha en línea, sin subagentes, a petición de Rafa. Cinco notas en
  `investigacion/` y su `README.md` con los siete hallazgos que cambian el plan. Decisión derivada:
  **el ejercicio de referencia del manual es el EBA 2027** (borrador del 11-jun-2026) y el 2025 es el
  último cerrado; las cifras de bancos reales salen del 2025. El desglose por país de las fichas EBA se
  saca con `herramientas/parse_eba_resultados.py`; la asignación de tres bloques IRB sin etiqueta por
  banco está marcada `[Likely]` y hay que verificarla antes de S4. Huecos pendientes, listados al final
  de cada nota: texto vigente de la CNBV, metodología del BCB, CMF/BDDK/BCRA, tramos numéricos de la P2G,
  informe completo del ejercicio geopolítico, cap. 2.4.3 y anexo IV de la nota EBA 2027. Ninguno bloquea
  el índice. Siguiente: F2.

- **2026-10-16 (cont. 2)** — Validación de la F1 con `deep-research` (cinco revisiones en paralelo, una
  por nota, más un informe de síntesis en `investigacion/reports/Validación F1 stress test.md`).
  Las cifras aguantaron; se corrigieron mecanismos y lecturas, y las cinco notas están reescritas con
  las correcciones. Cambios que afectan al índice:
  - **Cap. 27 rehecho como puente en cuatro pasos** (severidad neta de la base, denominador hogares +
    empresas, mezcla frente a intensidad, mecánica EBA frente a local). Tesis nueva: la distancia
    España–México la explican el riesgo de partida y la intensidad por segmento, no el escenario ni la
    mezcla. S4 se construye desde el CSV de la EBA.
  - **Cap. 11 reorientado:** el EBA 2027 no tiene suelos de cobertura; el capítulo es sobre *benchmarks*
    del BCE, comparación entre pares y QA (+88 pb en 2025).
  - Cap. 13 sobre la Guía ICAAP de julio de 2026; cap. 14 con el ejercicio geopolítico como caso central;
    cap. 18 con la asimetría del tipo de cambio; cap. 9 con la desaparición del *backstop* de SICR.
  - Matizar §39.2 del manual IRB: la concentración del deterioro en el primer año la explica sobre todo
    la previsión perfecta.
  Scripts de la validación en `herramientas/validacion_f1/`. Siguiente: F2.

- **2026-10-16 (cont. 3)** — F2. Índice v0.1 (31 capítulos) y, con los comentarios de Rafa, v0.2:
  metodología en una sola parte; hilo conductor mexicano aceptado "de momento"; y **cambio de lector**:
  "un documento que pase de persona con conocimientos en banca pero no en *stress test* a experto; no me
  importan los capítulos sino el contenido", asumiendo en el nivel básico "un conocimiento básico de IRB,
  pero poco más". Consecuencias: nueva Parte I de fundamentos (capital, PD *point-in-time*, IFRS 9,
  escenarios, econometría, la cadena completa y un *stress test* de juguete con anexo S0), tres niveles
  con objetivos por parte, autoevaluación (R6) y casos integrados (R7). La §7 de este archivo queda
  superada por `00-indice-manual-st.md`, que es la referencia.

- **2026-10-16 (cont. 4)** — Índice v0.2 aprobado. F3 hecha: `estilo.css` con acento azul (para
  distinguirlo del IRB), bloque `b-caso` con los cuatro tiempos en `<dl>`, marcas de nivel `n1-n3` y
  recuadro `objetivos`, todo con modo oscuro; `index.html` (portada, niveles, diez bloques, perímetro e
  índice a dos niveles con enlaces a todas las partes); `parte-00.html` (~3.300 palabras, con un primer
  CASO JST sobre citar el borrador en vez de la versión final); `herramientas/revision.py`, ejecutado
  sin errores. Verificado a la vista en claro y en oscuro. Siguiente: F4, Parte I (`parte-01.html`,
  caps. 1-8, la más importante para el nuevo lector).

- **2026-10-16 (cont. 5)** — F4, Parte I escrita (`parte-01.html`, ~8.700 palabras, 7 bloques
  NÚMEROS, todos con cifras ejecutadas). Entorno `.venv` creado. Tres scripts nuevos en `anexos/`:
  `s1a_satelite.py` (primera parte del S1), `s0_juguete.py` (S0) y `cifras_parte01.py`. Decisiones:
  - El satélite sintético lleva una pequeña no linealidad en recesión, para que el ejemplo de §6.2.1
    enseñe el sesgo de estimar sin crisis (con un modelo verdadero lineal no se veía nada).
  - El juguete usa el escenario JERS 2025 real de México, punto de partida común a los dos escenarios,
    suelo del REA de partida y un **margen antes de provisiones dado** (no proyectado, fuera de
    perímetro); sin margen, el CET1 se agotaba y el ejemplo engañaba.
  - Sus cifras caen dentro del rango real del EBA 2025 para México (resto minorista 21,6 % Santander,
    37,7 % BBVA), y el texto lo dice.
  - Capítulos de la Parte I más cortos que los del IRB (~1.100 palabras de media): son fundamentos.
    **Pendiente de que Rafa diga si la profundidad es la adecuada** antes de escribir la Parte II.
  Siguiente: Parte II (`parte-02.html`, caps. 9-13).

- **2026-10-16 (cont. 6)** — Rafa pidió **ampliar la Parte I antes de pasar a la II**. Hecho: de ~8.700 a
  ~12.400 palabras, 12 bloques NÚMEROS, todos ejecutados. Añadidos: §1.3.4 cómo se lee una ficha de
  resultados (Santander, EBA 2025); §2.1.5 distancia a los requerimientos (MDA, cifras ilustrativas) y
  §2.1.6 impuestos; §3.1.5 de TTC a PiT con el desplazamiento de Vasicek (PD TTC 2 %, ρ 0,15: 0,41 /
  1,30 / 3,53 / 8,27 % para Z = +1/0/−1/−2), §3.2.3 cómo se estima una matriz, §3.2.4 tasas anuales y
  trimestrales; §4.1.4 SICR en la práctica, §4.2.2 estructura temporal y previsión perfecta (PD a vida
  14,13 % plana frente a 24,30 % con senda adversa; provisión 63,6 frente a 109,4); §5.1.4 cómo se
  construye un adverso, ecuaciones puente y §5.2.4 lista de lectura; §6.1.5 cómo se elige un satélite y
  §6.3 validación (*backtest*: pico observado 13,85 % frente a 12,24 % proyectado; estabilidad del
  coeficiente del paro 0,198 / 0,230 / 0,236; sensibilidad a una desviación típica); §7.1.4
  descomposición del BCE de 2025 (8,1 pp brutos: 5,0 provisiones, 1,1 APR, 1,3 mercado, ~0,6
  operacional; 4,8 de ingresos); §7.2.3 dueños de cada eslabón; §8.2.3 sensibilidad del juguete (el
  coeficiente del paro ±20 % mueve −7,03 / +7,60 pp, el triple que la LGD). Scripts ampliados:
  `cifras_parte01.py` (Vasicek, frecuencias, estructura temporal), `s1a_satelite.py` (validación) y
  `s0_juguete.py` (función `sensibilidad()`). Índice de trabajo pasado a v0.3 con las subsecciones
  nuevas. Revisión automática sin errores. **Siguiente: Parte II (`parte-02.html`, caps. 9-13).**

- **2026-10-17** — F4, Parte II escrita (`parte-02.html`, caps. 9-13, ~14.100 palabras, nivel N2). Bloques:
  4 NÚMEROS, 3 NORMA, 3 QUÉ VIENE, 3 TRAMPA, 1 MARGEN, 1 PALANCA, 1 POR QUÉ, 1 DEFENSA y 1 CASO JST
  (12.2.3, envío tardío y con errores). Script nuevo `anexos/cifras_parte02.py`: Santander en tres
  ejercicios (173 / 90 / 510 pb; holguras de 380 y 280 pb), cuadre ΔProv frente a deterioro (762 M€ en
  Santander, 1 M€ en BBVA), tramos de P2G, palanca de 50 pb en el corte de 3 pp (175 M€ de CET1, 250 M€
  antes de impuestos), media de comparables de BBVA (227,8 / 200,0 pb; BBVA 186 pb a fin de 2027 frente
  a 218 de máximo), QA +88 pb (+28,6 %) y SCB promediado ilustrativo (salto medio 1,30 frente a 0,27 pp).
  Decisiones:
  - Todo lo `[Likely]` o `[Guessing]` de las notas va en cualitativo o con la cautela explícita (anexo
    12-D de la CUB, CNBV sobre provisión local, BDDK y NIC 29 en 2025 "según la prensa", vigencia del
    régimen argentino, origen de los 762 M€).
  - Sin datos reales de España frente a México: quedan para el cap. 32, según el registro de reparto.
  - Citas de normativa: art. 32.2 del Reglamento 1093/2010, arts. 100 y 104 ter de la CRD, EBA/GL/2026/06
    y EBA/GL/2018/04. Colegios de supervisores sin número de artículo.
  - Verificada a la vista en claro y en oscuro (capturas en `.capturas/p02-*`). `revision.py` en OK.
  Siguiente: Parte III-A (`parte-03a.html`, caps. 14-21).

- **2026-10-17 (cont.)** — F4, Parte III-A escrita (`parte-03a.html`, caps. 14-21, ~14.900 palabras, N2).
  Bloques: 10 NÚMEROS, 8 CASO JST (uno por capítulo; el del cap. 19, «Sus activos ponderados bajan en el
  adverso», es nuevo y se ha añadido al índice como 19.1.5), 3 CÓDIGO, 2 PALANCA, 2 DEFENSA, 2 TRAMPA,
  1 MARGEN y 1 QUÉ VIENE. Fuente primaria: el capítulo 2 de la nota EBA 2027 en borrador, leído entero
  (párrafos y recuadros citados con su número); capítulo 6.4 para impuestos y dividendos. Anexos nuevos
  ejecutados: `s1b_satelite.py`, `s2_migracion.py`, `s5_reverse.py` y `cifras_parte03a.py`. Decisiones:
  - Los *benchmarks* del BCE no son públicos: el contraste de S1b usa un *benchmark* ilustrativo (otro
    satélite más sensible al paro) y el texto lo dice cada vez.
  - S2 aplica literalmente las fórmulas de los recuadros 3-9 y da 33,83 % frente al 34,31 % del juguete;
    el texto explica la diferencia (el juguete simplificaba).
  - Matiz al manual IRB §39.2 hecho en la TRAMPA §16.3.3 (previsión perfecta, no migración).
  - Quitada una inferencia `[Guessing]` (que el ajuste del QA se concentró en crédito).
  `revision.py` en OK; verificada a la vista en claro y en oscuro (`.capturas/p03a-*`).
  Siguiente: Parte III-B (`parte-03b.html`, caps. 22-27, N3).

- **2026-10-17 (cont. 2)** — Rafa fijó como objetivo terminar el manual tomando las decisiones y publicarlo
  en un repositorio **público** de su GitHub. Hecho en esta sesión:
  - Parte III-B (caps. 22-27), Parte IV (28-30), Parte V (31-34) y Parte VI (35-36). Anexos nuevos
    ejecutados: `s3_traslacion.py`, `s4_puente.py` (embebe las tablas validadas del CSV de la EBA y reproduce
    el −0,26 / +7,64 de mezcla e intensidad), `s6_coherencia.py`, `cifras_parte03b.py`, `cifras_parte04.py` y
    `cifras_parte05.py`.
  - `anexos-codigo.html` se genera ejecutando todos los anexos (`herramientas/generar_anexos_codigo.py`);
    `anexos-referencia.html` con glosario, fuentes, mapa, calendario, remisiones al IRB, autoevaluación y casos.
  - F7: `generar_portada.py` rehecho (motivo: CET1 de la filial del juguete en el adverso) y
    `construir_kindle.py` adaptado a Mac y a este manual (enlaces sin ancla, ids duplicados). AZW3 y EPUB
    generados con Calibre 9.14 sin avisos.
  - Decisiones: las Partes III-B a VI son más concisas que las II y III-A (de 1.000 a 1.500 palabras por
    capítulo), porque son de nivel 3 y remiten a la metodología ya explicada; el S4 no descarga el CSV de la EBA
    (las cifras están validadas y el camino para regenerarlas está en `herramientas/validacion_f1/`);
    `herramientas/parse_eba_resultados.py` movido a `herramientas/obsoleto/`. Sin licencia formal, como el
    manual IRB («material educativo»).
  - Huecos abiertos que siguen en las notas de `investigacion/`: nota final y escenario del EBA 2027, anexo de
    lineamientos de la CUB, BCCh, BDDK, BCRA y el origen de los 762 M€ de Santander.
