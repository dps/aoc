from utils import *

D = [i.strip() for i in open("input", "r").readlines()]


def trace_pipe():
    global D
    start = None
    G, w, h = grid_from_strs(D)

    for r in range(h):
        for c in range(w):
            if G[r][c] == "S":
                start = (c, r)

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
                )
            if not d in visited:
                bfs.append((d, depth + 1))
                visited.add(d)


g, w, h, on_loop, result = trace_pipe()
print("Part 1: ", result)

# Remove all the junk from the map
for x in range(w):
    for y in range(h):
        if (x, y) not in on_loop:
            g[y][x] = "."

# Even/odd rule, with subpixel on corners. We pass under Js and Ls.
# We know S is a |.
tot = 0
for y, row in enumerate(g):
    for x, ch in enumerate(row):
        if ch == ".":
            xx, c = x - 1, 0  # Even/ odd rule - cast a ray out -x wards
            while xx >= 0:
                if (
                    g[y][xx] == "|"
                    or g[y][xx] == "F"
                    or g[y][xx] == "7"
                    or g[y][xx] == "S"
                ):
                    c += 1
                xx -= 1
            tot += 1 if c % 2 == 1 else 0

print("Part 2: ", tot)
