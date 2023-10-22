from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def apply_mask(mask, val):
    v = bin(val)[2:]
    vv = ((36-len(v))*'0') + v
    vvv = ''
    for m,x in zip(mask, vv):
        if m == 'X':
            vvv += x
        else:
            vvv += m
    return int(vvv, 2)

def part1():
    mem = {}
    mask = None
    for line in input:
        if line.split(" = ")[0] == "mask":
            mask = line.split(" = ")[1]
        else:
            vals = positive_ints(line)
            mem[vals[0]] = apply_mask(mask, vals[1])

    sum = 0
    for v in mem.values():
        sum += v

    aoc(sum)

M = {}
def set_all(addr, val, pos):
    if pos == len(addr):
        a = int(addr, 2)
        M[a] = val
    elif addr[pos] == 'X':
        set_all(addr[0:pos] + '0' + addr[pos+1:], val, pos+1)
        set_all(addr[0:pos] + '1' + addr[pos+1:], val, pos+1)
    else:
        set_all(addr, val, pos+1)

def write_mask(mask, base_addr, val):
    v = bin(base_addr)[2:]
    vv = ((36-len(v))*'0') + v
    vvv = ''
    for m,x in zip(mask, vv):
        if m == '0':
            vvv += x
        elif m == '1':
            vvv += '1'
        elif m == 'X':
            vvv += 'X'
    set_all(vvv, val, 0)

def part2():
    mask = None
    for line in input:
        if line.split(" = ")[0] == "mask":
            mask = line.split(" = ")[1]
        else:
            vals = positive_ints(line)
            write_mask(mask, vals[0], vals[1])

    sum = 0
    for v in M.values():
        sum += v

    aoc(sum)


part1()
part2()