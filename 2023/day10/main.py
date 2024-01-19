from utils import *

D = [i.strip() for i in open("input", "r").readlines()]


def trace_pipe():
    global D
    start = None
    G, w, h, start = grid_from_strs(D, find="S")
    shoelace = 0
    prev = None

    NEIGHBORS = {
        "S": [(0, 1)],
        "-": [(1, 0), (-1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(-1, 0), (0, -1)],
        "7": [(-1, 0), (0, 1)],
        "F": [(0, 1), (1, 0)],
        "|": [(0, -1), (0, 1)],
    }

    def neighbors(p):
        ch = G[p[1]][p[0]]
        for d in NEIGHBORS[ch]:
            yield (p[0] + d[0], p[1] + d[1])

    bfs, visited = deque([(start, 0)]), {start}

    while bfs:
        pos, depth = bfs.popleft()
        for d in neighbors(pos):
            if d == start and depth > 2:
                return (
                    G,
                    w,
                    h,
                    visited,
                    (((depth - 1) // 2) + 1 if depth % 2 == 1 else depth // 2),
                    shoelace + pos[0]*d[1] - pos[1] * d[0]
                )
            if not d in visited:
                shoelace += pos[0]*d[1] - pos[1] * d[0]
                bfs.append((d, depth + 1))
                visited.add(d)


g, w, h, on_loop, result, shoelace = trace_pipe()
print("day10 ", result, abs(shoelace)/2 - result + 1)
