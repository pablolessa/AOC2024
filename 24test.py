small = '24small.txt'
large = '24large.txt'
data = '24data.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

literals = set()
value = {}
f = filas.pop(0)
while f != '':
    a,b = f.split()
    a = a[:-1]
    literals.add(a)
    value[a] = int(b)
    f = filas.pop(0)

equation = {}
for f in filas:
    left, op, right, arrow, result = f.split() 
    equation[result] = (left,op,right)

terminal = set([x for x in equation if x[0] == 'z'])

operation = {'AND': lambda x,y: x & y, 'OR':lambda x,y: x | y, 'XOR': lambda x,y: x ^ y}
def evaluate(term):
    if term in literals:
        return value[term]
    else:
        left,op,right = equation[term]
        return operation[op](evaluate(left),evaluate(right)) 

def setliterals(x,y):
    global value
    for i in range(10):
        value['x0'+str(i)] = (x>>i)&1
    for i in range(10,45):
        value['x'+str(i)] = (x>>i)&1
    for i in range(10):
        value['y0'+str(i)] = (y>>i)&1
    for i in range(10,45):
        value['y'+str(i)] = (y>>i)&1

def testresult(x,y):
    for i in range(10):
        if not evaluate('z0'+str(i)) == ((x+y)>>i)&1:
            return False
    for i in range(10,45):
        if not evaluate('z'+str(i)) == ((x+y)>>i)&1:
            return False
    return True

def exchange(x,y):
    equation[x],equation[y] = equation[y],equation[x]

exchange('bjm','z07')
exchange('hsw','z13')
exchange('skf','z18')
exchange('nvr','wkr')

digits = 6
shift = 25
for x in range(2**digits):
    for y in range(2**digits):
        setliterals(x<< shift,y<<shift)
        if not testresult(x<<shift,y<<shift):
            print(x<<shift,y<<shift)
            exit()

from random import randint
N = 2**8
for k in range(N):
    x,y = randint(0,2**45),randint(0,2**45)
    setliterals(x,y)
    if not testresult(x,y):
        print(x,y)
        exit()
names = ['bjm','z07','hsw','z13','skf','z18','nvr','wkr']
names.sort()
print(','.join(names))
