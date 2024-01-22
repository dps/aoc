
from utils import *

from copy import copy
D = [i.strip() for i in open("input","r").readlines()]

w = len(D[0])
h = len(D)
world = defaultdict(lambda:' ')
DIR8 = [(1, -1), (-1, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

for r, row in enumerate(D):
    for c, ch in enumerate(row):
        world[(r,c)] = ch

seen = {}
rev_seen = {}

for i in range(1000):
    new_world = defaultdict(lambda:' ')

    for r in range(h):
        for c in range(w):
            adj = Counter([world[(r+d[0], c+d[1])] for d in DIR8])
            if world[(r,c)] == ".":
                if adj['|'] >= 3:
                    new_world[(r,c)] = "|"
                else:
                    new_world[(r,c)] = "."
            elif world[(r,c)] == "|":
                if adj['#'] >= 3:
                    new_world[(r,c)] = "#"
                else:
                    new_world[(r,c)] = "|"
            elif world[(r,c)] == "#":
                if adj['#'] >= 1 and adj['|'] >= 1:
                    new_world[(r,c)] = "#"
                else:
                    new_world[(r,c)] = "."
    
    world = copy(new_world)

    if i == 9:
        c = Counter(world.values())
        print("Part 1", c['|']*c['#'])

    b = tuple(world[(r,c)] for c in range(w) for r in range(h))
    if b in seen:
        j = seen[b]
        break
    seen[b] = i
    rev_seen[i] = b

target = 1000000000
loop_len = i-j
target -= j+1
target %= loop_len
b = rev_seen[j+target]
c = Counter(b)
print("Part 2", c['|']*c['#'])


