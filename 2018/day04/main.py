
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
input = [i.strip() for i in open("input","r").readlines()]

# [1518-10-12 23:58] Guard #421 begins shift
# [1518-08-05 00:24] falls asleep

def solve():

    ss = sorted(input)
    guards = defaultdict(lambda : defaultdict(int))
    for line in ss:
        lmin = int(line.split("]")[0].split(":")[1])

        if 'begins shift' in line:
            guard = int(line.split("#")[1].split(" ")[0])
        if 'falls asleep' in line:
            minute = lmin
        if 'wakes' in line:
            for m in range(minute, lmin):
                guards[guard][m] += 1
            minute = lmin

    mmax,amax = 0,0
    mg,ag = None, None
    for guard in guards.keys():
        asleep = sum([v for v in guards[guard].values()])
        sleepy_minute = max([v for v in guards[guard].values()])
        if sleepy_minute > mmax:
            mmax, mg = sleepy_minute, guard
        if asleep > amax:
            amax,ag = asleep, guard

    # Part 1
    aoc(ag * sorted([(v,k) for k,v in guards[ag].items()])[-1][1])
    # Part 2
    aoc(mg * sorted([(v,k) for k,v in guards[mg].items()])[-1][1])

solve()
