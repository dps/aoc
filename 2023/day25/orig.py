
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

for s,t in combinations(conn.keys(), 2):
    val, parts = nx.minimum_cut(graph, s, t)
    if val == 3 and len(parts) == 2:
        aoc(len(parts[0])*len(parts[1]))
        break

# Brute force, which works for example but is way too slow for input.
# print(len(conns))
# i = 0
# for dd in combinations(conns, 3):
#     if (i % 10000) == 0:
#         print(i)
#         print(i/7219585036)
#     cc = deepcopy(conns)
#     for d in dd:
#         cc.remove(d)

#     parts = []
#     for edge in cc:
#         to_connect = []
#         for p in parts:
#             if edge[0] in p or edge[1] in p:
#                 to_connect.append(p)
#         if len(to_connect) == 0:
#             parts.append(set([edge[0], edge[1]]))
#             continue
#         if len(to_connect) == 1:
#             to_connect[0].add(edge[0])
#             to_connect[0].add(edge[1])
#         elif len(to_connect) == 2:
#             to_connect[0].update(to_connect[1])
#             parts.remove(to_connect[1])
#         to_connect[0].add(edge[0])
#         to_connect[0].add(edge[1])

#     if len(parts) == 2:
#         aoc(len(parts[0])*len(parts[1]))
#         sys.exit(0)
#     i += 1

# print("done")