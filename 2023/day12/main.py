from utils import *

D = [i.strip() for i in open("input", "r").readlines()]

@cache
def ddfs(pattern, counts):
    # Early termination if we don't have enough chars left
    if sum(counts)+(len(counts)-1) > len(pattern):
        return 0

    # no more patterns to make, rest has to be "."
    if len(counts) == 0:
        if all([p=="?" or p=="." for p in pattern]):
            return 1
        else:
            return 0

    if pattern[0] == ".":
        return ddfs(pattern[1:], counts)

    tot = 0
    if pattern[0] == "?": # consider the . case
        tot += ddfs(pattern[1:], counts)
    
    # make a whole group here if we can
    if all([c=="#" or c=="?" for c in pattern[0:counts[0]]]) and ((pattern[counts[0]] != "#") if len(pattern) > counts[0] else True):
        tot += ddfs(pattern[counts[0] + 1:], counts[1:])

    return tot

def part1():
    global D
    tot = 0

    for line in D:
        status = line.split(" ")[0].rstrip(".")
        report = tuple(ints(line.split(" ")[1]))
        tot += ddfs(status, report)
    aoc(tot)

def part2():
    global D
    tot = 0

    for k, line in enumerate(D):
        status = line.split(" ")[0]
        report = ints(line.split(" ")[1])

        status = "?".join([status] * 5)
        report = tuple(report * 5)

        tot += ddfs(status, report)

    aoc(tot)


part1()
part2()
