from utils import *
from string import *
from math import gcd

input = [i.strip() for i in open("input","r").readlines()]



def part2():

    worlds = defaultdict(set)
    needed_worlds = set()
    for y, line in enumerate(input):
        for x, ch in enumerate(line):
            if ch == '#':
                worlds[0].add(x+1j*y)

    def count_in(level, direction):
        nonlocal worlds, needed_worlds
        # Returns count, [new_worlds_needed]
        if level not in worlds:
            needed_worlds.add(level)
            return 0
        else:
            if direction == 1j:
                return sum([1 for x in range(5) if x in worlds[level]])
            if direction == -1j:
                return sum([1 for x in range(5) if x+4j in worlds[level]])
            if direction == 1:
                return sum([1 for y in range(5) if y*1j in worlds[level]])
            if direction == -1:
                return sum([1 for y in range(5) if 4+y*1j in worlds[level]])

    def count_out(level, direction):
        nonlocal worlds, needed_worlds
        if level not in worlds:
            needed_worlds.add(level)
            return 0
        else:
            if direction == 1j:
                return 1 if 2+3j in worlds[level] else 0
            if direction == -1j:
                return 1 if 2+1j in worlds[level] else 0
            if direction == 1:
                return 1 if 3+2j in worlds[level] else 0
            if direction == -1:
                return 1 if 1+2j in worlds[level] else 0

    mi,mx = 0,1
    for _ in range(200):
        newworlds = defaultdict(set)
        needed_worlds = set()
        def iterate(w):
            nonlocal newworlds, needed_worlds
            for x in range(5):
                for y in range(5):
                    if x == 2 and y == 2:
                        continue
                    p=x+1j*y
                    cnt=0
                    for d in CDIR:
                        if (p+d).real < 0 or (p+d).real > 4 or (p+d).imag < 0 or (p+d).imag > 4:
                            cnt += count_out(w-1, d)
                        elif (p+d) != 2+2j:
                            if (p+d) in worlds[w]:
                                cnt+=1
                        else:
                            cnt += count_in(w+1, d)
                    if p in worlds[w]:
                        if cnt == 1:
                            newworlds[w].add(p)
                    else:
                        if cnt == 1 or cnt ==2:
                            newworlds[w].add(p)
        for w in range(mi,mx):
            iterate(w)
        nw = deepcopy(needed_worlds)
        for w in nw:
            iterate(w)
        worlds = newworlds
        mi = min(*worlds.keys())
        mx = max(*worlds.keys())+1
    # for w in sorted(worlds.keys()):
    #     print("World",w)
    #     print_world(worlds[w])
    #     print()
    aoc(sum([len(v) for k,v in worlds.items()]))


            

def part1():
    n = 0
    world = set()
    grid = defaultdict(lambda: defaultdict(str))
    for y, line in enumerate(input):
        for x, ch in enumerate(line):
            grid[y][x] = ch
            if ch == '#':
                world.add(x+1j*y)
    states = set()
    while True:
        n += 1
        newworld = set()
        for x in range(5):
            for y in range(5):
                p = x+1j*y
                cnt = 0
                for d in CDIR:
                    if (p+d) in world:
                        cnt+=1
                if p in world:
                    if cnt == 1:
                        newworld.add(p)
                else:
                    if cnt ==1 or cnt ==2:
                        newworld.add(p)
        if frozenset(newworld) in states:
            exp = 0
            acc = 0
            for y in range(5):
                for x in range(5):
                    p = x+1j*y
                    if p in newworld:
                        acc += 2**exp
                    exp += 1
            aoc(acc)
            return
        states.add(frozenset(newworld))
        world = newworld

part1()
part2()
