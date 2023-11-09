from utils import *

input = [i.strip() for i in open("input","r").readlines()]

pattern = [0, 1, 0, -1]

@cache
def rpt_gen(r, mx):
    res = []
    i = 0
    first = True
    while mx > 0:
        ch = pattern[i]
        for _ in range(r):
            if not first:
                res.append(ch)
                mx -= 1
            else:
                first = False
        i += 1
        i %= len(pattern)
    return res

def part1():
    val = input[0]
    mm = len(val)
    for c in range(100):
        nv = []
        for i in range(len(val)):
            p = i + 1
            nv.append(str(sum([int(x)*y for x,y in zip(val, rpt_gen(p, mm))]))[-1])
        val = nv

    aoc(val[0:8])

def part2():
    # Our offset is so deep in the digits that only the '1's matter.
    val = [int(i) for i in input[0]*10000]
    vl = len(val)
    digs = int(input[0][0:7])

    for _ in range(100):
        vv = deepcopy(val)
        for p in range(vl-2, digs-1, -1):
            vv[p] = (val[p] + vv[p+1]) % 10
        val = vv

    aoc("".join([str(i) for i in val[digs:digs+8]]))

part1()
part2()


