from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve():
    points = []
    stepmaps = []
    for wire in input:
        step = {}
        steps = 0
        p = set()
        x,y = 0,0
        for move in wire.split(","):
            d = RLUD[move[0]]
            c = int(move[1:])
            for _ in range(c):
                x = x + d[0]
                y = y + d[1]
                steps += 1
                p.add((x,y))
                step[(x,y)] = steps
        points.append(p)
        stepmaps.append(step)

    isect = points[0] & points[1]
    print(sorted([manhattan((0,0), p) for p in isect])[0])
    print(sorted([stepmaps[0][p] + stepmaps[1][p] for p in isect])[0])


solve()

