from collections import deque
from functools import reduce
from itertools import islice

D = list(map(int, open("input", "r").read().split(",")))
C = list(map(lambda ch: ord(ch), open("input", "r").read().strip()))
trailer = [17, 31, 73, 47, 23]


def hash(lens, p=0, ss=0, vals=deque(range(256))):
    for l in lens:
        vals.rotate(-p)
        left, right = deque(islice(vals, l)), deque(islice(vals, l, len(vals)))
        left.reverse()
        vals = left
        vals.extend(right)
        vals.rotate(p)
        p += l + ss
        ss += 1
    return vals, p, ss


def part2():
    C.extend(trailer)

    vals, p, ss = deque(range(256)), 0, 0
    for _ in range(64):
        vals, p, ss = hash(C, p, ss, vals)
    vl = list(vals)

    return "".join(
        [
            f"{reduce(lambda x,y: x^y, vl[s:s+16]):0{2}x}"
            for s in range(0, 256, 16)
        ]
    )


def part1():
    vals, _, _ = hash(D)
    return vals[0] * vals[1]


print(part1())
print(part2())
