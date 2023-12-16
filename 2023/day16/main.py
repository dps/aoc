from utils import *

D = [i.strip() for i in open("input", "r").readlines()]
tot = 0

g, w, h, _ = grid_from_strs(D)


def trybeam(ix, iy, idx, idy):
    beams = deque([(ix, iy, idx, idy)])
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
    while len(beams):
        beam = beams.popleft()
        x, y, dx, dy = beam
        if 0 <= x < w and 0 <= y < h:
            energize.add((x, y))
            if (x, y, dx, dy) in states:
                continue
            states.add((x, y, dx, dy))
            m = g[y][x]
            if m == ".":
                beams.append((x + dx, y + dy, dx, dy))
            elif m == "|":
                if abs(dy) == 1 and abs(dx) == 0:
                    beams.append((x + dx, y + dy, dx, dy))
                else:
                    beams.append((x, y + 1, 0, 1))
                    beams.append((x, y - 1, 0, -1))
            elif m == "-":
                if abs(dx) == 1 and abs(dy) == 0:
                    beams.append((x + dx, y + dy, dx, dy))
                else:
                    beams.append((x + 1, y, 1, 0))
                    beams.append((x - 1, y, -1, 0))
            else:
                dx, dy = GO[(m, dx, dy)]
                beams.append((x + dx, y + dy, dx, dy))

    return len(energize)


print("Part 1", trybeam(0, 0, 1, 0))

mm = 0
for y in range(h):
    mm = max(mm, trybeam(0, y, 1, 0))
    mm = max(mm, trybeam(w - 1, y, -1, 0))
for x in range(w):
    mm = max(mm, trybeam(x, 0, 0, 1))
    mm = max(mm, trybeam(x, h - 1, 0, -1))

print("Part 2", mm)
