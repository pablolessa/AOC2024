import cProfile
pr = cProfile.Profile()
pr.enable()

data = '06data.txt'
example = '06example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [list(f.strip()) for f in filas]

m,n = len(filas),len(filas[0])
def find_guard(board):
    guard = '^V<>'
    for i,f in enumerate(board):
        for j,c in enumerate(f):
            if c in guard:
                return i,j

i,j = find_guard(filas)
inc = {'^':(-1,0),'V':(1,0),'<':(0,-1),'>':(0,1)}
inci,incj = inc[filas[i][j]]

def getpath(board,i,j,inci,incj):
    positions = []
    while (i,j,inci,incj) not in positions:
        positions.append((i,j,inci,incj))
        newi,newj = i+inci,j+incj
        if newi not in range(m) or newj not in range(n):
            return set([(a,b) for (a,b,c,d) in positions])
        elif board[newi][newj] == '#':
            inci,incj = incj,-inci
        else:
            i,j = newi,newj

path = getpath(filas,i,j,inci,incj) 

def simulate(board,i,j,inci,incj):
    positions = set()
    while (i,j,inci,incj) not in positions:
        positions.add((i,j,inci,incj))
        newi,newj = i+inci,j+incj
        if (newi not in range(m)) or (newj not in range(n)):
            return 'Finished'
        elif board[newi][newj] == '#':
            inci,incj = incj,-inci
        else:
            i,j = newi,newj
    return 'Looped'

resultado = 0
for x,y in path:
    c = filas[x][y]
    if c == '.': 
        filas[x][y] = '#'
        if simulate(filas,i,j,inci,incj) == 'Looped':
            resultado += 1
        filas[x][y] = '.'

print(resultado)

pr.disable()
pr.print_stats()
