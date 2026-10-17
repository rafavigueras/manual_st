"""Divide la cartera minorista en hipotecas y resto (consumo, tarjetas, pymes minoristas) desde el CSV EBA ST2025.
Hipotecas = IRB 'Retail - Secured by residential real estate' (4150, o 4100 si no hay 4150) + STA 5300.
Resto minorista = IRB 4000 - hipotecas IRB + STA 4000. Uso: python3 retail_split.py <dir_dl>"""
import csv, sys, collections
DL = sys.argv[1]
LEI = {'5493006QMFDDMYWIAM13': 'Santander', 'K8MS7FD7N5Z2WQ51AZ71': 'BBVA'}
CC = {'28': 'España', '38': 'México', '43': 'EE. UU.', '31': 'Brasil', '42': 'Türkiye', '0': 'Grupo'}
agg = collections.defaultdict(float); exps = collections.Counter()
for ap, f, base in (('IRB', 'TRA_CRE_IRB.csv', '2532'), ('STA', 'TRA_CRE_STA.csv', '2533')):
    for r in csv.DictReader(open(f'{DL}/{f}', encoding='utf-8')):
        if r['LEI_Code'] not in LEI or r['Item'] not in (base + '003', base + '004') or r['Perf_status'] != '0': continue
        sc = {'11': 'act', '2': 'base', '3': 'adv'}.get(r['Scenario'])
        if sc is None or (sc != 'act' and r['Period'] != '202712'): continue
        if r['IFRS9_Stages'] not in '123': continue
        c = r['Country'] if r['Country_rank'] != '0' else '0'
        exps[(ap, r['Exposure'])] += 1
        agg[(LEI[r['LEI_Code']], ap, sc, c, r['Exposure'], r['Item'][-1])] += float(r['Amount'] or 0)
print('códigos minoristas IRB vistos:', sorted(e for a, e in exps if a == 'IRB' and e.startswith('4')))
def tot(b, ap, sc, c, ex, k): return agg.get((b, ap, sc, c, ex, k), 0.0)
print('| Banco | País | Segmento | Exposición inicial (M€) | ΔProv adv / exp. | ΔProv base / exp. |')
print('|---|---|---|---|---|---|')
for b in ('Santander', 'BBVA'):
    for c in ('0', '28', '38', '43', '31', '42'):
        if not any(k[0] == b and k[3] == c for k in agg): continue
        mort_ex = '4150' if any(tot(b, 'IRB', 'act', c, '4150', '3') for _ in [0]) else '4100'
        seg = {}
        for s in ('act', 'base', 'adv'):
            for k in ('3', '4'):
                m = tot(b, 'IRB', s, c, mort_ex, k) + tot(b, 'STA', s, c, '5300', k)
                o = tot(b, 'IRB', s, c, '4000', k) - tot(b, 'IRB', s, c, mort_ex, k) + tot(b, 'STA', s, c, '4000', k)
                seg[('Hipotecas', s, k)] = m; seg[('Resto minorista', s, k)] = o
        for sg in ('Hipotecas', 'Resto minorista'):
            E = seg[(sg, 'act', '3')]
            if E < 1: continue
            a = (seg[(sg, 'adv', '4')] - seg[(sg, 'act', '4')]) / E; bb = (seg[(sg, 'base', '4')] - seg[(sg, 'act', '4')]) / E
            print(f"| {b} | {CC[c]} | {sg} | {E:,.0f} | {a*100:.2f} % | {bb*100:.2f} % |".replace(',', '.').replace('.00 %', ',00 %'))
