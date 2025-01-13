archivo = open('01data.txt','r')
filas = archivo.readlines()
archivo.close()

lista1 = []
lista2 = []
for f in filas:
    strx,stry = f.split()
    x,y = int(strx),int(stry)
    lista1.append(x)
    lista2.append(y)

from collections import Counter

c = Counter(lista2)

print(sum([c[x]*x for x in lista1]))
