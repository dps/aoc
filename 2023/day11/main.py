
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]

def part1():
    global D
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    g,w,h,_ = grid_from_strs(D)
    expand_rows, expand_cols = [], []
    for y in range(h):
        if all((c == '.' for c in g[y])):
            expand_rows.append(y)
    print(expand_rows)
    for x in range(w):
        if all((g[y][x] == '.' for y in range(h))):
            expand_cols.append(x)
    print(expand_cols)
    expand_rows = sorted(expand_rows)
    expand_cols = sorted(expand_cols)

    def find_x(x):
        exp = [xx for xx in expand_cols if xx < x]
        return x + (1000000-1)*len(exp)
    def find_y(y):
        return y + (1000000-1)*len([yy for yy in expand_rows if yy < y])
    
    galaxies = set()
    yy = 0
    xx = 0
    for y in range(h):
        for x in range(w):
            if g[y][x] == '#':
                new_pos = (find_x(x), find_y(y))
                galaxies.add(new_pos)

    print(galaxies)

    pairs = list(combinations(galaxies, 2))
    print(len(pairs))

    def gneighbors(p):
        for d in DIR:
            q = (p[0] + d[0], p[1] + d[1])
            # if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
            #     continue
            yield (1, q)

    for a,b in pairs:
        #print(".", a, b)
        #dk = dynamic_a_star(gneighbors, a, b, manhattan)[0]
        #print(".", a,b, dk)
        #print(dk, manhattan(a,b))
        dk = manhattan(a,b)
        tot += dk
        
    
        
    aoc(tot)

part1()
#part2()
