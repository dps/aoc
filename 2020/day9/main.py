from utils import *

input = [int(i.strip()) for i in open("input.txt","r").readlines()]

def part1(window=25):
    trailing = []
    for line in input:
        if len(trailing) < window:
            trailing.append(line)
            continue
        good = False
        for (a,b) in combinations(trailing, 2):
            if a + b == line:
                good = True
                break
        if not good:
            aoc(line)
            return
        trailing = trailing[1:]
        trailing.append(int(line))

def part2(target=393911906):

    for start in range(len(input) - 1):
        t = input[start]
        for end in range(start+1, len(input)):
            t += input[end]
            if t > target:
                break
            if t == target:
                print(t,target,start,end)
                print(input[start:end])
                aoc(min(input[start:end])+max(input[start:end]))
                return
    pass

#part1()
part2()
