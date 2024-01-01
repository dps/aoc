from collections import deque

def solve(case):
    D = [i.strip() for i in open("input", "r").readlines()]

    g = [[c for c in row] for row in D]
    w = len(g[0])
    h = w # This problem uses a square grid

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
                    while 0 <= x + dx < w and 0 <= y+dy < h and g[y + dy][x + dx] == ".":
                        energize.add((x+dx,y+dy))
                        x,y = x + dx, y + dy
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

        return len(energize)


    if case == 0:
        print("Part 1", trybeam(0, 0, 1, 0))
        return 0

    mm = 0
    if case == 1:
        for y in range(h):
            mm = max(mm, trybeam(0, y, 1, 0))
    if case == 2:
        for y in range(h):
            mm = max(mm, trybeam(w - 1, y, -1, 0))
    if case == 3:
        for x in range(w):
            mm = max(mm, trybeam(x, 0, 0, 1))
    if case == 4:
        for x in range(w):
            mm = max(mm, trybeam(x, h - 1, 0, -1))

    return mm

if __name__ == "__main__":
    import concurrent.futures
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(solve, list(range(1, 5)))
        solve(0)
        print("Part 2", max(results))