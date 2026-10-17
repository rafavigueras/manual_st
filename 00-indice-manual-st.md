# Manual de Stress Test de Riesgo de Crédito para Grupos Bancarios Internacionales
## Índice detallado — versión de trabajo v0.4 (v0.2 aprobada el 2026-10-16)

**Objetivo:** llevar a una persona que conoce la banca y el IRB en lo básico, pero no el *stress test*, hasta el nivel de experto: alguien capaz de proyectar, revisar y defender ante el JST las pérdidas de crédito de un gran grupo con filiales fuera de la UE.
**Lo que se asume:** banca general y un IRB básico (qué son la PD, la LGD, la EAD, el RWA y el CET1, y que la fórmula IRB convierte parámetros en capital). **Nada más:** ni IFRS 9, ni escenarios macro, ni econometría, ni el propio *stress test*. Todo eso se construye aquí.
**Perímetro:** riesgo de crédito en los ejercicios de *stress test*: pérdidas, provisiones y RWA de crédito, y su llegada al CET1. Ejercicio europeo (EBA/BCE), *stress test* del ICAAP, ejercicios temáticos y ejercicios locales de las filiales fuera de la UE.
**Fuera de perímetro:** NII, mercado y contraparte, operacional y conducta, comisiones, liquidez. Ganchos de remisión donde tocan al crédito.
**Jurisdicción:** MUS/EBA como columna vertebral; Fed, Banco de Inglaterra, CNBV/Banxico, BCB, CMF, BDDK y BCRA como segunda capa, a través de las filiales de Santander y BBVA.
**Ejercicio de referencia:** EBA 2027 (borrador metodológico del 11-jun-2026). El EBA 2025 es el último cerrado y la fuente de las cifras reales.
**Principio editorial:** el del manual IRB: qué problema resuelve cada regla, a qué obliga, dónde deja margen y qué se hace con ese margen frente al supervisor. **Lo que manda es la progresión del contenido, no el número de capítulos.**
**Relación con el manual IRB:** el manual es autocontenido para su lector. Las remisiones al IRB son para profundizar, nunca para entender.

---

## Convenciones del manual

### Bloques marcados

| Marca | Contenido |
|---|---|
| **[NORMA]** | Referencia exacta y qué exige en una frase |
| **[POR QUÉ]** | Qué falló o qué se quiso conseguir |
| **[MARGEN]** | Discrecionalidad, silencio normativo, zona gris |
| **[PALANCA]** | Impacto en la caída de CET1 del adverso o en la P2G, con orden de magnitud en pb |
| **[TRAMPA]** | Error frecuente, hallazgo típico del QA |
| **[NÚMEROS]** | Ejemplo trabajado de principio a fin |
| **[CÓDIGO]** | Remisión al anexo ejecutable |
| **[DEFENSA]** | Cómo se argumenta ante el JST, validación o auditoría |
| **[QUÉ VIENE]** | Cambio en curso, sin fechas firmes ni números de norma en negociación |
| **[CASO JST]** | Situación con el supervisor: qué llega, qué hay detrás, la respuesta que funciona y la que empeora las cosas |

### Tres niveles

Cada capítulo lleva su nivel. Se puede leer por orden o por nivel.

| Nivel | Quién es al terminar | Partes |
|---|---|---|
| **N1 · Fundamentos** | Entiende un *stress test* de crédito de principio a fin y lo ha hecho en pequeño | 0 y I |
| **N2 · Practicante** | Puede trabajar en el equipo de proyección de un ejercicio real sin que le expliquen la mecánica | II y III-A |
| **N3 · Experto** | Diagnostica, mejora y defiende ante el JST los números de un grupo internacional | III-B, IV, V y VI |

Cada parte termina con **"Qué deberías saber hacer ahora"** y una autoevaluación corta (anexo R6).

### Hilo conductor

Las carteras de consumo y de empresas de una filial mexicana, proyectadas a la vez en el EBA del grupo y
en el ejercicio local de la CNBV. Nace en miniatura en el cap. 8 (el *stress test* de juguete) y crece
hasta el puente España–México del cap. 32. Se calibra con las tasas reales por segmento del EBA 2025.

---

# PARTE 0 — Cómo usar este manual

### 0.1 Para quién es
- 0.1.1 Lo que se asume y lo que no (prueba de entrada en el anexo R6)
- 0.1.2 Lo que este manual no es: ni una guía del ejercicio de un año ni un curso de econometría
- 0.1.3 La meta: de "sé lo que es una PD" a "sé defender ante el JST por qué mi pérdida es esta"

### 0.2 Rutas
- 0.2.1 La ruta completa: de N1 a N3
- 0.2.2 Incorporación urgente a un ejercicio en marcha (qué leer en la primera semana)
- 0.2.3 Por rol: proyección, validación, coordinación con el JST, filial no UE
- 0.2.4 Modo referencia: buscar desde el problema

