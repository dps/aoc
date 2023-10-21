from utils import *

input = [int(i.strip()) for i in open("input.txt","r").readlines()]

def part1():
    for p in combinations(input, 2):
        if sum(p) == 2020:
            aoc(p[0]*p[1])
            break

def part2():
    #p = map(lambda x: (x[0], x[1][0], x[1][1]), product(input, product(input, input)))
    for i in combinations(input, 3):
        if sum(i) == 2020:
            aoc(i[0]*i[1]*i[2])
            break

part1()
part2()