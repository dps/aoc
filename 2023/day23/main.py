from utils import *

D = [i.strip() for i in open("input","r").readlines()]
tot = 0

g,w,h,_ = grid_from_strs(D)
start = (1,0)
end = (w-2,h-1)

@cache
def grid_neighbors(p, part1=False):
    global g,w,h
    width = w
    height = h
    r = []
    dd = None
    if part1:
        if g[p[1]][p[0]] == ">":
            dd = (1,0)
        elif g[p[1]][p[0]] == "<":
            dd = (-1,0)
        elif g[p[1]][p[0]] == "^":
            dd = (0,-1)
        elif g[p[1]][p[0]] == "v":
            dd = (0, 1)
    for d in ([dd] if dd else DIR):
        q = (p[0] + d[0], p[1] + d[1])
        if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height or g[q[1]][q[0]] == "#":
            continue
        r.append(q)
    return r

def find_all_intersections(part1=False):
    res = []
    for x in range(w):
        for y in range(h):
            if g[y][x] == "." and len(grid_neighbors((x,y), part1)) > 2:
                res.append((x,y))
    return res

def find_edges_from_isect_to_isect(isects, part1=False):
    graph = defaultdict(lambda: defaultdict(tuple))
    for i in isects:
        o,p = i,i
        dests = []
        for d in grid_neighbors(o, part1):
            vv, l = set(), 1
            p = d
            vv.add(o)
            vv.add(p)
            found = True
            while p not in isects:
                nxt = [v for v in grid_neighbors(p, part1) if v not in vv]
                if len(nxt) == 0:
                    found = False
                    break
                l += 1
                p = nxt[0]
                vv.add(p)
            if found:
                dests.append((p[0],p[1],l)) # graph is origin -> (dest, len)
        graph[o[0]][o[1]] = dests
    return graph

for part1 in [True, False]:
    isect = set(find_all_intersections(part1)) | {start, end}
    graph = find_edges_from_isect_to_isect(isect, part1)

    mm = 0
    #Unpacking the tuple and defaultdict to x,y speeds this up 2x
    #visited = defaultdict(bool)
    visited = [[False for _ in range(h)] for _ in range(w)]
    def dfs(x, y, l):
        global mm,visited
        if visited[y][x]:
            return
        visited[y][x] = True
        if y == h-1:
            mm = max(l, mm)
        else:
            for xx,yy, ll in graph[x][y]:
                dfs(xx, yy, l+ll)
        visited[y][x] = False

    dfs(start[0],start[1],0)
    print("Part", "1" if part1 else "2", mm)