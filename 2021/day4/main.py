from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def winval(g):
    s = 0
    for r in g:
        for c in r:
            if (c[0] != "["):
                s+=int(c)
    return s

def winning(g):
  print(len(g))
  winning_cols = [e for e in range(len(g))]
  for row in g:
    if set([x[0] for x in row]) == set("["):
        print("row win")
        return True
    for i, col in enumerate(row):
        if not col[0] == "[" and i in winning_cols:
            winning_cols.remove(i)
  print(winning_cols)
  return len(winning_cols)


def part1():
    score = 0
    calls = input.pop(0).split(",")
    input.pop(0)
    grids = []
    grid = None
    to_parse = []
    for line in input:
        if len(line) == 0:
            grid = grid_from_strs(to_parse, spl=' ')
            grids.append(grid)
            to_parse = []
            continue
        to_parse.append(line)
    grid = grid_from_strs(to_parse, spl=' ')
    grids.append(grid)

    for call in calls:
        print(call)
        for i, grid in enumerate(grids):
            g = grid.g()
            for y in range(len(g)):
                for x in range(len(g[0])):
                    if not g[y][x][0] == '[' and int(g[y][x]) == int(call):
                        g[y][x] = "[" + call + "]"
            if winning(g):
                grid.print()
                print(int(call) * winval(g))
                return
        for grid in grids:
            grid.print()
        print()
        print("--------------")


    print(score)


def part2():
    score = 0
    calls = input.pop(0).split(",")
    input.pop(0)
    grids = []
    grid = None
    to_parse = []
    for line in input:
        if len(line) == 0:
            grid = grid_from_strs(to_parse, spl=' ')
            grids.append(grid)
            to_parse = []
            continue
        to_parse.append(line)
    grid = grid_from_strs(to_parse, spl=' ')
    grids.append(grid)

    for call in calls:
        print(call)
        to_remove = []
        for i, grid in enumerate(grids):
            g = grid.g()
            for y in range(len(g)):
                for x in range(len(g[0])):
                    if not g[y][x][0] == '[' and int(g[y][x]) == int(call):
                        g[y][x] = "[" + call + "]"
            if winning(g):
                if len(grids) == 1:
                    grid.print()
                    print("Final Winner ", int(call) * winval(g))
                    return
                else:
                    to_remove.append(grid)

        for k in to_remove:
            grids.remove(k)

        for grid in grids:
            grid.print()
        print()
        print("--------------")


    print(score)        

#part1()
part2()
