import re,sys
PER={'IRB':21,'STA':24}
for path in sys.argv[1:]:
    lines=open(path).read().split('\n'); ap=None; kind=None; found={}
    for l in lines:
        m=re.search(r'Credit risk (IRB|STA)',l)
        if m: ap=m.group(1)
        if re.search(r'Securitisation|Sovereign',l) and 'Stress Test' in l: ap=None
        if 'Restated' in l: kind='act'
        if 'Baseline Scenario' in l: kind='base'
        if 'Adverse Scenario' in l: kind='adv'
        if not ap: continue
        mm=re.match(r'^\s*(\d+)\s+([A-Z]{3,}(?: [A-Z]{2,})*)\s{2,}',l)
        if mm and mm.group(2)!='TOTAL': found.setdefault((ap,(int(mm.group(1))-1)//PER[ap]+1),set()).add((kind,mm.group(2)))
    print(path,'IRB blocks w/o inline label:',[i for i in range(2,12) if ('IRB',i) not in found])
    print(path,'STA blocks w/o inline label:',[i for i in range(2,12) if ('STA',i) not in found])
