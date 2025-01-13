data = '15data.txt'
smallexample = '15examplea.txt'
largeexample = '15exampleb.txt'
examplec = '15examplec.txt'
example = largeexample
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

i = 0
tablero = []
while filas[i] != '':
    tablero.append(list(filas[i].replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')))
    i += 1

def mostrar():
    for t in tablero:
        print(''.join(t))
    print()

i += 1
movimientos = ''.join([x for x in filas[i:] if x != ''])

inci = {'v':1, '^':-1, '<':0, '>':0}
incj = {'v':0, '^':0, '<':-1, '>':1}
movsi = [inci[c] for c in movimientos]
movsj = [incj[c] for c in movimientos]

def puede_mover_horizontal(i,j,di,dj):
    siguiente = tablero[i+di][j+dj]
    if siguiente == '#':
        return False
    elif siguiente == '.':
        return True
    else:
        return puede_mover(i+di,j+dj,di,dj)

def puede_mover_vertical(i,j,di,dj):
    f = puede_mover_vertical
    siguiente = tablero[i+di][j+dj]
    if siguiente == '#':
        return False
    elif siguiente == '.':
        return True
    elif siguiente == '[':
        return f(i+di,j+dj,di,dj) and f(i+di,j+dj+1,di,dj)
    elif siguiente == ']':
        return f(i+di,j+dj,di,dj) and f(i+di,j+dj-1,di,dj)


def puede_mover(i,j,di,dj):
    if di != 0:
        return puede_mover_vertical(i,j,di,dj)
    elif dj != 0:
        return puede_mover_horizontal(i,j,di,dj)

def mover_vertical(i,j,di,dj):
    f = mover_vertical
    actual = tablero[i][j]
    tablero[i][j] = '.'
    siguiente = tablero[i+di][j+dj]
    if siguiente == '[':
        f(i+di,j+dj,di,dj)
        f(i+di,j+dj+1,di,dj)
    elif siguiente == ']':
        f(i+di,j+dj,di,dj)
        f(i+di,j+dj-1,di,dj)
    tablero[i+di][j+dj] = actual
    
def mover_horizontal(i,j,di,dj):
    actual = tablero[i][j]
    tablero[i][j] = '.'
    siguiente = tablero[i+di][j+dj]
    if siguiente != '.':
        mover(i+di,j+dj,di,dj)
    tablero[i+di][j+dj] = actual

def mover(i,j,di,dj):
    if di != 0:
        mover_vertical(i,j,di,dj)
    elif dj != 0:
        mover_horizontal(i,j,di,dj)

for i in range(len(tablero)):
    for j in range(len(tablero[0])):
        if tablero[i][j] == '@':
            posi,posj = i,j

mostrar()
for k in range(len(movsi)):
    print(f'Move {movimientos[k]}:')
    di,dj = movsi[k],movsj[k]
    if puede_mover(posi,posj,di,dj):
        mover(posi,posj,di,dj)
        posi += di
        posj += dj
    mostrar()

resultado = 0
for i in range(len(tablero)):
    for j in range(len(tablero[0])):
        if tablero[i][j] == '[':
            resultado += 100*i + j
print(resultado)
