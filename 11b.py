data = '11data.txt'
example = '11example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
fila = filas[0].strip()

print(fila)

def numdigits(val):
    i = 1
    val //= 10
    while val != 0:
        i += 1
        val //= 10
    return i

def split(val):
    x = 10**(numdigits(val)//2)
    return val//x, val % x

assert(split(1234) == (12,34))

from functools import cache

@cache
def stones(val, steps):
    if steps == 0:
        return 1
    else:
        if val == 0:
            return stones(1,steps-1)
        elif numdigits(val) % 2 == 0:
            left,right= split(val)
            return stones(left,steps-1)+stones(right,steps-1)
        else:
            return stones(2024*val,steps-1)
l = [int(x) for x in fila.split()]
print(l)
print(sum([stones(x,75) for x in l]))


