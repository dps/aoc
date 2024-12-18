
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0
start = (0,0)
end = (70,70)

P = D[0:1024]
grid = defaultdict(int)
for line in P:
    x,y = ints(line)
    grid[(x,y)] = 1

def neighbors(p):
    x,y = p
    for dx,dy in DIR:
        if x+dx >= 0 and y+dy >= 0 and x+dx <= 70 and y+dy <= 70 and grid[(x+dx,y+dy)] == 0:
            yield (1, (x+dx,y+dy))
    
p1, path = dynamic_dijkstra(neighbors, start, end)

for d in D[1024:]:
    x,y = ints(d)
    grid[(x,y)] = 1
    if (x,y) not in path:
        continue
    a, path = dynamic_dijkstra(neighbors, start, end)
    if a == math.inf:
        p2 = (x,y)
        break

print(p1, p2)
