from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

inputs = None

def decode(cop):
    s = str(cop).zfill(5)
    return s[0],s[1],s[2],int(s[3:])

def intcode(mem, input_num):
    global inputs

    pc = 0
    op = None
    relbase = 0

    while True:
        l = 0
        md,my,mx,op = decode(mem[pc])

        def param(mode, p,):
            nonlocal relbase, mem
            if mode == '1':
                return p
            if mode == '0':
                return mem[p]
            if mode == '2':
                return mem[relbase + p]

        def dest(md, d):
            nonlocal relbase
            return d if md == '0' else relbase + d

        if op == 1:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[dest(md,d)] = param(mx, x) + param(my, y)
            l = 4
        elif op == 2:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[dest(md,d)] = param(mx, x) * param(my, y)
            l = 4
        elif op == 3: # input
            x = mem[pc+1]
            mem[dest(mx,x)] = inputs[input_num][0]
            inputs[input_num] = inputs[input_num][1:]
            l = 2
        elif op == 4: # output
            x = mem[pc+1]
            yield(param(mx, x))
            l = 2
        elif op == 5: # jump-if-true
            x, y = mem[pc+1], mem[pc+2]
            if param(mx, x) != 0:
                pc = param(my, y)
            else:
                l = 3
        elif op == 6: # jump-if-false
            x, y = mem[pc+1], mem[pc+2]
            if param(mx, x) == 0:
                pc = param(my, y)
            else:
                l = 3
        elif op == 7: # <
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if param(mx, x) < param(my, y):
                mem[dest(md,d)] = 1
            else:
                mem[dest(md,d)] = 0
            l = 4
        elif op == 8: # ==
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if param(mx, x) == param(my, y):
                mem[dest(md,d)] = 1
            else:
                mem[dest(md,d)] = 0
            l = 4
        elif op == 9: # relbase
            x = mem[pc+1]
            relbase += param(mx, x)
            l = 2
        elif op == 99:
            break
        pc += l


def part1():
    global inputs
    mem = defaultdict(int)
    for i, v in enumerate([int(x) for x in input[0].split(",")]):
        mem[i] = v
    inputs = [[1]]
    for a in intcode(mem, 0):
        aoc(a)

def part2():
    global inputs
    mem = defaultdict(int)
    for i, v in enumerate([int(x) for x in input[0].split(",")]):
        mem[i] = v
    inputs = [[2]]
    for a in intcode(mem, 0):
        aoc(a)

part1()
part2()
