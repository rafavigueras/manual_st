import zipfile,re,sys,html
def read(path):
    z=zipfile.ZipFile(path)
    ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        x=z.read('xl/sharedStrings.xml').decode()
        for si in re.findall(r'<si>(.*?)</si>',x,re.S):
            ss.append(html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>',si,re.S))))
    wbx=z.read('xl/workbook.xml').decode()
    names=re.findall(r'<sheet [^>]*name="([^"]+)"',wbx)
    rels=z.read('xl/_rels/workbook.xml.rels').decode()
    rid=re.findall(r'<sheet [^>]*r:id="([^"]+)"',wbx)
    tgt=dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"',rels))
    tgt.update({a:b for b,a in re.findall(r'Target="([^"]+)"[^>]*Id="([^"]+)"',rels)})
    out={}
    for n,r in zip(names,rid):
        p='xl/'+tgt[r].lstrip('/').replace('xl/','')
        x=z.read(p).decode()
        rows=[]
        for row in re.findall(r'<row[^>]*>(.*?)</row>',x,re.S):
            cells=[]
            for attrs,body in re.findall(r'<c ([^>]*?)(?:/>|>(.*?)</c>)',row,re.S):
                v=re.search(r'<v>(.*?)</v>',body or '')
                t=re.search(r't="(\w+)"',attrs)
                val=v.group(1) if v else (''.join(re.findall(r'<t[^>]*>(.*?)</t>',body or '')) or None)
                if t and t.group(1)=='s' and val is not None: val=ss[int(val)]
                cells.append(val)
            rows.append(cells)
        out[n]=rows
    return out
