
from utils import *

D = [ints(l) for l in open("input").readlines()]

def should_count(ii):
    dir = None
    for p,n in zip(ii, ii[1:]):
        if dir == None:
            dir = sign(n - p)
        elif sign(n - p) != dir:
            return False
        if abs(n - p) > 3 or n == p:
            return False
    return True

p1 = sum([should_count(line) for line in D])
p2 = sum([any(should_count(t) for t in combinations(line, len(line) - 1)) for line in D])

print(p1, p2)
