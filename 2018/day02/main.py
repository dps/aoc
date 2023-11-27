
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
input = [i.strip() for i in open("input","r").readlines()]

def part1():
    twos = 0
    threes = 0
    for line in input:
        c = Counter(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    aoc(twos*threes)

def part2():
    for pairs in combinations(input, 2):
        diff = 0
        same = []
        for l,r in zip(pairs[0], pairs[1]):
            if l != r:
                diff += 1
            else:
                same.append(l)
        if diff == 1:
            aoc("".join(same))
            return


part1()
part2()
