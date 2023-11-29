
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def react(chain):
    chain = list(chain)
    newchain = []
    for ch in chain:
        if newchain and ch == newchain[-1].swapcase():
            newchain.pop()
        else:
            newchain.append(ch)
    return len("".join(newchain))

def part1():
    aoc(react(input[0]))

def part2():
    cc = Counter(input[0].lower())
    aoc(min([react(deepcopy(input[0]).replace(k, "").replace(k.upper(), "")) for k in cc.keys()]))

    

part1()
part2()
