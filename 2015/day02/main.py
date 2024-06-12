
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def sa(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l

p1, p2 = 0, 0

for line in D:
    sides = ints(line)
    sides = sorted(sides)
    p1 += sa(*sides) + sides[0]*sides[1]
    p2 += reduce(operator.mul, sides) + 2*sides[0] + 2*sides[1]

print(p1, p2)