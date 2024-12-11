
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

@cache
def dfs(stone, depth, limit):
    if depth == limit:
        return 1
    if stone == 0:
        return dfs(1, depth+1, limit)
    ss = str(stone)
    l = len(ss)
    if len(ss) % 2 == 0:
        return dfs(int(ss[:l//2]), depth+1, limit) + dfs(int(ss[l//2:]), depth+1, limit)
    return dfs(stone*2024, depth+1, limit)

p1 = sum(dfs(s, 0, 25) for s in stones)
p2 = sum(dfs(s, 0, 75) for s in stones)

print(p1, p2)