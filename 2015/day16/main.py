from utils import *

D = [i.strip() for i in open("input", "r").readlines()]

sues = {}

for line in D:
    num = ints(line)[0]
    ll = line.split(":", maxsplit=1)[1]
    vs = ll.split(", ")
    r = {}
    for p in vs:
        k, v = p.split(": ")
        r[k.strip()] = int(v)
    sues[num] = r

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def solve(part=1):
    for i in range(1, 501):
        cantbe = False
        for k, v in target.items():
            if k in sues[i]:

                if part == 2 and k in ["cats", "trees"]:
                    if sues[i][k] <= v:
                        cantbe = True
                elif part == 2 and k in ["pomeranians", "goldfish"]:
                    if sues[i][k] >= v:
                        cantbe = True
                else:
                    if sues[i][k] != v:
                        cantbe = True
        if not cantbe:
            print(part, " is Sue #", i)

solve(1)
solve(2)