### 0.3 Cómo trabajar con las fuentes
- 0.3.1 Los documentos de cabecera: nota metodológica, plantillas, Q&A, escenario JERS, directrices de SREP
- 0.3.2 Borrador, final, Q&A y fe de erratas: no trabajar con la versión equivocada
- 0.3.3 **[QUÉ VIENE]** Qué partes caducan con cada ciclo

---

# PARTE I — Fundamentos [N1]

> Al terminar: entiendes qué es un *stress test* de crédito, sabes leer un escenario, entiendes por qué
> un escenario mueve provisiones y capital, y has hecho uno completo en una hoja.

## Capítulo 1 — Qué es un *stress test* y para qué sirve

### 1.1 La idea
- 1.1.1 Una pregunta "¿y si…?" aplicada al balance
- 1.1.2 Por qué existe: lo que enseñaron 2008 y la crisis soberana
- 1.1.3 Tres preguntas distintas: cuánto pierdo, qué tendría que pasar, si mis modelos responden

### 1.2 Lo que no es
- 1.2.1 No es una previsión ni tiene probabilidad
- 1.2.2 En la UE no es un examen de aprobado o suspenso
- 1.2.3 **[TRAMPA]** Comunicar a la dirección un "umbral" que no existe

### 1.3 Las piezas de cualquier ejercicio
- 1.3.1 Escenario, punto de partida, supuestos de balance, horizonte y métrica
- 1.3.2 Quién proyecta: el banco o el supervisor
- 1.3.3 Qué hace alguien con el resultado
- 1.3.4 Cómo se lee una ficha de resultados (Santander, EBA 2025)

## Capítulo 2 — El capital que se mueve: lo justo para un *stress test*

### 2.1 Del IRB que ya sabes al ratio que se estresa
- 2.1.1 Numerador y denominador: qué mueve el CET1 y qué mueve el RWA
- 2.1.2 La pila de requerimientos: mínimos, P2R, colchones, P2G
- 2.1.3 *Fully loaded* frente a transitorio, y por qué el supervisor mira el primero
- 2.1.4 **[NÚMEROS]** Un banco de 100.000 M€: cómo 1.000 M€ de pérdidas se convierten en puntos básicos
- 2.1.5 La distancia a los requerimientos (MDA)
- 2.1.6 Impuestos y otros detalles que mueven el número

### 2.2 Pérdida esperada regulatoria frente a provisión contable
- 2.2.1 Por qué hay dos números de pérdida
- 2.2.2 Exceso y déficit: cuándo una provisión mueve el CET1 y cuándo no (profundizar: manual IRB, cap. 32)

## Capítulo 3 — Del parámetro regulatorio al parámetro del *stress test*

### 3.1 Dos filosofías de PD
- 3.1.1 *Through-the-cycle* (lo que conoces del IRB) frente a *point-in-time*
- 3.1.2 Por qué un *stress test* necesita PD y LGD *point-in-time*
- 3.1.3 *Downturn* LGD no es LGD estresada
- 3.1.4 **[TRAMPA]** Proyectar con la PD regulatoria
- 3.1.5 Cómo se pasa de TTC a PiT: desplazamiento de Vasicek, escalado, transiciones **[NÚMEROS]**

### 3.2 De la tasa de *default* a la tasa de transición
- 3.2.1 Qué es una matriz de transición
- 3.2.2 Tasas de transición entre stages y tasas de pérdida
- 3.2.3 **[NÚMEROS]** Una matriz de tres estados, a mano; cómo se estima una matriz (cohortes)
- 3.2.4 Tasas anuales y trimestrales **[TRAMPA]**

## Capítulo 4 — Provisiones IFRS 9: lo imprescindible para un *stress test*

### 4.1 La lógica
- 4.1.1 Pérdida esperada contable: a 12 meses o a toda la vida
- 4.1.2 Los tres stages y qué los dispara (SICR, *credit-impaired*)
- 4.1.3 Escenarios ponderados en el modelo contable y escenario único en el *stress test*
- 4.1.4 El SICR en la práctica

### 4.2 Por qué un escenario mueve tanto las provisiones
- 4.2.1 El salto de 12 meses a vida: el efecto acantilado
- 4.2.2 **[NÚMEROS]** 1.000 M€ que pasan de stage 1 a stage 2
- 4.2.3 La estructura temporal de la PD y la previsión perfecta **[NÚMEROS]**
- 4.2.4 Lo que no hace falta saber de IFRS 9 para trabajar en un *stress test* (y dónde está si lo necesitas)

## Capítulo 5 — Escenarios macro: leerlos y entenderlos

### 5.1 Qué es un escenario
- 5.1.1 Variables, sendas, horizonte; base y adverso
- 5.1.2 Narrativa y calibración: de un relato a unas cifras
- 5.1.3 Niveles, tasas, acumulados y desviaciones frente a la base
- 5.1.4 Cómo se construye un adverso

