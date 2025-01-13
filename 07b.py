data = '07data.txt'
example = '07example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

def parsear_fila(f):
    l = f.split()
    izq = int(l[0][:-1])
    der = []
    for x in l[1:]:
        der.append(int(x.strip()))
    return izq, tuple(der)

def concat(a,b):
    '''concatenar dos enteros'''
    x = 10
    while x <= b:
        x = 10*x
    return x*a+b

def concat2(a,b):
    return int(str(a)+str(b))

from math import log
def concat3(a,b):
    c = b
    a *= 10
    c //= 10
    while c != 0:
        c //= 10
        a *= 10
    return a+b

def evaluar(par):
    izq,der = par
    if len(der)==1:
        return izq == der[0]
    else:
        parmas = (izq,(der[0]+der[1],)+der[2:])
        parpor = (izq,(der[0]*der[1],)+der[2:])
        parcon = (izq,(concat(der[0],der[1]),)+der[2:])
        return evaluar(parmas) or evaluar(parpor) or evaluar(parcon)

resultado = 0
for f in filas:
    par = parsear_fila(f)
    if evaluar(par):
        resultado += par[0]

print(resultado)
