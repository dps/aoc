
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0
order, pages = bundles(D)

before = defaultdict(list)

for entry in order:
    b,a = entry.split("|")
    before[a].append(b)

def reorder(seq):
    nn = []
    for s in seq:
        ml = len(nn)
        for i in range(len(nn)):
            if s in before[nn[i]]:
                ml = min(ml, i)
        nn.insert(ml, s)
    return nn


for toprint in pages:
    ok = True
    seq = toprint.split(",")
    seq.reverse()
    later = set()
    for s in seq:
        must_earlier = set(before[s])
        if must_earlier.intersection(later):
            ok = False
        later.add(s)
    if ok:
        p1 += int(seq[len(seq)//2])
    else:
        ll = reorder(toprint.split(","))
        p2 += int(ll[len(ll)//2])


print(p1, p2)
