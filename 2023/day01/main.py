
from utils import *
import string

input = [i.strip() for i in open("input","r").readlines()]

def digs(s):
    return re.findall(r"\d", s)

def nums(s):
    return re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", s)

def part1():
    tot = 0
    for line in input:
        l,r = digs(line)[0], digs(line)[-1]
        tot += int(l + r)        
    aoc(tot)

def part2():
    tot = 0    
    # gah they can overlap!
    #Like this: oneight
    
    dig = {ch: i for i,ch in enumerate(string.digits)}
    dig.update({"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9, "zero":0})

    for line in input:
        for i in range(len(line)):
            if nums(line[0:i]):
                l = dig[nums(line[0:i])[0]]
                break
        for i in range(len(line)-1, -1, -1):
            if nums(line[i:]):
                r = dig[nums(line[i:])[0]]
                break        
        tot += int(str(l) + str(r))
        
    aoc(tot)


part1()
part2()
