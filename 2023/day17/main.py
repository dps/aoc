from utils import *

D = [i.strip() for i in open("input","r").readlines()]

g,w,h,_ = grid_ints_from_strs(D)

maxw = max(max([i for i in line]) for line in g)
end = ((w-1),(h-1))

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
            if v[0] == end:
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

def in_bounds(p, d):
    global w,h
    x,y = p[0]+d[0], p[1] + d[1]
    return 0 <= x < w and 0 <= y < h

def cost(p, d):
    global g
    x,y = p[0]+d[0], p[1] + d[1]
    return g[y][x]

def cw(d):
    return {(1,0):(0,1), (0,1): (-1,0), (-1,0):(0,-1), (0,-1):(1,0)}[d]
def ccw(d):
    return {(1,0):(0,-1), (0,1): (1,0), (-1,0):(0,1), (0,-1):(-1,0)}[d]


def neighbors(state):
    global g, end, maxw
    if state == ("start", 0):
        for p,d in [((0,0),(1,0)),((0,0),(0,1))]:
            cc = 0
            for l in range(1,4):
                if in_bounds(p, (l*d[0], l*d[1])):
                    cc += cost(p, (l*d[0], l*d[1]))
                    yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), cw(d)))
                    yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), ccw(d)))
                else:
                    break
    else:
        p,d = state
        cc = 0
        for l in range(1,4):
            if in_bounds(p, (l*d[0], l*d[1])):
                cc += cost(p, (l*d[0], l*d[1]))
                yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), cw(d)))
                yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), ccw(d)))
            else:
                break

def neighbors2(state):
    global g, end, maxw
    if state == ("start", 0):
        for p,d in [((0,0),(1,0)),((0,0),(0,1))]:
            cc = 0
            for l in range(1,11):
                if in_bounds(p, (l*d[0], l*d[1])):
                    cc += cost(p, (l*d[0], l*d[1]))
                    if l >= 4:
                        yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), cw(d)))
                        yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), ccw(d)))
                else:
                    break
    else:
        p,d = state
        cc = 0
        for l in range(1,11):
            if in_bounds(p, (l*d[0], l*d[1])):
                cc += cost(p, (l*d[0], l*d[1]))
                if l >= 4:
                    yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), cw(d)))
                    yield (cc, ((p[0]+l*d[0], p[1]+l*d[1]), ccw(d)))
            else:
                break

print(dynamic_dijkstra(neighbors, ("start", 0), end)[0])
print(dynamic_dijkstra(neighbors2, ("start", 0), end)[0])