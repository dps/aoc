
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
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
    
    dig = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9, "zero":0}
    for line in input:
        l = ""
        r = ""
        ls = []
        rs = []
        for i in range(len(line)):
            l += line[i]
            r = line[len(line)-1-i] + r
            if len(nums(l)) > 0:
                ls.append(nums(l)[0])
            if len(nums(r)) > 0:
                rs.append(nums(r)[0])
            if ls and rs:
                break
            
        l = ls[0]
        r = rs[0]
        if l in dig.keys():
            l = dig[l]
        if r in dig.keys():
            r = dig[r]
        tot += int(str(l) + str(r))
        
    aoc(tot)


part1()
part2()
