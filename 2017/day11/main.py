
HEX_DIR_EVEN_X = {"n": (0, -1), "s": (0, 1), "ne": (1, -1), "se": (1, 0), "nw": (-1, -1), "sw": (-1, 0)}
HEX_DIR_ODD_X = {"n": (0, -1), "s": (0, 1), "ne": (1, 0), "se": (1, 1), "nw": (-1, 0), "sw": (-1, 1)}

def hex_dir(p, dir):
    x, _ = p[0], p[1]
    if x % 2 == 0:
        return HEX_DIR_EVEN_X[dir]
    else:
        return HEX_DIR_ODD_X[dir]

D = open("input","r").read().strip().split(",")

p = (0,0)
mmp = 0
for step in D:
    d = hex_dir(p, step)
    p = (p[0]+d[0],p[1]+d[1])
    mmp = max(mmp, p[0])

# p[0] is always the min number of steps from origin.
print(p[0], mmp)