from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

TARGET = 19690720

def intcode(mem, noun, verb):
    mem[1] = noun
    mem[2] = verb

    pc = 0
    op = None
    while True:
        op = mem[pc]
        if op == 1:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[d] = mem[x] + mem[y]
        elif op == 2:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[d] = mem[x] * mem[y]
        elif op == 99:
            break
        pc += 4

    return mem[0]

def part2():
    mem = [int(x) for x in input[0].split(",")]

    for noun in range(0,99):
        for verb in range(0,99):
            r = intcode(deepcopy(mem), noun, verb)
            if r == TARGET:
                aoc(noun*100+verb)
                return
            if r > TARGET:
                break

def part1():
    mem = [int(x) for x in input[0].split(",")]
    aoc(intcode(mem, 12, 2))

part1()
part2()
