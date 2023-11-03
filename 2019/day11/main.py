from utils import *

input = [i.strip() for i in open("input","r").readlines()]

inputs = None
pos = 0
world = defaultdict(int)

def decode(cop):
    s = str(cop).zfill(5)
    return s[0],s[1],s[2],int(s[3:])

def intcode(mem):
    global inputs, pos, world

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
            mem[dest(mx,x)] = world[pos]
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
    yield None

def part1():
    global inputs, world, pos
    mem = defaultdict(int)
    for i, v in enumerate([int(x) for x in input[0].split(",")]):
        mem[i] = v
    
    vect = -1j
    computer = intcode(mem)
    while True:
        c = next(computer)
        if c == None:
            break
        world[pos] = c
        d = next(computer) # 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
        if d == 0:
            vect *= -1j
        else:
            vect *= 1j
        pos += vect
    print(len(world.keys()))


def part2():
    global inputs, world, pos
    mem = defaultdict(int)
    for i, v in enumerate([int(x) for x in input[0].split(",")]):
        mem[i] = v
    
    vect = -1j
    computer = intcode(mem)
    world[pos] = 1
    while True:
        c = next(computer)
        if c == None:
            break
        world[pos] = c
        d = next(computer) # 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
        if d == 0:
            vect *= -1j
        else:
            vect *= 1j
        pos += vect
    w = set()
    for k,v in world.items():
        if v == 1:
            w.add(k)
    print_world(w)

part1()
inputs,pos,world = None, 0, defaultdict(int)
part2()
