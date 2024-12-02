
from utils import *

D = [l.strip() for l in open("input").readlines()]

p1,p2 = 0,0

def should_count(ii):
    dir = None
    skip = False
    for p,n in zip(ii, ii[1:]):
        if dir == None:
            dir = sign(n - p)
        else:
            if sign(n - p) != dir:
                return False
        
        if abs(n - p) > 3 or n == p:
            return False
    return True

for line in D:
    ii = ints(line)
    if should_count(ii):
        p1 += 1
    test = combinations(ii, len(ii)-1)
    for t in test:
        if should_count(t):
            p2 += 1
            break


print(p1, p2)
