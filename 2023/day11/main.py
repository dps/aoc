from itertools import combinations
from functools import cache

D = [i.strip() for i in open("input", "r").readlines()]

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def solve(part=1):
    global D

    g = [[ch for ch in row] for row in D]
    h = len(g)
    w = h #square grid
    expand_rows = [y for y in range(h) if all((c == "." for c in g[y]))]
    expand_cols = [x for x in range(w) if all((g[y][x] == "." for y in range(h)))]

    # can we speed up new_pos? [minor speedup]
    @cache
    def exx(x):
        return len([xx for xx in expand_cols if xx < x])

    @cache
    def eyy(y):
        return len([yy for yy in expand_rows if yy < y])

    def new_pos(x, y):
        return (
            x
            + (1 if part == 1 else 999999) * exx(x),
            y
            + (1 if part == 1 else 999999) * eyy(y),
        )

    galaxies = set()
    for y in range(h):
        for x in range(w):
            if g[y][x] == "#":
                galaxies.add(new_pos(x, y))

    print(sum((manhattan(a, b) for a, b in combinations(galaxies, 2))))


solve(1)
solve(2)
