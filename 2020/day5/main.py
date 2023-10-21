from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def seat_id(encoded):
    seat = (0, 127)
    for ch in encoded[0:7]:
        half = (seat[1]-seat[0]) // 2
        if ch == 'F':
            seat = (seat[0], seat[0] + half)
        elif ch == 'B':
            seat = (seat[1] - half, seat[1])
    if seat[0] != seat[1]:
        print("WEIRD")
    chair = (0, 7)
    for ch in encoded[-3:]:
        half = (chair[1]-chair[0]) // 2
        if ch == 'L':
            chair = (chair[0], chair[0] + half)
        elif ch == 'R':
            chair = (chair[1] - half, chair[1])
    return seat[0]*8 + chair[0]

def part1():
    res = 0
    for line in input:
        res = max(res, seat_id(line))
    
    aoc(res)

def part2():
    seen = set()
    for line in input:
        seen.add(seat_id(line))
    all = set(range(0, 127*8))
    rem = all - seen
    for x in rem:
        if x > 0 and x - 1 in rem:
            continue
        if x < 127*8 and x+1 in rem:
            continue
        aoc(x)
        return

part2()
