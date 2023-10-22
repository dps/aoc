from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def neighbors(x,y,z,w):
    for xx in [-1,0,1]:
        for yy in [-1,0,1]:
            for zz in [-1,0,1]:
                for ww in [-1,0,1]:
                    r = (x+xx,y+yy,z+zz,w+ww)
                    if r != (x,y,z,w):
                        yield r

def solve():
    active = set()
    for y, row in enumerate(input):
        for x, ch in enumerate(row):
            if ch == '#':
                active.add((x,y,0,0))

    for t in range(6):
        consider = set()
        next_active = set()

        for x,y,z,w in active:
            nn = neighbors(x,y,z,w)
            cnt = 0
            for n in nn:
                if n not in active:
                    consider.add(n)
                else:
                    cnt += 1
            if cnt == 2 or cnt == 3:
                next_active.add((x,y,z,w))
        for x,y,z,w in consider:
            nn = neighbors(x,y,z,w)
            cnt = 0
            for n in nn:
                if n in active:
                    cnt += 1
            if cnt == 3:
                next_active.add((x,y,z,w))
        active = next_active

    aoc(len(active))

solve()
