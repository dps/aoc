from utils import *

input = [i.strip() for i in open("input", "r").readlines()]


def quadratic(time, record):
    x1 = ((time - math.sqrt(time*time - 4 * record))/2)
    x0 = ((time + math.sqrt(time*time - 4 * record))/2)
    if int(x1) == x1:
        x1 += 1
    if int(x0) == x0:
        x0 -= 1
    return math.floor(x0) - math.ceil(x1) + 1

def solve():
    pt1, pt2 = 1, 0

    times = ints(input[0])
    distances = ints(input[1])
    # for time, record in zip(times, distances):
    #     c = 0
    #     for i in range(1, time - 1):
    #         if (time - i) * i > record:
    #             c += 1
    #     pt1 *= c

    time = ints(input[0].replace(" ", ""))[0]
    record = ints(input[1].replace(" ", ""))[0]
    # for i in range(1, time - 1):
    #     if (time - i) * i > record:
    #         pt2 += 1
    # print("Brute force", pt1, pt2)

    #print("Quadratic method:")
    print("pt1:", reduce(operator.mul, [quadratic(t,r) for (t,r) in zip(times, distances)]))
    print("pt2:", quadratic(time, record))



solve()
