from functools import cache
data = '21data.txt'
example = '21example.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

aux_module = __import__('21gen')
readmachine = aux_module.readmachine
machine = '21controlcontrolnumeric.txt'
start,states,transition,output = readmachine(machine)

from collections import defaultdict
infinity = 300
distance = defaultdict(dict)
for x in states:
    for y in states:
        distance[x][y] = infinity

for x in states:
    distance[x][x] = 0

for i in range(infinity):
    for x in states:
        for y in states:
            for z in transition[y]:
                w = transition[y][z]
                distance[x][w] = min(distance[x][w],distance[x][y]+1)

def shortest(s1,s2):
    '''shortest sequence of inputs leading from s1 to s2'''
    d = distance[s1][s2]
    if d == 0:
        return ''
    else:
        for x in transition[s1]:
            if distance[transition[s1][x]][s2] == d-1:
                return x+shortest(transition[s1][x],s2)

def findsequence(s):
    '''shortest sequence to produce s as output'''
    current = start
    result = []
    for c in s:
        x,i = invoutput[c]
        result.append(shortest(current,x)+i)
        current = transition[x][i]
    return ''.join(result)
        
invoutput = {}
for s in output:
    for i in output[s]:
        o = output[s][i]
        invoutput[o] = (s,i)

resultado = 0
for f in filas:
    print(f)
    s = findsequence(f)
    print(s)
    resultado += int(f[:-1])*len(s)
    print(f'{int(f[:-1])} * {len(s)}')
    print()

print(resultado)
