
from utils import *

p1,p2 = 0, 0
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
scores = defaultdict(int)
for num, line in enumerate(data(), 1):
    want, have = map(lambda l: set(map(int, l.strip().split())),
                     line.split(":")[1].strip().split("|"))
    scores[num] = len(want & have)
    if len(want & have):
        p1 += pow(2, len(want & have) - 1)

@cache
def countup(num):
    return scores[num] + sum((countup(n) for n in range(num + 1, num + scores[num] + 1)))

for num, _ in enumerate(data(), 1):
    p2 += 1 + countup(num)

print("part1", p1, "; part2", p2)
