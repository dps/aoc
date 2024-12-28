
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

graph = defaultdict(set)
ts = set()

for line in D:
    a,b = line.split("-")
    graph[a].add(b)
    graph[b].add(a)
    if a[0] == 't':
        ts.add(a)
    if b[0] == 't':
        ts.add(b)

interconnected_p1 = set()
for t in ts:
    for a,b in combinations(graph[t],2):
        if b in graph[a]:
            interconnected_p1.add(tuple(sorted([a,b,t])))

print(len(interconnected_p1))

clusters = [set()]

for n, vs in graph.items():
    spawn = False
    for c in clusters:
        if len(c) == 0 or all(x in vs for x in c):
            c.add(n)
        else:
            spawn = True
    if spawn:
        clusters.append({n})

changed = True
while changed:
    changed = False
    for n, vs in graph.items():
        for c in clusters:
            if all(x in vs for x in c):
                c.add(n)
                changed = True

f = list(clusters)
f.sort(key = lambda x: len(x), reverse=True)
print(",".join(sorted(list(f[0]))))
