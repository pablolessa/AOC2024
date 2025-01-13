archivo = open('04data.txt','r')
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

cuentan = ['MAS','SAM']
m,n = len(filas),len(filas[0])
resultado = 0
for i in range(m-2):
    for j in range(n-2):
        a = filas[i][j]+filas[i+1][j+1]+filas[i+2][j+2]
        b = filas[i+2][j]+filas[i+1][j+1]+filas[i][j+2]
        if a in cuentan and b in cuentan:
            resultado += 1

print(resultado)
