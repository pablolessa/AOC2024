archivo = open('02data.txt','r')
filas = archivo.readlines()
archivo.close()

def isSafe(l):
    incs = set([l[i]-l[i+1] for i in range(len(l)-1)])
    safeincs = [set([1]),set([2]),set([3]),set([1,2]),set([1,3]),set([2,3]),set([1,2,3])]
    safeincs = safeincs + [set([-i for i in x]) for x in safeincs]
    if incs in safeincs:
        return 1
    else:
        return 0

assert(isSafe([7,6,4,2,1]) == 1)
assert(isSafe([1,2,7,8,9]) == 0)
assert(isSafe([9,7,6,2,1]) == 0)
assert(isSafe([1,3,2,4,5]) == 0)
assert(isSafe([8,6,4,4,1]) == 0)
assert(isSafe([1,3,6,7,9]) == 1)

safe = 0
for f in filas:
    lista = [int(x) for x in f.split()]
    safe += isSafe(lista)

print(safe)
