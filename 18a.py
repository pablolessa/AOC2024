doexample = False

data = '18data.txt'
example = '18example.txt'

if doexample:
    archivo = open(example)
    N = 7 # tamaño grilla
    num_obs = 12 # número de obstaculos
else:
    archivo = open(data)
    N = 71 # tamaño grilla
    num_obs = 1024 # número de obstaculos


filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]


lista_obstaculos = [f.split(',') for f in filas]
lista_obstaculos = [(int(x),int(y)) for x,y in lista_obstaculos]

obstaculo = {}
for i in range(N):
    for j in range(N):
        obstaculo[(i,j)] = False

for x,y in lista_obstaculos[:num_obs]:
    obstaculo[(x,y)] = True

def mostrar():
    for i in range(N):
        f = []
        for j in range(N):
            if obstaculo[(j,i)]:
                f.append('#')
            else:
                f.append('.')
        print(' '.join(f))

mostrar()


start = (0,0)
target = (N-1,N-1)
infinity  = N**2 + 1 # ningún lugar alcanzable está a más de esta distancia

dist = []
dist.append([start])
obstaculo[start] = True
cur_dist = 0
while len(dist[cur_dist]) > 0:
    dist.append([])
    for x,y in dist[cur_dist]:
        if (x,y) == target:
            print(cur_dist)
            exit()
        else:
            for incx,incy in [(-1,0),(1,0),(0,-1),(0,1)]:
                vecinox = x+incx
                vecinoy = y+incy
                vecino = (vecinox,vecinoy)
                if 0 <= vecinox < N and 0 <= vecinoy < N and not obstaculo[vecino]:
                    dist[cur_dist+1].append(vecino)
                    obstaculo[vecino] = True
    cur_dist += 1
