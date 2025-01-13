data = '23data.txt'
example = '23example.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

sides = set()
vertices = set()
for f in filas:
    a,b = f.split('-')
    sides.add((a,b))
    sides.add((b,a))
    vertices.add(a)
    vertices.add(b)

from collections import defaultdict

neighbors = defaultdict(set)
for v in vertices:
    neighbors[v] = set([x for x in vertices if (v,x) in sides])

def BronKerbosch(clique, candidates, excluded):
    if candidates == set() and set() == excluded:
        yield clique
    else:
        while candidates != set():
            v = candidates.pop()
            setv = set([v])
            n = neighbors[v]
            for c in BronKerbosch(clique.union(setv), candidates.intersection(n), excluded.intersection(n)):
                yield c
            excluded.add(v)

record = 0
record_clique = set()
for clique in BronKerbosch(set(),vertices,set()):
    if len(clique) > record:
        record = len(clique)
        record_clique = clique

l = list(record_clique)
l.sort()
print(','.join(l))
