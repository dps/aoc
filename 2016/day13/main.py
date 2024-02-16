
from utils import *

D = int(open("input","r").read())

@cache
def wall(p):
    x,y = p
    b = len([1 for x in bin((x*x + 3*x + 2*x*y + y + y*y) + D) if x == '1'])
    return b%2 == 1

start = (1,1)
end = (31,39)

def neighbors(p):
    for d in DIR:
        q = (p[0]+d[0],p[1]+d[1])
        if 0 <= q[0] and 0 <= q[1] and not wall(q):
            yield (1, q)

print(dynamic_dijkstra(neighbors, start,end)[0])

Q, visited = deque([(start,0)]), set()
while Q:
    p, l = Q.popleft()
    if p in visited:
        continue
    visited.add(p)
    if l == 50:
        continue

    for _,q in neighbors(p):
        Q.append((q,l+1))

print(len(visited))