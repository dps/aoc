from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    res = 0
    for peeps in bundles(input):
        ans = set()
        for person in peeps:
            for ch in person:
                ans.add(ch)
        res += len(ans)
    
    aoc(res)

def part2():
    res = 0
    for peeps in bundles(input):
        ans = Counter()
        for person in peeps:
            ans.update(person)
        for ch in ans.keys():
            if ans[ch] == len(peeps):
                res += 1
    
    aoc(res)

part1()
part2()
