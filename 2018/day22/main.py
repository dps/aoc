
from utils import *

# * The region at `0,0` (the mouth of the cave) has a geologic index of `0`.
# * The region at the coordinates of the target has a geologic index of `0`.
# * If the region's `Y` coordinate is `0`, the geologic index is its `X` coordinate times `16807`.
# * If the region's `X` coordinate is `0`, the geologic index is its `Y` coordinate times `48271`.
# * Otherwise, the region's geologic index is the result of multiplying the erosion *levels* of the regions at `X-1,Y` and `X,Y-1`.

# A region's *erosion level* is its *geologic index* plus the cave system's *depth*, all [modulo] `20183`. Then:


depth = 7740
target = (12,763)

# depth = 510
# target = (10,10)

def elevel(n):
    return (n+depth)%20183

@cache
def geo_index(x,y):
    if (x,y) == (0,0) or (x,y) == target:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return ((geo_index(x-1,y)+depth)%20183) * ((geo_index(x,y-1)+depth)%20183)
    

# * If the *erosion level modulo `3`* is `0`, the region's type is *rocky*.
# * If the *erosion level modulo `3`* is `1`, the region's type is *wet*.
# * If the *erosion level modulo `3`* is `2`, the region's type is *narrow*.

print(sum(elevel(geo_index(x,y))%3 for x in range(target[0]+1) for y in range(target[1]+1)))

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

# 0 => rocky, 1 => wet, 2 => narrow
# 0 => neither, 1 => torch, 2 => climbing gear
target = (12, 763, 1)
start = (0,0,1)

def neighbors(state):
    x,y,e = state
    stype = elevel(geo_index(x,y))%3

    if stype == 0:
        yield (7, (x,y,2 if e == 1 else 1))
    elif stype == 1:
        yield (7, (x,y,0 if e == 2 else 2))
    elif stype == 2:
        yield (7, (x,y,1 if e == 0 else 0))

    for d in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx,ny = x + d[0], y + d[1]
        if nx < 0 or ny < 0:
            continue
        ntype = elevel(geo_index(nx,ny))%3
        if ntype == 0 and (e == 1 or e == 2):
            yield (1, (nx,ny,e))
        elif ntype == 1 and (e == 0 or e == 2):
            yield (1, (nx,ny,e))
        elif ntype == 2 and (e == 0 or e == 1):
            yield (1, (nx,ny,e))


print(dynamic_dijkstra(neighbors, start, target)[0])