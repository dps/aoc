D = [i.strip() for i in open("input", "r").readlines()]

g = list("".join(D))
w = len(D[0])
h = len(D)


def roll_north(g, w, h):
    new_grid = g[:]
    for j in range(h):
        for i in range(w):
            if g[w * j + i] == "O":
                jj = j
                while jj > 0 and not (
                    new_grid[(jj - 1) * w + i] == "O"
                    or new_grid[(jj - 1) * w + i] == "#"
                ):
                    jj -= 1
                new_grid[j * w + i] = "."
                new_grid[jj * w + i] = "O"
    return new_grid


def roll_west(g, w, h):
    new_grid = g[:]
    for i in range(w):
        for j in range(h):
            if g[w * j + i] == "O":
                ii = i
                while ii > 0 and not (
                    new_grid[j * w + (ii - 1)] == "O"
                    or new_grid[j * w + (ii - 1)] == "#"
                ):
                    ii -= 1
                new_grid[j * w + i] = "."
                new_grid[j * w + ii] = "O"
    return new_grid


def roll_south(g, w, h):
    new_grid = g[:]
    for j in range(h - 1, -1, -1):
        for i in range(w):
            if g[w * j + i] == "O":
                jj = j
                while jj < (h - 1) and not (
                    new_grid[(jj + 1) * w + i] == "O"
                    or new_grid[(jj + 1) * w + i] == "#"
                ):
                    jj += 1
                new_grid[j * w + i] = "."
                new_grid[jj * w + i] = "O"
    return new_grid


def roll_east(g, w, h):
    new_grid = g[:]
    for i in range(w - 1, -1, -1):
        for j in range(h):
            if g[w * j + i] == "O":
                ii = i
                while ii < (w - 1) and not (
                    new_grid[j * w + (ii + 1)] == "O"
                    or new_grid[j * w + (ii + 1)] == "#"
                ):
                    ii += 1
                new_grid[j * w + i] = "."
                new_grid[j * w + ii] = "O"
    return new_grid


def score(g, w, h):
    return sum((h - j) for i in range(w) for j in range(h) if g[j * w + i] == "O")


p1 = score(roll_north(g, w, h), w, h)

seen, reverse_seen = {}, {}
start, mod = None, None

for i in range(1000000000):
    g = roll_north(g, w, h)
    g = roll_west(g, w, h)
    g = roll_south(g, w, h)
    g = roll_east(g, w, h)

    fs = "".join(g)
    if fs in seen:
        start = seen[fs]
        mod = i - start
        break
    seen[fs] = i
    reverse_seen[i] = g

g = reverse_seen[start + ((1000000000 - start) % mod) - 1]
print("day14", p1, score(g, w, h))
