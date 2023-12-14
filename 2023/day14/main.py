
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]

def part1():
    global D
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    g,w,h,_ = grid_from_strs(D)
    new_grid = deepcopy(g)
    for j in range(h):
        for i in range(w):
            if g[j][i] == "O":
                jj = j
                while jj >0 and not (new_grid[jj-1][i] == 'O' or new_grid[jj-1][i] == '#'):
                    jj -= 1
                new_grid[j][i] = "."
                new_grid[jj][i] = "O"
            #print_grid(new_grid)
            #print(" ---  ")

    #print_grid(new_grid)
    for j in range(h):
        for i in range(w):
            if new_grid[j][i] == "O":
                tot += (h-j)
                

        
    aoc(tot)

part1()
#part2()
