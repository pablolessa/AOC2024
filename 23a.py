data = '23data.txt'
example = '23example.txt'
archivo = open(data)
filas = [f.strip() for f in archivo.readlines()]
archivo.close()

sides = set()
sides_t = set()
vertices = set()
vertices_t = set()
for f in filas:
    a,b = f.split('-')
    sides.add((a,b))
    sides.add((b,a))
    vertices.add(a)
    vertices.add(b)
    if 't' == a[0]:
        vertices_t.add(a)
        sides_t.add((a,b))
        sides_t.add((b,a))
    if 't' == b[0]:
        vertices_t.add(b)
        sides_t.add((a,b))
        sides_t.add((b,a))

vertices_o = vertices - vertices_t

triangles_ttt = 0
for a in vertices_t:
    for b in vertices_t:
        for c in vertices_t:
            if (a,b) in sides_t and (b,c) in sides_t and (c,a) in sides_t:
                triangles_ttt += 1

triangles_tto = 0
for a in vertices_t:
    for b in vertices_t:
        for c in vertices_o:
            if (a,b) in sides_t and (b,c) in sides and (c,a) in sides:
                triangles_tto += 1

triangles_too = 0
for a in vertices_t:
    for b in vertices_o:
        for c in vertices_o:
            if (a,b) in sides and (b,c) in sides and (c,a) in sides:
                triangles_too += 1

print(triangles_ttt//6 + triangles_tto//2 + triangles_too//2)
