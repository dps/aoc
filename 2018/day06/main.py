
from utils import *
from operator import itemgetter

input = [i.strip() for i in open("input","r").readlines()]

def part1():
    points = []
    counts = defaultdict(int)
    infinities = set()

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
            counts[closest[0][1]] += 1
            if xx == -1 or xx == mx+1 or yy == -1 or yy == my+1:
                infinities.add(closest[0][1])

    for i in infinities:
        del(counts[i])
    aoc(max(counts.items(), key=itemgetter(1))[1])


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


part1()
part2()
