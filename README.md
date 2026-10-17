# Manual de Stress Test de Riesgo de Crédito

Manual educativo sobre *stress testing* de riesgo de crédito en grupos bancarios con filiales dentro y fuera de Europa: cómo se traduce un escenario en pérdidas, provisiones y capital, qué exige el supervisor europeo (EBA, BCE y JST), cómo se viven los ejercicios locales de las filiales (Reserva Federal, Banco de Inglaterra, CNBV, Banco Central do Brasil…) y cómo se compara el número de España con el de México.

Lleva de «conozco la banca y el IRB en lo básico» a «sé defender ante el JST por qué mi pérdida es esta», en tres niveles (fundamentos, practicante, experto). Es hermano del [Manual de Capital y Provisiones](https://github.com/rafavigueras/manual_irb), pero se entiende solo.

## Leer el manual

- [Portada e índice](manual/index.html), con las partes en HTML (abrir en el navegador).
- [Manual completo en un solo fichero](manual/manual-completo.html).
- Libro electrónico: [EPUB](manual/Manual%20de%20Stress%20Test.epub) y [AZW3 para Kindle](manual/Manual%20de%20Stress%20Test.azw3).

## Contenido

| Parte | Nivel | Capítulos |
|---|---|---|
| 0 · Cómo usar este manual | — | Rutas de lectura y cómo trabajar con las fuentes |
| I · Fundamentos | N1 | 1-8: capital, PD *point-in-time*, IFRS 9, escenarios, satélites, la cadena completa y un *stress test* de juguete |
| II · El mapa y los actores | N2 | 9-13: la familia de ejercicios, quién decide qué, anatomía del ejercicio EBA, de la caída de capital a la P2G, el grupo multirregulador |
| III-A · La metodología que se aplica hoy | N2 | 14-21: punto de partida, satélites, stages, provisiones, *benchmarks* y QA, RWA y CET1, ICAAP, *reverse* y clima |
| III-B · Retos metodológicos | N3 | 22-27: series cortas, no linealidad, *overlays*, coherencia entre ejercicios, clima, *machine learning* |
| IV · El ejercicio frente al JST | N3 | 28-30: el ejercicio como proyecto, el ciclo de QA, situaciones recurrentes |
| V · Grupos internacionales | N3 | 31-34: arquitectura de grupo, comparabilidad España–México, cómo compara el supervisor, lo que viene |
| VI · El oficio | N3 | 35-36: tipos de encargo y árbol de diagnóstico |
| Anexos | — | S0-S6 (código Python ejecutado) y R1-R7 (glosario, fuentes, mapa de reguladores, calendario, remisiones al manual IRB, autoevaluación y casos) |

## Datos y fuentes

- El ejercicio de referencia es el europeo de 2027 (nota metodológica de la EBA en borrador del 11 de junio de 2026); las cifras de bancos reales son las del ejercicio de 2025, publicadas por la EBA el 1 de agosto de 2025, siempre con su fuente y fecha.
- Los datos de las carteras del hilo conductor (una filial mexicana con consumo y empresas) son sintéticos.
- La investigación de fuentes, con niveles de confianza por afirmación y su validación contra fuentes primarias, está en `investigacion/`. Los PDF originales no se incluyen.
- Todo el contenido está a fecha de octubre de 2026. Los bloques «Qué viene» caducan antes que el resto: comprueba el estado de cada norma antes de usarlo.

## Reproducir las cifras y los libros

Requiere Python 3 y, para los libros electrónicos, [Calibre](https://calibre-ebook.com/).

```bash
python3 -m venv .venv
.venv/bin/pip install numpy pandas scipy statsmodels pillow
.venv/bin/python -I anexos/s0_juguete.py                 # cualquier anexo S0-S6 o cifras_parteNN
.venv/bin/python -I herramientas/generar_anexos_codigo.py  # regenera anexos-codigo.html ejecutando todo
python3 -I herramientas/revision.py                        # revisión automática de enlaces, anclas y bloques
.venv/bin/python -I manual/generar_portada.py
.venv/bin/python -I manual/construir_kindle.py             # manual-completo.html, EPUB y AZW3
```

## Estructura

```
PROCESO.md                 decisiones, método, estado y notas de cada sesión
00-indice-manual-st.md     índice de trabajo a tres niveles
investigacion/             notas de research (F1) y su validación
anexos/                    programas Python que producen todas las cifras
herramientas/              revisión automática, generación de anexos, scripts de validación
manual/                    el libro: HTML, CSS, portada, EPUB y AZW3
```

## Autor

Rafael Vigueras

## Licencia

Material educativo. No constituye asesoramiento ni refleja la posición de ninguna entidad o supervisor; los casos con el supervisor son patrones anonimizados y no describen a ningún banco concreto.
