from utils import *
from functools import reduce
import operator
input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    score=set()
    g = grid_from_strs(input).g()
    # top
    for col in range(len(g[0])):
        cur = -1
        h = -1
        while cur < len(g[0]) - 1:
            if int(g[cur+1][col]) > h:
                h = int(g[cur+1][col])
                score.add((cur+1, col))
            cur += 1
    # btm
    for col in range(len(g[0])):
        cur = len(g[0])
        h = -1
        while cur >= 0:
            if int(g[cur-1][col]) > h:
                h = int(g[cur-1][col])
                score.add((cur-1, col))
            cur -= 1
    # left
    for row in range(len(g[0])):
        cur = -1
        h = -1
        while cur < len(g[0]) - 1:
            if int(g[row][cur+1]) > h:
                h = int(g[row][cur+1])
                score.add((row, cur+1))
            cur += 1
    # right
    for row in range(len(g[0])):
        cur = len(g[0])
        h = -1
        while cur >= 0:
            if int(g[row][cur-1]) > h:
                h = int(g[row][cur-1])
                score.add((row, cur-1))
            cur -= 1
    print(len(score))


def cs(g, x, y):
    s = len(g.g()[0])
    cs = []
    g.set_cursor(x,y)
    max = int(g.get())
    # up
    c = 0
    while g._cursor[1] > 0:
        g.move(0,-1)
        c+=1
        if int(g.get()) >= max:
            break
    cs.append(c)
    # down
    c = 0
    g.set_cursor(x,y)
    while g._cursor[1] < s-1:
        g.move(0,1)
        c+=1
        if int(g.get()) >= max:
            break
    cs.append(c)
    # left
    c = 0
    g.set_cursor(x,y)
    while g._cursor[0] > 0:
        g.move(-1,0)
        c+=1
        if int(g.get()) >= max:
            break
    cs.append(c)
    # right
    c = 0
    g.set_cursor(x,y)
    while g._cursor[0] < s-1:
        g.move(1,0)
        c+=1
        if int(g.get()) >= max:
            break
    cs.append(c)
    return reduce(operator.mul, cs, 1)

def part2():
    g = grid_from_strs(input)
    max_scene = 0
    for row in range(1,len(g.g()[0])-1):
        for col in range(1,len(g.g()[0])-1):
            x = cs(g, row, col)
            if x > max_scene:
                max_scene = x
    print(max_scene)


if __name__ == '__main__':
    part1()
    part2()