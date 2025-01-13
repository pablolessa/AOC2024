machine0 = '21machine0.txt'
machine1 = '21machine1.txt'
machine2 = '21machine2.txt'

from collections import defaultdict

def readmachine(filename):
    file = open(filename)
    filas = [f.strip() for f in file.readlines() if f.strip() != '']
    file.close()
    
    states = set()
    transition = defaultdict(dict)
    output = defaultdict(dict)
    
    c,current = filas[0].split()[0],filas[0].split()[1]
    assert(c == 'state')
    start = current
    states.add(current)
    for f in filas[1:]:
        l = f.split()
        if l[0] == 'state':
            states.add(l[1])
            current = l[1]
        elif l[0] == 'on':
            transition[current][l[1]] = l[3]
            if len(l) == 6:
                output[current][l[1]] = l[5]
    return start, states, transition, output

def reprstate(s):
    if type(s) == tuple:
        return ''.join(s)
    else:
        return s

def strmachine(m):
    start,states,transition,output = m
    result = []
    s = start
    result.append(f'state {reprstate(s)}')
    for i in transition[s]:
        if i in output[s]:
            result.append(f'on {i} goto {reprstate(transition[s][i])} output {output[s][i]}')
        else:
            result.append(f'on {i} goto {reprstate(transition[s][i])}')
    for s in states-set(start):
        result.append(f'state {reprstate(s)}')
        for i in transition[s]:
            if i in output[s]:
                result.append(f'on {i} goto {reprstate(transition[s][i])} output {output[s][i]}')
            else:
                result.append(f'on {i} goto {reprstate(transition[s][i])}')
    return '\n'.join(result)


def composemachines(m1,m2):
    '''Feed outputs of machine1 to machine2'''
    start1,states1,transition1,output1 = m1
    start2,states2,transition2,output2 = m2
    states = set()
    transition = defaultdict(dict)
    output = defaultdict(dict)

    for x in states1:
        for y in states2:
            states.add((x,y))
            
    for x,y in states:
        for i in transition1[x]:
            if i in output1[x]:
                if output1[x][i] in transition2[y]:
                    transition[(x,y)][i] = (transition1[x][i],transition2[y][output1[x][i]])
                    if output1[x][i] in output2[y]:
                        output[(x,y)][i] = output2[y][output1[x][i]]
            else:
                transition[(x,y)][i] = (transition1[x][i],y)
    return (start1,start2),states,transition,output


m1 = readmachine(machine1)
m2 = readmachine(machine2)
file = open('21numeric.txt','w')
file.write(strmachine(m2))
file.close()

m = composemachines(m1,m2)
file = open('21controlnumeric.txt','w')
file.write(strmachine(m))
file.close()
m = readmachine('21controlnumeric.txt')

m = composemachines(m1,m)
file = open('21controlcontrolnumeric.txt','w')
file.write(strmachine(m))
file.close()
