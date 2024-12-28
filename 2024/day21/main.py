
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

keypad = {0: '7', 1: '8', 2: '9', 1j: '4', 1+1j: '5', 2+1j: '6', 2j: '1', 1+2j: '2', 2+2j: '3', 1+3j: '0', 2+3j: 'A'}
rkeypad = {v: k for k,v in keypad.items()}
kstart = 2+3j

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
arrow_pad = {1: '^', 2: 'A', 1j: '<', 1+1j: 'v', 2+1j: '>'}
rarrow_pad = {v: k for k,v in arrow_pad.items()}
astart = 2

DD = {'^': -1j, 'v': 1j, '<': -1, '>': 1}
DDR = {v: k for k,v in DD.items()}

@cache
def find_shortest_paths(pt, start, end):
    # start is like '1' and end like '2' or 'A'
    sp = rkeypad[start] if pt == "key" else rarrow_pad[start]
    ep = rkeypad[end] if pt == "key" else rarrow_pad[end]
    pad = keypad if pt == "key" else arrow_pad

    shortest, shortest_paths = math.inf, []
    visited = set()
    def dfs(c, end, path, l):
        nonlocal shortest, shortest_paths,visited
        if l > shortest:
            return
        if c == end:
            if len(path) < shortest:
                shortest = len(path)
                shortest_paths = [path]
            elif len(path) == shortest:
                shortest_paths.append(path)
            return
        else:
            for d in DD.values():
                if c+d in pad and (c+d) not in visited:
                    visited.add(c+d)
                    dfs(c+d, end, path+DDR[d], l+1)
                    visited.remove(c+d)
    dfs(sp, ep, "", 0)
    return shortest_paths

shorts = {}
for a,b in permutations(arrow_pad.values(), 2):
    shorts[(a,b)] = [p + "A" for p in find_shortest_paths("arrow", a, b)]
for a in arrow_pad.values():
    shorts[(a,a)] = ["A"]

@cache
def shortest_len_dfs(a, b, depth):
    if depth == 1:
        return len(shorts[(a,b)][0])
    mm = math.inf
    for path in shorts[(a,b)]:
        acc = 0
        for prev,next in zip("A" + path, path):
            acc += shortest_len_dfs(prev, next, depth-1)
        mm = min(mm, acc)
    return mm

for depth in [2, 25]:
    ans = 0
    for line in D:
        prev = 'A'
        paths = [""]
        for ch in line:
            step_paths = find_shortest_paths("key", prev, ch)
            new_paths = []
            for path in paths:
                for step_path in step_paths:
                    new_paths.append(path+step_path+"A")
            paths = new_paths
            prev = ch

        next_paths = paths

        mm = math.inf
        for path in next_paths:
            l = 0
            for prev,next in zip("A" + path, path):
                l += shortest_len_dfs(prev, next, depth)
            mm = min(mm, l)

        ans += mm * int(line[:-1])

    print(ans)
