data = '13data.txt'
example = '13example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas if f.strip() != '']

def parsear(x):
    x = x.split()
    a = x[-2].replace('X','').replace('Y','').replace('=','').replace('+','').replace(',','')
    b = x[-1].replace('X','').replace('Y','').replace('=','').replace('+','').replace(',','')
    return int(a),int(b)

def solve(a,b,c,d,x,y):
    det = a*d-b*c
    u,v = (d*x-b*y)/det, (-c*x+a*y)/det
    if abs(u-int(u)) < 0.001 and abs(v-int(v)) < 0.001:
        return 3*int(u)+int(v)
    else:
        return 0 


resultado = 0
for i in range(len(filas)//3):
    a,c = parsear(filas[3*i])
    b,d = parsear(filas[3*i+1])
    x,y = parsear(filas[3*i+2])
    x,y = x+10000000000000,y+10000000000000
#    print(f'[{a},{b}][x] = [{x}]')
#    print(f'[{c},{d}][y] = [{y}]')
    resultado += solve(a,b,c,d,x,y)

print(resultado)
