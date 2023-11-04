from utils import *
from intcode import computer

input = [i.strip() for i in open("input","r").readlines()]

def part1():
    tot=0
    program = [int(x) for x in input[0].split(",")]

    screen = defaultdict(int)

    c = computer(program, lambda: 0)
    while True:
        x = next(c)
        if x == None:
            break
        y = next(c)
        b = next(c)
        screen[(x,y)] = b

    tot = sum([1 for k,v in screen.items() if v == 2])
    aoc(tot)

def print_world(world):
    mx = int(max([k[0] for k in world.keys()]))
    my = int(max([k[1] for k in world.keys()]))

    PX = {0: "⬛️", 1: "⬜️", 2: "🟧", 3: "🟦", 4: "⚪️"}

    print("\x1b[0;0H")
    for y in range(0, my+1):
        print("".join([PX[world[(x,y)]] for x in range(0, mx+1)]))

def part2():
    program = [int(x) for x in input[0].split(",")]
    program[0] = 2
    screen = defaultdict(int)

    ballpos = None
    paddlepos = None

    def inputfn():
        nonlocal ballpos, paddlepos
        if ballpos[0] < paddlepos[0]:
            return -1
        if ballpos[0] > paddlepos[0]:
            return 1
        return 0

    c = computer(program, inputfn)

    while True:
        x = next(c)
        if x == None:
            break
        y = next(c)
        b = next(c)
        screen[(x,y)] = b

        if b == 4:
            ballpos = (x,y)
        if b == 3:
            paddlepos = (x,y)

        #print_world(screen)

    aoc(screen[(-1,0)])

part1()
part2()