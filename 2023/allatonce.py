import time

D01 = [i.strip() for i in open("day01/input", "r").readlines()]
D02 = [i.strip() for i in open("day02/input", "r").readlines()]
D03 = [i.strip() for i in open("day03/input", "r").readlines()]
D04 = [i.strip() for i in open("day04/input", "r").readlines()]
D05 = [i.strip() for i in open("day05/input", "r").readlines()]
D06 = [i.strip() for i in open("day06/input", "r").readlines()]
D07 = [i.strip() for i in open("day07/input", "r").readlines()]
D08 = [i.strip() for i in open("day08/input", "r").readlines()]
D09 = [i.strip() for i in open("day09/input", "r").readlines()]
D10 = [i.strip() for i in open("day10/input", "r").readlines()]
D11 = [i.strip() for i in open("day11/input", "r").readlines()]
D12 = [i.strip() for i in open("day12/input", "r").readlines()]
D13 = [i.strip() for i in open("day13/input", "r").readlines()]
D14 = [i.strip() for i in open("day14/input", "r").readlines()]
D15 = [i.strip() for i in open("day15/input", "r").readlines()]
D16 = [i.strip() for i in open("day16/input", "r").readlines()]
D17 = [i.strip() for i in open("day17/input", "r").readlines()]
D18 = [i.strip() for i in open("day18/input", "r").readlines()]
D19 = [i.strip() for i in open("day19/input", "r").readlines()]
D20 = [i.strip() for i in open("day20/input", "r").readlines()]
D21 = [i.strip() for i in open("day21/input", "r").readlines()]
D22 = [i.strip() for i in open("day22/input", "r").readlines()]
D23 = [i.strip() for i in open("day23/input", "r").readlines()]
# day24 is inline below
D25 = [i.strip() for i in open("day25/input", "r").readlines()]

VERBOSE = False

def day01():
    dig = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    p1, p2 = 0, 0
    for line in D01:
        ns1, ns2 = [], []
        for i, ch in enumerate(line):
            if ch.isdigit():
                ns1.append(ch)
                ns2.append(ch)
            for dd, vv in dig.items():
                if line[i:].startswith(dd):
                    ns2.append(vv)
        p1 += int(ns1[0] + ns1[-1])
        p2 += int(ns2[0] + ns2[-1])

    if VERBOSE:
        print("day01", p1, p2)


import re
from functools import reduce
import operator


def day02():
    CAP = {"red": 12, "green": 13, "blue": 14}
    p1, p2 = 0, 0
    for game, line in enumerate(D02, 1):
        if all(
            [
                not any(x > mm for x in map(int, re.findall(f"(\d+) {color}", line)))
                for color, mm in CAP.items()
            ]
        ):
            p1 += game
        p2 += reduce(
            operator.mul,
            [max(map(int, re.findall(f"(\d+) {color}", line))) for color in CAP.keys()],
        )
    if VERBOSE:
        print("day02", p1, p2)


from itertools import product
from collections import defaultdict


