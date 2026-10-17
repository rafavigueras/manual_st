# -*- coding: utf-8 -*-
"""
Construye el AZW3 (formato nativo, para copiar al Kindle por USB) y el EPUB
(copia portatil) del manual, usando Calibre en lugar de pandoc, con ajustes
especificos para un Kindle Paperwhite 6a generacion (2012): pantalla 758x1024,
212 ppp, E Ink Pearl de 16 grises, sin soporte nativo de EPUB.

Uso (desde la raiz del proyecto):  .venv/bin/python -I manual/construir_kindle.py
Requiere Calibre instalado (ebook-convert en el PATH, en /Applications/calibre.app
o en la ruta habitual de Windows). Antes: .venv/bin/python -I manual/generar_portada.py

Pipeline:
  1. Fusiona los 11 HTML del manual en un unico documento, en orden de
     lectura, reescribiendo los enlaces cruzados entre paginas a anclas
     locales (ver fusionar_html()).
  2. Aplana estilo.css + kindle-eink.css a un unico kindle-flat.css con las
     variables CSS ya resueltas: el "flattener" de Calibre para formatos
     de e-ink legado no entiende var(--x) y descarta silenciosamente
     cualquier regla que la use (lo perdimos una vez; no otra).
  3. Autocierra <hr> y <br>: sin la barra de autocierre, el parser XHTML
     de Calibre pierde la cuenta de apertura/cierre y el libro termina en
     un amasijo de etiquetas repetidas (bug real, encontrado por ejecucion).
  4. Llama a ebook-convert dos veces: AZW3 (perfil kindle_pw, el dispositivo
     real) y EPUB (copia portatil / archivo).
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

MANUAL_DIR = Path(__file__).resolve().parent

ORDEN = [
    "index.html",
    "parte-00.html", "parte-01.html", "parte-02.html", "parte-03a.html", "parte-03b.html",
    "parte-04.html", "parte-05.html", "parte-06.html",
    "anexos-codigo.html", "anexos-referencia.html",
]
TITULO = "Stress Test de Riesgo de Credito"
NOMBRE = "Manual de Stress Test"

RE_BODY = re.compile(r"<body[^>]*>(.*)</body>", re.DOTALL | re.IGNORECASE)
RE_NAV = re.compile(r"<nav class=\"nav\">.*?</nav>", re.DOTALL)
RE_XLINK = re.compile(r'href="(?:parte-\d\d[ab]?|anexos-codigo|anexos-referencia|index)\.html#')
RE_XFILE = re.compile(r'href="((?:parte-\d\d[ab]?|anexos-codigo|anexos-referencia|index))\.html"')
RE_H1 = re.compile(r"<h1(?![^>]*\bid=)", re.IGNORECASE)


def fusionar_html() -> Path:
    partes = []
    for nombre in ORDEN:
        texto = (MANUAL_DIR / nombre).read_text(encoding="utf-8")
        m = RE_BODY.search(texto)
        if not m:
            raise SystemExit(f"No se encontro <body> en {nombre}")
        cuerpo = m.group(1)
        cuerpo = RE_NAV.sub("", cuerpo)
        cuerpo = RE_XLINK.sub('href="#', cuerpo)
        cuerpo = RE_XFILE.sub(lambda m: f'href="#doc-{m.group(1)}"', cuerpo)
        cuerpo = RE_H1.sub(f'<h1 id="doc-{Path(nombre).stem}"', cuerpo, count=1)
        partes.append(f"<!-- ===== {nombre} ===== -->\n" + cuerpo.strip())

    cuerpo_final = "\n\n".join(partes)
    cuerpo_final = re.sub(r"<hr\s*>", "<hr />", cuerpo_final)
    cuerpo_final = re.sub(r"<br\s*>", "<br />", cuerpo_final)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{TITULO}</title>
<link rel="stylesheet" href="kindle-flat.css">
</head>
<body>
{cuerpo_final}
</body>
</html>
"""

    salida = MANUAL_DIR / "manual-completo.html"
    salida.write_text(html, encoding="utf-8")

    ids_definidos = set(re.findall(r'id="([^"]+)"', html))
    ids_referenciados = set(re.findall(r'href="#([^"]+)"', html))
    huerfanos = sorted(r for r in ids_referenciados if r not in ids_definidos)
    if huerfanos:
        raise SystemExit(f"Anclas rotas tras la fusion: {huerfanos}")
    duplicados = sorted({i for i in re.findall(r'id="([^"]+)"', html) if html.count(f'id="{i}"') > 1})
    if duplicados:
        raise SystemExit(f"Anclas duplicadas tras la fusion: {duplicados}")
    restantes = re.findall(r'href="(?:parte-\d\d[ab]?|anexos-codigo|anexos-referencia|index)\.html[^"]*"', html)
    if restantes:
        raise SystemExit(f"Enlaces cruzados sin reescribir: {restantes}")

    print(f"  Fusionado: {salida.name}  ({len(html):,} caracteres, "
          f"{len(ids_definidos)} anclas, {len(ids_referenciados)} referencias resueltas)")
    return salida


