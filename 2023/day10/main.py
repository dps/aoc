
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def part1():
    global D
    on_loop, start = set(), None
    G,w,h = grid_from_strs(D)

    for r in range(h):
        for c in range(w):
            if G[r][c] == 'S':
                start = (c,r)

    def grid_neighbors(p, width, height=None, dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        height = width if not height else height
        for d in dir:
            q = (p[0] + d[0], p[1] + d[1])
            if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
                continue
            yield q

    NEIGHBORS = {
        "S": [(0,1)], #[(1, 0), (-1, 0), (0, 1), (0, -1)], #yes
        "-": [(1,0), (-1, 0)], # yes
        "L": [(0,-1), (1,0)], # yes
        "J": [(-1, 0), (0,-1)], # yes 
        "7": [(-1, 0), (0, 1)], # yes
        "F": [(0,1),(1,0)], # yes
        "|": [(0,-1),(0,1)], #yes
        ".": [] #yes
    }

    def neighbors(p):
        ch = G[p[1]][p[0]]
        dd = NEIGHBORS[ch]
        for d in grid_neighbors(p, w, h, dd):
            yield d

    on_loop.add(start)
    for s in list(neighbors(start)):
        on_loop.add(s)

    initial_dirs = list(zip(list(neighbors(start)), [1] * 4, range(4)))
    initial_set = set(zip(list(neighbors(start)),range(4)))
    for i in zip([start] * 4, range(4)):
        initial_set.add(i)

    bfs, visited = deque(initial_dirs), initial_set

    while bfs:
        pos, depth, start_dir = bfs.popleft()
        for d in neighbors(pos):
            if d == start and depth > 2:
                return G,w,h,on_loop, (((depth-1)//2)+1 if depth % 2 == 1 else depth//2)
            if not (d, start_dir) in visited:
                bfs.append((d, depth+1, start_dir))
                visited.add((d, start_dir))
                on_loop.add(d)

g,w,h,on_loop,result = part1()
print("Part 1: ", result)

# Remove all the junk from the map
for x in range(w):
    for y in range(h):
        if (x,y) not in on_loop:
            g[y][x] = "."

# Even/odd rule, with subpixel on corners. We pass under Js and Ls.
# We know S is a |.
tot = 0
for y,row in enumerate(g):
    for x,ch in enumerate(row):
        if ch == ".":
            xx, c = x-1, 0  # Even/ odd rule - cast a ray out -x wards
            while xx >= 0:
                if g[y][xx] == "|" or g[y][xx] == "F" or g[y][xx] == "7" or g[y][xx] == "S":
                    c+=1
                xx-=1
            tot += 1 if c%2 == 1 else 0

print("Part 2: ", tot)


