"""Parser de las fichas EBA ST2025 por banco a partir de `pdftotext -bbox`.

Reconstruye cada fila por su coordenada vertical (y) en vez de por el orden del
texto, de modo que la etiqueta de pais se asigna al bloque en que esta dibujada
y las celdas partidas en vertical (filas 11-12 del IRB) se leen bien.

Uso: python3 -I parse_bbox.py <fichero_bbox.html> <salida.json>
Salida: {approach: {scenario: {row: [S1,S2,S3,P1,P2,P3,cov]}}, labels: {approach: {block: pais}}}
"""
import re, sys, json, html

PER = {'IRB': 21, 'STA': 24}
COUNTRY_FIRST = {'SPAIN', 'UNITED', 'BRAZIL', 'CHILE', 'PORTUGAL', 'GERMANY', 'POLAND',
                 'MEXICO', 'FRANCE', 'TURKEY', 'PERU', 'COLOMBIA', 'ITALY', 'ARGENTINA',
                 'NETHERLANDS', 'BELGIUM', 'SWITZERLAND', 'URUGUAY', 'ROMANIA'}
NUM = re.compile(r'^-?[\d,]+(\.\d+)?%?-?$')


def val(t):
    t = t.replace(',', '')
    if t.endswith('%'):
        return float(t[:-1]) / 100
    return float(t)


def main(src, dst):
    pages = open(src, encoding='utf-8').read().split('<page ')[1:]
    data = {'IRB': {}, 'STA': {}}
    labels = {'IRB': {}, 'STA': {}}
    for p in pages:
        words = [(float(a), float(b), float(c), float(d), html.unescape(w)) for a, b, c, d, w in
                 re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>', p)]
        if not words:
            continue
        title = ' '.join(w[4] for w in words[:10])
        m = re.search(r'Credit risk (IRB|STA)', title)
        if not m:
            continue
        ap = m.group(1)
        texts = {w[4] for w in words}
        sc = 'adv' if 'Adverse' in texts else 'base' if 'Baseline' in texts else 'act'
        mx = min(w[0] for w in words)
        rows = [(w[1], w[3], int(w[4]), w[2]) for w in words
                if w[4].isdigit() and w[0] < mx + 40 and int(w[4]) < 300]
        tab = data[ap].setdefault(sc, {})
        for y0, y1, r, xr in rows:
            yc = (y0 + y1) / 2
            toks = []
            for x0, a, x1, b, w in sorted(words):
                if x0 <= xr + 1 or abs((a + b) / 2 - yc) > 2.5:
                    continue
                if w == '-':
                    toks.append(None)
                elif NUM.match(w):
                    if w.endswith('-') and len(w) > 1:
                        toks += [val(w[:-1]), None]
                    else:
                        toks.append(val(w))
            if toks:
                tab[str(r)] = toks[-7:]
        for x0, a, x1, b, w in words:
            if w in COUNTRY_FIRST:
                yc = (a + b) / 2
                y0, y1, r, xr = min(rows, key=lambda q: abs((q[0] + q[1]) / 2 - yc))
                blk = (r - 1) // PER[ap] + 1
                # nombre completo: palabras en la misma linea a la derecha (UNITED STATES / KINGDOM)
                same = sorted(z for z in words if abs((z[1] + z[3]) / 2 - yc) < 1 and z[0] >= x0 and z[0] < x0 + 150 and z[4].isupper())
                name = ' '.join(z[4] for z in same)
                labels[ap].setdefault(str(blk), set()).add(name)
    labels = {ap: {b: sorted(s) for b, s in d.items()} for ap, d in labels.items()}
    json.dump({'data': data, 'labels': labels}, open(dst, 'w'), indent=1)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
