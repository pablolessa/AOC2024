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

alto,ancho = len(filas),len(filas[0])

antinodes = set()
for antena in antenas:
    n = len(antenas[antena])
    for i in range(n):
        for j in range(i+1,n):
            a,b = antenas[antena][i]
            c,d = antenas[antena][j]
            N = 1 + min(ancho,alto)//max(abs(c-a),abs(d-b))
            for k in range(-N,N+1):
                antinodes.add((a+k*(c-a),b+k*(d-b)))

resultado = 0
for i,j in antinodes:
    if 0 <= i < alto and 0 <= j < ancho:
        resultado += 1

print(resultado)

