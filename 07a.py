#import cProfile
#pr = cProfile.Profile()
#pr.enable()

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

def evaluar(par):
    izq,der = par
    if len(der)==1:
        return izq == der[0]
    else:
        parmas = (izq,(der[0]+der[1],)+der[2:])
        parpor = (izq,(der[0]*der[1],)+der[2:])
        return evaluar(parmas) or evaluar(parpor)

resultado = 0
for f in filas:
    par = parsear_fila(f)
    if evaluar(par):
        resultado += par[0]

print(resultado)

#pr.disable()
#pr.print_stats()
