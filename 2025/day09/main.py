from utils import *

D = [line.strip() for line in open("input")]

# Part 1
corners = []
for line in D:
    corners.append(ints(line))

def area(x):
    a,b = x
    dr = abs(a[0]-b[0]) + 1
    dc = abs(a[1]-b[1]) + 1
    return dr * dc

big_rects = sorted(map(lambda p: (area(p), p), combinations(corners, 2)), reverse=True)
print("Part 1", max(big_rects)[0])

# Compress the grid
xs,ys = set(), set()
for line in D:
    x,y = ints(line)
    xs.add(x)
    ys.add(y)
xs = sorted(list(xs))
ys = sorted(list(ys))

MX = {x:i for i,x in enumerate(xs)}
MY = {y:i for i,y in enumerate(ys)}

def shrink(p):
    return (MX[p[0]], MY[p[1]])

W = set()

def add_line(p1, p2):
    if p1[0] == p2[0]:
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            W.add((p1[0], y))
    if p1[1] == p2[1]:
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            W.add((x, p1[1]))

corners = [shrink(ints(D[0]))]
prev = shrink(ints(D[0]))
for line in D[1:]:
    corners.append(shrink(ints(line)))
    add_line(prev, shrink(ints(line)))
    prev = shrink(ints(line))
add_line(prev, corners[0])


# Flood fill the inside of the area
Q = set([(corners[0][0]-1, corners[0][1]+1)])
visited = set()
while len(Q):
    p = Q.pop()
    if p in visited:
        continue
    visited.add(p)
    W.add(p)
    for dx in [-1,0,1]:
        for dy in [-1, 0, 1]:
            q = (p[0]+dx, p[1]+dy)
            if q not in W:
                Q.add(q)

def reject(rect):
    top = min(rect[0][1], rect[1][1])
    right = max(rect[0][0], rect[1][0])
    bottom = max(rect[0][1], rect[1][1])
    left = min(rect[0][0], rect[1][0])
    if (top, right) not in W:
        return True
    for x in range(left, right+1):
        for y in range(top, bottom+1):
            if (x,y) not in W:
                return True

    return False

for area, rect in big_rects:
    small_rect = shrink(rect[0]), shrink(rect[1])
    if not reject(small_rect):
        print("Part 2", area)
        exit(0)
