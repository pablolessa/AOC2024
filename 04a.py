archivo = open('04data.txt','r')
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

cuentan = ['XMAS','SAMX']
m,n = len(filas),len(filas[0])
resultado = 0
for i in range(m):
    for j in range(n):
       if i+3 < m and filas[i][j]+filas[i+1][j]+filas[i+2][j]+filas[i+3][j] in cuentan:
           resultado += 1
       if j+3 < n and filas[i][j]+filas[i][j+1]+filas[i][j+2]+filas[i][j+3] in cuentan:
           resultado += 1
       if i+3 < m and j+3 < n and filas[i][j]+filas[i+1][j+1]+filas[i+2][j+2]+filas[i+3][j+3] in cuentan:
           resultado += 1
       if i+3 < m and j-3 >= 0 and filas[i][j]+filas[i+1][j-1]+filas[i+2][j-2]+filas[i+3][j-3] in cuentan:
           resultado += 1

print(resultado)
