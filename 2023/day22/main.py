
from utils import *
from operator import itemgetter

D = [i.strip() for i in open("input","r").readlines()]

elevated = []
for brick, line in enumerate(D):
    s,e = line.split("~")
    ss,ee = ints(s),ints(e)
    #x,y,z
    # all bricks are only extruded in one dir
    extrude,small,large = None,None,None
    for ext in range(0,3):
        if ss[ext] != ee[ext]:
            extrude = ext
            small = ss if ss[ext] < ee[ext] else ee
            large = ss if ss[ext] > ee[ext] else ee
    if extrude == None:
        elevated.append([ss])
    else:
        bb = []
        for j in range(small[extrude], large[extrude]+1):
            bb.append(tuple((small[h] if h != extrude else j for h in range(3))))
        bb = sorted(bb, key=itemgetter(2))
        elevated.append(bb)

# Sort by z
elevated = sorted(elevated, key=lambda l: itemgetter(2)(l[0]))

def drop_bricks(elevated):
    new_bricks = []
    world=set()
    dropped = set()
    for i, brick in enumerate(elevated):
        while True:
            b = brick[0]
            zz = b[2]
            lowest = [o for o in brick if o[2] == zz]
            # try dropping by 1
            if any((v[0], v[1], v[2]-1) in world for v in lowest) or b[2] == 1:
                # settled
                new_bricks.append(brick)
                for cell in brick:
                    world.add(cell)
                break
            else:
                brick = tuple((k[0], k[1], k[2]-1) for k in brick)
                dropped.add(i)
    return new_bricks, len(dropped)

# Let them all settle once.
new_bricks, _ = drop_bricks(elevated)

p1, p2 = 0, 0
for i in range(len(new_bricks)):
    nb = deepcopy(new_bricks)
    nb.pop(i)
    _, dropped_count = drop_bricks(nb)
    if dropped_count == 0:
        p1 += 1
    p2 += dropped_count

print("Part 1:", p1, "Part 2:", p2)