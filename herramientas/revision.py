"""Revision automatica del manual.

Comprueba, sobre todos los .html de manual/:
  - enlaces internos a ficheros inexistentes (se listan aparte como "pendientes"
    si el fichero aun no se ha escrito) y anclas que no existen;
  - ids duplicados dentro de un fichero;
  - coherencia entre la clase de cada bloque y su etiqueta;
  - clases CSS usadas en el HTML y no definidas en estilo.css;
  - equilibrio de etiquetas HTML;
  - recuento de palabras y de bloques por fichero y por tipo.

Uso:  python3 herramientas/revision.py   (desde la raiz del proyecto)
"""
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MANUAL = RAIZ / "manual"

ETIQUETAS = {
    "b-norma": "Norma", "b-porque": "Por qué", "b-margen": "Margen",
    "b-palanca": "Palanca", "b-trampa": "Trampa", "b-numeros": "Números",
    "b-codigo": "Código", "b-defensa": "Defensa", "b-viene": "Qué viene",
    "b-caso": "Caso JST",
}
VACIAS = {"meta", "link", "br", "hr", "img", "input", "col", "wbr"}


class Lector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = Counter()
        self.enlaces = []
        self.clases = set()
        self.pila = []
        self.desequilibrios = []
        self.texto = []
        self.bloques = []          # (clase, etiqueta_texto)
        self._bloque_abierto = None
        self._en_etiqueta = False
        self._buffer_etiqueta = ""
        self._en_estilo = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids[a["id"]] += 1
        if tag == "a" and "href" in a:
            self.enlaces.append((a["href"], self.getpos()[0]))
        for c in (a.get("class") or "").split():
            self.clases.add(c)
        clases = (a.get("class") or "").split()
        if tag == "div" and "bloque" in clases:
            tipo = next((c for c in clases if c.startswith("b-")), None)
            self._bloque_abierto = tipo
        if tag == "span" and "etiqueta" in clases and self._bloque_abierto:
            self._en_etiqueta = True
            self._buffer_etiqueta = ""
        if tag in ("style", "script"):
            self._en_estilo = True
        if tag not in VACIAS:
            self.pila.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids[a["id"]] += 1

    def handle_endtag(self, tag):
        if tag in VACIAS:
            return
        if tag == "span" and self._en_etiqueta:
            self.bloques.append((self._bloque_abierto, self._buffer_etiqueta.strip()))
            self._en_etiqueta = False
            self._bloque_abierto = None
        if tag in ("style", "script"):
            self._en_estilo = False
        if self.pila and self.pila[-1][0] == tag:
            self.pila.pop()
        else:
            esperado = self.pila[-1] if self.pila else None
            self.desequilibrios.append((tag, self.getpos()[0], esperado))
            # recupera: busca la apertura mas cercana
            for i in range(len(self.pila) - 1, -1, -1):
                if self.pila[i][0] == tag:
                    del self.pila[i:]
                    break

    def handle_data(self, data):
        if self._en_etiqueta:
            self._buffer_etiqueta += data
        if not self._en_estilo:
            self.texto.append(data)


def clases_css():
    css = (MANUAL / "estilo.css").read_text(encoding="utf-8")
    return set(re.findall(r"\.([a-zA-Z][\w-]*)", css))


def main():
    ficheros = sorted(MANUAL.glob("*.html"))
    lectores = {}
    for f in ficheros:
        lec = Lector()
        lec.feed(f.read_text(encoding="utf-8"))
        lectores[f.name] = lec

    definidas = clases_css()
    errores = 0
    pendientes = defaultdict(set)
    total_palabras = 0
    total_bloques = Counter()

    for nombre, lec in lectores.items():
        problemas = []
        for id_, n in lec.ids.items():
            if n > 1:
                problemas.append(f"id duplicado: {id_} ({n} veces)")
        for href, linea in lec.enlaces:
            if re.match(r"^(https?:|mailto:)", href):
                continue
            destino, _, ancla = href.partition("#")
            destino = destino or nombre
            if destino not in lectores:
                if destino.endswith(".html") and "/" not in destino:
                    pendientes[destino].add(nombre)
                else:
                    problemas.append(f"l.{linea}: enlace a fichero inexistente {href}")
                continue
            if ancla and ancla not in lectores[destino].ids:
                problemas.append(f"l.{linea}: ancla inexistente {href}")
        for tipo, texto in lec.bloques:
            esperado = ETIQUETAS.get(tipo)
            if esperado is None:
                problemas.append(f"bloque con clase desconocida: {tipo}")
            elif texto != esperado:
                problemas.append(f"bloque {tipo} con etiqueta '{texto}' (esperada '{esperado}')")
        sin_definir = sorted(c for c in lec.clases if c not in definidas)
        if sin_definir:
            problemas.append("clases sin definir en estilo.css: " + ", ".join(sin_definir))
        for tag, linea, esperado in lec.desequilibrios:
            problemas.append(f"l.{linea}: cierre </{tag}> sin apertura (abierta: {esperado})")
        for tag, linea in lec.pila:
            if tag not in ("html", "body", "head"):
                problemas.append(f"l.{linea}: <{tag}> sin cerrar")

        palabras = len(" ".join(lec.texto).split())
        bloques = Counter(t for t, _ in lec.bloques)
        total_palabras += palabras
        total_bloques.update(bloques)
        resumen = ", ".join(f"{k[2:]} {v}" for k, v in sorted(bloques.items())) or "sin bloques"
        print(f"{nombre:28} {palabras:7,} palabras · {resumen}")
        for p in problemas:
            print(f"    ✗ {p}")
        errores += len(problemas)

    print(f"\nTotal: {len(ficheros)} ficheros · {total_palabras:,} palabras · "
          f"{sum(total_bloques.values())} bloques")
    if pendientes:
        print("\nFicheros enlazados que aún no existen (pendientes de escribir):")
        for destino, origenes in sorted(pendientes.items()):
            print(f"    · {destino} (desde {', '.join(sorted(origenes))})")
    print(f"\n{'OK' if errores == 0 else f'{errores} problema(s)'}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
