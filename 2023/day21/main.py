
from utils import *

D = [i.strip() for i in open("input","r").readlines()]
g,w,h,start = grid_from_strs(D, find="S")

# I figured out by curve fitting in Google Sheets (!) that it's a quadratic
# this gives an approximation of my answer:
# I could make this more accurate, will still be an inexact answer
def poly(x):
    return 21.3 + 2.95 * x + 0.869 * x *x

# Key insight then is that given the periodicity of the grid
# reachable(s+1w), reachable(s+2w), ... is quadratic.
# We want the specific quadratic for s = goal % w

goal = 26501365
s = goal % w

def grid_neighbors(p):
    for d in DIR:
        q = (p[0] + d[0], p[1] + d[1])
        yield (q)

reachable = defaultdict(set)
blocked = defaultdict(set)
things = defaultdict(lambda :defaultdict(int))
Q, visited = deque([(start, 0)]), set()
while Q:
    p,steps = Q.popleft()
    if steps == (s+2*w) + 1:
        break
    reachable[steps].add(p)
    for n in grid_neighbors(p):
        if g[n[1]%h][n[0]%w] != "#":
            if (n,steps+1) not in visited:
                Q.append((n, steps+1))
                visited.add((n, steps+1))
        else:
            blocked[steps+1].add(n)

P = len(reachable[s]), len(reachable[s+w]), len(reachable[s+2*w])
print(P)

# f(0) = points[0], f(1) = points[1], f(2) = points[2]
# f = ax^2 + bx + c
# c = points[0]
# b+a = points[1]-points[0]
# 4a+2b = points[2] - points[0]
# 2b = 2*(points[1]-points[0] - a)
# 4a+2*(points[1]-points[0] - a) = points[2] - points[0]
# a = (points[2] -2*points[1] + points[0]) / 2
def quadratic(n):
    global P
    a = (P[2] -2*P[1] + P[0]) / 2
    b = (P[1]-P[0] - a)
    c = P[0]
    return a*(n*n) + b*n + c

print(quadratic(goal//w))
