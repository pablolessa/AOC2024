data = '12data.txt'
example = '12example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

m,n = len(filas), len(filas[0])

def neighbors(p):
    i,j = p
    x,y = i+1,j
    if 0 <= x < m and 0 <= y < n:
        if filas[x][y] == filas[i][j]:
            yield x,y
    x,y = i-1,j
    if 0 <= x < m and 0 <= y < n:
        if filas[x][y] == filas[i][j]:
            yield x,y
    x,y = i,j+1
    if 0 <= x < m and 0 <= y < n:
        if filas[x][y] == filas[i][j]:
            yield x,y
    x,y = i,j-1
    if 0 <= x < m and 0 <= y < n:
        if filas[x][y] == filas[i][j]:
            yield x,y

regions = [set([(0,0)])]
for i in range(m):
    for j in range(n):
        myregion = set([(i,j)])
        for x,y in neighbors((i,j)):
            for r in regions:
                if (x,y) in r:
                    myregion.update(r)
        regions = [myregion] + [r for r in regions if r.intersection(myregion) == set()]


def perimeter(r):
    result = 0
    for x,y in r:
       if (x+1,y) not in r:
            result += 1
       if (x-1,y) not in r:
            result += 1
       if (x,y+1) not in r:
            result += 1
       if (x,y-1) not in r:
            result += 1
    return result

assert(perimeter(set([(0,0),(1,0),(2,0)]))== 8)
assert(perimeter(set([(0,0),(1,0),(0,1),(1,1)]))== 8)

resultado = 0
for r in regions:
    resultado += len(r) * perimeter(r)

print(resultado)