### 5.2 Leer una tabla del escenario de la JERS
- 5.2.1 **[NÚMEROS]** España y México en el adverso de 2025: PIB, paro, vivienda, tipo de cambio
- 5.2.2 **[TRAMPA]** Comparar severidad sin fijar la métrica
- 5.2.3 Variables que el escenario no trae y hay que derivar: ecuaciones puente
- 5.2.4 Una lista para leer cualquier escenario

## Capítulo 6 — Econometría mínima para modelos satélite

### 6.1 Las herramientas
- 6.1.1 Regresión con series temporales: lo que cambia frente a una regresión normal
- 6.1.2 Tasas como variable dependiente: transformaciones logit y probit
- 6.1.3 Retardos, tendencias y estacionariedad, sin teoría de más
- 6.1.4 Leer una elasticidad: "un punto de paro son tantos puntos de tasa de *default*"
- 6.1.5 Cómo se elige un satélite

### 6.2 Lo que suele salir mal
- 6.2.1 Pocas observaciones y pocas recesiones
- 6.2.2 Signos que no tienen sentido económico
- 6.2.3 **[NÚMEROS]** Un satélite estimado sobre veinte años de datos sintéticos
- 6.2.4 **[CÓDIGO]** Anexo S1 (primera parte)

### 6.3 Cómo se valida un satélite
- 6.3.1 *Backtest* fuera de muestra
- 6.3.2 Estabilidad
- 6.3.3 Sensibilidad **[NÚMEROS]** **[DEFENSA]**

## Capítulo 7 — Cómo se estresa el riesgo de crédito: la cadena completa

### 7.1 La cadena
- 7.1.1 Escenario → parámetros → flujos entre stages → provisiones → resultados → CET1
- 7.1.2 Y en paralelo: parámetros → RWA
- 7.1.3 Balance estático: por qué se congela el banco
- 7.1.4 De dónde sale la caída en un ejercicio real (descomposición del BCE, 2025) **[NÚMEROS]**

### 7.2 Dónde están las decisiones
- 7.2.1 Qué es mecánico y qué es criterio
- 7.2.2 Dónde mira el supervisor
- 7.2.3 Quién es dueño de cada eslabón
- 7.2.4 **[CASO JST]** La proyección que no es monótona

## Capítulo 8 — Un *stress test* de juguete, de principio a fin

### 8.1 El caso
- 8.1.1 Una cartera de consumo y otra de empresas de una filial mexicana (inicio del hilo conductor)
- 8.1.2 Escenario base y adverso de tres años
- 8.1.3 Satélite, matriz, provisiones, RWA y CET1, paso a paso

### 8.2 Leer el resultado
- 8.2.1 Por qué el primer año pesa más
- 8.2.2 Qué variable explica la mayor parte de la pérdida
- 8.2.3 **[CÓDIGO]** Anexo S0
- 8.2.4 Qué supuesto mueve más el resultado: sensibilidad **[NÚMEROS]**
- 8.2.5 Qué deberías saber hacer ahora (cierre de N1)

---

# PARTE II — El mapa y los actores [N2]

> Al terminar: sabes qué ejercicios hace un gran grupo, quién decide cada cosa, cómo es un ejercicio EBA
> por dentro y qué hacen el supervisor europeo y los locales con el resultado.

## Capítulo 9 — Un banco, seis números

### 9.1 La familia de ejercicios de un gran grupo
- 9.1.1 Ejercicio europeo (EBA/BCE)
- 9.1.2 *Stress test* del ICAAP y su *reverse*
- 9.1.3 Escenarios del plan de recuperación
- 9.1.4 Escenarios de IFRS 9 (y por qué no son un *stress test*)
- 9.1.5 Ejercicios macroprudenciales *top-down*
- 9.1.6 Ejercicios locales de las filiales fuera de la UE

### 9.2 Por qué no coinciden
- 9.2.1 Escenarios, balances y métricas distintas
- 9.2.2 **[NÚMEROS]** Santander en 2025-2026: −173 pb en el EBA, SHUSA −0,9 pp en la Fed, Santander UK −5,1 pp en el Banco de Inglaterra
- 9.2.3 **[DEFENSA]** Explicar a un consejo que el mismo grupo "aguanta" de cinco maneras
- 9.2.4 **[TRAMPA]** Equipos separados, satélites distintos

## Capítulo 10 — Quién decide qué

### 10.1 Los actores
- 10.1.1 EBA: metodología, plantillas, Q&A, publicación
- 10.1.2 JERS y BCE: los escenarios
- 10.1.3 BCE/MUS y el JST: QA, *benchmarks* y SREP
- 10.1.4 Banco de España y autoridades nacionales

### 10.2 La base normativa
- 10.2.1 **[NORMA]** Mandato del ejercicio europeo y test supervisor anual de la CRD
- 10.2.2 **[NORMA]** Directrices de SREP y *stress testing* supervisor (EBA/GL/2026/06)
- 10.2.3 **[NORMA]** Directrices de *stress testing* de las entidades (EBA/GL/2018/04)
- 10.2.4 **[MARGEN]** Lo que la nota no regula y se resuelve en Q&A

