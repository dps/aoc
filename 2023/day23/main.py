from utils import *

D = [i.strip() for i in open("input","r").readlines()]
tot = 0

g,w,h,_ = grid_from_strs(D)
start = (1,0)
end = (w-2,h-1)

@cache
def grid_neighbors(p):
    global g,w,h
    width = w
    height = h
    r = []
    for d in DIR:
        q = (p[0] + d[0], p[1] + d[1])
        if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height or g[q[1]][q[0]] == "#":
            continue
        r.append(q)
    return r

mm = 0
def p1(p, l, visited):
    global mm,g,end
    if p == end:
        mm = max(l, mm)
    else:
        d = None
        if g[p[1]][p[0]] == ">":
            d = (1,0)
        elif g[p[1]][p[0]] == "<":
            d = (-1,0)
        elif g[p[1]][p[0]] == "^":
            d = (0,-1)
        elif g[p[1]][p[0]] == "v":
            d = (0, 1)
        if d:
            if (p[0]+d[0],p[1]+d[1]) not in visited:
                p1((p[0]+d[0],p[1]+d[1]), l+1, visited | {p})
        else:
            for n in grid_neighbors(p):
                if n not in visited:
                    p1(n,l+1, visited | {p})

p1(start, 0, set())
print("Part 1", mm)


def find_all_intersections():
    res = []
    for x in range(w):
        for y in range(h):
            if g[y][x] == "." and len(grid_neighbors((x,y))) > 2:
                res.append((x,y))
    return res

isect = set(find_all_intersections()) | {start, end}

def find_edges_from_isect_to_isect(isects):
    graph = {}
    for i in isects:
        o,p = i,i
        dests = []
        for d in grid_neighbors(o):
            vv, l = set(), 1
            p = d
            vv.add(o)
            vv.add(p)
            while p not in isect:
                nxt = [v for v in grid_neighbors(p) if v not in vv]
                assert(len(nxt) == 1)
                l += 1
                p = nxt[0]
                vv.add(p)
            # we will find each edge in the graph twice (both directions)
            # give it a unique name so we don't walk it twice later.
            name = tuple(sorted([o,p],key = lambda x: x[0] + w*x[1]))
            dests.append((p,l,name)) # graph is origin -> (dest, len, name)
        graph[o] = dests
    return graph

graph = find_edges_from_isect_to_isect(isect)

mm = 0
def dfs(p, l, edges_taken,verts_visited,dbg):
    global end,mm
    if p == end:
        mm = max(l, mm)
    else:
        nxt = graph[p]
        for n,ll,name in nxt:
            if name not in edges_taken and n not in verts_visited:
                dfs(n, l+ll, edges_taken | {name}, verts_visited | {n}, dbg + [(n,ll)])


dfs(start,0,set(),set([start]),[(start,0)])
print("Part 2", mm) # 6322, 21.47s w/pypy3