def strip_dark_block(css: str) -> str:
    marker = css.find("@media (prefers-color-scheme: dark)")
    if marker == -1:
        return css
    brace_start = css.find("{", marker)
    depth = 0
    i = brace_start
    for i in range(brace_start, len(css)):
        if css[i] == "{":
            depth += 1
        elif css[i] == "}":
            depth -= 1
            if depth == 0:
                break
    return css[:marker] + css[i + 1:]


def aplanar_css() -> Path:
    base = (MANUAL_DIR / "estilo.css").read_text(encoding="utf-8")
    extra = (MANUAL_DIR / "kindle-eink.css").read_text(encoding="utf-8")

    base_sin_oscuro = strip_dark_block(base)
    root_match = re.search(r":root\s*\{([^}]*)\}", base_sin_oscuro)
    if not root_match:
        raise SystemExit("No se encontro el bloque :root en estilo.css")
    variables = dict(re.findall(r"--([\w-]+)\s*:\s*([^;]+);", root_match.group(1)))

    combinado = base_sin_oscuro + "\n\n" + extra

    def resolver(m: re.Match) -> str:
        nombre = m.group(1)
        if nombre not in variables:
            raise SystemExit(f"Variable sin resolver: --{nombre}")
        return variables[nombre]

    plano = re.sub(r"var\(--([\w-]+)\)", resolver, combinado)
    plano = re.sub(r":root\s*\{[^}]*\}", "", plano, count=1)

    restantes = re.findall(r"var\(--[\w-]+\)", plano)
    if restantes:
        raise SystemExit(f"Quedan var() sin resolver: {restantes}")

    salida = MANUAL_DIR / "kindle-flat.css"
    salida.write_text(plano, encoding="utf-8")
    print(f"  Aplanado: {salida.name}  ({len(variables)} variables resueltas)")
    return salida


def localizar_ebook_convert() -> str:
    ruta = shutil.which("ebook-convert")
    if ruta:
        return ruta
    for candidato in (Path("/Applications/calibre.app/Contents/MacOS/ebook-convert"),
                      Path(r"C:\Program Files\Calibre2\ebook-convert.exe")):
        if candidato.exists():
            return str(candidato)
    raise SystemExit("No se encuentra ebook-convert.exe. ¿Esta instalado Calibre?")


def convertir(fuente: Path, salida_nombre: str, extra_args: list[str]) -> None:
    ebook_convert = localizar_ebook_convert()
    portada = MANUAL_DIR / "portada.jpg"
    if not portada.exists():
        raise SystemExit("Falta portada.jpg: ejecutar antes .venv/bin/python -I manual/generar_portada.py")
    cmd = [
        ebook_convert, str(fuente), str(MANUAL_DIR / salida_nombre),
        "--title", TITULO,
        "--authors", "Rafael Vigueras",
        "--comments", "Stress testing de riesgo de credito en grupos bancarios con filiales dentro y fuera de Europa: metodologia EBA, supervisor y comparabilidad",
        "--cover", str(portada),
        "--language", "es",
        "--output-profile", "kindle_pw",
        "--level1-toc", "//h:h1",
        "--level2-toc", "//h:h2",
        "--toc-threshold", "1",
        "--max-toc-links", "250",
        "--toc-title", "Indice",
        "--chapter", "//h:h1",
        "--page-breaks-before", "//h:h1",
        "--unsmarten-punctuation",
        "--insert-blank-line-size", "0.3",
    ] + extra_args
    resultado = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    problemas = [l for l in resultado.stdout.splitlines() + resultado.stderr.splitlines()
                 if re.search(r"error|warn", l, re.IGNORECASE) and "Tag hr" not in l]
    if resultado.returncode != 0:
        print(resultado.stdout[-3000:])
        print(resultado.stderr[-3000:])
        raise SystemExit(f"ebook-convert fallo generando {salida_nombre}")
    if problemas:
        print(f"  AVISOS al generar {salida_nombre}:")
        for p in problemas:
            print(f"    {p}")
    tam_kb = (MANUAL_DIR / salida_nombre).stat().st_size / 1024
    print(f"  OK -> {salida_nombre}  ({tam_kb:,.0f} KB)")


def main() -> None:
    print("1. Fusionando HTML...")
    fuente = fusionar_html()
    print("2. Aplanando CSS (variables -> literales, perfil Kindle Paperwhite 212 ppp)...")
    aplanar_css()
    print("3. Generando AZW3 (formato nativo, el que se copia al dispositivo)...")
    convertir(fuente, f"{NOMBRE}.azw3", [])
    print("4. Generando EPUB (copia portatil / archivo)...")
    convertir(fuente, f"{NOMBRE}.epub", ["--epub-version", "3"])
    print("\nListo. Comprobaciones recomendadas antes de copiar al dispositivo:")
    print("  - Transferir el .azw3 (no el .epub) a la carpeta 'documents' del Kindle por USB")
    print("  - El .epub es la copia portatil, no se ha confirmado que este Paperwhite lo abra nativo")
    print("  - Revisar en el propio dispositivo: portada, tabla de contenidos, un capitulo con tabla ancha")


if __name__ == "__main__":
    main()
