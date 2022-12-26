import math
from utils import *
from functools import cache
from functools import cmp_to_key

input = [i.strip() for i in open("input.txt","r").readlines()]

flow = {}
connect = defaultdict(lambda : [])
tvalves = 0
dist = {}
start = 999

def floyd_warshall(graph, bidirectional=False):
    # Given a graph dict of format {vertex: [edges]}
    # returns the shortest path between every pair of nodes in the graph.
    dist = defaultdict(lambda : math.inf)
    for node, edges in graph.items():
        for dest in edges:
            dist[(node, dest)] = 1 # use weight if weighted
            if bidirectional:
                dist[(dest, node)] = 1
    # for node in graph.keys():
    #     dist[(node, node)] = 0
    for k in graph.keys():
        for i in graph.keys():
            for j in graph.keys():
                if dist[(i,j)] > dist[(i,k)] + dist[(k,j)]:
                    dist[(i,j)] = dist[(i,k)] + dist[(k,j)]
    return dist
    

def maxl(list):
    if len(list) == 0:
        return 0
    return max(list)

@cache
def dfs(here, mins_remaining, bitmask, players_remaining):
    acc = 0
    if mins_remaining <= 1: # it takes a min to open a valve
        if (players_remaining > 0):
            players_remaining -= 1
            return dfs(start, 26, bitmask, players_remaining)
        return 0

    ## Run past case!
    best = maxl([dfs(c, mins_remaining-dist[(here,c)], bitmask, players_remaining) 
                    for c in connect[here] if not (1<<c) & bitmask]) #if here == start else 0
    ## Open valve case
    if flow[here] > 0 and not bitmask & (1<<here):
        acc = (mins_remaining-1) * flow[here]
        mins_remaining -= 1 # It takes a min to open the valve
        if bitmask == tvalves:
            return acc
        # It takes a min to traverse the tunnel
        best = max(best, acc + maxl([dfs(c, mins_remaining-dist[(here,c)], bitmask | (1<<here), players_remaining) for c in connect[here] if not (1<<c) & bitmask]))

    return best

def solve():
    global tvalves, start, dist, connect

    all_conn = {}
    for row in input:
        # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
        valve = row.split(" ")[1]
        rate = int(row.split("rate=")[1].split(";")[0])
        if rate > 0:
            tvalves += 1
        if "lead to valves " in row:
            tunnels = row.split("lead to valves ")[1].split(", ")
        else:
            tunnels = [row.split("leads to valve ")[1]]
        flow[valve] = rate
        all_conn[valve] = tunnels

    remap = {p[0]:i for i,p in enumerate(sorted([(k,v) for k,v in flow.items()],
        key=cmp_to_key(lambda x,y: y[1]-x[1])))}
    start = remap["AA"]

    dist_pairs = floyd_warshall(all_conn)

    for (n,o), d in dist_pairs.items():
        if d != math.inf and flow[o] > 0:
            connect[remap[n]].append(remap[o])
            dist[(remap[n],remap[o])] = d

    tvalves = (1 << (len([(k,v) for k,v in flow.items() if k == "AA" or v > 0]) - 2)) - 1

    for k,v in remap.items():
        flow[v] = flow[k]
        del(flow[k])

    assert(dfs(start, 30, 0, 0) == 2320)
    assert(dfs(start, 26, 0, 1) == 2967)

solve()


# Progress:
# Initial DFS implementation without frozenset:
## time python main.py 
## python main.py  95.10s user 1.09s system 99% cpu 1:36.24 total
# With frozenset:
## python main.py  55.31s user 1.35s system 99% cpu 56.710 total
# With pypy:
## 40.93s user 1.75s system 99% cpu 42.686 total
# Remove non-flow valves (BFS dist table)
## 39.15s user 0.39s system 99% cpu 39.555 total
# int bitmask instead of frozenset
## 34.73s user 0.48s system 99% cpu 35.222 total
# floyd-warshall instead of BFS
## 31.14s user 0.55s system 99% cpu 31.733 total
