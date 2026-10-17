# -*- coding: utf-8 -*-
"""
Genera la portada del manual en escala de grises, a la resolucion de un Kindle Paperwhite
(758x1024). Pensada para tinta electronica: alto contraste, pocos tonos limpios, tipografia
grande.

El motivo grafico es la trayectoria del CET1 de la filial del hilo conductor (anexo S0): en el
adverso cae del 13,00 % al 7,77 %. Es la imagen central del libro: un escenario convertido en
una caida de capital.

Uso (desde la raiz del proyecto):  .venv/bin/python -I manual/generar_portada.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 758, 1024
AQUI = Path(__file__).resolve().parent
FUENTES = [Path("/System/Library/Fonts/Supplemental"), Path("/Library/Fonts"), Path(r"C:\Windows\Fonts")]

img = Image.new("L", (W, H), color=18)
draw = ImageDraw.Draw(img)


def fuente(nombres, tam):
    for carpeta in FUENTES:
        for n in nombres:
            if (carpeta / n).exists():
                return ImageFont.truetype(str(carpeta / n), tam)
    return ImageFont.load_default()


SANS = ["Arial.ttf", "arial.ttf"]
SANS_B = ["Arial Bold.ttf", "arialbd.ttf"]
SERIF = ["Georgia.ttf", "georgia.ttf"]


def centrado(y, texto, font, gris, esp=0):
    if esp:
        ancho = sum(draw.textlength(c, font=font) + esp for c in texto) - esp
        x = (W - ancho) / 2
        for c in texto:
            draw.text((x, y), c, font=font, fill=gris)
            x += draw.textlength(c, font=font) + esp
    else:
        ancho = draw.textlength(texto, font=font)
        draw.text(((W - ancho) / 2, y), texto, font=font, fill=gris)
    caja = font.getbbox(texto)
    return y + (caja[3] - caja[1]) + 12


y = 90
y = centrado(y, "MANUAL DE ESTUDIO Y REFERENCIA", fuente(SANS, 15), 200, esp=4)
y += 34
for linea in ("Stress Test", "de Riesgo de Crédito"):
    y = centrado(y, linea, fuente(SERIF, 62), 245)
y += 14
for linea in ("En grupos bancarios con filiales", "dentro y fuera de Europa"):
    y = centrado(y, linea, fuente(SANS, 22), 185)

# ---------- Motivo: CET1 de la filial en el adverso (anexo S0) ----------
x0, x1, ytop, ybot = 130, 628, 560, 830
draw.line([(x0, ybot), (x1, ybot)], fill=90, width=2)
adverso = [13.00, 9.68, 8.19, 7.77]


def punto(i, v):
    x = x0 + (x1 - x0) * i / 3
    yv = ybot - (v - 6.0) / (14.0 - 6.0) * (ybot - ytop)
    return x, yv


draw.line([punto(i, 13.0) for i in range(4)], fill=80, width=2)
draw.line([punto(i, v) for i, v in enumerate(adverso)], fill=235, width=7)
for i, v in enumerate(adverso):
    cx, cy = punto(i, v)
    draw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=235)
etq = fuente(SANS_B, 20)
cx, cy = punto(0, 13.0)
draw.text((cx - 20, cy - 42), "13,00 %", font=etq, fill=235)
cx, cy = punto(3, 7.77)
draw.text((cx - 60, cy + 18), "7,77 %", font=etq, fill=235)
centrado(ybot + 26, "−523 pb en el escenario adverso", fuente(SANS, 18), 160)

centrado(940, "RAFAEL VIGUERAS", fuente(SANS, 18), 200, esp=5)

img.convert("RGB").save(AQUI / "portada.jpg", quality=92)
print("portada.jpg generada")
