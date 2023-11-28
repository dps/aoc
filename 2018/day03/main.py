
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

#1 @ 429,177: 12x27

def part1():
    claims = defaultdict(int)
    
    for line in input:
        p = ints(line.split("@")[1])
        for x in range(p[0],p[0]+p[2]):
            for y in range(p[1],p[1]+p[3]):
                claims[(x,y)] += 1
        
    aoc(sum([1 for _,v in claims.items() if v >= 2]))

def part2():
    claims = defaultdict(int)
    
    for line in input:
        p = ints(line.split("@")[1])
        for x in range(p[0],p[0]+p[2]):
            for y in range(p[1],p[1]+p[3]):
                claims[(x,y)] += 1

    for line in input:
        id = line.split("@")[0]
        p = ints(line.split("@")[1])
        found = True
        for x in range(p[0],p[0]+p[2]):
            for y in range(p[1],p[1]+p[3]):
                if claims[(x,y)] > 1:
                    found = False
        if found:
            aoc(id)
            return

part1()
part2()
