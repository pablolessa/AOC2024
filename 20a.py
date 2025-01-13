data = '20data.txt'
example = '20example.txt'

archivo = open(data)

filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

alto,ancho = len(filas),len(filas[0])


for i in range(alto):
    for j in range(ancho):
        if filas[i][j] == 'S':
            camino = [(i,j)]
            break

i,j = camino[0]
lasti,lastj = i,j
while filas[i][j] != 'E':
    for inci,incj in ((-1,0),(1,0),(0,-1),(0,1)):
        if (i+inci,j+incj) != (lasti,lastj) and 0 <= i+inci < alto and 0 <= j + incj < ancho and filas[i+inci][j+incj] in '.E':
            lasti,lastj = i,j
            i,j = i+inci,j+incj
            camino.append((i,j))
            break

posicion = {}
for x,c in enumerate(camino):
    posicion[c] = x

from collections import defaultdict
cheat = defaultdict(int)

for x,c in enumerate(camino):
    i,j = c
    tryi,tryj = i-2,j
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 1
    tryi,tryj = i+2,j
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 1
    tryi,tryj = i,j-2
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 1
    tryi,tryj = i,j+2
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 1
    tryi,tryj = i+1,j+1
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 2
    tryi,tryj = i-1,j+1
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 2
    tryi,tryj = i+1,j-1
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 2
    tryi,tryj = i-1,j-1
    if 0 <= tryi < alto and 0 <= tryj < alto and filas[tryi][tryj] in '.SE' and posicion[(tryi,tryj)] > x+2:
        cheat[posicion[(tryi,tryj)]-x-2] += 2

result = sum([cheat[c] for c in cheat if c >= 100])
print(result)
