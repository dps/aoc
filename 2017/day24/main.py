from collections import defaultdict
import re

def ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))

D = [i.strip() for i in open("input","r").readlines()]

components = []
lefts = defaultdict(list)
start = None
for i, line in enumerate(D):
    l,r = ints(line)
    components.append((l,r))
    if l == 0:
        start = i
    lefts[l].append((i, r))
    lefts[r].append((i, l))

ll = 0
lses = []
mm = -1
def dfs(left, used, strength, length):
    global mm, ll, lses
    if length > ll:
        ll = length
        lses = []
    if length == ll:
        lses.append(strength)

    poss = [(i,r) for (i,r) in lefts[left] if i not in used]
    if len(poss) == 0:
        mm = max(mm, strength)
    else:
        for (i,r) in poss:
            dfs(r, used|{i}, strength+left+r, length+1)

dfs(0, set(), 0, 0)
print(mm, max(lses))

