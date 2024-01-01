
import string
import regex as re

input = [i.strip() for i in open("input", "r").readlines()]

def digs(s):
    return re.findall(r"\d", s)

def nums(s):
    return re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", s, overlapped=True)

def part1():
    tot = 0
    for line in input:
        l,r = digs(line)[0], digs(line)[-1]
        tot += int(l + r)        
    print(tot)

def part2():
    # gah they can overlap!
    #Like this: oneight
    
    dig = {ch: i for i,ch in enumerate(string.digits)}
    dig.update({"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9})

    tot = 0
    for line in input:
        l,r = dig[nums(line)[0]], dig[nums(line)[-1]]
        tot += int(str(l) + str(r))        
    print(tot)

part1()
part2()
