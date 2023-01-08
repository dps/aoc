from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]


def part1():
    procedure = []
    for line in input:
        action = line.split(" ")[0]
        ranges = ints(line)
        procedure.append((action, ranges))

    switches = set()
    for action, ranges in procedure:
        print(".")
        for x in range(ranges[0], ranges[1]+1):
            for y in range(ranges[2], ranges[3]+1):
                for z in range(ranges[4], ranges[5]+1):
                    if action == "on":
                        switches.add((x,y,z))
                    if action == "off" and (x,y,z) in switches:
                        switches.remove((x,y,z))

    tot = 0
    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                if (x,y,z) in switches:
                    tot += 1
    print(tot)


part1()
