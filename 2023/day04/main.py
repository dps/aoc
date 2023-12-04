
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def solve():
    p1 = 0
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    cards = defaultdict(int)
    for num, line in enumerate(input, 1):
        line = line.split(":")[1].strip()
        want = set(map(int, line.split("|")[0].strip().split()))
        have = set(map(int, line.split("|")[1].strip().split()))
        cards[num] = len(want & have)
        if len(want & have) > 0:
            p1 += pow(2, len(want & have) - 1)

    print("part1", p1)
    
    @cache
    def countup(num):
        tt = cards[num]
        return tt + sum((countup(n) for n in range(num + 1, num + tt + 1)))

    tot = 0    
    for num, line in enumerate(input, 1):
        tot += 1 + countup(num)

    print("part2", tot)

solve()
