
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def valid(vals):
    for v in permutations(vals):
        if v[0] >= v[1]+v[2]:
            return False
    return True

def gen():
    buff = []
    for line in D:
        buff.append(ints(line))
        if len(buff) == 3:
            for x in zip(*buff):
                yield x
            buff = []

print(sum([1 for line in D if valid(ints(line))]))
print(sum([1 for vals in gen() if valid(vals)]))