def day03():
    g = [[ch for ch in row] for row in D03]
    h = len(g)
    w = len(g[0])

    DIR8 = [(1, -1), (-1, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]
    p1, p2 = 0, 0
    gear_nums = defaultdict(list)
    for y, row in enumerate(g):
        num = 0
        has_part = False
        gears = set()
        for x, ch in enumerate(row + ["."]):
            if ch.isdigit():
                num = 10 * num + int(ch)
                for dx, dy in DIR8:
                    if 0 <= y + dy < h and 0 <= x + dx < w:
                        cc = g[y + dy][x + dx]
                        if not cc.isdigit() and cc != ".":
                            has_part = True
                        if cc == "*":
                            gears.add((x + dx, y + dy))
            elif num != 0:
                if has_part:
                    p1 += num
                for gear in gears:
                    gear_nums[gear].append(num)
                num, has_part, gears = 0, False, set()
    for g, l in gear_nums.items():
        if len(l) == 2:
            p2 += l[0] * l[1]

    if VERBOSE:
        print("day03", p1, p2)


from functools import cache


def day04():
    p1, p2 = 0, 0
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    scores = defaultdict(int)
    for num, line in enumerate(D04, 1):
        want, have = map(
            lambda l: set(map(int, l.strip().split())),
            line.split(":")[1].strip().split("|"),
        )
        scores[num] = len(want & have)
        if len(want & have):
            p1 += pow(2, len(want & have) - 1)

    @cache
    def countup(num):
        return scores[num] + sum(
            (countup(n) for n in range(num + 1, num + scores[num] + 1))
        )

    for num, _ in enumerate(D04, 1):
        p2 += 1 + countup(num)

    if VERBOSE:
        print("day04", p1, p2)


import math


def bundles(inp):
    r = []
    for line in inp:
        if line == "":
            yield r
            r = []
        else:
            r.append(line)
    yield (r)


def lmap(func, *iterables):
    return list(map(func, *iterables))


def day05():
    seeds = D05[0].split(":")[1].strip().split(" ")
    input = D05[2:]
    dirs = defaultdict(str)
    maps = defaultdict(list)
    for bundle in bundles(input):
        bun = list(bundle)
        fro, _, to = bun[0].split()[0].split("-")
        dirs[fro] = to
        for line in bun[1:]:
            d_start, src_start, lenf = map(int, line.split())
            maps[(fro, to)].append((d_start, src_start, lenf))

    r = []
    for s in seeds:
        t, n = "seed", int(s)
        while t != "location":
            fnd = maps[t, dirs[t]]
            for ff in fnd:
                if n >= ff[1] and n < (ff[1] + ff[2]):
                    n = ff[0] + (n - ff[1])
                    break
            t = dirs[t]
        r.append(n)
    p1 = min(r)

    r = []

    def pairs(ll):
        for x in range(0, len(ll), 2):
            yield (ll[x], ll[x + 1])

    for s, rg in pairs(lmap(int, seeds)):
        seed = s
        # We can skip forward each interval where there's nothing changing.
        while seed < s + rg:
            t = "seed"
            n = int(seed)
            canskip = math.inf
            while t != "location":
                fnd = maps[t, dirs[t]]
                for ff in fnd:
                    if n >= ff[1] and n < (ff[1] + ff[2]):
                        n = ff[0] + (n - ff[1])
                        canskip = min(canskip, ff[0] + ff[2] - n)
                        break
                t = dirs[t]
            r.append(n)
            assert canskip != math.inf
            seed += canskip
    if VERBOSE:
        print("day05", p1, min(r))


def quadratic(time, record):
    x1 = (time - math.sqrt(time * time - 4 * record)) / 2
    x0 = (time + math.sqrt(time * time - 4 * record)) / 2
    if int(x1) == x1:
        x1 += 1
    if int(x0) == x0:
        x0 -= 1
    return math.floor(x0) - math.ceil(x1) + 1


def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!


def day06():
    times = ints(D06[0])
    distances = ints(D06[1])

    time = ints(D06[0].replace(" ", ""))[0]
    record = ints(D06[1].replace(" ", ""))[0]
    if VERBOSE:
        print(
            "day06",
            reduce(operator.mul, [quadratic(t, r) for (t, r) in zip(times, distances)]),
            quadratic(time, record),
        )


from collections import Counter


order1 = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
order2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def hand_to_val(hand, part=1):
    d = 0
    for k in hand:
        d += (order1 if part == 1 else order2).index(k)
        d *= 100
    return d


def best_joker(hand):
    typ = Counter(hand)
    if hand == "JJJJJ":
        h2 = "AAAAA"
    else:
        mc = typ.most_common()
        if mc[0][0] == "J":
            mc = mc[1:]

        top = [n for n in mc if n[1] == mc[0][1]]
        tn = sorted([(order2.index(n[0]), n) for n in top])
        r = tn[-1][1][0]
        h2 = hand.replace("J", r)
    return h2


def day07():
    for part in [1,2]:
        hands = []
        for line in D07:
            hand, bid = line.split()
            if part == 1:
                typ = Counter(hand)
            elif part == 2:
                h2 = best_joker(hand)
                typ = Counter(h2)
            nc = Counter(list(typ.values()))
            score = max(typ.values()) * 100 + 10 * (nc[2] if 2 in nc else 0)

            hands.append((score * 10000000000000 + hand_to_val(hand, part), hand, bid))
        hands = sorted(hands)
        ans = sum([int(b[2]) * int(r) for r, b in enumerate(hands, 1)])
        if VERBOSE: print("day07 part", part, ans)

def day08():
    def traverse(start, part=1):
        c = start
        i = 0
        steps = 0
        while not (c == "ZZZ" if part == 1 else c.endswith("Z")):
            d = dirs[i]
            i += 1
            i = i % len(dirs)
            if d == "L":
                c = left[c]
            if d == "R":
                c = right[c]
            steps += 1
        return steps

    dirs = D08[0]
    D = D08[2:]
    left, right = {}, {}
    starts = []
    for line in D:
        origin = line.split(" = ")[0]
        if origin.endswith("A"):
            starts.append(origin)

        left[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[0][1:]
        right[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[1][:-1]

    # Part 1
    # if VERBOSE: print(traverse("AAA", part=1))

    cycles = []
    # is it a coprime modulus problem?
    for i, start in enumerate(starts):
        c = start
        i = 0
        steps = 0
        while not c.endswith("Z"):
            d = dirs[i]
            i += 1
            i = i % len(dirs)
            if d == "L":
                c = left[c]
            if d == "R":
                c = right[c]
            steps += 1
        cycles.append(steps)

    # No, it's simpler. The cycle lengths are all zero mod step length
    # len = 263
    # cycles = [19199, 11309, 17621, 20777, 16043, 15517]
    # mods = [x % 263 for x in cycles]
    # if VERBOSE: print(mods) => all zeros

    if VERBOSE:
        print("day08", traverse("AAA", part=1), math.lcm(*cycles))


from copy import copy


def day09():
    for part in [1,2]:
        tot = 0
        for line in D09:
            seq = ints(line) if part == 1 else list(reversed(ints(line)))
            s = copy(seq)
            diffs, diff = [], [None]
            while not all([d == 0 for d in diff]):
                diff = [b - a for a, b in zip(seq, seq[1:])]
                diffs.append(diff)
                seq = diff

            tot += s[-1] + sum(x[-1] for x in diffs[0:-1])
        if VERBOSE: print("day09", part, tot)
    return tot



from collections import deque


def grid_from_strs(lines, find=None):
    g = [[ch for ch in row] for row in lines]
    h = len(g)
    w = len(g[0])
    found = None
    if find:
        for y in range(h):
            for x in range(w):
                if g[y][x] == find:
                    found = (x, y)
                    return g, w, h, found
    return g, w, h, found


def day10():
    def trace_pipe():
        global D
        start = None
        G, w, h, start = grid_from_strs(D10, find="S")

        NEIGHBORS = {
            "S": [(0, 1)],
            "-": [(1, 0), (-1, 0)],
            "L": [(0, -1), (1, 0)],
            "J": [(-1, 0), (0, -1)],
            "7": [(-1, 0), (0, 1)],
            "F": [(0, 1), (1, 0)],
            "|": [(0, -1), (0, 1)],
        }

        def neighbors(p):
            ch = G[p[1]][p[0]]
            for d in NEIGHBORS[ch]:
                yield (p[0] + d[0], p[1] + d[1])

        bfs, visited = deque([(start, 0)]), {start}

        while bfs:
            pos, depth = bfs.popleft()
            for d in neighbors(pos):
                if d == start and depth > 2:
                    return (
                        G,
                        w,
                        h,
                        visited,
                        (((depth - 1) // 2) + 1 if depth % 2 == 1 else depth // 2),
                    )
                if not d in visited:
                    bfs.append((d, depth + 1))
                    visited.add(d)

    # part1
    g, w, h, on_loop, result = trace_pipe()

    # Remove all the junk from the map
    for x in range(w):
        for y in range(h):
            if (x, y) not in on_loop:
                g[y][x] = "."

    # Even/odd rule, with subpixel on corners. We pass under Js and Ls.
    # We know S is a |.
    tot = 0
    for y, row in enumerate(g):
        for x, ch in enumerate(row):
            if ch == ".":
                xx, c = x - 1, 0  # Even/ odd rule - cast a ray out -x wards
                while xx >= 0:
                    if (
                        g[y][xx] == "|"
                        or g[y][xx] == "F"
                        or g[y][xx] == "7"
                        or g[y][xx] == "S"
                    ):
                        c += 1
                    xx -= 1
                tot += 1 if c % 2 == 1 else 0

    if VERBOSE:
        print("day10", result, tot)


from itertools import combinations


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def day11(part=1):
    global D11

    for part in [1,2]:
        g = [[ch for ch in row] for row in D11]
        h = len(g)
        w = h  # square grid
        expand_rows = [y for y in range(h) if all((c == "." for c in g[y]))]
        expand_cols = [x for x in range(w) if all((g[y][x] == "." for y in range(h)))]

        # can we speed up new_pos? [minor speedup]
        @cache
        def exx(x):
            return len([xx for xx in expand_cols if xx < x])

        @cache
        def eyy(y):
            return len([yy for yy in expand_rows if yy < y])

        def new_pos(x, y):
            return (
                x + (1 if part == 1 else 999999) * exx(x),
                y + (1 if part == 1 else 999999) * eyy(y),
            )

        galaxies = set()
        for y in range(h):
            for x in range(w):
                if g[y][x] == "#":
                    galaxies.add(new_pos(x, y))

        res = sum((manhattan(a, b) for a, b in combinations(galaxies, 2)))
        if VERBOSE: print("day11", part, res)

    return res


def day12():
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
        global D12
        tot = 0

        for line in D12:
            status = line.split(" ")[0]
            report = tuple(map(int, line.split(" ")[1].split(",")))
            tot += solutions(status, report)
            
        return tot

    def part2():
        global D12
        tot = 0

        for line in D12:
            status = line.split(" ")[0]
            report = tuple(map(int, line.split(" ")[1].split(",")))

            status = ("?".join([status] * 5))
            report = tuple(report * 5)

            tot += solutions(status, report)

        return tot

    p1,p2 = part1(), part2()

    if VERBOSE: print("day12", p1, p2)


def day13():
    def reflect(grid, w, h, target_diff=0):
        for col in range(1, w):
            diff = 0
            for i in range(1, w):
                if col - i < 0 or col + (i - 1) > w - 1:
                    break
                for j in range(h):
                    a = grid[j][col - i]
                    b = grid[j][col + (i - 1)]
                    if a != b:
                        diff += 1
            if diff == target_diff:
                return col

        for row in range(1, h):
            diff = 0
            for i in range(1, h):
                if row - i < 0 or row + (i - 1) > h - 1:
                    break
                for j in range(w):
                    a = grid[row - i][j]
                    b = grid[row + (i - 1)][j]
                    if a != b:
                        diff += 1
            if diff == target_diff:
                return 100 * row

    p1, p2 = 0, 0

    for grid in bundles(D13):
        g, w, h, _ = grid_from_strs(grid)
        p1 += reflect(g, w, h, target_diff=0)
        p2 += reflect(g, w, h, target_diff=1)

    if VERBOSE: print("day13", p1, p2)


def day14():
    g = list("".join(D14))
    w = len(D14[0])
    h = len(D14)


    def roll_north(g, w, h):
        new_grid = g[:]
        for j in range(h):
            for i in range(w):
                if g[w * j + i] == "O":
                    jj = j
                    while jj > 0 and not (
                        new_grid[(jj - 1) * w + i] == "O"
                        or new_grid[(jj - 1) * w + i] == "#"
                    ):
                        jj -= 1
                    new_grid[j * w + i] = "."
                    new_grid[jj * w + i] = "O"
        return new_grid


    def roll_west(g, w, h):
        new_grid = g[:]
        for i in range(w):
            for j in range(h):
                if g[w * j + i] == "O":
                    ii = i
                    while ii > 0 and not (
                        new_grid[j * w + (ii - 1)] == "O"
                        or new_grid[j * w + (ii - 1)] == "#"
                    ):
                        ii -= 1
                    new_grid[j * w + i] = "."
                    new_grid[j * w + ii] = "O"
        return new_grid


    def roll_south(g, w, h):
        new_grid = g[:]
        for j in range(h - 1, -1, -1):
            for i in range(w):
                if g[w * j + i] == "O":
                    jj = j
                    while jj < (h - 1) and not (
                        new_grid[(jj + 1) * w + i] == "O"
                        or new_grid[(jj + 1) * w + i] == "#"
                    ):
                        jj += 1
                    new_grid[j * w + i] = "."
                    new_grid[jj * w + i] = "O"
        return new_grid


    def roll_east(g, w, h):
        new_grid = g[:]
        for i in range(w - 1, -1, -1):
            for j in range(h):
                if g[w * j + i] == "O":
                    ii = i
                    while ii < (w - 1) and not (
                        new_grid[j * w + (ii + 1)] == "O"
                        or new_grid[j * w + (ii + 1)] == "#"
                    ):
                        ii += 1
                    new_grid[j * w + i] = "."
                    new_grid[j * w + ii] = "O"
        return new_grid


    def score(g, w, h):
        return sum((h - j) for i in range(w) for j in range(h) if g[j * w + i] == "O")


    p1 = score(roll_north(g, w, h), w, h)

    seen, reverse_seen = {}, {}
    start, mod = None, None

    for i in range(1000000000):
        g = roll_north(g, w, h)
        g = roll_west(g, w, h)
        g = roll_south(g, w, h)
        g = roll_east(g, w, h)

        fs = "".join(g)
        if fs in seen:
            start = seen[fs]
            mod = i - start
            break
        seen[fs] = i
        reverse_seen[i] = g

    g = reverse_seen[start + ((1000000000 - start) % mod) - 1]
    if VERBOSE: print("day14", p1, score(g, w, h))


def words(s):
    return re.findall(r"[a-zA-Z]+", s)


def day15():
    def hashfn(str):
        r = 0
        for ch in str:
            r = ((r + ord(ch)) * 17) % 256
        return r

    p1 = sum(hashfn(v) for v in D15[0].split(","))

    boxes = defaultdict(lambda: {})
    for instr in D15[0].split(","):
        box, label = hashfn(words(instr)[0]), words(instr)[0]
        op = ("remove", None) if instr[-1] == "-" else ("set", int(instr.split("=")[1]))

        if op[0] == "set":
            boxes[box][label] = op[1]
        elif op[0] == "remove":
            try:
                del boxes[box][label]
            except:
                pass

    tot = 0
    for box, ll in boxes.items():
        for slot, label in enumerate(ll, 1):
            tot += (box + 1) * slot * boxes[box][label]
    if VERBOSE:
        print("day15", p1, tot)


# day 16, 17 in own files

RLUD = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


def day18():
    def compute_vertices(part=1):
        p = (0, 0)
        vertices = [p]
        path_len = 0
        for line in D18:
            p1dir, p1num, hex = line.split(" ")
            num = int(p1num) if part == 1 else int(hex[2:7], 16)
            dir = (
                p1dir
                if part == 1
                else {"0": "R", "1": "D", "2": "L", "3": "U"}[hex[7:8]]
            )
            d = RLUD[dir]
            p = (p[0] + num * d[0], p[1] + num * d[1])
            vertices.append(p)
            path_len += num
        return vertices, path_len

    def pairs(ll):
        for x in range(0, len(ll) - 1, 2):
            yield (ll[x], ll[x + 1])

    def shoelace(verts):
        res = 0
        for l, r in pairs(verts):
            res += l[0] * r[1] - l[1] * r[0]
        return res

    vertices, path_len = compute_vertices(part=1)
    p1 = int(shoelace(vertices) + path_len / 2 + 1)
    vertices, path_len = compute_vertices(part=2)
    if VERBOSE:
        print("day18", p1, int(shoelace(vertices) + path_len / 2 + 1))


def bundles(inp):
    r = []
    for line in inp:
        if line == "":
            yield r
            r = []
        else:
            r.append(line)
    yield (r)


def day19():
    tot = 0
    workflows, parts = bundles(D19)

    wf = {}
    for f in workflows:
        name = f.split("{")[0]
        steps = f.split("{")[1].split("}")[0].split(",")
        wf[name] = steps

    # Part 1
    for p in parts:
        xmas = {}
        for l, v in [x.split("=") for x in p[1:-1].split(",")]:
            xmas[l] = int(v)

        done = False
        state = "in"
        while not done:
            flow = wf[state]
            for step in flow:
                if ":" in step:
                    opr = operator.lt if "<" in step else operator.gt
                    ss = "<" if "<" in step else ">"
                    cmp, next = step.split(":")
                    var, val = cmp.split(ss)
                    if opr(xmas[var], int(val)):
                        state = next
                        break
                else:
                    state = step

            if state == "A" or state == "R":
                done = True
            if state == "A":
                tot += sum(xmas.values())

    p1 = tot

    # Part 2

    # xmas
    def pos(ch):
        return "xmas".index(ch)

    R = ((1, 4000), (1, 4000), (1, 4000), (1, 4000))

    def replace_range(pos, new_r, orig):
        return [orig[i] if i != pos else new_r for i in range(4)]

    def dfs(ranges, node):
        if node == "A":
            return reduce(operator.mul, [(j - i) + 1 for i, j in ranges])
        if node == "R":
            return 0
        tot = 0
        rules = wf[node]
        new_ranges = copy(ranges)
        for rule in rules:
            if ":" in rule:
                ss = "<" if "<" in rule else ">"
                cmp, dest = rule.split(":")
                var, val = cmp.split(ss)
                rp = pos(var)
                rr = new_ranges[rp]
                val = int(val)
                if val >= rr[0] and val <= rr[1]:
                    if ss == ">":
                        tot += dfs(
                            replace_range(rp, (val + 1, rr[1]), new_ranges), dest
                        )
                        new_ranges = replace_range(rp, (rr[0], val), new_ranges)
                    if ss == "<":
                        tot += dfs(
                            replace_range(rp, (rr[0], val - 1), new_ranges), dest
                        )
                        new_ranges = replace_range(rp, (val, rr[1]), new_ranges)
            else:
                tot += dfs(new_ranges, rule)
        return tot

    if VERBOSE:
        print("day19", p1, dfs(R, "in"))


import sys


def day20():
    # The graph
    dests, inputs, types = defaultdict(list), defaultdict(list), defaultdict(str)

    # State tracking
    states, inv_states = {}, defaultdict(lambda: defaultdict(bool))

    for line in D20:
        name, ds = line.split(" -> ")
        if name.startswith("%") or name.startswith("&"):
            tmp = name[0]
            name = name[1:]
            types[name] = tmp
        else:
            types[name] = "broadcast"
        states[name] = False
        dests[name] = [d.strip() for d in ds.split(",")]
        for d in dests[name]:
            inputs[d].append(name)
            inv_states[d][name] = False

    Q, lows, highs = deque([]), 0, 0

    def transmit(dests, val, src):
        nonlocal Q, lows, highs
        for dest in dests:
            Q.append((dest, val, src))
            if val:
                highs += 1
            else:
                lows += 1

    critical_inputs = inputs[inputs["rx"][0]]
    loops = {i: [] for i in critical_inputs}
    step = 0
    p1 = 0
    while True:
        transmit(["broadcaster"], False, "button")
        while Q:
            n, signal, from_ = Q.popleft()
            if n in critical_inputs and signal == False:
                loops[n].append(step)
                if all([len(s) > 1 for _, s in loops.items()]):
                    if VERBOSE:
                        print(
                            "day20",
                            p1,
                            reduce(operator.mul, [l[1] - l[0] for l in loops.values()]),
                        )
                    return
            action = types[n]
            if action == "%":
                if not signal:
                    states[n] = not states[n]
                    transmit(dests[n], states[n], n)
            elif action == "&":
                inv_states[n][from_] = signal
                for v in inv_states[n].values():
                    if v != True:
                        transmit(dests[n], True, n)
                        break
                else:
                    transmit(dests[n], False, n)
            else:  # action == "broadcast":
                transmit(dests[n], signal, n)
        if step == 999:
            p1 = lows * highs
        step += 1


DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def grid_from_strs(lines, find=None):
    g = [[ch for ch in row] for row in lines]
    h = len(g)
    w = len(g[0])
    found = None
    if find:
        for y in range(h):
            for x in range(w):
                if g[y][x] == find:
                    found = (x, y)
                    return g, w, h, found
    return g, w, h, found


def day21():
    g, w, h, start = grid_from_strs(D21, find="S")

    goal, s = 26501365, 26501365 % w
    p2stop = (s + 2 * w) + 1  # 328

    def compute_reachable():
        reachable = defaultdict(int)
        Q, visited = deque([(start, 0)]), defaultdict(set)
        visited[0] = set([start])
        while Q:
            p, steps = Q.popleft()
            if steps == p2stop:
                break
            reachable[steps] += 1
            for d in DIR:
                q = (p[0] + d[0], p[1] + d[1])
                if g[(p[1] + d[1]) % h][(p[0] + d[0]) % w] != "#":
                    if not steps + 1 in reachable:
                        reachable[steps + 1] = reachable[steps - 1]
                        visited[steps + 1] = visited[steps - 1]
                    if q not in visited[steps + 1]:
                        Q.append((q, steps + 1))
                        visited[steps + 1].add(q)
        return reachable

    reachable = compute_reachable()
    P = reachable[s], reachable[s + w], reachable[s + 2 * w]

    def quadratic(P, n):
        a = (P[2] - 2 * P[1] + P[0]) / 2
        b = P[1] - P[0] - a
        c = P[0]
        return a * (n * n) + b * n + c

    if VERBOSE:
        print("day21", reachable[64], int(quadratic(P, goal // w)))


from collections import deque

def day16():
    g = [[c for c in row] for row in D16]
    w = len(g[0])
    h = w  # This problem uses a square grid

    def trybeam(ix, iy, idx, idy):
        beams = deque([(ix, iy, idx, idy)])
        exits = set()
        GO = {
            ("\\", 1, 0): (0, 1),
            ("\\", -1, 0): (0, -1),
            ("\\", 0, 1): (1, 0),
            ("\\", 0, -1): (-1, 0),
            ("/", 1, 0): (0, -1),
            ("/", -1, 0): (0, 1),
            ("/", 0, 1): (-1, 0),
            ("/", 0, -1): (1, 0),
        }
        states = set()
        energize = set()
        while beams:
            beam = beams.popleft()
            x, y, dx, dy = beam
            if 0 <= x < w and 0 <= y < h:
                energize.add((x, y))
                if (x, y, dx, dy) in states:
                    continue
                states.add((x, y, dx, dy))
                m = g[y][x]
                if m == ".":
                    # Following all the "." right away is a 2x speedup
                    while (
                        0 <= x + dx < w and 0 <= y + dy < h and g[y + dy][x + dx] == "."
                    ):
                        energize.add((x + dx, y + dy))
                        x, y = x + dx, y + dy
                    beams.append((x + dx, y + dy, dx, dy))
                elif m == "-":
                    if abs(dx) == 1:
                        beams.append((x + dx, y + dy, dx, dy))
                    else:
                        beams.append((x + 1, y, 1, 0))
                        beams.append((x - 1, y, -1, 0))
                elif m == "|":
                    if abs(dy) == 1:
                        beams.append((x + dx, y + dy, dx, dy))
                    else:
                        beams.append((x, y + 1, 0, 1))
                        beams.append((x, y - 1, 0, -1))
                else:
                    dx, dy = GO[(m, dx, dy)]
                    beams.append((x + dx, y + dy, dx, dy))
            else:
                exits.add((x, y))
        return len(energize), exits

    p1 = trybeam(0, 0, 1, 0)[0]

    mm = 0
    exits = set()
    for y in range(h):
        if (-1, y) not in exits:
            mi, exits_ = trybeam(0, y, 1, 0)
            if mi > mm:
                mm = mi
            exits.update(exits_)
        if (w, y) not in exits:
            mi, exits_ = trybeam(w - 1, y, -1, 0)
            if mi > mm:
                mm = mi
            exits.update(exits_)

    for x in range(w):
        if (x, -1) not in exits:
            mi, exits_ = trybeam(x, 0, 0, 1)
            if mi > mm:
                mm = mi
            exits.update(exits_)
        if (x, h) not in exits:
            mi, exits_ = trybeam(x, h - 1, 0, -1)
            if mi > mm:
                mm = mi
            exits.update(exits_)

    if VERBOSE: print("day16", p1, mm)
    return mm

def day16_multi_process(case):
    g = [[c for c in row] for row in D16]
    w = len(g[0])
    h = w  # This problem uses a square grid

    def trybeam(ix, iy, idx, idy):
        beams = deque([(ix, iy, idx, idy)])
        GO = {
            ("\\", 1, 0): (0, 1),
            ("\\", -1, 0): (0, -1),
            ("\\", 0, 1): (1, 0),
            ("\\", 0, -1): (-1, 0),
            ("/", 1, 0): (0, -1),
            ("/", -1, 0): (0, 1),
            ("/", 0, 1): (-1, 0),
            ("/", 0, -1): (1, 0),
        }
        states = set()
        energize = set()
        while beams:
            beam = beams.popleft()
            x, y, dx, dy = beam
            if 0 <= x < w and 0 <= y < h:
                energize.add((x, y))
                if (x, y, dx, dy) in states:
                    continue
                states.add((x, y, dx, dy))
                m = g[y][x]
                if m == ".":
                    # Following all the "." right away is a 2x speedup
                    while (
                        0 <= x + dx < w and 0 <= y + dy < h and g[y + dy][x + dx] == "."
                    ):
                        energize.add((x + dx, y + dy))
                        x, y = x + dx, y + dy
                    beams.append((x + dx, y + dy, dx, dy))
                elif m == "-":
                    if abs(dx) == 1:
                        beams.append((x + dx, y + dy, dx, dy))
                    else:
                        beams.append((x + 1, y, 1, 0))
                        beams.append((x - 1, y, -1, 0))
                elif m == "|":
                    if abs(dy) == 1:
                        beams.append((x + dx, y + dy, dx, dy))
                    else:
                        beams.append((x, y + 1, 0, 1))
                        beams.append((x, y - 1, 0, -1))
                else:
                    dx, dy = GO[(m, dx, dy)]
                    beams.append((x + dx, y + dy, dx, dy))

        return len(energize)

    if case == 0:
        if VERBOSE:
            print("Part 1", trybeam(0, 0, 1, 0))
        return 0

    mm = 0
    if case == 1:
        for y in range(h):
            mm = max(mm, trybeam(0, y, 1, 0))
    if case == 2:
        for y in range(h):
            mm = max(mm, trybeam(w - 1, y, -1, 0))
    if case == 3:
        for x in range(w):
            mm = max(mm, trybeam(x, 0, 0, 1))
    if case == 4:
        for x in range(w):
            mm = max(mm, trybeam(x, h - 1, 0, -1))

    return mm

def day17():
    g = [int(ch) for row in D17 for ch in row]
    h = len(D17)
    w = len(D17[0])
    end = len(g) - 1
    MAX_SIZE = w * h * 9


    def dynamic_dijkstra(minimum, maximum, end):
        seen, mins = set(), [[MAX_SIZE] * (w + 2) for _ in range(w * h)]
        bh = [[] for _ in range(MAX_SIZE)]
        for state in (0, 1), (0, w):
            for c, (yx, d) in neighbors(state, minimum, maximum):
                mins[yx][d] = c
                bh[c].append((yx, d))
        for cost, vs in enumerate(bh):
            for v in vs:
                if v in seen:
                    continue

                if v[0] == end:
                    return cost

                seen.add(v)

                yx, d = v
                next_d = w//d
                next_cost = cost
                for l in range(1, maximum):
                    yx += d
                    if yx < 0 or end < yx or (d == 1 and yx % w == 0) or (d == -1 and yx % w == (w-1)):
                        break

                    next_cost += g[yx]
                    if l >= minimum:
                        m = mins[yx]
                        if next_cost < m[next_d]:
                            m[next_d] = next_cost
                            bh[next_cost].append((yx, next_d))
                        if next_cost < m[-next_d]:
                            m[-next_d] = next_cost
                            bh[next_cost].append((yx, -next_d))


    def neighbors(state, minimum, maximum):
        yx, d = state
        cc = 0
        for l in range(1, maximum):
            yx += d
            if yx < 0 or end < yx or (d == 1 and yx % w == 0) or (d == -1 and yx % w == (w-1)):
                break

            cc += g[yx]
            if l >= minimum:
                yield (cc, (yx, -w//d))
                yield (cc, (yx, w//d))


    p1 = dynamic_dijkstra(1, 4, end)
    p2 = dynamic_dijkstra(4, 11, end)
    if VERBOSE: print("day17", p1, p2)


def day22():
    elevated = []
    for brick, line in enumerate(D22):
        s, e = line.split("~")
        ss, ee = ints(s), ints(e)
        # x,y,z
        # all bricks are only extruded in one dir
        extrude, small, large = None, None, None
        for ext in range(0, 3):
            if ss[ext] != ee[ext]:
                extrude = ext
                small = ss if ss[ext] < ee[ext] else ee
                large = ss if ss[ext] > ee[ext] else ee
        if extrude == None:
            elevated.append([ss])
        else:
            bb = []
            for j in range(small[extrude], large[extrude] + 1):
                bb.append(tuple((small[h] if h != extrude else j for h in range(3))))
            bb = sorted(bb, key=itemgetter(2))
            elevated.append(bb)
    # Sort by z
    elevated = sorted(elevated, key=lambda l: itemgetter(2)(l[0]))

    def drop_bricks(elevated):
        world = {}
        supports = defaultdict(list)
        supported_by = defaultdict(list)
        for i, brick in enumerate(elevated):
            while True:
                b = brick[0]
                zz = b[2]
                lowest = [o for o in brick if o[2] == zz]
                # try dropping by 1
                if any((v[0], v[1], v[2] - 1) in world for v in lowest) or b[2] == 1:
                    bottom_supports = set(
                        [
                            world[(v[0], v[1], v[2] - 1)]
                            for v in lowest
                            if (v[0], v[1], v[2] - 1) in world
                        ]
                    )
                    # settled
                    supported_by[i] = bottom_supports
                    for k in bottom_supports:
                        supports[k].append(i)
                    for cell in brick:
                        world[cell] = i
                    break
                else:
                    brick = tuple((k[0], k[1], k[2] - 1) for k in brick)
        return supported_by, supports

    # Let them all settle once.
    supported_by, supports = drop_bricks(elevated)

    p1, p2 = 0, 0
    for i in range(len(D22)):
        # supported_by[i] => list -- i is supported by that list
        # supports[i] => list -- all the bricks supported by i
        if all([len(supported_by[j]) > 1 for j in supports[i]]):
            p1 += 1
        else:
            Q, moved = deque([i] + supports[i]), set([i])
            while Q:
                b = Q.popleft()
                if len(supported_by[b] - moved) == 0:
                    moved.add(b)
                    Q.extend(supports[b])
            p2 += len(moved) - 1
    if VERBOSE:
        print("day22", p1, p2)



def day23():
    g = [[ch for ch in row] for row in D23]
    h = len(g)
    w = len(g[0])
    start = (1, 0)
    end = (w - 2, h - 1)


    @cache
    def grid_neighbors(p, part1=False):
        nonlocal g, w, h
        width = w
        height = h
        r = []
        dd = None
        if part1:
            if g[p[1]][p[0]] == ">":
                dd = (1, 0)
            elif g[p[1]][p[0]] == "<":
                dd = (-1, 0)
            elif g[p[1]][p[0]] == "^":
                dd = (0, -1)
            elif g[p[1]][p[0]] == "v":
                dd = (0, 1)
        for d in [dd] if dd else [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            q = (p[0] + d[0], p[1] + d[1])
            if (
                q[0] < 0
                or q[1] < 0
                or q[0] >= width
                or q[1] >= height
                or g[q[1]][q[0]] == "#"
            ):
                continue
            r.append(q)
        return r


    def find_all_intersections(part1=False):
        nonlocal w,h
        res = []
        for x in range(w):
            for y in range(h):
                if g[y][x] == "." and len(grid_neighbors((x, y), part1)) > 2:
                    res.append((x, y))
        return res


    def find_edges_from_isect_to_isect(isects, start, end, part1=False):
        graph = {}
        for i in isects:
            o, p = i, i
            dests = []
            for d in grid_neighbors(o, part1):
                vv, l = set(), 1
                p = d
                vv.add(o)
                vv.add(p)
                found = True
                while p not in isects:
                    nxt = [v for v in grid_neighbors(p, part1) if v not in vv]
                    if len(nxt) == 0:
                        found = False
                        break
                    l += 1
                    p = nxt[0]
                    vv.add(p)
                if found:
                    dests.append((p[0], p[1], l))  # graph is origin -> (dest, len)
            graph[(o[0],o[1])] = dests
        # Remap the whole graph to integer node names so we
        # can mark visited really quickly.
        gg = {}
        map_ = {}
        for i,k in enumerate(graph.keys()):
            map_[k] = i
        for k,v in graph.items():
            gg[map_[k]] = [(map_[(x[0],x[1])],x[2]) for x in v]
        return gg,map_[start],map_[end]

    ans = []
    for part1 in [True, False]:
        isect = set(find_all_intersections(part1)) | {start, end}
        graph,start_,end_ = find_edges_from_isect_to_isect(isect, start, end, part1)
        
        mid_points = defaultdict(list)

        MID_DEPTH = int(len(graph.keys()) / 2) - 2
        mm = 0
        visited = 0

        def outbound_dfs(n, l, d):
            nonlocal mm, visited, mid_points
            if visited & 1<<n:
                return
            if not part1 and d == MID_DEPTH:
                mid_points[n].append((l,visited))
                return
            visited |= 1<<n
            if n == end_:
                mm = max(l, mm)
            else:
                for nn, ll in graph[n]:
                    outbound_dfs(nn, l + ll, d+1)
            visited ^= 1<<n


        def return_dfs(n, l, d):
            nonlocal mm, visited, mid_points
            if d == MID_DEPTH:
                return
            if visited & 1<<n:
                return
            visited |= 1<<n
            if n == start_:
                mm = max(l, mm)
            else:
                for nn, ll in graph[n]:
                    if nn in mid_points:
                        for l_, visited_ in mid_points[nn]:
                            if l+ll+l_ < mm:
                                break
                            if (visited_|1<<nn) & visited == 0:
                                mm = max(l+ll+l_, mm)
                    return_dfs(nn, l + ll, d+1)
            visited ^= 1<<n

        sadd, eadd = 0,0
        start_, sadd = graph[start_][0]
        if not part1:
            end_, eadd = graph[end_][0]

        outbound_dfs(start_, sadd, 0)
        if not part1:
            for k in mid_points.keys():
                mid_points[k] = sorted(mid_points[k], reverse=True)
            return_dfs(end_, eadd, 0)
        
        ans.append(mm)
    if VERBOSE: print("day23", ans[0], ans[1])

from operator import itemgetter
import z3

def drun(func):
    START = time.perf_counter()
    func()
    END = time.perf_counter()
    print(f"{func.__name__} {END - START:.4f}s")

def day24():
    stones = lmap(ints, [i.strip() for i in open("day24/input", "r").readlines()])
    tot = 0

    def isect_sympy(s1, s2):
        s1x, s1y, _, s1dx, s1dy, _ = s1
        s2x, s2y, _, s2dx, s2dy, _ = s2

        try:
            n1 = (-s1x * s2dy + s1y * s2dx - s2dx * s2y + s2dy * s2x) / (
                s1dx * s2dy - s1dy * s2dx
            )
            n2 = (s1dx * s1y - s1dx * s2y - s1dy * s1x + s1dy * s2x) / (
                s1dx * s2dy - s1dy * s2dx
            )
            ix = s1x + n1 * s1dx
            iy = s1y + n1 * s1dy
            return ix, iy, n1, n2
        except ZeroDivisionError:
            return None

    for p, q in combinations(stones, 2):
        i = isect_sympy(p, q)
        if (
            i != None
            and 200000000000000 <= i[0] <= 400000000000000
            and 200000000000000 <= i[1] <= 400000000000000
        ):
            n, m = i[2], i[3]
            if n > 0 and m > 0:
                tot += 1

    s = stones
    def gaussian_elimination(A):
        n = len(A)

        # Forward elimination
        for i in range(n):
            # Search for maximum in this column
            maxEl = abs(A[i][i])
            maxRow = i
            for k in range(i+1, n):
                if abs(A[k][i]) > maxEl:
                    maxEl = abs(A[k][i])
                    maxRow = k

            # Swap maximum row with current row
            A[maxRow], A[i] = A[i], A[maxRow]

            # Make all rows below this one 0 in current column
            for k in range(i+1, n):
                c = -A[k][i] / A[i][i]
                for j in range(i, n+1):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]

        # Solve equation Ax=b for an upper triangular matrix A
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = A[i][n] / A[i][i]
            for k in range(i-1, -1, -1):
                A[k][n] -= A[k][i] * x[i]

        return x

    Ab = [[s[0][4] - s[1][4], s[1][3] - s[0][3], s[1][1] - s[0][1], s[0][0] - s[1][0], s[0][4] * s[0][0] - s[0][1] * s[0][3] - s[1][4] * s[1][0] + s[1][1] * s[1][3]],
        [s[1][4] - s[2][4], s[2][3] - s[1][3], s[2][1] - s[1][1], s[1][0] - s[2][0], s[1][4] * s[1][0] - s[1][1] * s[1][3] - s[2][4] * s[2][0] + s[2][1] * s[2][3]],
        [s[2][4] - s[3][4], s[3][3] - s[2][3], s[3][1] - s[2][1], s[2][0] - s[3][0], s[2][4] * s[2][0] - s[2][1] * s[2][3] - s[3][4] * s[3][0] + s[3][1] * s[3][3]],
        [s[3][4] - s[4][4], s[4][3] - s[3][3], s[4][1] - s[3][1], s[3][0] - s[4][0], s[3][4] * s[3][0] - s[3][1] * s[3][3] - s[4][4] * s[4][0] + s[4][1] * s[4][3]]]

    # Solve using Gaussian Elimination
    x = [round(i) for i in gaussian_elimination(Ab)]

    sx, sy, dx, _ = x

    # From above.
    t0 = (s[0][0] - sx) / (dx - s[0][3])
    t1 = (s[1][0] - sx) / (dx - s[1][3])

    # This is just the equation for velocity between positions given time
    # elapsed.
    dz = ((s[1][2] + t1*s[1][5]) - (s[0][2] + t0*s[0][5])) / (t1 - t0)

    # sz + t1 dz - s12 - t1 s15 = 0
    # sz = -t1 dz +s12 + t1 s15
    sz = -t1 * dz + s[1][2] + t1*s[1][5]

    if VERBOSE: print("day24", tot, int(sx)+int(sy)+int(sz))


import random


def day25():

    vertices = defaultdict(set)
    for line in D25:
        from_, to_ = line.split(":")
        to_ = to_.strip()
        vertices[from_].update(to_.split(" "))
        for e in to_.split(" "):
            vertices[e].add(from_)

    def kargers(vertices):
        while True:
            # Implementation based on https://en.wikipedia.org/wiki/Karger%27s_algorithm
            # V maps node name to a list of nodes connected via edges (incl. repeats!) and a set
            # of the original nodes which have been merged in to n.
            V = {n: (list(v), set([n])) for n, v in vertices.items()}

            while len(V.keys()) > 2:
                e = random.choice(list(V.keys()))
                f = random.choice(V[e][0])

                u, v = V[e], V[f]

                for edge in v[0]:
                    if edge != e and edge != f:
                        u[0].append(edge)
                        V[edge][0].remove(f)
                        V[edge][0].append(e)
                V[e] = ([d for d in u[0] if d != f], u[1] | v[1])

                del V[f]

            if len(list(V.values())[0][0]) == 3:
                return reduce(operator.mul, [len(v[1]) for v in V.values()])

    res = kargers(vertices)
    if VERBOSE: print("day25", res)


def prime_the_pump(i):
    time.sleep(0.5)


if __name__ == "__main__":
    import concurrent.futures

    running = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(10):
            running.append(executor.submit(prime_the_pump, i))
        concurrent.futures.wait(running, return_when=concurrent.futures.ALL_COMPLETED)
        if VERBOSE:
            print("primed")
        running = []
        START = time.time_ns()
        running.append(executor.submit(drun, day23))
        running.append(executor.submit(drun, day25))
        running.append(executor.submit(drun, day17))
        running.append(executor.submit(drun, day22))
        running.append(executor.submit(drun, day01))
        running.append(executor.submit(drun, day02))
        running.append(executor.submit(drun, day03))
        running.append(executor.submit(drun, day04))
        running.append(executor.submit(drun, day05))
        running.append(executor.submit(drun, day06))
        running.append(executor.submit(drun, day07))
        running.append(executor.submit(drun, day08))
        running.append(executor.submit(drun, day09))
        running.append(executor.submit(drun, day10))
        running.append(executor.submit(drun, day11))
        running.append(executor.submit(drun, day12))
        running.append(executor.submit(drun, day13))
        running.append(executor.submit(drun, day14))
        running.append(executor.submit(drun, day24))
        running.append(executor.submit(drun, day15))
        running.append(executor.submit(drun, day18))
        running.append(executor.submit(drun, day19))
        running.append(executor.submit(drun, day20))
        running.append(executor.submit(drun, day21))
        running.append(executor.submit(drun, day16))

    concurrent.futures.wait(running, return_when=concurrent.futures.ALL_COMPLETED)
    END = time.time_ns()
    print("**** total time (s):", (END - START) / 1e9)
