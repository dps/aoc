from utils import *

D = [line.strip() for line in open("input")]

ranges, ingredients = list(bundles(D))

R = []

for r in ranges:
    a, b = r.split('-')
    a = int(a)
    b = int(b)
    R.append((a, b))

def isfresh(n):
    for a, b in R:
        if n >= a and n <= b:
            return True
    return False

def part1():
    tot = 0
    for n in ingredients:
        if isfresh(int(n)):
            tot += 1
    return tot

print(part1())

def part2():
    intersected = {R[0][0]: R[0]}
    for range in R[1:]:
        matching = set([range])
        for k, other_range in intersected.items():
            if ((range[1] >= other_range[0] and range[1] <= other_range[1]) or 
                (range[0] >= other_range[0] and range[0] <= other_range[1])):
                matching.add(other_range)
        left = min(map(lambda x: x[0], matching))
        right = max(map(lambda x: x[1], matching))
        for k in matching-{range}:
            del intersected[k[0]]
        intersected[left] = (left, right)
    return sum(map(lambda x: x[1] - x[0] + 1, intersected.values()))

print(part2())
