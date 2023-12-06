from utils import *

input = [i.strip() for i in open("input", "r").readlines()]


def solve():
    pt1, pt2 = 1, 0

    times = ints(input[0])
    distances = ints(input[1])
    for time, record in zip(times, distances):
        c = 0
        for i in range(1, time - 1):
            if (time - i) * i > record:
                c += 1
        pt1 *= c

    time = ints(input[0].replace(" ", ""))[0]
    record = ints(input[1].replace(" ", ""))[0]
    for i in range(1, time - 1):
        if (time - i) * i > record:
            pt2 += 1
    print(pt1, pt2)


solve()
