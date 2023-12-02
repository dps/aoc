
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def part1():
    tot = 0

    cap = {"red": 12, "green": 13, "blue": 14}
    
    for line in input:
        game = line.split(":")[0].split(" ")[-1]
        tries = line.split(":")[1].strip()
        possible = True
        for g in tries.split(";"):
            pairs = g.strip().split(",")
            for pair in pairs:
              num,color = pair.strip().split(" ")
              if int(num) > cap[color]:
                  possible = False
        if possible:
            tot += int(game)        
    aoc(tot)

def part2():
    tot = 0
    
    for line in input:
        tries = line.split(":")[1].strip()
        ms = defaultdict(int)
        for g in tries.split(";"):
            pairs = g.strip().split(",")
            for pair in pairs:
              num,color = pair.strip().split(" ")
              ms[color] = max(ms[color], int(num))
        tot += reduce(operator.mul, ms.values())
    aoc(tot)

part1()
part2()
