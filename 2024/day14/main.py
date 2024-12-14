
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0
W, H = 101, 103

robots = []
for line in D:
    robots.append(ints(line))


def print_dict_world(world):
    mix = int(min([k[0] for k in world.keys()]))
    miy = int(min([k[1] for k in world.keys()]))
    mx = int(max([k[0] for k in world.keys()]))
    my = int(max([k[1] for k in world.keys()]))

    for y in range(miy, my + 1):
        for x in range(mix, mx + 1):
            if (x, y) in world:
                print(world[(x, y)], end="")
            else:
                print(".", end="")
        print()

def part1(robots):
    a,b,c,d = [], [], [], []
    for robot in robots:
        if robot[0] < W//2 and robot[1] < H//2:
            a.append(robot)
        elif robot[0] < W//2 and robot[1] > H//2:
            b.append(robot)
        elif robot[0] > W//2 and robot[1] < H//2:
            c.append(robot)
        elif robot[0] > W//2 and robot[1] > H//2:
            d.append(robot)
    print("Part 1:", len(a) * len(b) * len(c) * len(d))

maxd = math.inf
minj = 0
max_world = None
for j in range(10000):
    new_robots = []
    for robot in robots:
        new_robots.append(((robot[0]+robot[2])%W, (robot[1]+robot[3])%H, robot[2], robot[3]))
    robots = new_robots

    if j == 99:
        part1(robots)

    world = defaultdict(int)
    for robot in robots:
        world[robot[0], robot[1]] += 1

    prox = robots[0:10]
    dist = 0
    for p in combinations(prox, 2):
        dist += cartesian(p[0], p[1])
    if dist < maxd:
        maxd = dist
        minj = j+1
        max_world = world

print("Part 2:", minj)
print("You should see a christmas tree")
print_dict_world(max_world)
