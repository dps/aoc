from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    #194,556 -> 739,556
    points = defaultdict(int)
    score = 0
    for line in input:
        ends = line.split("->")
        start = lmap(int, ends[0].split(","))
        end = lmap(int, ends[1].split(","))
        if start[0] == end[0]: #vertical
            if start[1] > end[1]:
                tmp = deepcopy(start)
                start = end
                end = tmp
            for y in range(start[1], end[1] + 1):
                points[(start[0],y)] += 1
        if start[1] == end[1]: #horiz
            if start[0] > end[0]:
                tmp = deepcopy(start)
                start = end
                end = tmp
            for x in range(start[0], end[0] + 1):
                points[(x,start[1])] += 1
    for (k,v) in points.items():
        if v >= 2:
            score += 1
    print(score)

def part2():
    #194,556 -> 739,556
    points = defaultdict(int)
    score = 0
    for line in input:
        ends = line.split("->")
        start = lmap(int, ends[0].split(","))
        end = lmap(int, ends[1].split(","))

        if start[0] != end[0] and start[1] != end[1]: #diag
            if start[1] > end[1]:
                tmp = deepcopy(start)
                start = end
                end = tmp
            xdir = 1 if start[0] < end[0] else -1
            for i, y in enumerate(range(start[1], end[1] + 1)):
                points[(start[0]+i*xdir,y)] += 1
        elif start[0] == end[0]: #vertical
            if start[1] > end[1]:
                tmp = deepcopy(start)
                start = end
                end = tmp
            for y in range(start[1], end[1] + 1):
                points[(start[0],y)] += 1
        elif start[1] == end[1]: #horiz
            if start[0] > end[0]:
                tmp = deepcopy(start)
                start = end
                end = tmp
            for x in range(start[0], end[0] + 1):
                points[(x,start[1])] += 1
    for (k,v) in points.items():
        if v >= 2:
            score += 1
    print(score)

part1()
part2()
