
from utils import *

# root@ebhq-gridcenter# df -h
# Filesystem              Size  Used  Avail  Use%
# /dev/grid/node-x0-y0     89T   65T    24T   73%

D = [i.strip() for i in open("input","r").readlines()]

w,h = 0,0
nodes = {}
caps = {}
used = {}
for line in D[2:]:
    vals = positive_ints(line)
    nodes[(vals[0],vals[1])] = tuple(vals[2:])
    caps[(vals[0],vals[1])] = vals[2]
    used[(vals[0],vals[1])] = vals[3]
    w = max(w, vals[0])
    h = max(h, vals[1])

w+=1
h+=1

c = 0
for a,b in combinations(nodes.keys(),2):
    if nodes[a][1] > 0 and nodes[a][1] <= nodes[b][2]:
        c += 1
    if nodes[b][1] > 0 and nodes[b][1] <= nodes[a][2]:
        c += 1
print(c)

# Algorithm is move free space to square left of goal (BFS around the wall)
# Then move it left along the top - each square takes five moves.
free = [k for k,v in nodes.items() if v[1] == 0][0]
phase1_goal = (w-2,0)
Q,visited = deque([(free,0)]),{free}
while Q:
    p,l = Q.popleft()
    if p == phase1_goal:
        break
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        q = (p[0]+d[0], p[1]+d[1])
        if 0 <= q[0] < w and 0 <= q[1] < h and q not in visited:
            if caps[p] >= used[q]:
                visited.add(q)
                Q.append((q,l+1))

phase1 = l+1
free = p
print(phase1 + 5*(free[0]))