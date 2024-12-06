
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0

P = None
d = -1j
R = len(D)
C = len(D[0])
for x in range(C):
    for y in range(R):
        if D[y][x] == "^":
            P = (x + 1j*y)

p1visited = set()

def isloop(obs):
    global p1visited
    p = P
    d = -1j
    visited, p1visited = set(), set()
    visited.add((p,d))
    p1visited.add(p)
    while p.real < C-1 and p.imag < R-1 and p.real >= 0 and p.imag >= 0:
        q = p + d
        while D[int(q.imag)][int(q.real)] == "#" or q == obs:
            # turn right 90 degrees
            d = d * 1j
            q = p + d
        p = q

        if (p,d) in visited:
            return 1
        visited.add((p,d))
        p1visited.add(p)
    if obs == None:
        return len(p1visited)
    return 0

p1 = isloop(None)

for obs in p1visited:
    p2 += isloop(obs)

print(p1, p2)