from utils import *

D = int(open("input", "r").readlines()[0].strip())
# corners are odd square numbers
# 1, 9, 25, 49

p2 = None
p = 0
d, m, n = 1, 1, 1
spiral = defaultdict(int)
spiral[0] = 1
pos = {1: 0}
world = set([0])
while n < D:
    n += 1
    q = p + d
    if abs(q.imag) > m or abs(q.real) > m:
        d = d * (1j)
        q = p + d
        if abs(q.imag) <= m and abs(q.real) <= m and q not in world:
            p = q
        else:
            d = 1
            m += 1
            p = p + d
    else:
        p = q
    if p2 == None:
        spiral[p] = sum([spiral[p + q] for q in CDIR8])
        if spiral[p] > D:
            p2 = spiral[p]
    pos[n] = p
    world.add(p)

print(int(abs(pos[D].imag) + abs(pos[D].real)))
print(p2)
