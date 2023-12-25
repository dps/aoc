
from utils import *
import networkx as nx

D = [i.strip() for i in open("input","r").readlines()]

tot = 0

graph = nx.DiGraph()

conn = defaultdict(list)
conns = set()
for line in D:
    from_, to_ = line.split(":")
    to_ = to_.strip()
    conn[from_] = to_.split(" ")
    for e in to_.split(" "):
        l = sorted([from_, e])
        conns.add((l[0], l[1]))
        graph.add_edge(from_, e, capacity=1.0)
        graph.add_edge(e, from_, capacity=1.0)

cut = nx.minimum_edge_cut(graph)
assert(len(cut) == 3)

cc = deepcopy(conns)
for d in cut:
    cc.remove(tuple(sorted(d)))

parts = []
for edge in cc:
    to_connect = []
    for p in parts:
        if edge[0] in p or edge[1] in p:
            to_connect.append(p)
    if len(to_connect) == 0:
        parts.append(set([edge[0], edge[1]]))
        continue
    if len(to_connect) == 1:
        to_connect[0].add(edge[0])
        to_connect[0].add(edge[1])
    elif len(to_connect) == 2:
        to_connect[0].update(to_connect[1])
        parts.remove(to_connect[1])
    to_connect[0].add(edge[0])
    to_connect[0].add(edge[1])

assert(len(parts) == 2)

aoc(len(parts[0])*len(parts[1]))
