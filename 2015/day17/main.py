
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

containers = []
for i,line in enumerate(D):
    containers.append((int(line),i))

combs = set()

ways = defaultdict(set)

def count_bits(num):
    r = 0
    while num > 0:
        if num & 1:
            r += 1
        num = num >> 1
    return r

@cache
def dfs(available, used, rem):
    global combs
    if rem < 0:
        return
    if rem == 0:
        nused = count_bits(used)
        combs.add(used)
        ways[nused].add(used)
        return
    for i,choice in enumerate(containers):
        if 2**i & available:
            dfs(available - 2**i, used + 2**i, rem-choice[0])

avail = sum(2**i for i,_ in enumerate(containers))

dfs(avail, 0, 150)

print(len(combs))
print(len(ways[sorted(ways.keys())[0]]))
