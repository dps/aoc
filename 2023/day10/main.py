
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def part1():
    global D
    tot = 0
    
    G,w,h = grid_from_strs(D)
    start = None
    for r in range(h):
        for c in range(w):
            if G[r][c] == 'S':
                start = (c,r)

    def grid_neighbors(p, width, height, dir):
        for d in dir:
            q = (p[0] + d[0], p[1] + d[1])
            if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
                continue
            yield (q)

    NEIGHBORS = {
        "S": [(0,-1),(0,1)], # by inspection of input data.
        "-": [(1,0), (-1, 0)],
        "L": [(0,-1), (1,0)],
        "J": [(-1, 0), (0,-1)], 
        "7": [(-1, 0), (0, 1)],
        "F": [(0,1),(1,0)],
        "|": [(0,-1),(0,1)],
        ".": []
    }
    def neighbors(p):
        ch = G[p[1]][p[0]]
        dd = NEIGHBORS[ch]
        for d in grid_neighbors(p, w, h, dd):
            yield d

    max_with_neighbor = (0, (start[0], start[1]))

    initial_dirs = list(zip(list(neighbors(start)), [1] * 4, range(4)))
    initial_set = set(zip(list(neighbors(start)),range(4)))
    for i in zip([start] * 4, range(4)):
        initial_set.add(i)

    bfs, visited = deque(initial_dirs), initial_set

    while bfs:
        pos, depth, start_dir = bfs.popleft()
        for d in neighbors(pos):
            if d == start and depth > 2:
                if depth % 2 == 1:
                    return ((depth-1)//2)+1
                else:
                    return depth//2
            if not (d, start_dir) in visited:
                bfs.append((d, depth+1, start_dir))
                visited.add((d, start_dir))
        

def part2():
    global D
    tot = 0

    on_loop = set()
    
    G,w,h = grid_from_strs(D)
    start = None
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
            #outsides = [(p[0]+x[0], p[1]+x[1]) for x in d[2]]
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
    # NEIGHBORS_WITH_LEFT_SIDE = {
    #     "S": [(0,1, [(-1,0)])], #[(1, 0), (-1, 0), (0, 1), (0, -1)], #yes
    #     "-": [(1,0, [(0,-1)]), (-1, 0, [(0,1)])], # yes
    #     "L": [(0,-1, [(-1,0),(0,1)]), (1,0,[(1,-1)])], # yes
    #     "J": [(-1, 0, [(1,0),(0,1)]), (0,-1, [(-1,-1)])], # yes 
    #     "7": [(-1, 0, [(-1,1)]), (0, 1, [(0,-1),(1,0)])], # yes
    #     "F": [(0,1, [(1,1)]),(1,0, [(-1,0),(0,-1)])], # yes
    #     "|": [(0,-1, [(-1,0)]),(0,1,[(1,0)])], #yes
    #     ".": [] #yes
    # }

    def neighbors(p):
        ch = G[p[1]][p[0]]
        # print("neighbors ", ch)
        dd = NEIGHBORS[ch]
        # print("dd", ch, dd)
        for d in grid_neighbors(p, w, h, dd):
            # print("----", d)
            yield d

    # snodes = list(zip(list(neighbors(start)), [1]*8))
    # svisited = set(snodes)
    # print(start)

    print(":::")

    max_with_neighbor = (0, (start[0], start[1]))

    on_left = set()
    on_loop.add(start)
    for s in list(neighbors(start)):
        on_loop.add(s)

    initial_dirs = list(zip(list(neighbors(start)), [1] * 4, range(4)))
    initial_set = set(zip(list(neighbors(start)),range(4)))
    for i in zip([start] * 4, range(4)):
        initial_set.add(i)

    #bfs, visited = deque([(start, 0)]), {start}
    bfs, visited = deque(initial_dirs), initial_set

    maxes = defaultdict(int)

    while bfs:
        pos, depth, start_dir = bfs.popleft()
        # print("***", pos, depth, start_dir)
        # print(pos, G[pos[1]][pos[0]], "neighbors:")
        for d in neighbors(pos):
            # print("   ", d)
            if d == start and depth > 2:
                # print("STARTAGAIN", depth)
                if depth % 2 == 1:
                    # print("result ", ((depth-1)//2)+1)
                    return G,w,h,on_loop
                else:
                    # print("result", depth//2)
                    return G,w,h,on_loop
            if not (d, start_dir) in visited:
                bfs.append((d, depth+1, start_dir))
                visited.add((d, start_dir))
                on_loop.add(d)

    print("terminated")

#part1()
g,w,h,on_loop = part2()
print(len(on_loop), w,h)
for x in range(w):
    for y in range(h):
        if (x,y) not in on_loop:
            g[y][x] = "."

print("\n".join([" ".join(row) for row in g]))

# outside = set()
# for x in range(-1, w+1):
#     outside.add((x,-1))
#     outside.add((x,h))
# for y in range(-1, h+1):
#     outside.add((-1,y))
#     outside.add((w,y))


tot = 0
for y,row in enumerate(g):
    for x,ch in enumerate(row):
        if ch == ".":
            xx = x-1
            c = 0
            corners = []
            while xx >= 0:
                if g[y][xx] == "|" or g[y][xx] == "F" or g[y][xx] == "7" or g[y][xx] == "S":
                    corners.append(g[y][xx])
                    c+=1
                xx-=1
            if c%2 == 1:
                print(x,y, corners)
            else:
                g[y][x] = " "
            # if c%2 == 1:
            #     g[y][x] = chr(ord('&')+c)
            #     if chr(ord('&')+c) == 'm':
            #         print()
            tot += 1 if c%2 == 1 else 0

VV = {"7":"┐", "L":"└"}
print("\n".join([" ".join(row) for row in g]))

print(tot) # 1420 too high; 451 too high  450 too high



