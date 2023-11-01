from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def decode(cop):
    s = str(cop).zfill(5)
    return s[0] == '1',s[1] == '1',s[2] == '1',int(s[3:])

def intcode(mem, input):
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
            mem[d] = input
            l = 2
        elif op == 4: # output
            x = mem[pc+1]
            aoc((x if mx else mem[x]))
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

    return mem[0]

mem = [int(x) for x in input[0].split(",")]
intcode(mem[:], 1)
intcode(mem[:], 5)

