
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def traverse(start, part=1):
    c = start
    i = 0
    steps = 0
    while not (c == "ZZZ" if part == 1 else c.endswith("Z")):
        d = dirs[i]
        i+=1
        i = i % len(dirs)
        if d == 'L':
            c = left[c]
        if d == 'R':
            c = right[c]
        steps += 1
    return steps

dirs = input[0]
D = input[2:]
left, right = {}, {}
starts = []
for line in D:
    origin = line.split(" = ")[0]
    if origin.endswith("A"):
        starts.append(origin)

    left[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[0][1:]
    right[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[1][:-1]

# Part 1
print(traverse("AAA", part=1))

cycles = []
# is it a coprime modulus problem?
for i,start in enumerate(starts):
    c = start
    i = 0
    steps = 0
    while not c.endswith("Z"):
        d = dirs[i]
        i+=1
        i = i % len(dirs)
        if d == 'L':
            c = left[c]
        if d == 'R':
            c = right[c]
        steps += 1
    cycles.append(steps)

# No, it's simpler. The cycle lengths are all zero mod step length 
# len = 263
# cycles = [19199, 11309, 17621, 20777, 16043, 15517]
# mods = [x % 263 for x in cycles]
# print(mods) => all zeros

print(math.lcm(*cycles))
