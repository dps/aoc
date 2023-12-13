
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]

def reflect(grid,w,h):
    c, r = None, None
    for col in range(1,w):
        reflect = True
        for i in range(1, w):
            if col - i < 0 or col+(i-1) > w-1:
                break
            for j in range(h):
                a = grid[j][col-i]
                b = grid[j][col+(i-1)]
                if a != b:
                    reflect = False
                    break
            if reflect == False:
                break
        if reflect:
            return col

    for row in range(1,h):
        reflect = True
        for i in range(1, h):
            if row - i < 0 or row+(i-1) > h-1:
                break
            for j in range(w):
                a = grid[row-i][j]
                b = grid[row+(i-1)][j]
                if a != b:
                    reflect = False
                    break
            if reflect == False:
                break
        if reflect:
            return 100 * row
    


def part1():
    global D
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    for grid in bundles(D):
        g,w,h,_ = grid_from_strs(grid)
        tot += reflect(g,w,h)
        
    aoc(tot)

part1()
#part2()
