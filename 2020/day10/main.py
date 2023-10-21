from utils import *

input = [int(i.strip()) for i in open("input.txt","r").readlines()]

def part1():
    adaptors = sorted(input)
    one = 0
    three = 1
    prev = 0
    for a in adaptors:
        if (a - prev) == 1:
            one += 1
        if (a - prev) == 3:
            three += 1
        prev = a
    aoc(one * three)

sorted_adapters = []

@cache
def dfs(starting_joltage, target_joltage, start):
    global sorted_adapters
    tot = 0
    for i in range(start, len(sorted_adapters)):
        adapter = sorted_adapters[i]
        if adapter - starting_joltage <= 3:
            if adapter + 3 >= target_joltage:
                tot = tot + 1
            else:
                tot = tot + dfs(adapter, target_joltage, i+1)
        else:
            break
    return tot

def part2():
    global sorted_adapters
    device = max(input) + 3
    sorted_adapters = sorted(input)
    aoc(dfs(0, device, 0))

part1()
part2()
