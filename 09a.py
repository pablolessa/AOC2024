data = '09data.txt'
example = '09example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
tira = filas[0].strip()

def convertir(t):
    i = 0
    l = []
    while i < len(t):
        n = int(t[i])
        if i % 2== 0:
            l = l + [i//2] * n
        else:
            l = l + [-1] * n
        i += 1
    return l

def toString(l):
    s = ''
    for c in l:
        if c == -1:
            s = s+'.'
        else:
            s =  s+str(c)
    return s

def compact(l):
    first = 0
    last = len(l)-1
    while first < last:
        if l[first] == -1 and l[last] != -1:
            l[first],l[last] = l[last],l[first]
        if l[first] != -1:
            first += 1
        if l[last] == -1:
            last -= 1
    return l

def strip(l):
    while len(l) != 0 and l[-1] == -1:
        l.pop()
    return l

def count(l):
    result = 0
    for i,x in enumerate(l):
        result += i*x
    return result

l = convertir(tira)
c = compact(l)
s = strip(c)
print(count(s))
