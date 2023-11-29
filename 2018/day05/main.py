
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def react(inp):
    chain = list(inp)

    newchain = []

    while len(newchain) != len(chain):
        if newchain != []:
            chain = newchain
            newchain = []
        skip = 0
        for l,r in zip(chain, chain[1:]):
            if skip > 0:
                skip -= 1
                continue
            if l != r and l.lower() == r.lower():
                skip += 1
            else:
                newchain.append(l)
        if not skip:
            newchain.append(chain[-1])

    return len(chain)

def part1():
    aoc(react(input[0]))

def part2():
    cc = Counter(input[0].lower())
    aoc(min([react(deepcopy(input[0]).replace(k, "").replace(k.upper(), "")) for k in cc.keys()]))

    

part1()
part2()
