from utils import *

D = [i.strip() for i in open("input", "r").readlines()]


@cache
def dfs(so_far, group_c, pattern, counts):
    def proceed(ch):
        if ch == ".":
            if group_c > 0 and group_c < counts[0]:  # this is now impossible
                return 0
            if group_c > 0 and group_c == counts[0]:  # found a possibility
                return dfs(so_far + ".", 0, pattern[1:], counts[1:])
            if group_c == 0:  # We weren't in a group, continue
                return dfs(so_far + ".", 0, pattern[1:], counts)
        if ch == "#":
            if group_c + 1 <= counts[0]:  # group is possible
                return dfs(so_far + "#", group_c + 1, pattern[1:], counts)
            else:
                return 0

    if len(counts) == 0 and not len(pattern) == 0:
        if all([p != "#" for p in pattern]):
            return 1
        else:
            return 0

    if len(pattern) == 0:
        if len(counts) == 0:
            return 1
        if len(counts) == 1 and group_c == counts[0]:
            return 1
        return 0

    ch = pattern[0]
    if ch == "?":
        return proceed(".") + proceed("#")
    else:
        return proceed(ch)


@cache
def ddfs(pattern, counts):
    if len(counts) == 0:
        if all([p=="?" or p=="." for p in pattern]):
            return 1
        else:
            return 0
    if sum(counts) > len(pattern):
        return 0

    if pattern[0] == ".":
        return ddfs(pattern[1:], counts)

    tot = 0
    if pattern[0] == "?": # do the . case
        tot += ddfs(pattern[1:], counts)
    
    if all([c=="#" or c=="?" for c in pattern[0:counts[0]]]) and ((pattern[counts[0]] != "#") if len(pattern) > counts[0] else True):
        tot += ddfs(pattern[counts[0] + 1:], counts[1:])

    return tot

@cache
def dfs(pi, ci, group_c, pattern, counts):
    def proceed(ch):
        if ch == ".":
            if group_c > 0 and group_c < counts[ci]:  # this is now impossible
                return 0
            if group_c > 0 and group_c == counts[ci]:  # found a possibility
                return dfs(pi+1, ci+1, 0, pattern, counts)
            if group_c == 0:  # We weren't in a group, continue
                return dfs(pi+1,ci+1, 0, pattern, counts)
        if ch == "#":
            if group_c + 1 <= counts[ci]:  # group is possible
                return dfs(pi+1, ci, group_c + 1, pattern, counts)
            else:
                return 0
        return 0

    if ci == len(counts)-1 and not pi == len(pattern)-1:
        if all([p != "#" for p in pattern[pi:]]):
            return 1
        else:
            return 0

    if pi == len(pattern)-1:
        if ci == len(counts):
            return 1
        if ci == len(counts)-1 and group_c == counts[ci]:
            return 1
        return 0

    ch = pattern[pi]
    if ch == "?":
        return proceed(".") + proceed("#")
    else:
        return proceed(ch)

def part1():
    global D
    tot = 0

    for line in D:
        status = line.split(" ")[0].rstrip(".")
        report = tuple(ints(line.split(" ")[1]))
        tot += ddfs(status, report)
        #dfs.cache_clear()
    aoc(tot)


pattern = None
counts = None


@cache
def dfs2(pattern_idx, counts_idx, group_c):
    global pattern, counts
    if pattern_idx == len(pattern):
        if counts_idx == len(counts) and group_c == 0:
            return 1
        elif counts_idx == len(counts) - 1 and counts[counts_idx] == group_c:
            return 1
        else:
            return 0
    result = 0
    for c in [".", "#"]:
        if pattern[pattern_idx] == c or pattern[pattern_idx] == "?":
            if c == "." and group_c == 0:
                result += dfs2(pattern_idx + 1, counts_idx, 0)
            elif (
                c == "."
                and group_c > 0
                and counts_idx < len(counts)
                and counts[counts_idx] == group_c
            ):
                result += dfs2(pattern_idx + 1, counts_idx + 1, 0)
            elif c == "#":
                result += dfs2(pattern_idx + 1, counts_idx, group_c + 1)
    return result

status, report = None, None


def part2():
    global D, results, status, report
    tot = 0

    for k, line in enumerate(D):
        status = line.split(" ")[0]
        report = ints(line.split(" ")[1])

        status = "?".join([status] * 5)
        report = tuple(report * 5)

        tot += ddfs(status, report)
        #dfs2.cache_clear()

    aoc(tot)


part1()
part2()