### 10.3 De dónde sale el escenario
- 10.3.1 Cómo se construye el adverso; el base de los países no UE sale del FMI
- 10.3.2 Qué hay por país y qué falta

## Capítulo 11 — Anatomía de un ejercicio EBA

### 11.1 Rasgos estructurales
- 11.1.1 *Bottom-up* restringido con elementos *top-down*
- 11.1.2 Balance estático: sustitución, sin *workout*, sin curas, sin crecimiento
- 11.1.3 Perímetro, pro forma y la lista cerrada de eventos
- 11.1.4 Modelos admitidos y la excepción del cambio de enfoque

### 11.2 Calendario y entregas
- 11.2.1 Del borrador a la publicación
- 11.2.2 **[QUÉ VIENE]** El ciclo 2027, sin fechas firmes
- 11.2.3 Plantillas, guía y nota explicativa

### 11.3 Qué cambia de 2025 a 2027
- 11.3.1 Menos datos y plantillas que imitan FINREP/COREP
- 11.3.2 NII etiquetado como *top-down*; titulizaciones a proyección propia
- 11.3.3 Fin del *backstop* de SICR; S3 deja de ser NPE; nuevo criterio de país
- 11.3.4 El módulo climático
- 11.3.5 **[QUÉ VIENE]** Puntos de partida desde FINREP/COREP en 2029

### 11.4 Publicación
- 11.4.1 Qué se publica banco a banco
- 11.4.2 La base de datos CSV de la EBA como herramienta

## Capítulo 12 — Qué hace el supervisor con el resultado

### 12.1 De la caída de capital a la P2G
- 12.1.1 Los dos pasos del BCE
- 12.1.2 La tabla de tramos (0-3 / 3-6 / 6-9 / >9 pp) y sus rangos
- 12.1.3 P2G de apalancamiento
- 12.1.4 **[PALANCA]** Por qué 50 pb pueden no mover la P2G y otros 50 sí
- 12.1.5 **[NÚMEROS]** Santander y BBVA en el tramo 1, y lo que eso no dice

### 12.2 La parte cualitativa
- 12.2.1 Calidad de datos, cooperación y puntualidad
- 12.2.2 Del *stress test* al Elemento 2 del SREP y a la P2R
- 12.2.3 **[CASO JST]** "Su envío ha sido tardío y con errores"

### 12.3 Más allá del SREP
- 12.3.1 Distribuciones, planificación de capital y apetito de riesgo
- 12.3.2 P2G no vinculante y lo que pide la Guía ICAAP 2026
- 12.3.3 **[QUÉ VIENE]** P2G bienal
- 12.3.4 Contraste: el SCB de la Fed, vinculante y promediado

## Capítulo 13 — El grupo multi-regulador

### 13.1 Tres familias de ejercicio
- 13.1.1 El banco proyecta con escenarios o parámetros del supervisor
- 13.1.2 El supervisor proyecta con sus modelos
- 13.1.3 Mixto, con acciones de gestión

### 13.2 Fichas por jurisdicción
- 13.2.1 EE. UU.: Fed, SCB y comentario público
- 13.2.2 Reino Unido: el *Bank Capital Stress Test* bienal
- 13.2.3 México: CNBV y Banxico
- 13.2.4 Brasil: test macro del BCB, ICAAP local y Resolución CMN 4.966
- 13.2.5 Chile: IAPE e IEF
- 13.2.6 Türkiye y Argentina: ISEDES, IAC y NIC 29

### 13.3 Lo que no se compara sin traducir
- 13.3.1 Métricas: CET1 FL, ICAP, IB/IPR1/ICP
- 13.3.2 **[TRAMPA]** El "10,5 %" de México y el de Brasil
- 13.3.3 Colegios de supervisores

---

# PARTE III — Metodología: de lo que se aplica hoy a los retos

> Bloque A [N2]: la metodología vigente, al nivel de quien la ejecuta. Bloque B [N3]: los problemas
> abiertos y cómo se resuelven en un proyecto. Al terminar: puedes construir, revisar y criticar las
> proyecciones de crédito de un ejercicio real.

## Bloque A — La metodología que se aplica hoy [N2]

## Capítulo 14 — El punto de partida

### 14.1 Perímetro y fuentes
- 14.1.1 Coste amortizado en pérdidas; perímetro COREP en RWA
- 14.1.2 Dos puntos de partida (2025 y 2026)
- 14.1.3 Conciliación con FINREP y COREP

### 14.2 Clasificación
- 14.2.1 Stages, *credit-impaired* y POCI
- 14.2.2 Sectores, países y el umbral del 0,5 % NACE
- 14.2.3 País inmediato frente a riesgo último

### 14.3 Parámetros de partida *point-in-time*
- 14.3.1 Del modelo de provisiones al parámetro del ejercicio
- 14.3.2 Aproximaciones históricas: "solo más conservador"
- 14.3.3 **[CASO JST]** "Sus PD de partida están por debajo de sus pares"

