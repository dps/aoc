
from utils import *
D = [i.strip() for i in open("input","r").readlines()]

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
# The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved
# on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied
# by 2024 is engraved on the new stone.

p1, p2 = 0, 0
stones  = ints(D[0])


for limit in [25, 75]:
    counts = defaultdict(int)
    counts.update({s:1 for s in stones})
    for _ in range(limit):
        new_counts = defaultdict(int)
        for k, v in counts.items():
            if k == 0:
                new_counts[1] += v
            elif len(str(k)) % 2 == 0:
                new_counts[int(str(k)[:len(str(k))//2])] += v
                new_counts[int(str(k)[len(str(k))//2:])] += v
            else:
                new_counts[k*2024] += v
        counts = new_counts

    print(sum(counts.values()))