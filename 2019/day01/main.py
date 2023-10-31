from utils import *

input = [int(i.strip()) for i in open("input.txt","r").readlines()]

def part1():
    aoc(sum((n // 3) - 2 for n in input))

def part2():
    tot = 0
    for n in input:
        inc = (n // 3) - 2
        while inc > 0:
            tot = tot + inc
            inc = (inc // 3) - 2

    aoc(tot)

part1()
part2()