## Capítulo 15 — Modelos satélite en el ejercicio real

### 15.1 Qué se le pide a un satélite
- 15.1.1 Solidez econométrica y sensibilidad: los estándares mínimos
- 15.1.2 Nivel de modelización: grado, cartera, sector

### 15.2 La jerarquía de enfoques
- 15.2.1 Satélites propios por delante de los *benchmarks* del BCE
- 15.2.2 La regla del 10 % de la clase pivote
- 15.2.3 La elección inicial no se cambia
- 15.2.4 **[MARGEN]** La mezcla justificada de modelo y *benchmark*

### 15.3 LGD bajo escenario
- 15.3.1 Garantías, vivienda e inmobiliario comercial
- 15.3.2 Cura implícita, costes y tiempo en *default*
- 15.3.3 **[NÚMEROS]** Hilo conductor: el consumo mexicano bajo el adverso JERS
- 15.3.4 **[CÓDIGO]** Anexo S1 (segunda parte)

### 15.4 Sectores y divisa
- 15.4.1 Sensibilidades sectoriales y reparto por VAB o por tamaño
- 15.4.2 Préstamos en divisa: el umbral del 5 %
- 15.4.3 **[CASO JST]** "Sus satélites no responden al PIB del escenario"

## Capítulo 16 — Transiciones entre stages, entradas en S3 y curas

### 16.1 La mecánica del ejercicio
- 16.1.1 Flujos permitidos y sin curas desde S3
- 16.1.2 Matrices *point-in-time*
- 16.1.3 Previsión perfecta y reversión a seis años

### 16.2 SICR sin *backstop*
- 16.2.1 Qué desaparece en 2027
- 16.2.2 El criterio contable de cada banco como fuente de dispersión
- 16.2.3 **[CASO JST]** "Su stage 2 crece la mitad que el de sus pares"

### 16.3 El efecto de primer año
- 16.3.1 Por qué el deterioro se concentra en el primer año
- 16.3.2 **[NÚMEROS]** Santander y BBVA en 2025
- 16.3.3 **[TRAMPA]** Atribuirlo a la migración de stages cuando es la previsión perfecta
- 16.3.4 **[CÓDIGO]** Anexo S2

## Capítulo 17 — Pérdidas y provisiones bajo balance estático

### 17.1 Las fórmulas prescritas
- 17.1.1 Nuevos S3 y su provisión
- 17.1.2 S1 y S2 a 12 meses y a vida
- 17.1.3 El suelo implícito del S3 antiguo
- 17.1.4 El último año y la ponderación 5/6 – 1/6

### 17.2 Exposición
- 17.2.1 Sustitución de lo que vence
- 17.2.2 Fuera de balance
- 17.2.3 Soberanos: parámetros prescritos

### 17.3 Leer los resultados
- 17.3.1 Del stock de provisiones al deterioro en resultados
- 17.3.2 **[TRAMPA]** Leer el S3 de 2027 como una tasa de mora
- 17.3.3 **[CASO JST]** "Su cobertura de S3 baja en el adverso"

## Capítulo 18 — *Benchmarks*, pares y QA

### 18.1 Lo que no hay
- 18.1.1 Sin suelos de cobertura ni de LGD
- 18.1.2 Los únicos suelos: REA de partida y titulizaciones

### 18.2 Los *benchmarks* del BCE
- 18.2.1 Qué son y cuándo son obligatorios
- 18.2.2 Enviar antes de ver el *benchmark*
- 18.2.3 **[PALANCA]** El QA de 2025 sumó 88 pb a la caída del sistema

### 18.3 La comparación entre pares
- 18.3.1 Estadísticas de la EBA y análisis horizontal
- 18.3.2 **[CASO JST]** "Su proyección es demasiado optimista"
- 18.3.3 **[DEFENSA]** Cuándo se defiende el modelo propio y cuándo se acepta el *benchmark*

## Capítulo 19 — RWA bajo estrés y llegada al CET1

### 19.1 RWA
- 19.1.1 Migración de grados coherente con los *defaults*
- 19.1.2 *Default* en IRB: LGD regulatoria menos ELBE
- 19.1.3 Reestimación de parámetros, suelos y escalares
- 19.1.4 Suelo del REA y *output floor*
- 19.1.5 **[CASO JST]** "Sus activos ponderados bajan en el adverso"

### 19.2 Al CET1
- 19.2.1 Pérdida esperada regulatoria, exceso y déficit
- 19.2.2 Impuestos y dividendos en el ejercicio
- 19.2.3 Lo que aportan los demás riesgos (remisión)
- 19.2.4 **[NÚMEROS]** Descomponer una caída de CET1

## Capítulo 20 — El *stress test* del ICAAP

### 20.1 Lo que pide la Guía ICAAP de 2026
- 20.1.1 Perspectiva normativa y económica
- 20.1.2 Escenarios propios, más severos y específicos
- 20.1.3 *Management buffer* y P2G

