
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

cover = max(-mix+mxx,-miy+mxy,-miz+mxz)
pow2 = math.ceil(math.log2(cover))-1
e = 2**pow2

oct = ((-e,e),(-e,e),(-e,e))

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


def intersect_box(bot_num, box):    
    (lx,hx),(ly,hy),(lz,hz) = box
    hx,hy,hz=hx-1,hy-1,hz-1
    x,y,z,r = bots[bot_num]
    # if center is inside box, true:
    if lx <= x <= hx and ly <= y <= hy and lz <= z <= hz:
        return True
    
    distance = 0
    if x < lx:  # Bot is to the left of the box
        distance += (lx - x)
    elif x > hx:  # Bot is to the right of the box
        distance += (x - hx)
    if y < ly:  # Bot is below the box
        distance += (ly - y)
    elif y > hy:  # Bot is above the box
        distance += (y - hy)
    if z < lz:  # Bot is in front of the box
        distance += (lz - z)
    elif z > hz:  # Bot is behind the box
        distance += (z - hz)

    return distance <= r


def isect_count(box):
    return len([b for b in bots.keys() if intersect_box(b, box)])


to_handle = [(-math.inf, -(oct[0][1]-oct[0][0]), oct, 0)]
while to_handle:
    cnt, width, oct,level = heapq.heappop(to_handle)

    if width == 0:
        print("Part 2", manhattan3((0,0,0), (oct[0][0], oct[1][0], oct[2][0])))
        break

    boxen = cut_box(oct)
    width = boxen[0][0][1] - boxen[0][0][0]
    isects = sorted([(isect_count(box), box) for box in boxen],reverse=True)
    mx = isects[0][0]

    for count, box in isects:
        if count == mx:
            heapq.heappush(to_handle, (-count, -width, box, level+1))
