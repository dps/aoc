from utils import *

D = [i.strip() for i in open("input", "r").readlines()]

g, w, h, _ = grid_ints_from_strs(D)
end = ((w - 1), (h - 1))


def dynamic_dijkstra(neighbors, start, end):
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


def cw(d): return {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}[d]
def ccw(d): return {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}[d]

def in_bounds(p, d): return 0 <= p[0] + d[0] < w and 0 <= p[1] + d[1] < h
def cost(p, d): return g[p[1] + d[1]][p[0] + d[0]]

def neighbors(state, part=1):
    for p, d in [((0, 0), (1, 0)), ((0, 0), (0, 1))] if state == ("start") else [state]:
        cc = 0
        for l in range(1, 4 if part == 1 else 11):
            if in_bounds(p, (l * d[0], l * d[1])):
                cc += cost(p, (l * d[0], l * d[1]))
                if part == 1 or l >= 4:
                    yield (cc, ((p[0] + l * d[0], p[1] + l * d[1]), cw(d)))
                    yield (cc, ((p[0] + l * d[0], p[1] + l * d[1]), ccw(d)))
            else:
                break

# pypy3 main.py  1.16s user 0.02s system 99% cpu 1.187 total
print("Part 1", dynamic_dijkstra(neighbors, ("start"), end)[0])
print("Part 2", dynamic_dijkstra(lambda s: neighbors(s, part=2), ("start"), end)[0])
