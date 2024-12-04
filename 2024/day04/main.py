
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0

for r in range(len(D)):
    for c in range(len(D[0])):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                m = 4
                for i, ch in enumerate("XMAS"):
                    if (r + dx*i < 0) or (r + dx*i) >= len(D) or (c + dy*i) < 0 or (c + dy*i) >= len(D[0]):
                        continue
                    if D[r+dx*i][c+dy*i] == ch:
                        m -= 1
                if m == 0:
                    p1 += 1

grid = defaultdict(lambda: ".")
for r in range(len(D)):
    for c in range(len(D[0])):
        grid[(r,c)] = D[r][c]

for r in range(len(D)):
    for c in range(len(D[0])):
        if (r,c) in grid and grid[(r,c)] == "A":
            cs = 0
            if grid[(r-1,c-1)] == "M" and grid[(r+1,c+1)] == "S":
                cs += 1
            if grid[(r-1,c-1)] == "S" and grid[(r+1,c+1)] == "M":
                cs += 1
            if grid[(r+1,c-1)] == "M" and grid[(r-1,c+1)] == "S":
                cs += 1
            if grid[(r+1,c-1)] == "S" and grid[(r-1,c+1)] == "M":
                cs += 1
            if cs == 2:
                p2 += 1


print(p1, p2)
