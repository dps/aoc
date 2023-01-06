from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def explode(n):
    exploded = False
    p, acc = [], -1
    for i in n:
        if exploded and acc == -1:
            acc = i[1]
        elif i[0] == 5 and not exploded:
            if len(p) > 0:
                p[-1] = (p[-1][0], p[-1][1] + i[1])
            p.append((i[0]-1, 0))
            exploded = True
        else:
            if acc > 0:
                p.append((i[0], i[1] + acc))
                acc = 0
            else:
                p.append(i)
    return exploded, p

def split(n):
    split, p = False, []
    for i in n:
        if not split and i[1] > 9:
            split = True
            p.extend([(i[0] + 1, i[1]//2), (i[0] + 1, int(math.ceil(i[1]/2)))])
        else:
            p.append(i)
    return split, p

def magnitude(sn):
    max_d = max(i[0] for i in sn)
    for depth in range(max_d, 0, -1):
        q, l = [], None
        for d,r in sn:
            if d != depth: q.append((d,r))
            elif l != None:
                q.append((depth-1, 3*l + 2*r))
                l = None
            else: l = r
        sn = q
    return(q[0][1])

def parse_sn(sn):
    n,d = [],0
    for ch in sn:
        if ch == "[":
            d += 1
        if ch == "]":
            d -= 1
        if ch.isdigit():
            n.append((d, int(ch)))
    return n 

def add(a,b):
    n = [(x[0]+1, x[1]) for x in a] + [(x[0]+1, x[1]) for x in b]
    changed = True
    while changed:
        changed, n = explode(n)
        if changed:
            continue
        changed, n = split(n)
    return n

def part1():
    print(magnitude(reduce(add, [parse_sn(x) for x in input])))

def part2():
    inp = [parse_sn(i) for i in input]
    m = 0
    for a,b in itertools.combinations(inp, 2):
        m = max(m, magnitude(add(a, b)))
        m = max(m, magnitude(add(b, a)))
    print(m)

part1()
part2()