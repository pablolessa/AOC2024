data = '14data.txt'
example = '14example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas if f.strip() != '']

width,height = filas.pop(0).split()
width,height = int(width),int(height)

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

def show():
    for y in range(height):
        l = []
        for x in range(width):
            n = sum([1 for i in range(N) if xcoords[i] == x and ycoords[i] == y])
            if n!= 0:
                l.append(str(n))
            else:
                l.append('.')
        print(''.join(l))

for t in range(7916):
    for i in range(N):
        xcoords[i] += xincs[i]
        ycoords[i] += yincs[i]
        xcoords[i] %= width
        ycoords[i] %= height

show()
'''
from os import system
t = 0
while True:
    s = input()
    if s.strip() == '':
        for i in range(N):
            xcoords[i] += xincs[i]
            ycoords[i] += yincs[i]
            xcoords[i] %= width
            ycoords[i] %= height
        t += 1
    elif s.strip() == 'b':
        for i in range(N):
            xcoords[i] -= xincs[i]
            ycoords[i] -= yincs[i]
            xcoords[i] %= width
            ycoords[i] %= height
        t -= 1
    system('clear')
    print(t)
    show()
'''