### 20.2 Balance dinámico y acciones de gestión
- 20.2.1 Plan de negocio bajo estrés
- 20.2.2 Acciones creíbles y acciones de papel
- 20.2.3 **[CASO JST]** "Su plan crece en plena crisis"

### 20.3 Coherencia con el ejercicio europeo
- 20.3.1 Mismos modelos, distintos supuestos
- 20.3.2 **[DEFENSA]** Por qué el ICAAP sale distinto del EBA

## Capítulo 21 — *Reverse stress test* y ejercicios temáticos

### 21.1 *Reverse stress test*
- 21.1.1 Del umbral al escenario
- 21.1.2 El ejercicio geopolítico del BCE de 2026
- 21.1.3 Canales de transmisión
- 21.1.4 **[CASO JST]** El catálogo de incoherencias del BCE
- 21.1.5 **[CÓDIGO]** Anexo S5

### 21.2 Clima
- 21.2.1 El climático de 2022 y *Fit-for-55*
- 21.2.2 El módulo climático del EBA 2027
- 21.2.3 **[QUÉ VIENE]** Más clima en los próximos ciclos

## Bloque B — Retos metodológicos y cómo abordarlos [N3]

## Capítulo 22 — Series cortas y rupturas estructurales
- 22.1 El problema: pocas recesiones; pandemia, moratorias y avales; el ciclo de tipos
- 22.2 Cómo se aborda: ventanas, tratamiento de periodos atípicos, información externa
- 22.3 **[CASO JST]** "Su modelo se estima sin la pandemia"

## Capítulo 23 — No linealidad, colas y escenarios fuera de la muestra
- 23.1 El problema: elasticidades de tiempos normales; escenarios fuera del rango
- 23.2 Cómo se aborda: especificaciones no lineales; contraste con *benchmarks* y episodios históricos
- 23.3 **[CASO JST]** "Su sensibilidad es la mitad que en 2008"

## Capítulo 24 — Ajustes de experto y *overlays*
- 24.1 Cuándo son legítimos; *overlays* por stage en las plantillas
- 24.2 Documentación: cuantificación, dirección, reversión
- 24.3 **[TRAMPA]** El *overlay* que solo baja la pérdida
- 24.4 **[CASO JST]** "Su *overlay* no tiene soporte cuantitativo"

## Capítulo 25 — Coherencia entre ejercicios
- 25.1 Dónde se rompe: EBA, ICAAP, IFRS 9, recuperación, locales; satélites distintos; la asimetría del tipo de cambio
- 25.2 Cómo se gobierna: inventario de modelos y usos
- 25.3 **[NÚMEROS]** La misma cartera mexicana en tres ejercicios
- 25.4 **[CÓDIGO]** Anexo S6
- 25.5 **[CASO JST]** "¿Por qué su ICAAP pierde menos que su EBA?"

## Capítulo 26 — Clima: horizontes largos y datos que no existen
- 26.1 El problema: décadas frente a tres años; el dato que falta
- 26.2 Cómo se aborda: *proxies* trazables; del choque climático al VAB y al crédito
- 26.3 **[CASO JST]** "Su *proxy* no es trazable"
- 26.4 **[QUÉ VIENE]** El alcance físico fuera del EEE

## Capítulo 27 — *Machine learning* en modelos satélite
- 27.1 Dónde aporta y dónde no
- 27.2 Cómo se defiende: *challenger* frente a principal
- 27.3 **[QUÉ VIENE]** Reglamento de IA y riesgo de modelo
- 27.4 **[CASO JST]** "No entendemos por qué su modelo responde así"

---

# PARTE IV — El ejercicio frente al JST: situaciones prácticas [N3]

> Al terminar: sabes cómo se organiza un ejercicio, cómo funciona el QA y cómo responder a lo que llega.

## Capítulo 28 — El ejercicio como proyecto

### 28.1 Organización
- 28.1.1 Planificación, riesgos, finanzas y filiales: quién hace qué
- 28.1.2 Equipos mixtos internos y externos
- 28.1.3 El calendario real de nueve meses y sus picos

### 28.2 Preparación
- 28.2.1 *Gap analysis* de datos y herramientas
- 28.2.2 Simulación previa de impactos y posición frente a pares
- 28.2.3 **[TRAMPA]** Modelizar antes de cerrar el punto de partida

## Capítulo 29 — El ciclo de QA

### 29.1 Cómo funciona
- 29.1.1 Envíos, controles automáticos y rondas
- 29.1.2 *Flags*, preguntas y plazos
- 29.1.3 La nota explicativa como pieza de defensa

### 29.2 Cómo se responde
- 29.2.1 Clasificar el *flag*: dato, método o criterio
- 29.2.2 **[DEFENSA]** La escalera argumental aplicada al QA
- 29.2.3 **[CASO JST]** El reenvío de última hora

## Capítulo 30 — Situaciones recurrentes

