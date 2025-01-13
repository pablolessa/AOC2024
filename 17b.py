data = '17data.txt'
example = '17exampleb.txt'
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
    return True

def bxl():
    global B
    global IP
    B = B ^ prog[IP+1]
    IP += 2
    return True

def bst():
    global B
    global IP
    B = combo(prog[IP+1])%8
    IP += 2
    return True

def jnz():
    global IP
    if A == 0:
        IP += 2
    else:
        IP = prog[IP+1]
    return True

def bxc():
    global B
    global IP
    B = B ^ C 
    IP += 2
    return True

def out():
    global IP
    std_out.append(combo(prog[IP+1]) % 8)
    IP += 2
    result = std_out == prog[:len(std_out)]
    return result

def bdv():
    global B
    global IP
    B = A >> combo(prog[IP+1])
    IP += 2
    return True

def cdv():
    global C
    global IP
    C = A >> combo(prog[IP+1])
    IP += 2
    return True

instructions = [adv,bxl,bst,jnz,bxc,out,bdv,cdv]

A_backup = 106086382266778-1
B_backup = B
C_backup = C
N = len(prog)
while std_out != prog:
    A_backup += 1
    if A_backup % 1000000 == 0:
        print(f'A_backup = {A_backup}')

    std_out = []
    A = A_backup
    B = B_backup
    C = C_backup
    IP = 0
    while 0 <= IP < N and instructions[prog[IP]]():
        pass

print(A_backup)
