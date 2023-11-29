
from utils import *
from operator import itemgetter

input = [i.strip() for i in open("input","r").readlines()]

def part1():
    points = []
    world = defaultdict(int)
    mx,my = 0,0
    for line in input:
        x,y = map(int, line.split(","))
        mx,my = max(mx, x), max(my, y)
        points.append(x+1j*y)

    for xx in range(-1, mx+2):
        for yy in range(-1, my+2):
            closest = sorted([(manhattani(xx+1j*yy, p),i) for i,p in enumerate(points)], key=itemgetter(0))
            if closest[0][0] == closest[1][0]:
                continue
            world[xx+1j*yy] = closest[0][1]
    
    infinities = set()
    for xx in range(-1, mx+2):
        infinities.add(world[xx+1j*-1])
        infinities.add(world[xx+1j*(my+1)])
    for yy in range(-1, mx+2):
        infinities.add(world[-1+1j*yy])
        infinities.add(world[(mx+1)+1j*yy])

    cc = Counter()
    for v in world.values():
        if v not in infinities:
            cc[v] += 1

    aoc(cc.most_common()[0])


def part2():
    points = []
    world = set()
    mx,my = 0,0
    for line in input:
        x,y = map(int, line.split(","))
        mx,my = max(mx, x), max(my, y)
        points.append(x+1j*y)

    for xx in range(-1, mx+2):
        for yy in range(-1, my+2):
            closest = sum([manhattani(xx+1j*yy, p) for p in points])
            if closest < 10000:
                world.add(xx+1j*yy)
    
    aoc(len(world))


#part1()
part2()
