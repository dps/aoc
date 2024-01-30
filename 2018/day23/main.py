
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

bots = {}
mx,O = -math.inf,None
mix,miy,miz = math.inf, math.inf, math.inf
mxx,mxy,mxz = -math.inf,-math.inf,-math.inf

for i, line in enumerate(D):
    x,y,z,r = ints(line)
    if r > mx:
        mx = r
        O = (x,y,z,r)
    bots[i] = (x,y,z,r)
    mix,miy,miz = min(mix,x),min(miy,y),min(miz,z)
    mxx,mxy,mxz = max(mxx,x),max(mxy,y),max(mxz,z)

print(f"{mix}~{mxx} {-mix+mxx}, {miy}~{mxy} {-miy+mxy}, {miz}~{mxz} {-miz+mxz}")

cover = max(-mix+mxx,-miy+mxy,-miz+mxz)
pow2 = math.ceil(math.log2(cover))-1
e = 2**pow2

oct = ((-e,e),(-e,e),(-e,e))
print(f"{-e}~{e}")


def cut_box(box):
    boxes = []
    xext,yext,zext = box[0][1]-box[0][0], box[1][1]-box[1][0], box[2][1]-box[2][0]
    xext,yext,zext = xext//2,yext//2,zext//2
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                boxes.append(((box[0][0],box[0][0]+xext) if x == 0 else (box[0][0]+xext,box[0][1]),
                              (box[1][0],box[1][0]+yext) if y == 0 else (box[1][0]+yext,box[1][1]),
                              (box[2][0],box[2][0]+zext) if z == 0 else (box[2][0]+zext,box[2][1])))
    return boxes

origin = O[0:3]

p1 = len([b for b in bots.values() if manhattan3(b[0:3], origin) <= mx])
print("Part 1", p1)

def intersect(b1, b2):
    return manhattan3(bots[b1][0:3], bots[b2][0:3]) <= bots[b1][3]+bots[b2][3]

def intersectp(b, p):
    return manhattan3(bots[b][0:3], p) <= bots[b][3]

# def intersect_box(bot_num, box):
#     _, closest = sorted([(manhattan3(c, bots[bot_num][0:3]),c) for c in corners(box)])[0]
#     return intersectp(bot_num, closest)

def intersect_box(bot_num, box):
    (lx,hx),(ly,hy),(lz,hz) = box
    x,y,z,r = bots[bot_num]

    # if center is inside box, true:
    if lx <= x < hx and ly <= y < hy and lz <= z < hz:
        return True
    # figure out which face is closest to bot center
    # Initialize distance from bot center to the closest point on the box
    distance = 0

    # Check the x dimension
    if x <= lx:  # Bot is to the left of the box
        distance += (lx - x) ** 2  # Square of distance from bot to the closest x-face of the box
    elif x > hx:  # Bot is to the right of the box
        distance += (x - hx) ** 2  # Square of distance from bot to the closest x-face of the box

    # Check the y dimension
    if y <= ly:  # Bot is below the box
        distance += (ly - y) ** 2  # Square of distance from bot to the closest y-face of the box
    elif y > hy:  # Bot is above the box
        distance += (y - hy) ** 2  # Square of distance from bot to the closest y-face of the box

    # Check the z dimension
    if z <= lz:  # Bot is in front of the box
        distance += (lz - z) ** 2  # Square of distance from bot to the closest z-face of the box
    elif z > hz:  # Bot is behind the box
        distance += (z - hz) ** 2  # Square of distance from bot to the closest z-face of the box

    # Check if the closest distance is within the radius
    return distance <= r ** 2


def isect_count(box):
    return len([b for b in bots.keys() if intersect_box(b, box)])

max_by_level = defaultdict(int)
to_handle = deque([(oct,0,math.inf)])
results = []
while to_handle:
    oct, level, then_mx = to_handle.popleft()
    if then_mx < max_by_level[level]:
        continue
    boxen = cut_box(oct)
    print(boxen)
    isects = sorted([(isect_count(box), box, (box[0][1]-box[0][0])) for box in boxen],reverse=True)
    mx = isects[0][0]
    width = isects[0][2]
    if width == 1:
        results.append((mx, isects[0][1], level))
        continue
    if mx > max_by_level[level]:
        print(mx, level, width, isects[0][1])
        max_by_level[level] = mx
        for isect in isects:
            if isect[0] == mx and isect[0] >= max_by_level[level]:
                to_handle.append((isect[1], level+1,isect[0]))

print(results)
print((47350438, 43804862, 19685812))