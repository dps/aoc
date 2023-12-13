
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]

def reflect(grid,w,h):
    c, r = None, None
    results = []
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
            results.append(col)

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
            results.append(100 * row)
    return results
    


def part1():
    global D
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    for grid in bundles(D):
        g,w,h,_ = grid_from_strs(grid)
        tot += reflect(g,w,h)
        
    aoc(tot)

def part2():
    global D
    tot = 0
    
    for grid in bundles(D):
        g,w,h,_ = grid_from_strs(grid)

        orig = set(reflect(g,w,h))
        print(orig)

        escape = False
        for r in range(h):
            for c in range(w):
                print(r,c)
                t = g[r][c]
                print(t)
                g[r][c] = "#" if t == "." else "."
                print(g)
                test = set(reflect(g,w,h))
                test = test - orig
                print("test", test)
                if len(test) == 1:
                    tot += test.pop()
                    escape = True
                    break
                g[r][c] = t
            if escape:
                break
        
    aoc(tot)

#part1()
part2() # 29388 too low
