
from utils import *
import hashlib

salt = open("input","r").read().strip()

w = 4
start = (0,0, "")
end = (3,3, None)
UDLR = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
dirs = "UDLR"


def dynamic_dijkstra(neighbors, start, end):
    q, seen, mins = [(0, start, [])], set(), {start: 0}
    while q:
        (cost, v, path) = heapq.heappop(q)
        if v not in seen:
            seen.add(v)
            path = path + [v]
            if v[0:2] == end[0:2]:
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

@cache
def mdn(path):
    return hashlib.md5((salt+path).encode()).hexdigest()[0:4]

found = set()
def neighbors(p):
    x,y,path = p
    h = mdn(path)
    for i,ch in enumerate(UDLR):
        x_,y_ = x+UDLR[ch][0], y+UDLR[ch][1]
        if 0 <= x_ < w and 0 <= y_ < w and h[i] in "bcdef" and path+ch not in found:
            yield 1, (x_,y_,path+ch)

print("pt1", dynamic_dijkstra(neighbors, start, end)[1][-1][-1])

m = 0
while True:
    res = dynamic_dijkstra(neighbors, start, end)
    if res[0] == math.inf:
        break
    path = res[1][-1][-1]
    found.add(path)
    m = max(m, len(path))

print("pt2", m)