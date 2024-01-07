from functools import cache
import re

D = [i.strip() for i in open("input", "r").readlines()]

def lmap(func, *iterables):
    return list(map(func, *iterables))

def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!

@cache
def ddfs(pattern, counts):
    # Early termination if we don't have enough chars left
    if sum(counts)+(len(counts)-1) > len(pattern):
        return 0

    # no more patterns to make, rest has to be "." or "?"=>"."
    if len(counts) == 0:
        for p in pattern:
            if p == '#': return 0
        return 1
        # if all([p != "#" for p in pattern]):
        #     return 1
        # else:
        #     return 0

    if pattern[0] == ".":
        return ddfs(pattern[1:], counts)

    tot = 0
    if pattern[0] == "?": # consider the . case
        tot += ddfs(pattern[1:], counts)
    
    # replacing this all is no appreciable speedup
    if all([c != "." for c in pattern[0:counts[0]]]) and ((pattern[counts[0]] != "#") if len(pattern) > counts[0] else True):
        tot += ddfs(pattern[counts[0] + 1:], counts[1:])

    return tot

def part1():
    global D
    tot = 0

    for line in D:
        status = line.split(" ")[0].rstrip(".")
        report = tuple(map(int, line.split(" ")[1].split(",")))
        tot += ddfs(status, report)
        
    print(tot)

def part2():
    global D
    tot = 0

    for line in D:
        status = line.split(" ")[0]
        report = tuple(map(int, line.split(" ")[1].split(",")))

        status = ("?".join([status] * 5)).rstrip(".")
        report = tuple(report * 5)

        tot += ddfs(status, report)

    print(tot)


part1()
part2()
