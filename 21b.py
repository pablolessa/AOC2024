from functools import cache
data = '21data.txt'
example = '21example.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

numeric = ['789','456','123','*0A']
invnumeric = {}
for i in range(len(numeric)):
    for j in range(len(numeric[0])):
        if numeric[i][j] != '*':
            invnumeric[numeric[i][j]] = (i,j)

def numeric_paths(x,y):
    ix,jx = invnumeric[x]
    iy,jy = invnumeric[y]
    imin = min(ix,iy)
    jmax = max(jx,jy)
    result = []
    if jx < jy:
        result.append(('>',abs(jx-jy)))
    if ix > iy:
        result.append(('^',abs(ix-iy)))
    if jx > jy:
        result.append(('<',abs(jx-jy)))
    if ix < iy:
        result.append(('v',abs(ix-iy)))
    yield result
    if len(result) == 2 and numeric[ix][jy] != '*' and numeric[iy][jx] != '*':
        yield (result[1],result[0])

directional = ['*^A','<v>']
invdirectional = {}
for i in range(len(directional)):
    for j in range(len(directional[0])):
        if directional[i][j] != '*':
            invdirectional[directional[i][j]] = (i,j)

def directional_paths(x,y):
    ix,jx = invdirectional[x]
    iy,jy = invdirectional[y]
    result = []
    if ix < iy:
         result.append(('v',abs(ix-iy)))
    if jx < jy:
         result.append(('>',abs(jx-jy)))
    if ix > iy:
         result.append(('^',abs(ix-iy)))
    if jx > jy:
         result.append(('<',abs(jx-jy)))
    yield tuple(result)
    if len(result) == 2 and directional[ix][jy] != '*' and directional[iy][jx] != '*':
        yield (result[1],result[0])

@cache
def directional_dist(x,y,leadingas = 0):
    if leadingas == 0:
        results = []
        for path in directional_paths(x,y):
            results.append(sum([i for d,i in path])) 
        return min(results)
    else:
        results = []
        for path in directional_paths(x,y):
            result = 0
            current = 'A'
            for target,i in path:
                result += directional_dist(current,target,leadingas-1) + i
                current = target
            result += directional_dist(current,'A',leadingas-1)
            results.append(result)
        return min(results)

@cache
def numeric_dist(x,y,leadingas = 0):
    if leadingas == 0:
        results = []
        for path in numeric_paths(x,y):
            results.append(sum([i for d,i in path])) 
        return min(results) 
    else:
        results = []
        for path in numeric_paths(x,y):
            result = 0
            current = 'A'
            for target,i in path:
                result += directional_dist(current,target,leadingas-1) + i
                current = target
            result += directional_dist(current,'A',leadingas-1)
            results.append(result)
        return min(results)

@cache
def cost(s, leadingas = 0):
    current = 'A'
    result = 0
    for c in s:
        result += numeric_dist(current,c,leadingas) + 1
        current =  c
    return result

leading = 25
resultado = 0
for f in filas:
    x,y = cost(f,leading), int(f[:-1])
    print(f'{x} * {y}')
    resultado += x*y

print(resultado)
