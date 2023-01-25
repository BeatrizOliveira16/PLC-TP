import re

text=open('exemplo-utf8.bib', 'r', encoding='UTF-8')
file=open('doc.html','w',encoding='UTF-8')
d={}
chaves={}
autores={}
titulos={}
for line in text:
  l = re.findall(r'^@(?i:[a-z]*)', line)
  key = re.findall(r'{(\w+|(\w+[:-]\w+)),$', line)
  authors = re.findall(r'^(\s)*(?i:author)(\s)*=(\s)*((\{|\")[^}|"]*(\}|\"))', line)
  title= re.findall(r'^(\s)*(?i:title)(\s)*=(\s)*((\{|\")[^}|"]*(\}|\"))', line)
  for x in l:
    if x != None:
      d[x.lower()] = d.get(x.lower(),0)+1
  for k in key:
    if k != None:
      if x.lower() not in chaves:
        chaves[x.lower()] = []
        if type(k) == tuple:
            chaves[x.lower()].append(str(k[0]))
        else:
             chaves[x.lower()].append(str(k))
      else:
          if type(k) == tuple:
            chaves[x.lower()].append(str(k[0]))
          else:
            chaves[x.lower()].append(str(k))
  for a in authors:
    if a != None:
        if x.lower() not in autores:
          autores[x.lower()] = []
        autores[x.lower()].append(str(a[3][1:len(a[3])-2]))
  for t in title:
    if t != None:
      if x.lower() not in titulos:
        titulos[x.lower()]=[]
      titulos[x.lower()].append(str(t[3][1:len(a[3])-2]))
print
tempo = lambda t: 's' if t > 1 else ''
for k, v in d.items():
  file.write(f'\n      <P>The category {k} appears {v} time{tempo(v)}')

for c in chaves.values():
  file.write(f'\n      <P>The the following keys: {c}.</P>')

for a in autores.values():
  file.write(f'\n      <P>The authors mentioned are {a}.</P>\n')

for ti in titulos.values():
  file.write(f'\n      <P>The titles referenced are {ti}.</P>')
text.close()
file.close()
