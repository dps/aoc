
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

graph = defaultdict(list)

for line in D:
    toks = line.split()
    graph[toks[0]].append((int(toks[4]), toks[2]))
    graph[toks[2]].append((int(toks[4]), toks[0]))

places = set(graph.keys())

min_dist = math.inf
max_dist = -math.inf

def dfs(point, dest, l, route, visited, part=1):
    global min_dist, max_dist, graph
    if part == 1 and l > min_dist:
        return
    if point == dest and len(visited) == len(places):
        if part == 2 and l > max_dist:
            max_dist = l
        if part == 1 and l < min_dist:
            min_dist = l
        return

    for nxt in graph[point]:
        if nxt[1] not in visited:
            dfs(nxt[1], dest, l+nxt[0], route + [nxt[1]], frozenset(visited | {nxt[1]}), part)


for s,e in combinations(places, 2):
    dfs(s,e,0,[], set([s]))
    dfs(e,s,0,[], set([s]))
    dfs(s,e,0,[], set([s]), 2)
    dfs(e,s,0,[], set([s]), 2)


print(min_dist, max_dist)
