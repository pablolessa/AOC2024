archivo = open('02data.txt','r')
filas = archivo.readlines()
archivo.close()

def isSafe2(l):
    incs = [l[i+1]-l[i] for i in range(len(l)-1)]
    safeincs = [set([1]),set([2]),set([3]),set([1,2]),set([1,3]),set([2,3]),set([1,2,3])]
    safeincs = safeincs + [set([-i for i in x]) for x in safeincs]
    incs = incs
    if set(incs[1:]) in safeincs:
        return 1
    if set(incs[:-1]) in safeincs:
        return 1
    for i in range(len(incs)-1):
        newincs = incs[:i]+[incs[i]+incs[i+1]]+incs[i+2:]
        if set(newincs) in safeincs:
            return 1
    return 0

assert(isSafe2([7,6,4,2,1]) == 1)
assert(isSafe2([1,2,7,8,9]) == 0)
assert(isSafe2([9,7,6,2,1]) == 0)
assert(isSafe2([1,3,2,4,5]) == 1)
assert(isSafe2([8,6,4,4,1]) == 1)
assert(isSafe2([1,3,6,7,9]) == 1)
assert(isSafe2([5,1,2,3,4,5])==1)
assert(isSafe2([1,2,3,4,5,0])==1)

safe = 0
for f in filas:
    lista = [int(x) for x in f.split()]
    safe += isSafe2(lista)

print(safe)
