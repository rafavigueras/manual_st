"""Genera manual/anexos-codigo.html ejecutando cada anexo y volcando su codigo y su salida.

Regla del manual: ningun numero se publica sin haberse ejecutado. Este script es la garantia:
la salida que aparece en el anexo es la de la ultima ejecucion, no una copia a mano.

Uso (desde la raiz del proyecto):  .venv/bin/python -I herramientas/generar_anexos_codigo.py
"""
import html
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PY = RAIZ / ".venv" / "bin" / "python"
if not PY.exists():
    PY = Path(sys.executable)

ANEXOS = [
    ("S0", "El <i>stress test</i> de juguete", ["s0_juguete.py"], "capítulo 8 y secciones 19.2.4 y 21.1.1",
     "Una filial mexicana con una cartera de consumo y otra de empresas, el escenario de la JERS de 2025 para México, "
     "satélites, flujos entre stages, provisiones con y sin previsión perfecta, activos ponderados con suelo y CET1. "
     "Termina con la sensibilidad de la pérdida de consumo a cada supuesto."),
    ("S1", "Modelo satélite de PD y LGD", ["s1a_satelite.py", "s1b_satelite.py"], "capítulos 6, 15, 22 y 23",
     "Primera parte: estimación de un satélite logit sobre veinte años de datos sintéticos con dos recesiones, lectura "
     "de elasticidades, el error de estimar sin crisis y las tres pruebas de validación. Segunda parte: proyección con "
     "el escenario de la JERS para México y España, contraste con un <i>benchmark</i> ilustrativo (los del BCE no son "
     "públicos) y LGD hipotecaria en función del LTV con la caída de la vivienda del adverso."),
    ("S2", "Migración de stages bajo escenario", ["s2_migracion.py"], "capítulos 16 y 17",
     "Las fórmulas de provisiones de los recuadros 3 a 9 de la nota metodológica de 2027 aplicadas a la cartera de "
     "consumo del hilo conductor: previsión perfecta, reversión en seis años, ponderación 5/6 &ndash; 1/6 del último "
     "año, suelo del stage 3 antiguo y tres criterios de SICR."),
    ("S3", "Traslación del escenario a geografías no UE", ["s3_traslacion.py"], "capítulo 31",
     "Severidad por país en acumulado y en desviación, la vivienda turca en nominal y frente al base, tres traslaciones "
     "para Argentina (que no tiene fila en el escenario) y la asimetría del tipo de cambio en la filial del juguete."),
    ("S4", "Puente de comparabilidad España–México", ["s4_puente.py"], "capítulos 31 y 32",
     "Los pasos 1 a 3 del puente con los datos publicados por la EBA del ejercicio de 2025 para Santander y BBVA en "
     "España y México: cocientes, severidad neta, denominador y descomposición en mezcla e intensidad."),
    ("S5", "<i>Reverse stress test</i>", ["s5_reverse.py"], "capítulo 21",
     "Sobre el juguete del anexo S0: el múltiplo del adverso que produce una caída objetivo y, moviendo por separado "
     "paro y PIB, el escenario más plausible en distancia de Mahalanobis."),
    ("S6", "Coherencia entre ICAAP y ejercicio europeo", ["s6_coherencia.py"], "capítulo 25 y sección 32.5",
     "La misma cartera con los mismos modelos en tres ejercicios (europeo, ICAAP y local tipo supervisor mexicano) y "
     "el puente con el europeo en dos pasos, escenario y balance."),
]
CIFRAS = [
    ("cifras_parte01.py", "Parte I"), ("cifras_parte02.py", "Parte II"), ("cifras_parte03a.py", "Parte III-A"),
    ("cifras_parte03b.py", "Parte III-B"), ("cifras_parte04.py", "Parte IV"), ("cifras_parte05.py", "Parte V"),
]


def ejecutar(script):
    r = subprocess.run([str(PY), "-I", str(RAIZ / "anexos" / script)], cwd=RAIZ, capture_output=True,
                       text=True, timeout=600)
    if r.returncode != 0:
        sys.exit(f"Error al ejecutar {script}:\n{r.stderr}")
    return r.stdout.rstrip()


def bloque_codigo(script):
    codigo = (RAIZ / "anexos" / script).read_text(encoding="utf-8").rstrip()
    salida = ejecutar(script)
    return (f'<h3>{script}</h3>\n<pre><code>{html.escape(codigo)}</code></pre>\n'
            f'<pre class="salida">{html.escape(salida)}</pre>\n')


def main():
    partes = []
    for clave, titulo, scripts, usos, desc in ANEXOS:
        cuerpo = "".join(bloque_codigo(s) for s in scripts)
        partes.append(
            f'<!-- ============================================================ -->\n'
            f'<h2 id="{clave}">Anexo {clave} &mdash; {titulo}</h2>\n'
            f'<p>{desc}</p>\n<p class="small">Se usa en: {usos}. Ejecución: '
            f'<code>.venv/bin/python -I anexos/{scripts[0]}</code>'
            + (f' (y <code>anexos/{scripts[1]}</code>)' if len(scripts) > 1 else '') + '.</p>\n' + cuerpo)
    cifras = []
    for script, parte in CIFRAS:
        cifras.append(f'<h3>{script} ({parte})</h3>\n<pre class="salida">{html.escape(ejecutar(script))}</pre>\n')
    pagina = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Anexos de código</title>
<link rel="stylesheet" href="estilo.css">
</head>
<body>

<p class="eyebrow">Anexos · Código</p>
<h1>Anexos de código</h1>
<p class="subtitulo">Los programas que producen todas las cifras del manual, con su salida.</p>

<p class="lead">Todas las cifras de los bloques NÚMEROS, PALANCA y CASO JST que no salen directamente de una fuente pública salen de estos programas, y la salida que aparece debajo de cada uno es la de su última ejecución, generada automáticamente el {date.today().strftime('%d/%m/%Y')} por <code>herramientas/generar_anexos_codigo.py</code>. Están escritos en Python con numpy, pandas, scipy y statsmodels, y se ejecutan desde la raíz del proyecto con el entorno virtual del repositorio. Los datos de bancos reales son públicos y llevan su fuente; los datos de las carteras del hilo conductor son sintéticos. El objetivo de estos anexos no es dar un modelo para producción, sino que cada mecanismo del texto se pueda ver, cambiar y volver a ejecutar.</p>

<hr/>

{"".join(partes)}
<!-- ============================================================ -->
<h2 id="cifras">Cifras de los ejemplos de cada parte</h2>
<p>Los ejemplos que no forman parte de un anexo tienen su propio programa por parte. Se reproduce solo su salida; el código está en <code>anexos/</code>.</p>
{"".join(cifras)}
<nav class="nav">
<p><a href="parte-06.html">← Parte VI</a> · <a href="index.html">Índice</a> · <a href="anexos-referencia.html">Anexos de referencia →</a></p>
</nav>

</body>
</html>
"""
    (RAIZ / "manual" / "anexos-codigo.html").write_text(pagina, encoding="utf-8")
    print("anexos-codigo.html generado")


if __name__ == "__main__":
    main()
