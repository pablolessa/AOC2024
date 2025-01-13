data = '16data.txt'
examplea = '16examplea.txt'
exampleb= '16exampleb.txt'
example = exampleb
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

for f in filas:
    print(f)

m,n = len(filas),len(filas[0])

def buscarS():
    for i in range(m):
        for j in range(n):
            if filas[i][j] == 'S':
                return i,j
def buscarE():
    for i in range(m):
        for j in range(n):
            if filas[i][j] == 'E':
                return i,j


Si,Sj = buscarS()
Ei,Ej = buscarE()
print('S: ',Si,Sj)
print('E: ',Ei,Ej)

def infinito():
    return 1000*(4*m*n+1)

from collections import defaultdict
dist = defaultdict(infinito)

S1 = (Si,Sj,0,1)
dist[S1] = 0

def mykey(x):
    return dist[x]

activo = [S1]
while len(activo) != 0:
    activo.sort(key = mykey)
    actual = activo[0]
    i,j,inci,incj = actual 

    vecino = (i,j,-incj,inci)
    if dist[vecino] > dist[actual]:
        dist[vecino] = min(dist[vecino],dist[actual]+1000)
        if vecino not in activo:
            activo.append(vecino)

    vecino = (i,j,incj,-inci)
    if dist[vecino] > dist[actual]:
        dist[vecino] = min(dist[vecino],dist[actual]+1000)
        if vecino not in activo:
            activo.append(vecino)

    if filas[i+inci][j+incj] == '.' or filas[i+inci][j+incj] == 'E':
        vecino = (i+inci,j+incj,inci,incj)
        if dist[vecino] > dist[actual]:
            dist[vecino] = min(dist[vecino],dist[actual]+1)
            if vecino not in activo:
                activo.append(vecino)

    activo.pop(0)

E1 = (Ei,Ej)+(1,0)
E2 = (Ei,Ej)+(-1,0)
E3 = (Ei,Ej)+(0,1)
E4 = (Ei,Ej)+(0,-1)
curdist = min(dist[E1],dist[E2],dist[E3],dist[E4])

Elist = [E1,E2,E3,E4]

path = [[x for x in Elist if dist[x] == curdist]]
l = path[0]
while len(l) != 0:
    l = []
    for x in path[-1]:
        i,j,di,dj = x 
        previo = (i,j,-dj,di)
        if dist[previo] == dist[x] - 1000:
            l.append(previo)
        previo = (i,j,dj,-di)
        if dist[previo] == dist[x]-1000:
            l.append(previo)
        previo = (i-di,j-dj,di,dj)
        if dist[previo] == dist[x]-1:
            l.append(previo)
    path.append(l)

buenos = set()
for l in path:
    for i,j,_,_ in l:
        buenos.add((i,j))
print(len(buenos))




        



