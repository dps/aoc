
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.

def hashfn(str):
    r = 0
    for ch in str:
        o = ord(ch)
        r += o
        r *= 17
        r %= 256
    return r


def part1():
    global D
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    vals = D[0].split(",")
    for v in vals:
        tot += hashfn(v)
        
    aoc(tot)

part1()
#part2()
