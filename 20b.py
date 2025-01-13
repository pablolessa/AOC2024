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

for x in range(len(camino)):
    for y in range(x+3,len(camino)):
        path_dist = abs(x-y)
        starti,startj = camino[x]
        endi,endj = camino[y]
        grid_dist = abs(starti-endi) + abs(startj-endj)
        if grid_dist <= min(20,path_dist):
            cheat[path_dist-grid_dist] += 1

#for c in sorted(cheat.keys()):
#    if c >= 50:
#        print(f'There are {cheat[c]} cheats that save {c} picoseconds.')

result = sum([cheat[c] for c in cheat if c >= 100])
print(result)
