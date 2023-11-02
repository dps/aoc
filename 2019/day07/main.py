from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]
inputs = None

def decode(cop):
    s = str(cop).zfill(5)
    return s[0] == '1',s[1] == '1',s[2] == '1',int(s[3:])

def intcode(mem, input_num):
    global inputs
    pc = 0
    op = None
    while True:
        l = 0
        md,my,mx,op = decode(mem[pc]) # True => immediate mode

        if op == 1:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[d] = (x if mx else mem[x]) + (y if my else mem[y])
            l = 4
        elif op == 2:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[d] = (x if mx else mem[x]) * (y if my else mem[y])
            l = 4
        elif op == 3: # input
            d = mem[pc+1]
            mem[d] = inputs[input_num][0]
            inputs[input_num] = inputs[input_num][1:]
            l = 2
        elif op == 4: # output
            x = mem[pc+1]
            yield((x if mx else mem[x]))
            l = 2
        elif op == 5: # jump-if-true
            x, y = mem[pc+1], mem[pc+2]
            if (x if mx else mem[x]) != 0:
                pc = (y if my else mem[y])
            else:
                l = 3
        elif op == 6: # jump-if-false
            x, y = mem[pc+1], mem[pc+2]
            if (x if mx else mem[x]) == 0:
                pc = (y if my else mem[y])
            else:
                l = 3
        elif op == 7: # <
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if (x if mx else mem[x]) < (y if my else mem[y]):
                mem[d] = 1
            else:
                mem[d] = 0
            l = 4
        elif op == 8: # ==
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if (x if mx else mem[x]) == (y if my else mem[y]):
                mem[d] = 1
            else:
                mem[d] = 0
            l = 4
        elif op == 99:
            break
        pc += l

    yield None

def part1():
    global inputs
    mem = [int(x) for x in input[0].split(",")]

    msf = 0
    for vals in permutations(range(5)):
        acc = 0
        for v in vals:
            inputs = [[int(v), int(acc)]]
            r = next(intcode(mem[:], 0))
            acc = r
        msf = max(msf, acc)
    aoc(msf)

def part2():
    global inputs
    mem = [int(x) for x in input[0].split(",")]

    msf = 0
    for vals in permutations(range(5,10)):
        inputs = [[v] for v in vals]
        inputs[0].append(0)
        computers = [intcode(mem[:], i) for i in range(5)]

        running = 0
        out = 0
        prev = 0
        while True:
            prev = out
            out = next(computers[running])
            if out == None:
                break
            running += 1
            running %= 5
            inputs[running].append(out)
        msf = max(msf, prev)
    aoc(msf)

part1()
part2()