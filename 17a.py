data = '17data.txt'
example = '17example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
filas = [f.strip() for f in filas]

A = int(filas.pop(0).split()[-1])
B = int(filas.pop(0).split()[-1])
C = int(filas.pop(0).split()[-1])
print(f'Register A: {A}')
print(f'Register B: {B}')
print(f'Register C: {C}')
print()
filas.pop(0)
prog = [int(x) for x in filas.pop(0).split()[-1].split(',')]

IP = 0 # instruction pointer
std_out = []

print(f'Program: {prog}')

def combo(x):
    if 0 <= x <= 3:
        return x
    elif x == 4:
        return A
    elif x == 5:
        return B
    elif x == 6:
        return C
    else:
        raise(BaseException('Invalid combo operand value'))

def adv():
    global A
    global IP
    A = A >> combo(prog[IP+1])
    IP += 2

def bxl():
    global B
    global IP
    B = B ^ prog[IP+1]
    IP += 2

def bst():
    global B
    global IP
    B = combo(prog[IP+1])%8
    IP += 2

def jnz():
    global IP
    if A == 0:
        IP += 2
    else:
        IP = prog[IP+1]

def bxc():
    global B
    global IP
    B = B ^ C
    IP += 2

def out():
    global IP
    std_out.append(combo(prog[IP+1]) % 8)
    IP += 2

def bdv():
    global B
    global IP
    B = A >> combo(prog[IP+1])
    IP += 2

def cdv():
    global C
    global IP
    C = A >> combo(prog[IP+1])
    IP += 2

instructions = [adv,bxl,bst,jnz,bxc,out,bdv,cdv]

while 0 <= IP < len(prog):
    instructions[prog[IP]]()

print(','.join([str(x) for x in std_out]))
