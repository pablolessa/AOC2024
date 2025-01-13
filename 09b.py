data = '09data.txt'
example = '09example.txt'
archivo = open(data)
filas = archivo.readlines()
archivo.close()
tira = filas[0].strip()


def convertir(t):
    i = 0
    l = []
    pos = 0
    while i < len(t):
        n = int(t[i])
        if i % 2== 0:
            l.append((i//2,pos,pos+n-1))
        pos += n
        i += 1
    return l

def toString(l):
    _,_,n = l[-1]
    n += 1
    s = ['.']*n
    for id,i,j in l:
        for k in range(i,j+1):
            s[k] = str(id)+'|'
    return ''.join(s)

def compact(l):
    idpositions = list(range(len(l)))
    currentid = len(l)-1
    while currentid > 0:
        pos = idpositions[currentid]
        ID,i,j = l[pos]
        size = j-i+1
        firsti,firstj = -1,-1
        gappos = 0
        for _,secondi,secondj in l[:pos+1]:
            gapsize = secondi-1-firstj
            if gapsize >= size:
                l.insert(gappos,(ID,firstj+1,firstj+size))
                l.pop(pos+1)
                for a,b in enumerate(l):
                    ID2,_,_ = b
                    idpositions[ID2] = a
                break
            firsti,firstj = secondi,secondj
            gappos += 1
        currentid -= 1

def count(l):
    result = 0
    for ID,i,j in l:
        for k in range(i,j+1):
            result += k*ID
    return result

l = convertir(tira)
compact(l)
print(count(l))
