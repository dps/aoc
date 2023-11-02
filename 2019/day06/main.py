from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    orbs = {}
    leaves = set()
    for line in input:
        c,o = line.split(")")[0],line.split(")")[1]
        orbs[o] = c
        leaves.add(o)
    tot = 0
    for l in leaves:
       chain = l
       while orbs[chain] != 'COM':
          tot += 1
          chain = orbs[chain]
       tot += 1
    aoc(tot)

def part2():
    orbs = {}
    for line in input:
        c,o = line.split(")")
        orbs[o] = c

    chain = "SAN"
    d = -1
    while orbs[chain] != 'COM':
        tmp = orbs[chain]
        orbs[chain] = d
        chain = tmp
        d += 1

    chain = "YOU"
    d = -1
    while type(orbs[chain]) != int:
        chain = orbs[chain]
        d += 1
    aoc(d + orbs[chain])

part1()
part2()