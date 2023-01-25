import re

def processa_nome(m):
    primeiro = m[1]
    ultimo = m[2].lstrip()
    return f"{ultimo},{primeiro[0]}."

text = open('exemplo-utf8.bib', 'r', encoding='UTF-8')
file = open('indice.html', 'w', encoding='UTF-8')
autores=[]
file.write('<!DOCTYPE  HTML PUBLIC>\n<HTML>\n   <HEAD>\n      <meta charset="UTF-8"/>\n      <TITLE>Indíce de autores</TITLE>\n   </HEAD>\n   <BODY>')
for line in text:
    authors = re.findall(r'^(\s)*(?i:author)(\s)*=(\s)*((\{|\")[^}|"]*(\}|\"))', line)
    for a in authors:
        if a!=None and (a[3] not in autores):
            autores.append(a[3][1:len(a[3])-1])

resultado=[]
for element in autores:
   for i in element.split(' and '):
       resultado.append(i)
resultado.sort()
#print(resultado)

#retirar elementos repetidos da lista de autores
repetidos = []
[repetidos.append(x) for x in resultado if x not in repetidos]
repetidos.sort()
#print(repetidos)

#colocar os abreviados numa lista
abreviados = []
for element in resultado:
    e = re.match('(.).(.).(.)(.)', element, flags=0)
    if e!= None and e not in abreviados:
        abreviados.append(e)
#print(abreviados)

#por os nomes que nao sao abreviaturas numa lista
nome = []
for r in repetidos:
    if r not in abreviados:
        nome.append(r)

repetidos = []
[repetidos.append(x) for x in nome if x not in repetidos]
repetidos.sort()

file.write('\n      <h1>Author Index</h1>')
for r in repetidos:
    file.write(f'<P>{r} \n</P>')
