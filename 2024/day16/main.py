
from utils import *
from tqdm import tqdm

D = [i.strip() for i in open("test","r").readlines()]

grid = {x+1j*y: ch for y, line in enumerate(D) for x, ch in enumerate(line)}

start = [p for p in grid if grid[p] == "S"][0]
end = [p for p in grid if grid[p] == "E"][0]


def dynamic_dijkstra(neighbors, start, end):
    q, seen, mins = [(0, start, [])], set(), {start: 0}
    while q:
        (cost, v, path) = heapq.heappop(q)
        if v not in seen:
            seen.add(v)
            path = path + [v]
            if v[0] == end[0]:
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

def neighbors(x):
    cc, d = x
    d = eval(d)
    p = cc[0]+cc[1]*1j
    if grid[p+d] != "#":
        yield (1, (((p+d).real, (p+d).imag), str(d)))
    yield (1000, ((p.real, p.imag), str(d*1j)))
    yield (1000, ((p.real, p.imag), str(d*-1j)))

B= set()
c = dynamic_dijkstra(neighbors, ((start.real, start.imag), "1"), ((end.real, end.imag), "1j"))
print(c[0]) # Part 1

M = c[0]
for p in c[1]:
    B.add((int(p[0][0]), int(p[0][1])))

gg = grid.copy()
for p in c[1]:#tqdm(c[1]):
    if grid[p[0][0]+p[0][1]*1j] == "S" or grid[p[0][0]+p[0][1]*1j] == "E":
        continue
    assert grid[p[0][0]+p[0][1]*1j] == "."
    grid[p[0][0]+p[0][1]*1j] = "#"
    d = dynamic_dijkstra(neighbors, ((start.real, start.imag), "1"), ((end.real, end.imag), "1"))
    assert d[0] >= M
    if d[0] == M:
        for p in d[1]:
            B.add((int(p[0][0]), int(p[0][1])))
    grid = gg.copy()

# R = len(D)
# C = len(D[0])
# for y in range(R):
#     for x in range(C):
#         if (x, y) in B:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()

print(len(B))
