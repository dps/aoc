
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("test","r").readlines()]

results = set()
rr = set()
debug = False
def dfs(so_far, group_c, pattern, counts):
    global rr, debug
    debug = False
    if so_far == ".###.##..#.":
        debug = True
    if debug:
        print("***", so_far, group_c, pattern, counts)

    def proceed(ch):
        if debug:
            print("proceed", ch)
        if ch == ".":
            if group_c > 0 and group_c < counts[0]: # this is now impossible
                print("impossible 1")
                return 0
            if group_c > 0 and group_c == counts[0]: # found a possibility
                if debug: print("%", so_far + ".", 0, pattern[1:], counts[1:])
                return dfs(so_far + ".", 0, pattern[1:], counts[1:])
            if group_c == 0: # We weren't in a group, continue
                return dfs(so_far + ".", 0, pattern[1:], counts)
        if ch == "#":
            if group_c + 1 <= counts[0]: # group is possible
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
            print("FOUND0", so_far)
            rr.add(so_far)
            return 1
        if len(counts) == 1 and group_c == counts[0]:
            print("FOUND", so_far)
            rr.add(so_far)
            return 1
        return 0

    ch = pattern[0]
    if debug: print("%%", ch)
    if ch == "?":
        return proceed(".") + proceed("#")
    else:
        return proceed(ch)
    # if ch == ".":
    #     if group_c < counts[0]: # this is now impossible
    #         return 0
    #     if group_c > 0 and group_c == counts[0]: # found a possibility
    #         return dfs(so_far + ".", 0, pattern[1:], counts[1:])
    #     if group_c == 0: # We weren't in a group, continue
    #         return dfs(so_far + ".", 0, pattern[1:], counts)
    # if ch == "#":
    #     if group_c + 1 <= counts[0]: # ggroup is possible
    #         return dfs(so_far + "#", group_c + 1, pattern[1:], counts)
    #     else:
    #         return 0


# def dfs(consumed, group_c, status, to_make):
#     global results
#     #print("dfs", consumed, group_c, status, to_make)
#     if len(to_make)
#     if len(status) == 0 and (len(to_make) == 0 or group_c == to_make[0]):
#         results.add(consumed)
#         return
#     if len(status) == 0:
#         return
#     else:
#         if status[0] == ".":
#             if group_c > 0:
#                 print(consumed, status)
#                 if to_make[0] != group_c:
#                     return
#                 to_make = to_make[1:]
#             dfs(consumed + ".", 0, status[1:], to_make)
#         elif status[0] == "#":
#             dfs(consumed + "#", group_c + 1, status[1:], to_make)
#         elif status[0] == "?":
#             # Try both ways
#             if len(to_make)> 0 and group_c < to_make[0]:
#                 dfs(consumed + "#", group_c + 1, status[1:], to_make)
#             dfs(consumed + ".", 0, status[1:], to_make)


def perms(p, s):
    global results
    if len(s) == 0:
        results.add(p)
        return
    if s[0] != "?":
        perms(p+s[0], s[1:])
    else:
        perms(p+"#", s[1:])
        perms(p+".", s[1:])

def calc_report(s):
    gs = s.split(".")
    r = []
    for g in gs:
        c = Counter(g)["#"]
        if c > 0:
            r.append(c)
    return r

def part1():
    global D, results
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    for line in D:
        status = line.split(" ")[0].rstrip(".")
        report = ints(line.split(" ")[1])
        tot += dfs("", 0, status, report)
        # results = set()
        # perms("", status)
        # gg = set()
        # for a in results:
        #     if calc_report(a) == report:
        #         gg.add(a)
        #         tot += 1
        # print(gg.difference(rr))
    aoc(tot)

part1()
#part2()
