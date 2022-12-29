from utils import *
from math import ceil
input = [i.strip() for i in open("input.txt","r").readlines()]

recipes = []
for i, line in enumerate(input):
    costs = ints(line)
    bots = [(costs[1],0,0,0), (costs[2],0,0,0), (costs[3], costs[4],0,0), (costs[5], 0, costs[6],0)]
    max_ore, max_clay, max_obsidian = max([c[0] for c in bots]), max([c[1] for c in bots]), max([c[2] for c in bots])
    recipes.append((bots, (max_ore, max_clay, max_obsidian, math.inf)))

def max_geodes_from_new_bots(mins):
    return triangle(mins - 1)

global_best = 0
@cache
def dfs(n, robots, resources, mins_remaining):
    global global_best
    if mins_remaining == 1:  # This case => 45x speedup!
        return resources[3] + robots[3]
    if mins_remaining <= 0:
        return resources[3]

    if (resources[3] + robots[3] * mins_remaining + max_geodes_from_new_bots(mins_remaining)) <= global_best:
        return 0
    
    bots, maxes = recipes[n]
    best = resources[3] + mins_remaining * robots[3]
    for b, bot in enumerate(bots):
        if (resources[b]//mins_remaining) + robots[b] >= maxes[b]:
            continue
        wait_mins = 1 + max([(ceil((r-resources[i])/robots[i]) if robots[i] > 0 else math.inf)
                             if r > 0 else 0 for i,r in enumerate(bot)])
        if wait_mins < mins_remaining:
            new_robots = tuple(robots[i] + (1 if b==i else 0) for i in range(4))
            new_resources = tuple(min(resources[i] + robots[i]*wait_mins - bot[i], maxes[i]*mins_remaining) for i in range(4))
            best = max(best, dfs(n, new_robots, new_resources, mins_remaining - wait_mins))

    if global_best < best:
        global_best = best
    return best

### Speedups
# Rewrote to branch on next robot choice instead of mins_remaining (6x speedup)
# Wrote a case for mins_remaining = 1 (45x speedup)
# If this branch can do no better than the global max already seen, return early (6x speedup)
# (orig) if robots[b] > maxes[b], don't build excess production capacity (14x speedup)
# (slightly better) if (resources[b]//mins_remaining) + robots[b] >= maxes[b] (30% speedup)
# - if the resources we have in hand plus the robots we have allow us to buld any robot in any remaining min,
#   don't build more of that robot type.
# min(resources[i] + robots[i]*wait_mins - bot[i], maxes[i]*mins_remaining)
# - If we have resources we can never use, throw them away, reduces the search space. (minor speedup)

def part1():
    global global_best
    acc = 0
    for i in range(len(recipes)):
        global_best = 0
        acc += (i+1) * dfs(i, (1,0,0,0), (0,0,0,0), 24)
    print(acc)
    return acc

def part2():
    global global_best
    acc = 1
    for i in range(3):
        global_best = 0
        acc *= dfs(i, (1,0,0,0), (0,0,0,0), 32)
    print(acc)
    return acc

#~/pypy3.9/bin/python main.py  0.91s user 0.05s system 98% cpu 0.969 total
assert(part1() == 1404)
assert(part2() == 5880)