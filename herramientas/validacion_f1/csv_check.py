"""Recalcula el desglose por pais desde la base de datos CSV de la EBA (full_database ST2025)
y lo compara con el calculo hecho desde los PDF. Uso: python3 csv_check.py <dir_dl> <dir_work>"""
import csv, sys, json, collections
sys.path.insert(0, sys.argv[2])
from xlsx import read
DL, W = sys.argv[1], sys.argv[2]
md = read(DL + '/Metadata_TR.xlsx')
cname = {r[0]: r[1] for r in md['Country'][1:] if r and r[0]}
LEI = {'5493006QMFDDMYWIAM13': 'san', 'K8MS7FD7N5Z2WQ51AZ71': 'bbva'}
# (banco, enfoque, escenario, pais, rank, exposicion, item, stage) -> importe
agg = collections.defaultdict(float)
seen = collections.Counter()
for ap, f, base in (('IRB', 'TRA_CRE_IRB.csv', '2532'), ('STA', 'TRA_CRE_STA.csv', '2533')):
    with open(f'{DL}/{f}', encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            if r['LEI_Code'] not in LEI: continue
            it = r['Item']
            if it not in (base + '003', base + '004'): continue
            sc = {'11': 'act', '2': 'base', '3': 'adv'}.get(r['Scenario'])
            if sc is None: continue
            if sc != 'act' and r['Period'] != '202712': continue
            seen[(LEI[r['LEI_Code']], ap, r['Portfolio'], r['Perf_status'])] += 1
            if r['Perf_status'] != '0': continue
            key = (LEI[r['LEI_Code']], ap, sc, r['Country'], r['Country_rank'], r['Exposure'], 'E' if it.endswith('003') else 'P', r['IFRS9_Stages'])
            agg[key] += float(r['Amount'] or 0)
print('combinaciones portfolio/perf vistas:', sorted(set((k[1], k[2], k[3]) for k in seen)))
ranks = sorted(set((k[0], k[1], k[3], k[4]) for k in agg))
for bank in ('san', 'bbva'):
    print(bank, 'IRB pais por rank:', [(r, cname.get(c, c)) for b, ap, c, r in ranks if b == bank and ap == 'IRB'])
    print(bank, 'STA pais por rank:', [(r, cname.get(c, c)) for b, ap, c, r in ranks if b == bank and ap == 'STA'])
BUCKETS = {'TODO': [('IRB', '0'), ('STA', '0')],
           'HH+NFC': [('IRB', '3000'), ('IRB', '4000'), ('STA', '3000'), ('STA', '4000'), ('STA', '5000')],
           'MINORISTA': [('IRB', '4000'), ('STA', '4000'), ('STA', '5300')],
           'EMPRESAS': [('IRB', '3000'), ('STA', '3000'), ('STA', '5400'), ('STA', '5600')]}
def g(bank, ap, sc, c, rk, ex, kind, st):
    return agg.get((bank, ap, sc, c, rk, ex, kind, st), 0.0)
res = {}
for bank in ('san', 'bbva'):
    keys = sorted(set((c, r) for b, ap, c, r in ranks if b == bank and ap == 'IRB'), key=lambda x: int(x[1]))
    for c, rk in keys:
        for bu, parts in BUCKETS.items():
            E0 = P0 = PA = PB = 0
            for ap, ex in parts:
                for st in '123':
                    E0 += g(bank, ap, 'act', c, rk, ex, 'E', st); P0 += g(bank, ap, 'act', c, rk, ex, 'P', st)
                    PA += g(bank, ap, 'adv', c, rk, ex, 'P', st); PB += g(bank, ap, 'base', c, rk, ex, 'P', st)
            res[(bank, cname.get(c, c) if rk != '0' else 'GRUPO', bu)] = (E0, (PA - P0) / E0 if E0 else None, (PB - P0) / E0 if E0 else None)
# comparar con PDF (recalculo con compute.metrics)
import importlib.util
spec = importlib.util.spec_from_file_location('cp', W + '/compute_lib.py'); cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
maxdiff = 0; n = 0
for bank in ('san', 'bbva'):
    d = json.load(open(f'{W}/{bank}.json'))
    names = {int(b): v[0] for b, v in d['labels']['IRB'].items()}; names[1] = 'GRUPO'
    for blk, nm in names.items():
        csvname = {'UNITED KINGDOM': 'United Kingdom', 'UNITED STATES': 'United States', 'GRUPO': 'GRUPO'}.get(nm, nm.title())
        for bu in BUCKETS:
            m = cp.metrics(d, blk, bu)
            ra = (m['PA'] - m['P0']) / m['E0']
            c = res.get((bank, csvname, bu))
            if c is None:
                print('FALTA en CSV', bank, nm, bu); continue
            n += 1
            dif = max(abs(c[0] - m['E0']) / m['E0'], abs(c[1] - ra) * 100)
            maxdiff = max(maxdiff, dif)
            if abs(c[0] - m['E0']) > 5 or abs(c[1] - ra) > 0.0002:
                print('DIF', bank, nm, bu, 'PDF', round(m['E0']), f'{ra:.4%}', 'CSV', round(c[0]), f'{c[1]:.4%}')
print('comparaciones', n, 'max diferencia relativa (expo) o en pp (ratio):', round(maxdiff, 5))
