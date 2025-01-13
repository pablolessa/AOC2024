data = '08data.txt'
example = '08example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

from collections import defaultdict

antenas = defaultdict(list)

for i,f in enumerate(filas):
    for j,c in enumerate(f):
        if c.isalpha() or c.isdigit():
            antenas[c].append((i,j))

antinodes = set()
for antena in antenas:
    n = len(antenas[antena])
    for i in range(n):
        for j in range(i+1,n):
            a,b = antenas[antena][i]
            c,d = antenas[antena][j]
            antinodes.add((a-(c-a),b-(d-b)))
            antinodes.add((c+(c-a),d+(d-b)))

m,n = len(filas),len(filas[0])
resultado = 0
for i,j in antinodes:
    if 0 <= i < m and 0 <= j < n:
        resultado += 1

print(resultado)

