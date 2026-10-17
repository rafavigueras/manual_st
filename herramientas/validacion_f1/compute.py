"""Calcula el desglose por pais (todas las carteras y solo hogares + empresas) a partir
del JSON de parse_bbox.py. Uso: python3 -I compute.py san.json bbva.json
"""
import json, sys

PER = {'IRB': 21, 'STA': 24}
TOP = {'IRB': [1, 2, 3, 4, 5, 6, 10, 17, 18, 20], 'STA': [1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 17, 18, 19, 20, 21, 23]}
TOTAL = {'IRB': 21, 'STA': 24}
# cubos: (enfoque, desplazamiento de fila dentro del bloque)
BUCKETS = {
    'TODO': [('IRB', 21), ('STA', 24)],
    'HH+NFC': [('IRB', 6), ('IRB', 10), ('STA', 8), ('STA', 11), ('STA', 13)],
    'MINORISTA': [('IRB', 10), ('STA', 11), ('STA', 14)],
    'EMPRESAS': [('IRB', 6), ('STA', 8), ('STA', 15), ('STA', 16)],
}


def row(d, ap, sc, blk, off):
    return d['data'][ap][sc].get(str((blk - 1) * PER[ap] + off))


def check(d, name):
    issues = 0
    for ap in ('IRB', 'STA'):
        for sc in ('act', 'base', 'adv'):
            for blk in range(1, 12):
                tot = row(d, ap, sc, blk, TOTAL[ap])
                for k in range(6):
                    s = sum((row(d, ap, sc, blk, o) or [0] * 7)[k] for o in TOP[ap])
                    if abs(s - tot[k]) > 3:
                        issues += 1
                        print(f'  DESCUADRE {name} {ap} {sc} blk{blk} col{k}: suma {s} vs TOTAL {tot[k]}')
                # filas hijas de STA 13 = 14+15+16
                if ap == 'STA':
                    for k in range(6):
                        s = sum(row(d, ap, sc, blk, o)[k] for o in (14, 15, 16))
                        if abs(s - row(d, ap, sc, blk, 13)[k]) > 3:
                            issues += 1
                            print(f'  DESCUADRE hijas STA13 {name} {sc} blk{blk} col{k}')
                # balance estatico: exposicion total constante
            for blk in range(1, 12):
                e0 = sum(row(d, ap, 'act', blk, TOTAL[ap])[0:3])
                for sc2 in ('base', 'adv'):
                    e = sum(row(d, ap, sc2, blk, TOTAL[ap])[0:3])
                    if abs(e - e0) > 5:
                        print(f'  exposicion no constante {name} {ap} {sc2} blk{blk}: {e0} -> {e}')
    print(f'{name}: descuadres de suma = {issues}')


def metrics(d, blk, bucket):
    E0 = P0 = PA = PB = S30 = S3A = S3B = EA = EI = 0
    for ap, off in BUCKETS[bucket]:
        a = row(d, ap, 'act', blk, off); b = row(d, ap, 'base', blk, off); v = row(d, ap, 'adv', blk, off)
        e = sum(a[0:3]); E0 += e; P0 += sum(a[3:6]); S30 += a[2]
        PA += sum(v[3:6]); PB += sum(b[3:6]); S3A += v[2]; S3B += b[2]; EA += sum(v[0:3])
        if ap == 'IRB':
            EI += e
    return dict(E0=E0, P0=P0, PA=PA, PB=PB, S30=S30, S3A=S3A, S3B=S3B, EA=EA, EI=EI)


def pct(x):
    return f'{x * 100:.2f} %'.replace('.', ',')


def fmt(x):
    return f'{x:,.0f}'.replace(',', '.')


out = {}
for f in sys.argv[1:]:
    d = json.load(open(f))
    check(d, f)
    names = {int(b): v[0] for b, v in d['labels']['IRB'].items()}
    sta = {int(b): v[0] for b, v in d['labels']['STA'].items()}
    assert names == sta, (names, sta)
    names[1] = 'GRUPO'
    out[f] = {}
    for bucket in BUCKETS:
        print(f'\n### {f} · {bucket}')
        print('| País | Exposición inicial (M€) | Provisiones iniciales (M€) | Prov. 2027 adv (M€) | Prov. 2027 base (M€) | S3 inicial | ΔProv adv / exp. | ΔProv base / exp. | Adv − base | S3 2027 adv | Peso IRB |')
        print('|---|---|---|---|---|---|---|---|---|---|---|')
        for blk in range(1, 12):
            m = metrics(d, blk, bucket)
            E0 = m['E0']
            ra = (m['PA'] - m['P0']) / E0; rb = (m['PB'] - m['P0']) / E0
            out[f][(names[blk], bucket)] = (ra, rb, m)
            print(f"| {names[blk]} | {fmt(E0)} | {fmt(m['P0'])} | {fmt(m['PA'])} | {fmt(m['PB'])} | {pct(m['S30'] / E0)} | {pct(ra)} | {pct(rb)} | {pct(ra - rb)} | {pct(m['S3A'] / m['EA'])} | {m['EI'] / E0 * 100:.0f} % |")

# cocientes
print('\n### Cocientes')
S, B = sys.argv[1], sys.argv[2]
for bucket in BUCKETS:
    for bank in (S, B):
        mx = out[bank][('MEXICO', bucket)]; es = out[bank][('SPAIN', bucket)]
        print(f'{bucket} {bank} MX/ES adv: {mx[0]*100:.4f} / {es[0]*100:.4f} = {mx[0]/es[0]:.3f}; base: {mx[1]*100:.4f}/{es[1]*100:.4f} = {mx[1]/es[1]:.3f}; adv-base: {(mx[0]-mx[1])/(es[0]-es[1]):.3f}')
    for c in ('SPAIN', 'MEXICO', 'UNITED STATES', 'UNITED KINGDOM', 'FRANCE', 'GRUPO'):
        if (c, bucket) in out[B] and (c, bucket) in out[S]:
            b = out[B][(c, bucket)]; s = out[S][(c, bucket)]
            print(f'{bucket} {c} BBVA/SAN adv: {b[0]*100:.4f} / {s[0]*100:.4f} = {b[0]/s[0]:.3f}; base {b[1]/s[1]:.3f}; adv-base {(b[0]-b[1])/(s[0]-s[1]):.3f}')
