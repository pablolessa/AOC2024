archivo = open('05data.txt')
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

i = 0
while filas[i] != '':
    i += 1

filas1 = filas[:i]
filas2 = filas[i+1:]

previos = {}
posteriores = {}
for x in filas1:
    a,b = x.split('|')
    if b in previos.keys():
        previos[b].append(a)
    else:
        previos[b] = [a]
    if a in posteriores.keys():
        posteriores[a].append(b)
    else:
        posteriores[a] = [b]

def enOrden(l):
    for i,x in enumerate(l):
        if x in previos.keys():
            for y in l[i+1:]:
                if y in previos[x]:
                    return False
        if x in posteriores.keys():
            for y in l[:i]:
                if y in posteriores[x]:
                    return False
    return True

def orden(a,b):
    if a in previos.keys() and b in previos[a]:
        return 1
    if a in posteriores.keys() and b in posteriores[a]:
        return -1
    if b in previos.keys() and a in previos[b]:
        return -1
    if b in posteriores.keys() and a in posteriores[b]:
        return 1
    return 0

from functools import cmp_to_key

ordenkey = cmp_to_key(orden)
resultados = []
for x in filas2:
    l = x.split(',')
    if not enOrden(l):
        l.sort(key = ordenkey)
        resultados.append(int(l[len(l)//2]))

print(sum(resultados))
