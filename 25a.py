example = '25example.txt'
data = '25data.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

assert((1+len(filas))%8 == 0)
N = (1+len(filas))//8
width = 5
space = 5

keys = set()
locks = set()
def process(l):
    global keys
    global locks
    hashtags = [0]*width
    for f in l:
        for i,c in enumerate(f):
            if c == '#':
                hashtags[i] += 1
    if l[0] == '#'*width:
#        print('Lock')
        locks.add(tuple([x-1 for x in hashtags]))
    else:
#        print('Key')
        assert(l[-1] == '#'*width)
        keys.add(tuple([x-1 for x in hashtags]))
#    for f in l:
#        print(f)
#    print(tuple([x-1 for x in hashtags]))
#    print()

for i in range(N):
    process(filas[8*i:8*i+7])

result = 0
for lock in locks:
    for key in keys:
        if max([x+y for x,y in zip(lock,key)]) <= space:
            result += 1
print(result)
