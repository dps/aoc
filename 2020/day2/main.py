from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    valid = 0
    for line in input:
        nums, letter, password = line.split(" ")
        letter = letter[0]
        ns = positive_ints(nums)
        c = Counter(password)
        lcount = c[letter]
        if lcount >= ns[0] and lcount <= ns[1]:
            valid += 1

    aoc(valid)

def part2():
    valid = 0
    for line in input:
        nums, letter, password = line.split(" ")
        letter = letter[0]
        ns = positive_ints(nums)
        lcount = 0
        if password[ns[0] - 1] == letter:
            lcount += 1
        if password[ns[1] - 1] == letter:
            lcount += 1

        if lcount == 1:
            valid = valid + 1

    aoc(valid)

part1()
part2()
