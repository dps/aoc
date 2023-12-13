
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def reflect(grid,w,h,target_diff=0):
    for col in range(1,w):
        diff = 0
        for i in range(1, w):
            if col - i < 0 or col+(i-1) > w-1:
                break
            for j in range(h):
                a = grid[j][col-i]
                b = grid[j][col+(i-1)]
                if a != b:
                    diff += 1
        if diff == target_diff:
            return col

    for row in range(1,h):
        diff = 0
        for i in range(1, h):
            if row - i < 0 or row+(i-1) > h-1:
                break
            for j in range(w):
                a = grid[row-i][j]
                b = grid[row+(i-1)][j]
                if a != b:
                    diff += 1
        if diff == target_diff:
            return (100 * row)


p1,p2 = 0,0

for grid in bundles(D):
    g,w,h,_ = grid_from_strs(grid)
    p1 += reflect(g,w,h,target_diff=0)
    p2 += reflect(g,w,h,target_diff=1)
    
print("part1:", p1, " part2:", p2)
