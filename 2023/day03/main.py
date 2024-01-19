
from itertools import product
from collections import defaultdict
input = [i.strip() for i in open("input","r").readlines()]

g = [[ch for ch in row] for row in input]
h = len(g)
w = len(g[0])

DIR8 = [(1, -1), (-1, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

def solve():
    global g, w, h
    p1,p2 = 0,0
    gear_nums = defaultdict(list)
    for y, row in enumerate(g):
        num = 0
        has_part = False
        gears = set()
        for x, ch in enumerate(row + ["."]):
            if ch.isdigit():
                num = 10*num + int(ch)
                for dx,dy in DIR8:
                    if 0 <= y+dy < h and 0 <= x+dx < w:
                        cc = g[y+dy][x+dx]
                        if not cc.isdigit() and cc != ".":
                            has_part = True
                        if cc == "*":
                            gears.add((x+dx, y+dy))
            elif num != 0:
                if has_part:
                    p1 += num
                for gear in gears:
                    gear_nums[gear].append(num)
                num, has_part, gears = 0, False, set()
    for g,l in gear_nums.items():
        if len(l) == 2:
            p2 += l[0]*l[1]

    print(p1, p2)

solve()
