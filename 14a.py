data = '14data.txt'
example = '14example.txt'
archivo = open(example)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas if f.strip() != '']

width,height = filas.pop(0).split()
width,height = int(width),int(height)
print(f'ancho = {width},alto = {height}')

xcoords = []
ycoords = []
xincs = []
yincs = []
for f in filas:
    a,b = f.split()
    a,b = a[2:],b[2:]
    x,y = eval(a)
    v,w = eval(b)
    xcoords.append(x)
    ycoords.append(y)
    xincs.append(v)
    yincs.append(w)

N = len(xcoords)
print(xcoords)
print(xincs)
print()
T = 100
for i in range(T):
    for i in range(N):
        xcoords[i] += xincs[i]
        ycoords[i] += yincs[i]
        xcoords[i] %= width
        ycoords[i] %= height

for y in range(height):
    l = []
    for x in range(width):
        n = sum([1 for i in range(N) if xcoords[i] == x and ycoords[i] == y])
        if n!= 0:
            l.append(str(n))
        else:
            l.append('.')
    print(''.join(l))

def quad1(x,y):
    if x < width//2 and y < height//2:
        return 1
    else:
        return 0

def quad2(x,y):
    if x > width//2 and y < height//2:
        return 1
    else:
        return 0


def quad3(x,y):
    if x < width//2 and y > height//2:
        return 1
    else:
        return 0

def quad4(x,y):
    if x > width//2 and y > height//2:
        return 1
    else:
        return 0

q1,q2,q3,q4 = 0,0,0,0
for i in range(N):
    q1 += quad1(xcoords[i],ycoords[i])
    q2 += quad2(xcoords[i],ycoords[i])
    q3 += quad3(xcoords[i],ycoords[i])
    q4 += quad4(xcoords[i],ycoords[i])

print(q1*q2*q3*q4)

