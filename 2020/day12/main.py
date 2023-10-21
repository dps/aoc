from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    p = 0
    d = 1.0
    for line in input:
        ch = line[0]
        val = int(line[1:])
        if ch == 'F':
            p = p + d * val
        if ch == 'N':
            p = p + 1j * val
        if ch == 'S':
            p = p - 1j * val
        if ch == 'W':
            p = p - val
        if ch == 'E':
            p = p + val
        if ch == 'R':
            if val == 90:
                d = d * -1j
            if val == 180:
                d = -d
            if val == 270:
                d = d * 1j
        if ch == 'L':
            if val == 90:
                d = d * 1j
            if val == 180:
                d = -d
            if val == 270:
                d = d * -1j
    aoc(int(abs(p.real) + abs(p.imag)))

def part2():
    p = 0
    d = 10+1j
    for line in input:
        ch = line[0]
        val = int(line[1:])
        if ch == 'F':
            p = p + d * val
        if ch == 'N':
            d = d + 1j * val
        if ch == 'S':
            d = d - 1j * val
        if ch == 'W':
            d = d - val
        if ch == 'E':
            d = d + val
        if ch == 'R':
            if val == 90:
                d = d * -1j
            if val == 180:
                d = -d
            if val == 270:
                d = d * 1j
        if ch == 'L':
            if val == 90:
                d = d * 1j
            if val == 180:
                d = -d
            if val == 270:
                d = d * -1j
    aoc(int(abs(p.real) + abs(p.imag)))

part2()
