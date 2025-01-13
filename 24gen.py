small = '24small.txt'
large = '24large.txt'
data = '24data.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

literals = set()
value = {}
f = filas.pop(0)
while f != '':
    a,b = f.split()
    a = a[:-1]
    literals.add(a)
    value[a] = int(b)
    f = filas.pop(0)

equation = {}
for f in filas:
    left, op, right, arrow, result = f.split() 
    equation[result] = (left,op,right)

terminal = set([x for x in equation if x[0] == 'z'])

operation = {'AND': lambda x,y: x & y, 'OR':lambda x,y: x | y, 'XOR': lambda x,y: x ^ y}
def evaluate(term):
    if term in literals:
        return value[term]
    else:
        left,op,right = equation[term]
        return operation[op](evaluate(left),evaluate(right)) 

def alphabet():
    for c in 'abcdefghijklmnopqrstuvwxyz':
        yield c
def count():
    i = 1
    while True:
        yield str(i)
        i += 1
unique = {}
for x in literals:
    unique[x] = alphabet()
unique['OR'] = count()
unique['XOR'] = count()
unique['AND'] = count()

file = open('24graph.dot','w')
file.write('digraph {\n')
for x in equation:
    left,op,right = equation[x]
    if left in literals:
        left += next(unique[left])
    if right in literals:
        right += next(unique[right])
    op += next(unique[op])
    file.write(f'{left} -> {op};\n')
    file.write(f'{right} -> {op};\n')
    file.write(f'{op} -> {x};\n')
file.write('}')
file.close()

import os
os.system('dot -Tps 24graph.dot -O')
os.system('ps2pdf 24graph.dot.ps')

print(f'There are {len([x for x in literals if x[0] == "x"])} x-literals')
print(f'There are {len([x for x in literals if x[0] == "y"])} y-literals')
print(f'There are {len(terminal)} z-terms')
