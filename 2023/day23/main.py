
from utils import *

D = [i.strip() for i in open("input","r").readlines()]
tot = 0

g,w,h,_ = grid_from_strs(D)
start = (1,0)
end = (w-2,h-1)

mm = 0
def dfs(p, l, visited):
    global mm,g,end
    #print("dfs", p, l, visited)
    if p == end:
        #print("END", visited)
        mm = max(l, mm)
    else:
        # d = None
        # if g[p[1]][p[0]] == ">":
        #     d = (1,0)
        # elif g[p[1]][p[0]] == "<":
        #     d = (-1,0)
        # elif g[p[1]][p[0]] == "^":
        #     d = (0,-1)
        # elif g[p[1]][p[0]] == "v":
        #     d = (0, 1)
        # if d:
        #     if (p[0]+d[0],p[1]+d[1]) not in visited:
        #         dfs((p[0]+d[0],p[1]+d[1]), l+1, visited | {p})
        # else:
            for n in grid_neighbors(p,w,h):
                if n not in visited and g[n[1]][n[0]] != "#":
                    dfs(n,l+1, visited | {p})

dfs(start, 0, set())
print(mm)


# Q,visited = deque([(start,0)]),set()
# mm = 0
# while Q:
#     p,l = Q.popleft()
#     mm = max(mm, l)
#     d = None
#     if g[p[1]][p[0]] == ">":
#         d = (1,0)
#     elif g[p[1]][p[0]] == "<":
#         d = (-1,0)
#     elif g[p[1]][p[0]] == "^":
#         d = (0,-1)
#     elif g[p[1]][p[0]] == "v":
#         d = (0, 1)
#     if d != None:
#         n = (p[0]+d[0], p[1]+d[1])
#         if n not in visited:
#             Q.append((n,l+1))
#             visited.add(n)
#     else:
#         for n in grid_neighbors(p,w,h):
#             if n not in visited and g[n[1]][n[0]] != "#":
#                 Q.append((n, l+1))
#                 visited.add(n)

    
aoc(mm)