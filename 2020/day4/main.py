from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    res = 0
    passp = set()
    for line in input:
        if line == '':
            print(passp)
            passp -= {'cid'}
            if passp == {'hcl', 'hgt', 'ecl', 'eyr', 'byr', 'pid', 'iyr'}:
                res += 1
            passp = set()
            continue
        for field in line.split(' '):
            passp.add(field.split(':')[0])
    passp -= {'cid'}
    if passp == {'hcl', 'hgt', 'ecl', 'eyr', 'byr', 'pid', 'iyr'}:
        res += 1
    aoc(res)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def valid(k,v):
    if k == 'byr':
        return re.match('\d{4}', v) != None and 1920 <= int(v) <= 2002
    if k == 'iyr':
        return re.match('\d{4}', v) != None and 2010 <= int(v) <= 2020
    if k == 'eyr':
        return re.match('\d{4}', v) != None and 2020 <= int(v) <= 2030
    if k == 'hgt':
        return (re.match('\d+(cm|in)', v) != None) and (150 <= int(v[:-2]) <= 193 if v[-2:] == 'cm' else 59 <= int(v[:-2]) <= 76)
    if k == 'hcl':
        return re.match('#[0-9a-f]{6}$', v) != None
    if k == 'ecl':
        return v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    if k == 'pid':
        return re.match('\d{9}$', v) != None
    if k == 'cid':
        return True
    print("WEIRD!!!!")
    return False

def part2():
    res = 0
    passp = set()
    for line in input:
        if line == '':
            passp -= {'cid'}
            if passp == {'hcl', 'hgt', 'ecl', 'eyr', 'byr', 'pid', 'iyr'}:
                res += 1
            passp = set()
            continue
        for field in line.split(' '):
            if valid(field.split(":")[0], field.split(":")[1]):
                #print(field)
                passp.add(field.split(':')[0])
            else:
                pass
    passp -= {'cid'}
    if passp == {'hcl', 'hgt', 'ecl', 'eyr', 'byr', 'pid', 'iyr'}:
        res += 1
    aoc(res)

part2()
