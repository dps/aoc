
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
input = [i.strip() for i in open("input","r").readlines()]

def part1():
    tot, prod = 0, 1
    max_sum = max([sum(map(int, lines)) for lines in bundles(input)])
    
    for line in input:
        pass
        
    aoc(max_sum)

part1()
#part2()
