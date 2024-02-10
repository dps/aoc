
from utils import *
from itertools import islice

key = open("input","r").read().strip()
print(key)
trailer = [17, 31, 73, 47, 23]

def hash_(lens, p=0, ss=0, vals=deque(range(256))):
    for l in lens:
        vals.rotate(-p)
        left, right = deque(islice(vals, l)), deque(islice(vals, l, len(vals)))
        left.reverse()
        vals = left
        vals.extend(right)
        vals.rotate(p)
        p += l + ss
        ss += 1
    return vals, p, ss

def hash(C):
    C.extend(trailer)

    vals, p, ss = deque(range(256)), 0, 0
    for _ in range(64):
        vals, p, ss = hash_(C, p, ss, vals)
    vl = list(vals)

    return "".join(
        [
            f"{reduce(lambda x,y: x^y, vl[s:s+16]):>08b}"
            for s in range(0, 256, 16)
        ]
    )

G, w = [], 128
for i in range(w):
    C = list(map(lambda ch: ord(ch), f"{key}-{i}"))
    b = hash(C)
    G.extend(list(b))

print(len([1 for c in G if c == '1']))

gc = 0
for i in range(w*w):
    if G[i] == "1":
        gc += 1
        Q, visited = deque([i]), set()
        while Q:
            p = Q.popleft()
            if p in visited:
                continue
            visited.add(p)
            G[p] = '*'
            for d in [-w,-1,1,w]:
                if (p % w) == w-1 and d == 1 or (p % w) == 0 and d == -1:
                    continue
                q = p + d
                if 0 <= q < w*w and G[q] == '1':
                    Q.append(q)

print(gc)


