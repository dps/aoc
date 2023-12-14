
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def roll_north(g,w,h):
    new_grid = deepcopy(g)
    for j in range(h):
        for i in range(w):
            if g[j][i] == "O":
                jj = j
                while jj >0 and not (new_grid[jj-1][i] == 'O' or new_grid[jj-1][i] == '#'):
                    jj -= 1
                new_grid[j][i] = "."
                new_grid[jj][i] = "O"
    return new_grid

def rotate_clock(g):
    return [list(x) for x in list(zip(*g[::-1]))]

def score(g,w,h):
    return sum((h-j) for i in range(w) for j in range(h) if g[j][i] == "O")

g,w,h,_ = grid_from_strs(D)
print("Part 1:", score(roll_north(g, w, h),w,h))

seen, reverse_seen = {}, {}
start, mod = None, None

for i in range(1000000000):
    for _ in range(4):
        g = roll_north(g,w,h)
        g = rotate_clock(g)
    
    fs = "".join(["".join(x) for x in g])
    if fs in seen:
        print("loop> ", seen[fs], i - seen[fs])
        start = seen[fs]
        mod = i - start
        break
    seen[fs] = i
    reverse_seen[i] = g

    # test is loop at 2 == 9, so every 7  2 + [((1000000000-2)%7)]
    # input is loop at 175 == 184
    # after 175 we loop every nine
    # we need the value at 175 + [(1000000000-175) % 9] - 1

g = reverse_seen[start + ((1000000000 - start) % mod) - 1]
print("Part 2:", score(g, w, h))