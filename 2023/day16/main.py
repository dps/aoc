from collections import deque


def solve():
    D = [i.strip() for i in open("input", "r").readlines()]

    g = [[c for c in row] for row in D]
    w = len(g[0])
    h = w  # This problem uses a square grid

    def trybeam(ix, iy, idx, idy):
        beams = deque([(ix, iy, idx, idy)])
        exits = set()
        GO = {
            ("\\", 1, 0): (0, 1),
            ("\\", -1, 0): (0, -1),
            ("\\", 0, 1): (1, 0),
            ("\\", 0, -1): (-1, 0),
            ("/", 1, 0): (0, -1),
            ("/", -1, 0): (0, 1),
            ("/", 0, 1): (-1, 0),
            ("/", 0, -1): (1, 0),
        }
        states = set()
        energize = set()
        while beams:
            beam = beams.popleft()
            x, y, dx, dy = beam
            if 0 <= x < w and 0 <= y < h:
                energize.add((x, y))
                if (x, y, dx, dy) in states:
                    continue
                states.add((x, y, dx, dy))
                m = g[y][x]
                if m == ".":
                    # Following all the "." right away is a 2x speedup
                    while (
                        0 <= x + dx < w and 0 <= y + dy < h and g[y + dy][x + dx] == "."
                    ):
                        energize.add((x + dx, y + dy))
                        x, y = x + dx, y + dy
                    beams.append((x + dx, y + dy, dx, dy))
                elif m == "-":
                    if abs(dx) == 1:
                        beams.append((x + dx, y + dy, dx, dy))
                    else:
                        beams.append((x + 1, y, 1, 0))
                        beams.append((x - 1, y, -1, 0))
                elif m == "|":
                    if abs(dy) == 1:
                        beams.append((x + dx, y + dy, dx, dy))
                    else:
                        beams.append((x, y + 1, 0, 1))
                        beams.append((x, y - 1, 0, -1))
                else:
                    dx, dy = GO[(m, dx, dy)]
                    beams.append((x + dx, y + dy, dx, dy))
            else:
                exits.add((x, y))
        return len(energize), exits

    p1 = trybeam(0, 0, 1, 0)[0]

    mm = 0
    exits = set()
    for y in range(h):
        if (-1, y) not in exits:
            mi, exits_ = trybeam(0, y, 1, 0)
            if mi > mm:
                mm = mi
            exits.update(exits_)
        if (w, y) not in exits:
            mi, exits_ = trybeam(w - 1, y, -1, 0)
            if mi > mm:
                mm = mi
            exits.update(exits_)

    for x in range(w):
        if (x, -1) not in exits:
            mi, exits_ = trybeam(x, 0, 0, 1)
            if mi > mm:
                mm = mi
            exits.update(exits_)
        if (x, h) not in exits:
            mi, exits_ = trybeam(x, h - 1, 0, -1)
            if mi > mm:
                mm = mi
            exits.update(exits_)

    print("day16", p1, mm)
    return mm


if __name__ == "__main__":
    import time

    START = time.time_ns()
    solve()
    print(">>>", (time.time_ns() - START) / 1e9, "s")
