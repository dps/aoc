from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1(xx=3,yy=1):
    res = 0
    g, _, h = grid_from_strs(input)
    y = 0
    while y < h:
        if g.get() == '#':
            res += 1
        g.move(xx,yy)
        y += yy
    aoc(res)
    return res

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
def part2():
    aoc(part1(1,1) * part1(3, 1) * part1(5,1) * part1(7,1) * part1(1,2))

part1()
part2()
