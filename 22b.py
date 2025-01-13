data = '22data.txt'
example = '22example.txt'
example2 = '22example2.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

nums = [int(f) for f in filas]

def mix(x,y):
    return x^y

assert(mix(42,15) == 37)

def prune(x):
    return x % 16777216

assert(prune(100000000) == 16113920)

def evolve(x):
    x = mix(64*x,x)
    x = prune(x)
    x = mix(x//32,x)
    x = prune(x)
    x = mix(2048*x,x)
    x = prune(x)
    return x

test_vals = [15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432, 5908254]

x = 123
test_vals2 = []
for i in range(10):
    x = evolve(x)
    test_vals2.append(x)

assert(test_vals == test_vals2)

def evolven(x,n = 1):
    for i in range(n):
        x = evolve(x)
    return x

def price(x):
    return x%10
test_vals3 = [3, 0, 6, 5, 4, 4, 6, 4, 4, 2]
assert(test_vals3 == [price(x) for x in [123]+test_vals2[:-1]])

from itertools import product
strategies = set(product(range(-19,20),repeat=4))
score = dict([(s,0) for s in strategies])

def update(x):
    appeared = set()
    a = x
    b = evolve(a)
    c = evolve(b)
    d = evolve(c)
    e = evolve(d)
    current = (price(b)-price(a),price(c)-price(b),price(d)-price(c),price(e)-price(d))
    for i in range(2000-4):
        if current not in appeared:
            appeared.add(current)
            score[current] += price(e)
        a,b,c,d,e = b,c,d,e,evolve(e)
        current = (price(b)-price(a),price(c)-price(b),price(d)-price(c),price(e)-price(d))

for x in nums:
    print(x)
    update(x)

print(f'Max score = {max([score[s] for s in strategies])}')
