from utils import *

D = [line.strip() for line in open("input")]

def part1():
    tot = 0
    for row, line in enumerate(D):
        for col, ch in enumerate(line):
            if ch == '@':
                c = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (dx == 0 and dy == 0) or (row + dy < 0) or (col + dx < 0) or (row + dy >= len(D)) or (col + dx >= len(D[0])):
                            continue
                        if D[row + dy][col + dx] == '@':
                            c += 1
                if c < 4:
                    tot += 1
    return tot

def part2():
    tot, changed = 0, 1
    grid = deepcopy(D)
    while changed > 0:
        new_grid = deepcopy(grid)
        changed = 0
        for row, line in enumerate(grid):
            for col, ch in enumerate(line):
                if ch == '@':
                    c = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if (dx == 0 and dy == 0) or (row + dy < 0) or (col + dx < 0) or (row + dy >= len(grid)) or (col + dx >= len(grid[0])):
                                continue
                            if grid[row + dy][col + dx] == '@':
                                c += 1
                    if c < 4:
                        tot += 1
                        changed += 1
                        new_grid[row] = new_grid[row][:col] + '.' + new_grid[row][col + 1:]
        grid = new_grid

    return tot

print(part1())
print(part2())