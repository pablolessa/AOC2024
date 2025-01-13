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

result = 0
for x in terminal:
    result += evaluate(x) << int(x[1:])

print(result)