### 30.1 Catálogo
- 30.1.1 **[CASO JST]** La proyección por debajo del *benchmark*
- 30.1.2 **[CASO JST]** El punto de partida que no cuadra con FINREP
- 30.1.3 **[CASO JST]** El *overlay* que no se compra
- 30.1.4 **[CASO JST]** La filial que trae su propio modelo
- 30.1.5 **[CASO JST]** La nota explicativa que no explica
- 30.1.6 **[CASO JST]** El cambio de perímetro a mitad de ejercicio

### 30.2 Patrones
- 30.2.1 Lo que el JST está comprobando de verdad
- 30.2.2 Respuestas que empeoran las cosas

### 30.3 Después del resultado
- 30.3.1 P2G, P2R y hallazgos; carta de resultados
- 30.3.2 Remediación y preparación del siguiente ciclo
- 30.3.3 **[CASO JST]** "Las deficiencias de 2025 siguen abiertas"

---

# PARTE V — Avanzada: grupos internacionales y los próximos años [N3]

> Al terminar: sabes organizar el ejercicio de un grupo con filiales fuera de la UE, gobernar sus datos,
> explicar por qué dos números del mismo grupo no coinciden y anticipar los proyectos que vienen.

## Capítulo 31 — Arquitectura de un ejercicio de grupo

### 31.1 Matriz y filiales
- 31.1.1 Quién proyecta cada país y con qué modelos
- 31.1.2 Satélites locales frente a satélites del grupo
- 31.1.3 Consolidación y ajustes de grupo

### 31.2 El escenario fuera de la UE
- 31.2.1 Traslación de las variables JERS a cada geografía
- 31.2.2 Lo que falta: bolsa, swaps, Argentina
- 31.2.3 Türkiye en desviación, no en nominal
- 31.2.4 **[CÓDIGO]** Anexo S3

### 31.3 Divisa, perímetro y contabilidad
- 31.3.1 La asimetría del tipo de cambio en la práctica
- 31.3.2 **[NÚMEROS]** Polonia: un cambio de perímetro real entre 2025 y 2027
- 31.3.3 NIC 29: Türkiye y Argentina
- 31.3.4 **[CASO JST]** "¿Por qué México pesa más en pérdidas que en balance?"

### 31.4 Datos repartidos
- 31.4.1 Sistemas, definiciones y calendarios locales; residencia de datos
- 31.4.2 GAAP locales frente a IFRS 9
- 31.4.3 RDARR: la guía de 2024 incluye el *stress test*; prioridades 2026-2028
- 31.4.4 Linaje de la filial al CSV de la EBA y conciliaciones previas
- 31.4.5 **[QUÉ VIENE]** Puntos de partida desde FINREP/COREP en 2029
- 31.4.6 **[CASO JST]** "Su dato de México no cuadra con su reporting"

## Capítulo 32 — Comparabilidad: del cociente al puente

### 32.1 La pregunta del JST
- 32.1.1 ¿Por qué Santander México no da lo mismo en el EBA que ante la CNBV?
- 32.1.2 ¿Por qué México cuesta más que España, y BBVA México más que Santander México?
- 32.1.3 **[TRAMPA]** El cociente que coincide por casualidad (el 3,2x)

### 32.2 Paso 1: normalizar la severidad
- 32.2.1 Adverso menos base
- 32.2.2 El escenario JERS para México y España en desviación
- 32.2.3 **[NÚMEROS]** El base ya consume mucho en México

### 32.3 Paso 2: limpiar el denominador
- 32.3.1 Hogares y empresas, sin soberanos ni bancos centrales
- 32.3.2 **[NÚMEROS]** Del 50,8 % al 82,3 %

### 32.4 Paso 3: separar mezcla e intensidad
- 32.4.1 La descomposición por segmentos
- 32.4.2 **[NÚMEROS]** México: −0,26 pp de mezcla, +7,64 pp de intensidad
- 32.4.3 **[CASO JST]** "La misma cartera, el doble de pérdida"

### 32.5 Paso 4: traducir la mecánica EBA a la local
- 32.5.1 Balance estático frente a plan de negocios
- 32.5.2 IFRS 9 frente a PI × SP × EI y NIF C-16
- 32.5.3 CET1 FL frente a ICAP; sin acciones frente a Plan de Acción Preventivo
- 32.5.4 Base FMI frente a escenario por oficio; tipo de cambio de cierre frente a senda
- 32.5.5 **[CÓDIGO]** Anexo S4

### 32.6 Por qué la comparación local es sintética
- 32.6.1 Ningún número local publicado por banco
- 32.6.2 Otros contrastes del mismo grupo: SHUSA y Santander UK

## Capítulo 33 — Cómo compara el supervisor y cómo se defiende un número
- 33.1 El análisis horizontal: pares por geografía y modelo de negocio; lo que el JST ve y el mercado no
- 33.2 **[DEFENSA]** Explicar una diferencia en cuatro frases
- 33.3 **[CASO JST]** "Sus pares en México pierden más"

