data = '22data.txt'
example = '22example.txt'
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

print(sum([evolven(x,2000) for x in nums]))

