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
    world={}
    supports=defaultdict(list)
    supported_by=defaultdict(list)
    for i, brick in enumerate(elevated):
        while True:
            b = brick[0]
            zz = b[2]
            lowest = [o for o in brick if o[2] == zz]
            # try dropping by 1
            if any((v[0], v[1], v[2]-1) in world for v in lowest) or b[2] == 1:
                bottom_supports = set([world[(v[0], v[1], v[2]-1)] for v in lowest if (v[0], v[1], v[2]-1) in world])
                # settled
                supported_by[i] = bottom_supports
                for k in bottom_supports:
                    supports[k].append(i)
                for cell in brick:
                    world[cell] = i
                break
            else:
                brick = tuple((k[0], k[1], k[2]-1) for k in brick)
    return supported_by, supports
# Let them all settle once.
supported_by, supports = drop_bricks(elevated)

p1, p2 = 0, 0
for i in range(len(D)):
    #supported_by[i] => list -- i is supported by that list
    #supports[i] => list -- all the bricks supported by i
    if all([len(supported_by[j]) > 1 for j in supports[i]]):
        p1 += 1
    else:
        Q, moved = deque([i] + supports[i]), set([i])
        while Q:
            b = Q.popleft()
            if len(supported_by[b] - moved) == 0:
                moved.add(b)
                Q.extend(supports[b])
        p2 += len(moved) - 1
print("day22", p1, p2)