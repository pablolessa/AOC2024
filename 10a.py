data = '10data.txt'
example = '10example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

for f in filas:
    print(f)

def score(board,i,j):
    m,n = len(board),len(board[0])
    if board[i][j] != '0':
        return 0
    neighbors = [set([(i,j)])]
    for level in range(1,10):
        newguys = set()
        for x,y in neighbors[level-1]:
            for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0 <= a < m and 0 <= b < n and board[a][b] == str(level):
                    newguys.add((a,b))
        neighbors.append(newguys)
    return len(neighbors[9])

m,n = len(filas),len(filas[0])
resultado = 0
for i in range(m):
    for j in range(n):
        resultado += score(filas,i,j)

print(resultado)

