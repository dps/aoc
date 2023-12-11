from utils import *

D = [i.strip() for i in open("input", "r").readlines()]


def solve(part=1):
    global D

    g, w, h, _ = grid_from_strs(D)
    expand_rows = [y for y in range(h) if all((c == "." for c in g[y]))]
    expand_cols = [x for x in range(w) if all((g[y][x] == "." for y in range(h)))]

    def new_pos(x, y):
        return (
            x
            + (1 if part == 1 else 999999) * len([xx for xx in expand_cols if xx < x]),
            y
            + (1 if part == 1 else 999999) * len([yy for yy in expand_rows if yy < y]),
        )

    galaxies = set()
    for y in range(h):
        for x in range(w):
            if g[y][x] == "#":
                galaxies.add(new_pos(x, y))

    aoc(sum((manhattan(a, b) for a, b in combinations(galaxies, 2))))


solve(1)
solve(2)
