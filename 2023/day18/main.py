
RLUD = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
D = [i.strip() for i in open("input","r").readlines()]

def compute_vertices(part=1):
    p = (0,0)
    vertices = [p]
    path_len = 0
    for line in D:
        p1dir,p1num,hex = line.split(" ")
        num = int(p1num) if part==1 else int(hex[2:7], 16)
        dir = p1dir if part==1 else {"0": "R", "1": "D", "2": "L", "3": "U"}[hex[7:8]]
        d = RLUD[dir]
        p = (p[0] + num*d[0], p[1] + num*d[1])
        vertices.append(p)
        path_len += num
    return vertices, path_len

def pairs(ll):
    for x in range(0,len(ll)-1,2):
        yield (ll[x], ll[x+1])

def shoelace(verts):
    res = 0
    for l,r in pairs(verts):
         res += l[0]*r[1] - l[1] * r[0]
    return res

vertices, path_len = compute_vertices(part=1)
print("Part 1", int(shoelace(vertices) + path_len/2 + 1))
vertices, path_len = compute_vertices(part=2)
print("Part 2", int(shoelace(vertices) + path_len/2 + 1))
