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

resultados = []
for x in filas2:
    l = x.split(',')
    if enOrden(l):
        resultados.append(int(l[len(l)//2]))

print(sum(resultados))
