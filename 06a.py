filename = '06data.txt'
archivo = open(filename)
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

done = False
while not done:
    filas[i][j] = 'X'
    newi,newj = i+inci,j+incj
    if newi not in range(m) or newj not in range(n):
        done = True
    elif filas[newi][newj] == '#':
        inci,incj = incj,-inci
    else:
        i,j = newi,newj

resultado = 0
for f in filas:
    resultado += sum([1 for c in f if c == 'X'])

print(resultado)




