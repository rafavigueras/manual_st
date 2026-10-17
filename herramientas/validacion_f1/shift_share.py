"""Descomposicion mezcla/intensidad de la diferencia BBVA - Santander en hogares+empresas, por pais,
con tres segmentos (hipotecas, resto minorista, empresas). Fuente: CSV EBA ST2025. Uso: python3 shift_share.py <dir_dl>"""
import csv, sys, collections
DL = sys.argv[1]
LEI = {'5493006QMFDDMYWIAM13': 'S', 'K8MS7FD7N5Z2WQ51AZ71': 'B'}
agg = collections.defaultdict(float)
for ap, f, base in (('IRB', 'TRA_CRE_IRB.csv', '2532'), ('STA', 'TRA_CRE_STA.csv', '2533')):
    for r in csv.DictReader(open(f'{DL}/{f}', encoding='utf-8')):
        if r['LEI_Code'] not in LEI or r['Item'] not in (base + '003', base + '004') or r['Perf_status'] != '0' or r['IFRS9_Stages'] not in '123': continue
        sc = {'11': 'act', '3': 'adv', '2': 'base'}.get(r['Scenario'])
        if sc is None or (sc != 'act' and r['Period'] != '202712'): continue
        c = r['Country'] if r['Country_rank'] != '0' else '0'
        agg[(LEI[r['LEI_Code']], ap, sc, c, r['Exposure'], r['Item'][-1])] += float(r['Amount'] or 0)
def t(b, ap, s, c, e, k): return agg.get((b, ap, s, c, e, k), 0.0)
def seg(b, c, s, k):
    m = t(b, 'IRB', s, c, '4150', k) + t(b, 'STA', s, c, '5300', k)
    o = t(b, 'IRB', s, c, '4000', k) - t(b, 'IRB', s, c, '4150', k) + t(b, 'STA', s, c, '4000', k)
    co = t(b, 'IRB', s, c, '3000', k) + t(b, 'STA', s, c, '3000', k) + t(b, 'STA', s, c, '5400', k) + t(b, 'STA', s, c, '5600', k)
    return {'hip': m, 'resto_min': o, 'empresas': co}
for c, n in (('28', 'España'), ('38', 'México'), ('0', 'Grupo')):
    for sc in ('adv', 'base'):
        w = {}; r = {}
        for b in 'SB':
            E = seg(b, c, 'act', '3'); P0 = seg(b, c, 'act', '4'); P1 = seg(b, c, sc, '4')
            tot = sum(E.values())
            w[b] = {k: E[k] / tot for k in E}; r[b] = {k: (P1[k] - P0[k]) / E[k] for k in E}
        LS = sum(w['S'][k] * r['S'][k] for k in w['S']); LB = sum(w['B'][k] * r['B'][k] for k in w['B'])
        mix = sum((w['B'][k] - w['S'][k]) * r['S'][k] for k in w['S'])
        inten = sum(w['B'][k] * (r['B'][k] - r['S'][k]) for k in w['S'])
        print(f"{n} {sc}: pesos S {', '.join(f'{k} {v*100:.1f}%' for k,v in w['S'].items())} | pesos B {', '.join(f'{k} {v*100:.1f}%' for k,v in w['B'].items())}")
        print(f"   tasas S {', '.join(f'{k} {v*100:.2f}%' for k,v in r['S'].items())} | tasas B {', '.join(f'{k} {v*100:.2f}%' for k,v in r['B'].items())}")
        print(f"   total S {LS*100:.2f}% B {LB*100:.2f}% dif {(LB-LS)*100:.2f} pp = mezcla {mix*100:.2f} pp + intensidad {inten*100:.2f} pp")
