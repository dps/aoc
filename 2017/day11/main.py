
HEX_DIR = {0: {"n": (0, -1), "s": (0, 1), "ne": (1, -1), "se": (1, 0), "nw": (-1, -1), "sw": (-1, 0)},
           1:{"n": (0, -1), "s": (0, 1), "ne": (1, 0), "se": (1, 1), "nw": (-1, 0), "sw": (-1, 1)}}

D = open("input","r").read().strip().split(",")

p = (0,0)
mmp = 0
for step in D:
    d = HEX_DIR[p[0] % 2][step]
    p = (p[0]+d[0], p[1]+d[1])
    mmp = max(mmp, p[0])

# p[0] is always the min number of steps from origin.
print(p[0], mmp)