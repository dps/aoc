
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]



def part1():
    global D
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    G,w,h = grid_from_strs(D)
    start = None
    for r in range(h):
        for c in range(w):
            if G[r][c] == 'S':
                start = (c,r)

    print(w,h,start)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    def grid_neighbors(p, width, height=None, dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]):
        height = width if not height else height
        for d in dir:
            q = (p[0] + d[0], p[1] + d[1])
            if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
                continue
            yield (q)

    NEIGHBORS = {
        "S": [(0,-1),(0,1)], #[(1, 0), (-1, 0), (0, 1), (0, -1)], #yes
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
        print("neighbors ", ch)
        dd = NEIGHBORS[ch]
        print("dd", ch, dd)
        for d in grid_neighbors(p, w, h, dd):
            print("----", d)
            yield d

    # snodes = list(zip(list(neighbors(start)), [1]*8))
    # svisited = set(snodes)
    # print(start)

    print(":::")

    max_with_neighbor = (0, (start[0], start[1]))

    initial_dirs = list(zip(list(neighbors(start)), [1] * 4, range(4)))
    initial_set = set(zip(list(neighbors(start)),range(4)))
    for i in zip([start] * 4, range(4)):
        initial_set.add(i)

    #bfs, visited = deque([(start, 0)]), {start}
    bfs, visited = deque(initial_dirs), initial_set

    maxes = defaultdict(int)

    while bfs:
        pos, depth, start_dir = bfs.popleft()
        print("***", pos, depth, start_dir)
        print(pos, G[pos[1]][pos[0]], "neighbors:")
        for d in neighbors(pos):
            print("   ", d)
            if d == start and depth > 2:
                print("STARTAGAIN", depth)
                if depth % 2 == 1:
                    print("result ", ((depth-1)//2)+1)
                    return
                else:
                    print("result", depth//2)
                    return
            if not (d, start_dir) in visited:
                bfs.append((d, depth+1, start_dir))
                visited.add((d, start_dir))

    print("terminated")
        
    #aoc(tot)

part1()  # 111 is too low, 112 is too low
#part2()
