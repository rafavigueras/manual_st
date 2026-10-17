import re, sys
PER={'IRB':21,'STA':24}
def num(t):
    t=t.replace(',','')
    if t.endswith('%'): return float(t[:-1])/100
    if t.endswith('-'): t=t[:-1]
    try: return float(t)
    except: return None
def parse(path, home):
    lines=open(path,encoding='utf-8').read().split('\n')
    approach=kind=None; vals={}; labels={}
    for l in lines:
        m=re.search(r'Credit risk (IRB|STA)',l)
        if m: approach=m.group(1)
        if re.search(r'Securitisation|Sovereign',l) and 'Stress Test' in l: approach=None
        if 'Restated' in l: kind='act'
        if 'Baseline Scenario' in l: kind='base'
        if 'Adverse Scenario' in l: kind='adv'
        if not approach: continue
        per=PER[approach]
        mm=re.match(r'^\s*(\d+)\s+([A-Z]{3,}(?: [A-Z]{2,})*)\s{2,}',l)
        if mm and mm.group(2)!='TOTAL':
            labels[(approach,(int(mm.group(1))-1)//per+1)]=mm.group(2)
        mt=re.match(r'^\s*(\d+)\s+TOTAL\s+[\d,]',l)
        if mt and int(mt.group(1))%per==0:
            toks=[x for x in (num(t) for t in l.split()[2:]) if x is not None]
            vals[(approach,kind,int(mt.group(1))//per)]=toks[-7:]
    d={}
    for (ap,kd,i),v in vals.items():
        lab=labels.get((ap,i)) or labels.get(('STA',i)) or ('GRUPO' if i==1 else (home if i==2 else f'?{i}'))
        d[(ap,kd,lab)]=v
    return d
for f in sys.argv[1:]:
    d=parse(f,'SPAIN')
    countries=sorted({k[2] for k in d})
    print('##',f.split('/')[-1])
    print(f"{'pais':16}{'expo0':>10}{'S3%0':>7}{'prov0':>8}{'prov27adv':>10}{'dProvAdv/expo':>14}{'dProvBase/expo':>15}{'S3%27adv':>9}{'IRBshare':>9}")
    for c in countries:
        E0=P0=PA=PB=S30=S3A=0; EI=0
        for ap in ('IRB','STA'):
            a=d.get((ap,'act',c)); b=d.get((ap,'base',c)); v=d.get((ap,'adv',c))
            if not a or not v: continue
            e=sum(a[0:3]); E0+=e; P0+=sum(a[3:6]); S30+=a[2]
            PA+=sum(v[3:6]); S3A+=v[2]; PB+=sum(b[3:6]) if b else 0
            if ap=='IRB': EI+=e
        if E0==0: continue
        print(f"{c:16}{E0:10,.0f}{S30/E0:7.2%}{P0:8,.0f}{PA:10,.0f}{(PA-P0)/E0:14.2%}{(PB-P0)/E0:15.2%}{S3A/E0:9.2%}{EI/E0:9.0%}")
