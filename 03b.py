archivo = open('03data.txt','r')
filas = archivo.readlines()
archivo.close()

def isMul(s):
    if s[:4] != 'mul(':
        return False
    if s[-1] != ')':
        return False
    if s[4:-1].find(',') == -1:
        return False
    spl = s[4:-1].split(',')
    if len(spl) != 2:
        return False
    left,right = spl
    if len(left) not in (1,2,3):
        return False
    if len(right) not in (1,2,3):
        return False
    for x in left+right:
        if not x.isdigit():
            return False
    return True

assert(isMul('mul(1,2)'))
assert(not isMul(' mul(1,2)'))
assert(not isMul('mul(1111,2)'))
assert(not isMul('mul(1111,2)2'))
assert(not isMul('mul(*kf1,23)'))

def mul(x,y):
    return x*y

enabled = 1
resultado = 0
for f in filas:
    for i in range(len(f)):
        if f[i:i+4] == 'do()':
            enabled = 1
        if f[i:i+7] == "don't()":
            enabled = 0
        if f[i:i+4] == 'mul(':
            candidates = set([f[i:i+4+x+1+y+1] for x,y in [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]])
            for c in candidates:
                if isMul(c):
                    resultado += enabled*eval(c)
                    break
print(resultado)
