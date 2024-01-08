from collections import defaultdict

D = [i.strip() for i in open("input", "r").readlines()]

# This algorithm is by KayZGames, see
# https://www.reddit.com/r/adventofcode/comments/18ge41g/comment/kd0orps/
# rrutkows ported it to python. I still find it hard to believe this is so
# much faster than the DP version as they do ~~ the same thing.
# But it is - nice work folks!
def solutions(row, pattern):
    permutations = defaultdict(int)
    permutations[(0, 0)] = 1 # key is (group_id, group_amount)
    for c in row:
        next = []
        for key, perm_count in permutations.items():
            group_id, group_amount = key
            if c != '#': #'.' or '?'
                if group_amount == 0:
                    next.append((group_id, group_amount, perm_count))
                elif group_amount == pattern[group_id]:
                    next.append((group_id + 1, 0, perm_count))
            if c != '.': #'#' or '?'
                if group_id < len(pattern) and group_amount < pattern[group_id]:
                    next.append((group_id, group_amount + 1, perm_count))
        permutations.clear()
        for group_id, group_amount, perm_count in next:
            permutations[(group_id, group_amount)] += perm_count

    def is_valid(group_id, group_amount):
         return group_id == len(pattern) or group_id == len(pattern) - 1 and group_amount == pattern[group_id]
    return sum(v for k, v in permutations.items() if is_valid(*k))


def part1():
    global D
    tot = 0

    for line in D:
        status = line.split(" ")[0]
        report = tuple(map(int, line.split(" ")[1].split(",")))
        tot += solutions(status, report)
        
    print(tot)

def part2():
    global D
    tot = 0

    for line in D:
        status = line.split(" ")[0]
        report = tuple(map(int, line.split(" ")[1].split(",")))

        status = ("?".join([status] * 5))
        report = tuple(report * 5)

        tot += solutions(status, report)

    print(tot)


part1()
part2()
