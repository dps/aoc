
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0

P = D[0:1024]
grid = defaultdict(int)
for line in P:
    x,y = ints(line)
    grid[(x,y)] = 1

def dynamic_dijkstra(neighbors, start, end):
    """
    neighbors is a function which takes current node and returns a list of (weight, neighbor)
    pairs or () if no neighbors exist.
    returns (sum(path weights), path)
    """
    q, seen, mins = [(0, start, [])], set(), {start: 0}
    while q:
        (cost, v, path) = heapq.heappop(q)
        if v not in seen:
            seen.add(v)
            path = path + [v]
            if v == end:
                return (cost, path)

            for c, neighbor in neighbors(v):
                if neighbor in seen:
                    continue
                prev = mins.get(neighbor, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[neighbor] = next
                    heapq.heappush(q, (next, neighbor, path))

    return math.inf, None


def neighbors(p):
    x,y = p
    for dx,dy in DIR:
        if x+dx >= 0 and y+dy >= 0 and x+dx <= 70 and y+dy <= 70 and grid[(x+dx,y+dy)] == 0:
            yield (1, (x+dx,y+dy))
    
p1, _ = dynamic_dijkstra(neighbors, (0,0), (70,70))

for d in D[1024:]:
    x,y = ints(d)
    grid[(x,y)] = 1
    a, _ = dynamic_dijkstra(neighbors, (0,0), (70,70))
    if a == math.inf:
        p2 = (x,y)
        break

print(p1, p2)
