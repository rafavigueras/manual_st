import re,sys
PER={'IRB':21,'STA':24}
for path in sys.argv[1:]:
    lines=open(path).read().split('\n')
    ap=kind=None; cur=None; out={}
    for l in lines:
        m=re.search(r'Credit risk (IRB|STA)',l)
        if m: ap=m.group(1)
        if re.search(r'Securitisation|Sovereign',l) and 'Stress Test' in l: ap=None
        if 'Restated' in l: kind='act'
        if 'Baseline Scenario' in l: kind='base'
        if 'Adverse Scenario' in l: kind='adv'
        if not ap: continue
        mr=re.match(r'^\s*(\d+)\s',l)
        if mr: cur=(int(mr.group(1))-1)//PER[ap]+1
        for mm in re.finditer(r'\b([A-Z]{3,}(?: [A-Z]{2,})*)\b',l[:45]):
            w=mm.group(1)
            if w in ('TOTAL','CIU','SME','IRB','STA','EUR'): continue
            out.setdefault((ap,kind,cur),set()).add(w)
    print('##',path)
    for ap in ('IRB','STA'):
        for kind in ('act','base','adv'):
            blocks=sorted(k[2] for k in out if k[0]==ap and k[1]==kind and k[2])
            print(ap,kind,[ (b,sorted(out[(ap,kind,b)])) for b in blocks])