## Capítulo 34 — Lo que viene
- 34.1 **[QUÉ VIENE]** UE: simplificación, reporting integrado, clima y geopolítica en el ciclo ordinario, P2G bienal
- 34.2 **[QUÉ VIENE]** Fuera de la UE: SCB promediado y comentario público en la Fed; vuelta a colchones sistémicos en el Banco de Inglaterra; divergencia transatlántica
- 34.3 Supervisión con datos e IA: *benchmarks* más finos, menos margen para el modelo propio
- 34.4 Los proyectos que se generan

---

# PARTE VI — El oficio [N3]

## Capítulo 35 — Tipologías de encargo y cómo entrar en uno
- 35.1 Preparación, ejecución integrada, validación de segunda línea, QA independiente, *benchmark*
- 35.2 Las dos primeras semanas en un proyecto
- 35.3 **[TRAMPA]** Prometer un número antes de ver el punto de partida

## Capítulo 36 — El árbol de diagnóstico
- 36.1 ¿Qué ejercicio, qué métrica, qué escenario?
- 36.2 ¿Dónde está la pérdida: país, segmento, stage?
- 36.3 ¿Es severidad, mezcla o intensidad?
- 36.4 ¿Qué va a preguntar el JST?
- 36.5 **[DEFENSA]** Defender un número no es defender el número más bajo

---

# ANEXOS

## Anexos de código (Python, ejecutados)

### Anexo S0 — [CÓDIGO] El *stress test* de juguete
- Una cartera, dos escenarios, tres años: del satélite al CET1 en un solo script

### Anexo S1 — [CÓDIGO] Modelo satélite de PD y LGD
- Primera parte (N1): estimación sobre datos sintéticos y lectura de elasticidades
- Segunda parte (N2): proyección bajo el adverso JERS para España y México y contraste con un *benchmark*

### Anexo S2 — [CÓDIGO] Migración de stages bajo escenario
- Matrices *point-in-time*, previsión perfecta, reversión a seis años, efecto de primer año

### Anexo S3 — [CÓDIGO] Traslación del escenario a geografías no UE
- Tablas JERS por país; variables que faltan; Türkiye en desviaciones; Argentina con "Rest of the world"

### Anexo S4 — [CÓDIGO] Puente de comparabilidad España–México
- Lectura del CSV de la EBA; severidad neta, denominador, mezcla e intensidad; comparación sintética con un ejercicio tipo CNBV

### Anexo S5 — [CÓDIGO] *Reverse stress test*
- Del objetivo de caída al escenario más plausible

### Anexo S6 — [CÓDIGO] Coherencia entre ICAAP y EBA
- Misma cartera, dos supuestos de balance, conciliación de la diferencia

## Anexos de referencia

### Anexo R1 — Glosario (con la traducción entre la jerga de la EBA, del BCE y de los reguladores locales)
### Anexo R2 — Fuentes y cómo seguir lo que viene
### Anexo R3 — Mapa de reguladores por país
### Anexo R4 — Calendario tipo de un ciclo (EBA, Fed, Banco de Inglaterra, CNBV)
### Anexo R5 — Tabla de remisiones al manual IRB, para profundizar
### Anexo R6 — Autoevaluación por nivel
- Prueba de entrada (lo que se asume)
- Preguntas de cierre de N1, N2 y N3, con respuestas razonadas
- Preguntas tipo JST y tipo entrevista
### Anexo R7 — Casos prácticos integrados
- Caso 1 (N1): el *stress test* de juguete con otra cartera
- Caso 2 (N2): proyección de una cartera hipotecaria española bajo el adverso EBA
- Caso 3 (N3): responder a tres *flags* del QA sobre la filial mexicana
- Caso 4 (N3): explicar al JST la diferencia entre el EBA y el ejercicio local

---

## Control de versiones del índice

| Versión | Fecha | Cambios |
|---|---|---|
| v0.1 | 2026-10-16 | Índice inicial a tres niveles, tras la F1 validada |
| v0.2 | 2026-10-16 | Cambio de lector: de "conoce la banca y el IRB básico" a experto. Nueva Parte I de fundamentos (caps. 1-8: capital, PD *point-in-time*, IFRS 9, escenarios, econometría, la cadena y un *stress test* de juguete). Metodología en una sola parte con dos bloques. Tres niveles (N1-N3) con objetivos por parte. Nuevos anexos S0, R6 (autoevaluación) y R7 (casos integrados). Manual autocontenido; el IRB queda como referencia para profundizar |
| v0.3 | 2026-10-16 | Parte I ampliada a petición de Rafa: subsecciones nuevas en los caps. 1-8 (ficha de resultados, MDA, TTC a PiT, SICR, estructura temporal, construcción del escenario, selección y validación de satélites, descomposición del BCE, dueños de la cadena, sensibilidad del juguete) |
| v0.4 | 2026-10-17 | Cap. 19: nuevo 19.1.5 [CASO JST] "Sus activos ponderados bajan en el adverso", para cumplir un caso por capítulo en las Partes III-VI |
