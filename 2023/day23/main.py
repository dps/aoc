from utils import *

D = [i.strip() for i in open("i2","r").readlines()]
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

# # debugging
# too_long = [((1, 0), 0), ((11, 15), 109), ((41, 7), 150), ((57, 11), 136), ((75, 15), 218), ((105, 7), 238), ((135, 39), 462), ((113, 35), 198), ((79, 39), 190), ((57, 43),\
#  130), ((29, 37), 186), ((19, 37), 22), ((17, 65), 258), ((35, 59), 88), ((29, 89), 104), ((33, 113), 128), ((57, 107), 238), ((59, 79), 166), ((59, 57), 90), ((89, 55), \
# 132), ((85, 75), 116), ((85, 105), 194), ((57, 107), 138), ((65, 137), 190), ((29, 131), 234), ((7, 103), 330), ((17, 83), 154), ((29, 89), 74), ((59, 79), 272), ((85, 75\
# ), 170), ((103, 83), 102), ((109, 53), 172), ((137, 65), 188), ((137, 81), 44), ((103, 83), 272), ((99, 107), 148), ((85, 105), 56), ((81, 129), 152), ((105, 131), 178), \
# ((99, 107), 122), ((135, 111), 272), ((125, 133), 176), ((139, 140), 69)]

# gg = deepcopy(g)
# print(graph[(1, 0)])
# print(graph[(11,15)])

# def trace(path, gg):
#     L = 0
#     t = deque(path)
#     o = t.popleft()[0]
#     gg[o[1]][o[0]] = chr(ord(gg[o[1]][o[0]]) + 1)
#     visited = set([o])
#     while t:
#         ds = graph[o]
#         po = o
#         o,le = t.popleft()
#         f = None
#         for j in ds:
#             if j[0] == o:
#                 f = j
#                 break
#         assert(f != None)
#         print(len(f[3]) , le)
#         assert(len(f[3]) == le+1)
#         for c in f[3]:
#             if c == po:
#                 continue
#             if c in visited:
#                 print("ERE", c, gg[c[1]][c[0]])
#             assert(c not in visited)
#             L += 1
#             gg[c[1]][c[0]] = chr(ord(gg[c[1]][c[0]]) + 1)
#             visited.add(c)

#     return gg, L

# gg,L = trace(too_long, gg)
# print_grid(gg)
# print(L)
# sys.exit(0)
mm = 0
def dfs(p, l, taken,visited,dbg):
    #print("dfs", p, l , taken)
    global end,mm
    if p == end:
        mm = max(l, mm)
        print("MAX", mm, l)
    else:
        nxt = graph[p]
        for n,ll,name in nxt:
            if name not in taken and n not in visited:
                dfs(n, l+ll, taken | {name}, visited | {n}, dbg + [(n,ll)])


print(dfs(start,0,set(),set([start]),[(start,0)]))
print(mm) # 6322