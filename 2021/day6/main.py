from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    score = 0
    fish = lmap(int, input[0].split(","))
    for day in range(80):
        to_add = []
        for i,f in enumerate(fish):
            if f == 0:
                fish[i] = 7
                to_add.append(8)
            fish[i] -= 1
        fish.extend(to_add)
    print(len(fish))

def part2(days):
    score = 0
    fish = lmap(int, input[0].split(","))
    timer = defaultdict(int)
    for f in fish:
        timer[f] += 1
    for day in range(days):
        new_timer = defaultdict(int)
        for k,v in timer.items():
            if k == 0:
                new_timer[8] = v
                new_timer[6] += v
            else:
                new_timer[k-1] += v
        timer = new_timer
    print(sum([v for k,v in timer.items()]))

#part1()
part2(80)
part2(256)
