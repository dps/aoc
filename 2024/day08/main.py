
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

ant = defaultdict(list)

R, C = len(D), len(D[0])
p1, p2 = set(), set()
an1x, an1y, an2x, an2y = 0, 0, 0, 0

for y, row in enumerate(D):
    for x, ch in enumerate(row):
        if ch != ".":
            ant[ch].append((x, y))
            p2.add((x, y))

for k, v in ant.items():
    for a,b in combinations(v, 2):
        dx, dy = abs(b[0] - a[0]), abs(b[1] - a[1])
        left, right = (a, b) if a[0] <= b[0] else (b, a)

        harmonic = 0
        dirs = {1, 2}
        while True:
            harmonic += 1

            if left[1] <= right[1]:
                an1x, an1y = left[0] - harmonic * dx, left[1] - harmonic * dy
                an2x, an2y = right[0] + harmonic * dx, right[1] + harmonic * dy
            else:
                an1x, an1y = left[0] - harmonic * dx, left[1] + harmonic * dy
                an2x, an2y = right[0] + harmonic * dx, right[1] - harmonic * dy

            if (1 in dirs) and an1x >= 0 and an1x < C and an1y >= 0 and an1y < R:
                if harmonic == 1:
                    p1.add((an1x, an1y))
                p2.add((an1x, an1y))
            else:
                dirs -= {1}
            
            if (2 in dirs) and an2x >= 0 and an2x < C and an2y >= 0 and an2y < R:
                if harmonic == 1:
                    p1.add((an2x, an2y))
                p2.add((an2x, an2y))
            else:
                dirs -= {2}
            
            if len(dirs) == 0:
                break


print(len(p1), len(p2))
