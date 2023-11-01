from utils import *

min = 402328
max = 864247

def check(num):
    s = str(num)
    prev = '0'
    repeat = False
    for ch in s:
        if ch < prev:
            return False
        if ch == prev:
            repeat = True
        prev = ch
    return repeat 

def check2(num):
    s = str(num)
    prev = '0'
    conseq = []
    c = 0
    for ch in s:
        if ch < prev:
            return False
        if ch == prev:
            c += 1
        else:
            conseq.append(c)
            c = 1
        prev = ch
    conseq.append(c)
    return 2 in conseq 

def solve():
    aoc(sum([1 for i in range(min, max) if check(i)]))
    aoc(sum([1 for i in range(min, max) if check2(i)]))

solve()

