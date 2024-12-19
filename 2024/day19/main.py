
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0
designs = [d.strip() for d in D[0].split(",")]
patterns = D[2:]

@cache
def dfs(pattern):
    return 1 if len(pattern) == 0 else sum(dfs(pattern[len(design):]) for design in designs if pattern.startswith(design))

for pattern in patterns:
    s = dfs(pattern)
    p1 += 1 if s > 0 else 0
    p2 += s
        
print(p1, p2)