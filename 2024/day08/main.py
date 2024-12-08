
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

ant = defaultdict(list)
R, C = len(D), len(D[0])
p1, p2 = set(), set()

for y, row in enumerate(D):
    for x, ch in enumerate(row):
        if ch != ".":
            ant[ch].append(x + 1j*y)
            p2.add(x + 1j*y)

for k, v in ant.items():
    for a,b in permutations(v, 2): # we get both orderings
        v = a - b
        for harmonic in range(max(C, R)):
            n = a + harmonic * v
            if n.real >= 0 and n.real < C and n.imag >= 0 and n.imag < R:
                if harmonic == 1:
                    p1.add(n)
                p2.add(n)
            else:
                break

print(len(p1), len(p2))
