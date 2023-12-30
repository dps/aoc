from utils import *

D = [i.strip() for i in open("input", "r").readlines()]
g, w, h, start = grid_from_strs(D, find="S")

# I figured out by curve fitting in Google Sheets (!) that it's a quadratic
# this gives an approximation of my answer:
# I could make this more accurate, will still be an inexact answer
def poly(x):
    return 21.3 + 2.95 * x + 0.869 * x * x


# Key insight then is that given the periodicity of the grid
# reachable(s+1w), reachable(s+2w), ... is quadratic.
# We want the specific quadratic for s = goal % w

goal = 26501365
s = goal % w
p2stop = (s + 2 * w) + 1

def compute_reachable():
    reachable = defaultdict(int)
    Q, visited = deque([(start, 0)]), defaultdict(set)
    while Q:
        p, steps = Q.popleft()
        if steps == 328:
            break
        reachable[steps] += 1
        for d in DIR:
            q = (p[0] + d[0], p[1] + d[1])
            # if q in ever_visited:
            #     continue
            # ever_visited.add(q)
            if g[(p[1]+d[1]) % h][(p[0]+d[0]) % w] != "#":
                if q not in visited[steps+1]:
                    Q.append((q, steps + 1))
                    visited[steps+1].add(q)
    return reachable

reachable = compute_reachable()

print("Part 1", reachable[64])
P = reachable[s], reachable[s + w], reachable[s + 2 * w]

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
    a = (P[2] - 2 * P[1] + P[0]) / 2
    b = P[1] - P[0] - a
    c = P[0]
    return a * (n * n) + b * n + c

print("Part 2", int(quadratic(goal // w)))
