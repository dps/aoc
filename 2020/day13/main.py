from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    earliest = int(input[0])
    times = positive_ints(input[1])
    i = 0
    while True:
        for bus in times:
            if (earliest + i) % bus == 0:
                aoc(i * bus)
                return
        i += 1

def extended_euclidean(a, b):
    """
    Returns a pair of numbers (x, y) such that a * x + b * y = gcd(a, b)
    """
    if b == 0:
        return (1, 0)
    else:
        (x, y) = extended_euclidean(b, a % b)
        return (y, x - (a // b) * y)

def chinese_remainder_theorem(nr):
    """
    Solve the system of linear congruences:
    x ≡ rems[0] (mod nums[0])
    x ≡ rems[1] (mod nums[1])
    ...
    x ≡ rems[k] (mod nums[k])

    Where nums are pairwise coprime.
    """
    # Calculate the product of all nums
    N = 1
    for n,_ in nr:
        N *= n

    result = 0
    for n, r in nr:
        m = N // n
        inv_m, _ = extended_euclidean(m, n)
        result += r * inv_m * m

    return result % N

def part2():
    remainders = []
    times = input[1].split(',')
    for j, bus in enumerate(times):
        if bus != 'x':
            remainders.append((int(bus),int(bus) - j))
    aoc(chinese_remainder_theorem(remainders))
    
part1()
part2()