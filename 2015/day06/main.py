
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def solve(part=1):
    lights = defaultdict(int)

    for line in D:
        r = ints(line)
        ops = line.split()

        for x in range(r[0], r[2]+1):
            for y in range(r[1], r[3]+1):
                if ops[0] == "turn":
                    if ops[1] == "on":
                        lights[(x,y)] = 1 if part == 1 else lights[x,y] + 1
                    else:
                        lights[(x,y)] = 0 if part == 1 else lights[x,y] - 1
                        if lights[(x,y)] < 0:
                            lights[(x,y)] = 0
                else:
                    if part == 1:
                        lights[(x,y)] = 0 if lights[(x,y)] == 1 else 1
                    else:
                        lights[(x,y)] += 2
    return sum(lights.values())

print(solve(1), solve(2))                    