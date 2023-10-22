from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve(target=2020):
    nums = defaultdict(lambda:[])
    last = None
    for i,x in enumerate(input[0].split(',')):
        nums[int(x)] = [i+1]
        last = int(x)
    t = len(input[0].split(',')) + 1
    while t <= target:
        spoken = None
        if len(nums[last]) == 1:
            spoken = 0
        else:
            spoken = nums[last][0] - nums[last][1]
        if len(nums[spoken]) > 0:
            nums[spoken] = [t, nums[spoken][0]]
        else:
            nums[spoken] = [t]
        t += 1
        last = spoken
    aoc(last)

solve(2020)
solve(30000000)