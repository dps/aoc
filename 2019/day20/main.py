from utils import *
from string import *

input = [i for i in open("input","r").readlines()]


def part1():
    grid = [list(line[2:-3]) for line in input[2:-2]]
    portals = defaultdict(list)
    sqsz = len(input[3]) - 4
    dwidth = 27
    for i, (a,b) in enumerate(zip(list(input[0]), list(input[1]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((i-2,0))
            grid[0][i-2]="*"
    for i, (a,b) in enumerate(zip(list(input[-2]), list(input[-1]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((i-2,sqsz))
            grid[sqsz][i-2] = "*"
    for i, (a,b) in enumerate(zip([a[0] for a in input[2:-2]], [b[1] for b in input[2:-2]])):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((0,i))
            grid[i][0] = "*"
    for i, line in enumerate(input[2:-2]):
        a,b = line[-3], line[-2]
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((sqsz-2,i))
            grid[i][sqsz-2] = "*"
    
    for i, (a,b) in enumerate(zip(list(input[dwidth+2]), list(input[dwidth+3]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((i-2,dwidth-1))
            grid[dwidth-1][i-2] = "*"

    for i, (a,b) in enumerate(zip(list(input[dwidth*3+3]), list(input[dwidth*3+4]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            grid[dwidth*3+3][i-2] = "*"
            portals[a+b].append((i-2,dwidth*3+3))

    for i, (a,b) in enumerate(zip([a[29] for a in input[2:-2]], [b[30] for b in input[2:-2]])):
        if a in ascii_uppercase and b in ascii_uppercase:
            grid[i][26] = "*"
            portals[a+b].append((26,i))    

    for i, (a,b) in enumerate(zip([a[82] for a in input[2:-2]], [b[83] for b in input[2:-2]])):
        if a in ascii_uppercase and b in ascii_uppercase:
            grid[i][82] = "*"
            portals[a+b].append((82,i))

    wrap = {}
    for _,v in portals.items():
        if len(v) == 2:
            l,r = v[0],v[1]
            wrap[l] = r
            wrap[r] = l
    
    start, end = portals['AA'][0], portals['ZZ'][0]
    grid[start[1]][start[0]] = "."
    grid[end[1]][end[0]] = "."

    def neighbors(p):
        if grid[p[1]][p[0]] == "*":
            yield 1,wrap[p]
        for n in grid_neighbors(p, len(grid[0]), len(grid)):
            if grid[n[1]][n[0]] in [".","*"]:
                yield 1,n

    aoc(dynamic_dijkstra(neighbors, start, end)[0])

def part2():
    grid = [list(line[2:-3]) for line in input[2:-2]]
    portals = defaultdict(list)
    sqsz = len(input[3]) - 4
    dwidth = 27
    for i, (a,b) in enumerate(zip(list(input[0]), list(input[1]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((i-2,0))
            grid[0][i-2]="$"
    for i, (a,b) in enumerate(zip(list(input[-2]), list(input[-1]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((i-2,sqsz))
            grid[sqsz][i-2] = "$"
    for i, (a,b) in enumerate(zip([a[0] for a in input[2:-2]], [b[1] for b in input[2:-2]])):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((0,i))
            grid[i][0] = "$"
    for i, line in enumerate(input[2:-2]):
        a,b = line[-3], line[-2]
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((sqsz-2,i))
            grid[i][sqsz-2] = "$"
    
    for i, (a,b) in enumerate(zip(list(input[dwidth+2]), list(input[dwidth+3]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            portals[a+b].append((i-2,dwidth-1))
            grid[dwidth-1][i-2] = "*"

    for i, (a,b) in enumerate(zip(list(input[dwidth*3+3]), list(input[dwidth*3+4]))):
        if a in ascii_uppercase and b in ascii_uppercase:
            grid[dwidth*3+3][i-2] = "*"
            portals[a+b].append((i-2,dwidth*3+3))

    for i, (a,b) in enumerate(zip([a[29] for a in input[2:-2]], [b[30] for b in input[2:-2]])):
        if a in ascii_uppercase and b in ascii_uppercase:
            grid[i][26] = "*"
            portals[a+b].append((26,i))    

    for i, (a,b) in enumerate(zip([a[82] for a in input[2:-2]], [b[83] for b in input[2:-2]])):
        if a in ascii_uppercase and b in ascii_uppercase:
            grid[i][82] = "*"
            portals[a+b].append((82,i))

    wrap = {}
    for _,v in portals.items():
        if len(v) == 2:
            l,r = v[0],v[1]
            wrap[l] = r
            wrap[r] = l
    
    start, end = portals['AA'][0], portals['ZZ'][0]
    start, end = (start[0], start[1], 0), (end[0], end[1], 0)
    grid[start[1]][start[0]] = "#"
    grid[end[1]][end[0]] = "@"

    def neighbors(p):
        if grid[p[1]][p[0]] == "*":
            yield 1,(wrap[p[0],p[1]][0], wrap[p[0],p[1]][1], p[2]+1)
        if grid[p[1]][p[0]] == "$" and p[2] > 0:
            yield 1,(wrap[p[0],p[1]][0], wrap[p[0],p[1]][1], p[2]-1)

        for n in grid_neighbors((p[0],p[1]), len(grid[0]), len(grid)):
            if grid[n[1]][n[0]] in [".", "*", "$"]:
                yield 1,(n[0],n[1],p[2])
            if grid[n[1]][n[0]] == "@" and p[2] == 0:
                yield 1,(n[0],n[1],p[2])

    aoc(dynamic_dijkstra(neighbors, start, end)[0])

part1()
part2()
