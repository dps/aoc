import re
from copy import copy

def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!

D = [i.strip() for i in open("input","r").readlines()]

def solve(part=1):
    tot = 0
    for line in D:
        seq = ints(line) if part == 1 else list(reversed(ints(line)))
        s = copy(seq)
        diffs, diff = [], [None]
        while not all([d == 0 for d in diff]):
            diff = [b-a for a,b in zip(seq, seq[1:])]
            diffs.append(diff)
            seq = diff
        
        tot += s[-1] + sum(x[-1] for x in diffs[0:-1])

    print(tot)

solve(1)
solve(2)
