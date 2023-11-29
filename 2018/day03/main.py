
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

#1 @ 429,177: 12x27

def part1():
    claims = defaultdict(int)
    
    for line in input:
        id, x,y,w,h = ints(line)
        for xx in range(x,x+w):
            for yy in range(y,y+h):
                claims[(xx,yy)] += 1
        
    aoc(sum([1 for _,v in claims.items() if v >= 2]))

def part2():
    claims = defaultdict(int)
    revclaims = defaultdict(list)
    
    for line in input:
        id, x,y,w,h = ints(line)
        for xx in range(x,x+w):
            for yy in range(y,y+h):
                claims[(xx,yy)] += 1
                revclaims[id].append((xx,yy))

    for k,v in revclaims.items():
        if all([claims[p] == 1 for p in v]):
            aoc(k)
            return

part1()
part2()
