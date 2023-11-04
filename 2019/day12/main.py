from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def part1():
    moons = []
    for line in input:
        #<x=12, y=0, z=-15>
        p = ints(line)
        moons.append([p[0],p[1],p[2],0,0,0])

    for i in range(1000):
        for pairs in combinations(range(len(moons)), 2):
            l,r = pairs[0], pairs[1]
            for a in [0,1,2]:
                if moons[l][a] > moons[r][a]:
                    moons[l][a+3] -= 1
                    moons[r][a+3] += 1
                if moons[l][a] < moons[r][a]:
                    moons[l][a+3] += 1
                    moons[r][a+3] -= 1

        for m in range(len(moons)):
            moons[m][0],moons[m][1],moons[m][2] = moons[m][0] + moons[m][3], moons[m][1] + moons[m][4], moons[m][2] + moons[m][5]

    tot_energy = 0
    for m in moons:
        pe = abs(m[0]) + abs(m[1]) + abs(m[2])
        ke = abs(m[3]) + abs(m[4]) + abs(m[5])
        tot_energy += pe * ke


    aoc(tot_energy)

def part2():
    moons = []
    for line in input:
        #<x=12, y=0, z=-15>
        p = ints(line)
        moons.append([p[0],p[1],p[2],0,0,0])

    repeats = []
    for axis in [0,1,2]:
        states = set()
        i = 0
        while True:
            state = tuple([(m[axis],m[axis+3]) for m in moons])
            if state in states:
                repeats.append(i)
                break
            states.add(state)
            i += 1
            for pairs in combinations(range(len(moons)), 2):
                l,r = pairs[0], pairs[1]
                a = axis
                if moons[l][a] > moons[r][a]:
                    moons[l][a+3] -= 1
                    moons[r][a+3] += 1
                if moons[l][a] < moons[r][a]:
                    moons[l][a+3] += 1
                    moons[r][a+3] -= 1

            for m in range(len(moons)):
                moons[m][0],moons[m][1],moons[m][2] = moons[m][0] + moons[m][3], moons[m][1] + moons[m][4], moons[m][2] + moons[m][5]
    
    aoc(math.lcm(*repeats))

part1()
part2()