# This is the more complicated version which minimizes runtime by sharding across
# cores. simple.py contains the pre-sharded version.
from utils import *

D = [i.strip() for i in open("input", "r").readlines()]

g, w, h, _ = grid_from_strs(D)
start = (1, 0)
end = (w - 2, h - 1)


@cache
def grid_neighbors(p, part1=False):
    global g, w, h
    width = w
    height = h
    r = []
    dd = None
    if part1:
        if g[p[1]][p[0]] == ">":
            dd = (1, 0)
        elif g[p[1]][p[0]] == "<":
            dd = (-1, 0)
        elif g[p[1]][p[0]] == "^":
            dd = (0, -1)
        elif g[p[1]][p[0]] == "v":
            dd = (0, 1)
    for d in [dd] if dd else DIR:
        q = (p[0] + d[0], p[1] + d[1])
        if (
            q[0] < 0
            or q[1] < 0
            or q[0] >= width
            or q[1] >= height
            or g[q[1]][q[0]] == "#"
        ):
            continue
        r.append(q)
    return r


def find_all_intersections(part1=False):
    res = []
    for x in range(w):
        for y in range(h):
            if g[y][x] == "." and len(grid_neighbors((x, y), part1)) > 2:
                res.append((x, y))
    return res


def find_edges_from_isect_to_isect(isects, start, end, part1=False):
    graph = {}
    for i in isects:
        o, p = i, i
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
                dests.append((p[0], p[1], l))  # graph is origin -> (dest, len)
        graph[(o[0],o[1])] = dests
    # Remap the whole graph to power of two integer node names so we
    # can mark visited really quickly.
    gg = {}
    map_ = {}
    for i,k in enumerate(graph.keys()):
        map_[k] = pow(2,i)
    for k,v in graph.items():
        gg[map_[k]] = [(map_[(x[0],x[1])],x[2]) for x in v]
    return gg,map_[start],map_[end]

def partition():
    parts = []
    for part1 in [True, False]:
        part = []
        isect = set(find_all_intersections(part1)) | {start, end}
        graph,start_,end_ = find_edges_from_isect_to_isect(isect, start, end, part1)

        mm = 0
        visited = 0

        Q = []
        def unroll_to_depth4(n, l, d):
            global mm, visited
            if d > 4:
                return
            if visited & n:
                return
            visited |= n
            if n == end_:
                mm = max(l, mm)
            else:
                for nn, ll in graph[n]:
                    if d == 4:
                        Q.append((d, nn, l + ll, visited))
                    unroll_to_depth4(nn, l + ll, d+1)
            visited ^= n
        unroll_to_depth4(start_,0,0)
        for state in Q:
            part.append((state, graph, end_))
        parts.append(part)
    return parts

visited, mm = 0,0
def start_dfs(data):
    global visited,mm
    state, graph, end_ = data
    _, n, l, visited = state
    mm = 0
    def dfs(n, l):
        global mm, visited
        if visited & n:
            return
        visited |= n
        if n == end_:
            mm = max(l, mm)
        else:
            for nn, ll in graph[n]:
                dfs(nn, l + ll)
        visited ^= n
    dfs(n,l)
    return mm

if __name__ == "__main__":
    part1_data,part2_data = partition()
    import concurrent.futures
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(start_dfs, part1_data)
        print(max(results))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(start_dfs, part2_data)
        print(max(results))