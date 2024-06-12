
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def solve(part=1):
    lights = defaultdict(bool)

    for r, row in enumerate(D):
        for c, ch in enumerate(row):
            if ch == "#":
                lights[1j*r + c] = True

    # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

    def iterate(grid):
        new_grid = defaultdict(bool)
        for r in range(100):
            for c in range(100):
                cn = 0
                for d in CDIR8:
                    if grid[1j*r + c + d]:
                        cn += 1

                if grid[1j*r + c]:
                    new_grid[1j*r + c] = cn == 2 or cn == 3
                else:
                    new_grid[1j*r + c] = cn == 3
        return new_grid

    def stick_corners():
        if part == 1:
            return
        lights[0] = True
        lights[99] = True
        lights[99j] = True
        lights[99j + 99] = True

    for _ in range(100):
        stick_corners()
        lights = iterate(lights)

    stick_corners()
    print(sum(lights.values()))

solve(1)
solve(2)
