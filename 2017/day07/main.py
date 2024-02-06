
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

weights = {}
graph = defaultdict(list)
pre = defaultdict(int)

for line in D:
    name = line.split(" ")[0]
    w = ints(line)[0]
    weights[name] = w
    _ = pre[name]

    if "->" in line:
        _,r = line.split(" -> ")
        graph[name] = [o.strip() for o in r.split(",")]
        for d in graph[name]:
            pre[d] += 1

root = [n for n,v in pre.items() if v==0][0]
print(root)

tots = {}
def dfs(node):
    if len(graph[node]) == 0:
        tots[node] = weights[node]
    else:
        sub = [dfs(c) for c in graph[node]]
        tots[node] = sum(sub) + weights[node]
    return tots[node]

dfs(root)

q,q_mode,p = root,0,root
while True:
    children = [(tots[n], n) for n in graph[p]]
    mode = Counter([c[0] for c in children]).most_common()[0][0]
    odd = [o for o in children if o[0] != mode]
    if len(odd) == 0:
        # my parent needs to change
        print(q_mode - sum([o[0] for o in children]))
        break
    else:
        q = p
        q_mode = mode
        p = odd[0][1]
