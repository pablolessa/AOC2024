data = '17data.txt'
example = '17exampleb.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

A = int(filas.pop(0).split()[-1])
B = int(filas.pop(0).split()[-1])
C = int(filas.pop(0).split()[-1])
filas.pop(0)
prog = [int(x) for x in filas.pop(0).split()[-1].split(',')]


def f(a):
   b = a%8
   b = b^5
   c = a>>b
   b = b^6
   a = a>>3
   b = b^c
   return b%8

from collections import defaultdict

preimages = defaultdict(list)

for i in range(1024):
    preimages[f(i)].append(i)

def pastable(x,y):
    '''Do x and y share the middle 7 digits'''
    return (x % 2**7) == (y>>3)

def paste(x,y):
    return (x<<3) | y

assert(pastable(0b1101010101, 0b1010101110))

solution_list = []

def g(sol = []):
    i = len(sol)
    if i == 0:
        x = prog[i]
        for y in preimages[x]:
            sol.append(y)
            g(sol)
            sol.pop()
    elif i == len(prog):
        global solution_list
        solution_list.append(tuple(sol))
    else:
        x = prog[i]
        for y in preimages[x]:
            if pastable(y,sol[-1]):
                sol.append(y)
                g(sol)
                sol.pop()

g([])

def paste_sol(t):
    result = 0
    for i,x in enumerate(t):
        result = result | (x << 3*i)
    return result

pasted_list = [paste_sol(t) for t in solution_list]
pasted_list.sort()
assert(pasted_list[0] < pasted_list[-1])
print(pasted_list[0])
print(len(pasted_list))
