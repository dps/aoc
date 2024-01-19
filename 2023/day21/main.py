from utils import *

D = [i.strip() for i in open("input", "r").readlines()]
g, w, h, start = grid_from_strs(D, find="S")

goal, s = 26501365, 26501365 % w
p2stop = (s + 2 * w) + 1 # 328

def compute_reachable():
    reachable = defaultdict(int)
    Q, visited = deque([(start, 0)]), defaultdict(set)
    visited[0] = set([start])
    while Q:
        p, steps = Q.popleft()
        if steps == p2stop:
            break
        reachable[steps] += 1
        for d in DIR:
            q = (p[0] + d[0], p[1] + d[1])
            if g[(p[1]+d[1]) % h][(p[0]+d[0]) % w] != "#":
                if not steps+1 in reachable:
                    reachable[steps+1] = reachable[steps-1]
                    visited[steps+1] = visited[steps-1]
                if q not in visited[steps+1]:
                    Q.append((q, steps + 1))
                    visited[steps+1].add(q)
    return reachable

reachable = compute_reachable()
print("Part 1", reachable[64])
P = reachable[s], reachable[s + w], reachable[s + 2 * w]

def quadratic(P, n):
    a = (P[2] - 2 * P[1] + P[0]) / 2
    b = P[1] - P[0] - a
    c = P[0]
    return a * (n * n) + b * n + c

print("Part 2", int(quadratic(P, goal // w)))