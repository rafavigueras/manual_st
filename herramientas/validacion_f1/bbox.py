import re,sys,html
COUNTRIES={'SPAIN','UNITED','BRAZIL','CHILE','PORTUGAL','GERMANY','POLAND','MEXICO','FRANCE','TURKEY','PERU','COLOMBIA','ITALY','ARGENTINA'}
for path in sys.argv[1:]:
    pages=open(path).read().split('<page ')[1:]
    print('##',path)
    for pi,p in enumerate(pages,1):
        words=[(float(a),float(b),float(c),float(d),html.unescape(w)) for a,b,c,d,w in re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>',p)]
        title=' '.join(w[4] for w in words[:10])
        if 'IRB' not in title: continue
        sc='adv' if any(w[4]=='Adverse' for w in words) else 'base' if any(w[4]=='Baseline' for w in words) else 'act'
        mx=min(w[0] for w in words)
        rows=[(y0,y1,int(w)) for x0,y0,x1,y1,w in words if w.isdigit() and x0<mx+40 and int(w)<300]
        res=[]
        for x0,y0,x1,y1,w in words:
            if w in COUNTRIES and x0<0.5*max(z[2] for z in words):
                yc=(y0+y1)/2
                near=sorted(rows,key=lambda r:abs((r[0]+r[1])/2-yc))[:1]
                res.append(f"{w}->row{near[0][2]}(blk{(near[0][2]-1)//21+1}, dy={abs((near[0][0]+near[0][1])/2-yc):.1f})")
        print(pi,sc,'; '.join(res))
