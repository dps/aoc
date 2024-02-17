
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

r = []
cands = []
starts = []
for line in D:
    l,h = positive_ints(line)
    r.append((l,h))
    starts.append(l)
    cands.append(h+1)

starts = sorted(starts)

for ra in r:
    l,h = ra
    cands = [c for c in cands if not (l <= c and c <= h)]

cc = sorted(cands)
print(cc[0])

starts.append(4294967296)
ss = (s for s in starts)

tot = 0
s = -1
for c in cc:
    while s < c:
        s = next(ss)
    tot += (s-c)

print(tot)