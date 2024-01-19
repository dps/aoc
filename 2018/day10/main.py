
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

points = []
for line in D:
    # position=< -9767,  50146> velocity=< 1, -5>
    x, y, vx, vy = ints(line)
    points.append((x, y, vx, vy))

def centroid_distance(points):
    xs = [i[0] for i in points]
    ys = [i[1] for i in points]
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)
    return sum(manhattan((x,y), (cx,cy)) for x,y,_,_ in points)

prev = centroid_distance(points)
prev_points = None
time_elapsed = 0
while True:
    for i in range(len(points)):
        points[i] = (points[i][0]+points[i][2], points[i][1]+points[i][3], points[i][2], points[i][3])
    time_elapsed += 1
    curr = centroid_distance(points)
    if curr > prev:
        break
    prev = curr
    prev_points = points[:]

def print_world(world):
    mix, miy = int(min([p[0] for p in world])), int(min([p[1] for p in world]))
    mx, my = int(max([p[0] for p in world])), int(max([p[1] for p in world]))
    for y in range(miy, my + 1):
        print(
            "".join(["#" if (x,y) in world else "." for x in range(mix, mx + 1)])
        )

world = set()
for p in prev_points:
    world.add((p[0], p[1]))
print("Part 1:")
print_world(world)
print("Part 2", time_elapsed - 1)
