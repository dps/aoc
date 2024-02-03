import re
from functools import reduce

def ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))

def manhattan4(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2]) + abs(p[3] - q[3])

clusters = []

for line in open("input","r").readlines():
    point = tuple(ints(line))
    found = []
    for i,c in enumerate(clusters):
        for q in c:
            if manhattan4(point, q) <= 3:
                c.add(point)
                found.append((i,c))
                break
    if not found:
        clusters.append(set([point]))
    if len(found) > 1:
        new = reduce(set.union, [c for _,c in found])
        to_del = set([i for i,_ in found])
        clusters = [c for i,c in enumerate(clusters) if i not in to_del]
        clusters.append(new)

print(len(clusters))
