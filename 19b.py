data = '19data.txt'
example = '19example.txt'

archivo = open(data)

filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

patterns = set([x.strip() for x in filas.pop(0).split(',')])
print(f'patterns = {patterns}')

from collections import defaultdict

graph = defaultdict(set)

for x in patterns:
    for i in range(len(x)):
        graph[x[:i]].add(x[:i+1])
    graph[x].add('')

terminal_state = defaultdict(bool)

for x in graph:
    if '' in graph[x]:
        graph[x].update(graph[''])
        graph[x].remove('')
        terminal_state[x] = True


print(f'graph = {graph}')

def label(x):
    return x[-1]

from functools import cache

@cache
def makable(s,state=''):
    if s == '':
        if terminal_state[state]:
            return 1
        else:
            return 0
    else:
        steps = [y for y in graph[state] if label(y) == s[0]]
        if steps == []:
            return 0
        else:
            return sum([makable(s[1:],y) for y in steps])

filas.pop(0)

desired = []
for f in filas:
    desired.append(f)

print(f'desired = {desired}')
print()
print(sum([makable(x) for x in desired]))

