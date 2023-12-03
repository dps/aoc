
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def part1():
    tot = 0    
    symbols = set()
    pnums = []
    for y, line in enumerate(input):
        partial_num = ''
        p_num_pos = []
        for x, ch in enumerate(line):
            if ch.isdigit():
                partial_num += ch
                p_num_pos.append(x + 1j*y)
            elif ch != '.':
                symbols.add(x + 1j*y)
                if partial_num != '':
                    pnums.append((partial_num, p_num_pos))
                    partial_num = ''
                    p_num_pos = []
            else:
                if partial_num != '':
                    pnums.append((partial_num, p_num_pos))
                    partial_num = ''
                    p_num_pos = []
        if partial_num != '':
            pnums.append((partial_num, p_num_pos))
            partial_num = ''
            p_num_pos = []

    
    for nstr, poses in pnums:
        print(nstr, poses)
        b = False
        for p in poses:
            if b:
                break
            for d in CDIR8:
                if p+d in symbols:
                    tot += int(nstr)
                    b=True
                    break

    aoc(tot)

def part2():
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(input)])
    
    symbols = set()
    nums = {}
    pnums = []
    for y, line in enumerate(input):
        partial_num = ''
        p_num_pos = []
        for x, ch in enumerate(line):
            if ch.isdigit():
                partial_num += ch
                p_num_pos.append(x + 1j*y)
            elif ch != '.':
                symbols.add((ch, x + 1j*y))
                if partial_num != '':
                    pnums.append((partial_num, p_num_pos))
                    partial_num = ''
                    p_num_pos = []
            else:
                if partial_num != '':
                    pnums.append((partial_num, p_num_pos))
                    partial_num = ''
                    p_num_pos = []
        if partial_num != '':
            pnums.append((partial_num, p_num_pos))
            partial_num = ''
            p_num_pos = []

    
    # for nstr, poses in pnums:
    #     print(nstr, poses)
    #     b = False
    #     for p in poses:
    #         if b:
    #             break
    #         for d in CDIR8:
    #             if p+d in symbols:
    #                 tot += int(nstr)
    #                 b=True
    #                 break

    for t,p in symbols:
        if t != "*":
            continue
        c = 0
        ss = []

        for pn in pnums:
            b=False
            for pnn in pn[1]:
                if b:
                    break
                for d in CDIR8:
                    if pnn+d == p:
                        c += 1
                        ss.append(int(pn[0]))
                        b = True
                        break
        print(c, tot, ss)
        if c ==2:
            tot += ss[0] * ss[1]

    aoc(tot)

part2()
#part2()
