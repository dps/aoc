
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
input = [i.strip() for i in open("input","r").readlines()]

def part1():
    prod = 1
    times = ints(input[0])
    distances = ints(input[1])
    td = list(zip(times, distances))

    for time,record in td:
        c = 0
        for i in range(1,time-1):
            if (time-i)*i > record:
                c += 1
        prod *= c        
    aoc(prod)

def part2():
    prod = 1
    times = ints(input[0].replace(" ",""))
    distances = ints(input[1].replace(" ",""))
    td = list(zip(times, distances))

    for time,record in td:
        c = 0
        for i in range(1,time-1):
            if (time-i)*i > record:
                c += 1
        prod *= c        
    aoc(prod)

part1()
part2()
