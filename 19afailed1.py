data = '19data.txt'
example = '19example.txt'

archivo = open(data)

filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

patterns = [x.strip() for x in filas.pop(0).split(',')]
print(f'patterns = {patterns}')

filas.pop(0)

desired = []
for f in filas:
    desired.append(f)

print(f'desired = {desired}')

min_desired = min([len(x) for x in desired])
print(f'min_desired = {min_desired}')


gen = []
gen.append(set(patterns))
i = 0
while min([len(x) for x in gen[i]]) < min_desired:
    gen.append(set())
    for x in gen[i]:
        for y in patterns:
            gen[i+1].add(x+y)
    i += 1

makable = set()
for x in gen:
    makable.update(x)

result = sum([1 for x in desired if x in makable])
print()
print(result)
