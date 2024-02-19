import heapq
import math

D = [i.strip() for i in open("input","r").readlines()]

w = len(D[0])
h = len(D)
G = "".join(D)

m = -1
for i,ch in enumerate(G):
    if ch == '0':
        start = i
    if ch.isdigit():
        m = max(m, int(ch))

sp = start
start = (start, tuple(False for i in range(m)))

def neighbors(pos):
    p, vv = pos
    for d in [-w,-1,1,w]:
        if G[p+d] != "#":
            k = -1
            if G[p+d].isdigit():
                k = int(G[p+d]) - 1
            yield (1, (p+d, tuple(x if i != k else True for i,x in enumerate(vv))))

def dynamic_dijkstra(neighbors, start, part):
    global sp
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
            if all(v[1]) and (part == 1 or v[0] == sp):
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

print(dynamic_dijkstra(neighbors, start, 1)[0])
print(dynamic_dijkstra(neighbors, start, 2)[0])