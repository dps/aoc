
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def part1():
    aoc(sum(map(int, input)))
    
def part2():
    tot = 0
    tots = set([0])
    while True:
        for line in input:
            tot += int(line)
            if tot in tots:
                aoc(tot)
                return
            tots.add(tot)

part1()
part2()
