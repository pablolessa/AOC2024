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


def border(r):
    outgoing = []
    for x,y in r:
        for (z,w) in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if (z,w) not in r:
                outgoing.append(((x,y,z,w)))
    return outgoing 

def nextto(p,q):
    '''True if two border elements are adjacent on a side'''
    x,y,z,w = p
    x2,y2,z2,w2 = q
    if z-x == z2-x2 and w-y == w2-y2:
        if (x-x2,y-y2) in [(1,0),(-1,0),(0,1),(0,-1)]:
            return True
    return False


def sides(r):
    elems = border(r)
    allsides = []
    for x in elems:
        myside = set([x])
        added = True
        while added:
            added = False
            for y in set(elems)-myside:
                init = False
                for z in myside:
                    if nextto(y,z):
                        init = True
                if init:
                    myside.add(y)
                    added = True
        addit = True
        for s in allsides:
            if s == myside:
                addit= False
        if addit:
            allsides.append(myside) 
    return len(allsides)


for f in filas:
    print(f)

resultado = 0
for r in regions:
    resultado += sides(r)*len(r)

print(resultado)
