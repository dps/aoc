
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
input = [i.strip() for i in open("input","r").readlines()]

# [1518-10-12 23:58] Guard #421 begins shift
# [1518-08-05 00:24] falls asleep

def solve():

    dates = [(l.split("]")[0][1:].replace('-','').replace(' ','').replace(':',''), l) for l in input]
    ss = [r for _,r in sorted(dates)]

    guards = defaultdict(lambda : defaultdict(int))
    guard = None
    minute = 0
    awake = True
    for line in ss:
        lmin = int(line.split("]")[0].split(":")[1])

        if 'begins shift' in line:
            if awake == False:
                for m in range(minute, 60):
                    guards[guard][m] += 1

            guard = int(line.split("#")[1].split(" ")[0])
            awake = True
            minute = 0
        if 'falls asleep' in line:
            minute = lmin
            awake = False
        if 'wakes' in line:
            for m in range(minute, lmin):
                guards[guard][m] += 1
            minute = lmin
            awake = True

    mmax,amax = 0,0
    mg,ag = None, None
    for guard in guards.keys():
        asleep = sum([v for v in guards[guard].values()])
        sleepy_minute = max([v for v in guards[guard].values()])
        if sleepy_minute > mmax:
            mmax = sleepy_minute
            mg = guard
        if asleep > amax:
            amax = asleep
            ag = guard
    # Part 1
    aoc(ag * sorted([(v,k) for k,v in guards[ag].items()])[-1][1])
    # Part 2
    aoc(mg * sorted([(v,k) for k,v in guards[mg].items()])[-1][1])

solve()
