from utils import *
import random
from math import ceil

input = [i.strip() for i in open("simple.txt","r").readlines()]

blueprints = {}

def can_build(num, resources):
    costs = blueprints[num]["costs"]
    build = []
    for i,c in enumerate(costs):
        r = resources

        # My reading of the question is that the factory can only build
        # one robot at a time.
        if r[0] >= c[0] and r[1] >= c[1] and r[2] >= c[2]:
            b = (1 if i==0 else 0,
                1 if i==1 else 0,
                1 if i==2 else 0,
                1 if i==3 else 0)
            if (i == 3): # If we can build a geode robot do it right away
                return [(b,c,i)]

            build.append((b,c,i))

    #print("lcb", build)
    return build

@cache
def max_cost(num, resource_num):
    costs = blueprints[num]["costs"]
    m = 0
    for v in costs:
        m = max(m, v[resource_num])
    print("max_cost", num, resource_num, m)
    return m

#resource order: ore, clay, obsidian, geodes
@cache
def maximize(num, robots, resources, mins_remaining):
    #print("maximize", num, robots, resources, mins_remaining)
    if mins_remaining == 0:
        #print("0 mins", resources[3])
        return resources[3]
    could_spend = can_build(num, resources)

    to_prune = []
    might_build_this_round = set()
    if len(could_spend) > 1:
        for option in could_spend:
            if robots[option[2]] >= max_cost(num, option[2]):
                to_prune.append(option)
            elif robots[option[2]] * mins_remaining + resources[option[2]] > mins_remaining * max_cost(num, option[2]):
                to_prune.append(option)
            else:
                might_build_this_round.add(option[2])

    for p in to_prune:
        could_spend.remove(p)

    if len(could_spend) == 0:
        could_spend.append(((0,0,0,0), (0,0,0,0), None))
    elif could_spend[0][2] != 3:
        could_spend.append(((0,0,0,0), (0,0,0,0), None))

    # Each robot can collect 1 of its resource type per minute.
    # It also takes one minute for the robot factory to construct any type of robot,
    # although it consumes the necessary resources available when construction begins.
    best = 0
    for bom in could_spend:
        if bom[2] != None:
            next_resources = (resources[0] + robots[0] - bom[1][0],
                            resources[1] + robots[1] - bom[1][1],
                            resources[2] + robots[2] - bom[1][2],
                            resources[3] + robots[3])
            next_robots = (robots[0] + bom[0][0],
                        robots[1] + bom[0][1],
                        robots[2] + bom[0][2],
                        robots[3] + bom[0][3],
                        )
            best = max(best, maximize(num, next_robots, next_resources, mins_remaining - 1))
        else:
            next_resources = (resources[0] + robots[0] - bom[1][0],
                            resources[1] + robots[1] - bom[1][1],
                            resources[2] + robots[2] - bom[1][2],
                            resources[3] + robots[3])
            next_robots = (robots[0] + bom[0][0],
                        robots[1] + bom[0][1],
                        robots[2] + bom[0][2],
                        robots[3] + bom[0][3],
                        )
            best = max(best, maximize(num, next_robots, next_resources, mins_remaining - 1))

    return best
    

def part1():
    for i, line in enumerate(input):
        blueprint = {}
        #Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.

        num = ints(line.split(":")[0])[0]
        robot_descs = line.split(":")[1].split(".")
        for robot in robot_descs:
            print(robot)
            g = re.match(r"Each (\w+) robot costs ([^.]*)", robot.strip())
            if not g:
                break
            name = g.groups()[0]
            material_string = g.groups()[1]
            materials = {x[1]:x[0] for x in [re.match(r"(\d+) (\w+)", m.strip()).groups() for m in material_string.split("and")]}
            dd = defaultdict(int)
            for k,v in materials.items():
                dd[k] = int(v)
            blueprint[name] = (dd["ore"], dd["clay"], dd["obsidian"])
        blueprint["n"] = int(num)
        blueprint["costs"] = (blueprint["ore"], blueprint["clay"], blueprint["obsidian"], blueprint["geode"])
        blueprints[int(num)] = blueprint
    print(blueprints)


    tot = 0
    for k,blueprint in blueprints.items():
        m = solve(k, (1,0,0,0), (0,0,0,0), 24)
        print("***>", k, m)
        tot += k * m

    print(tot)
    return tot

def part2():
    for i, line in enumerate(input):
        blueprint = {}
        #Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.

        num = ints(line.split(":")[0])[0]
        robot_descs = line.split(":")[1].split(".")
        for robot in robot_descs:
            print(robot)
            g = re.match(r"Each (\w+) robot costs ([^.]*)", robot.strip())
            if not g:
                break
            name = g.groups()[0]
            material_string = g.groups()[1]
            materials = {x[1]:x[0] for x in [re.match(r"(\d+) (\w+)", m.strip()).groups() for m in material_string.split("and")]}
            dd = defaultdict(int)
            for k,v in materials.items():
                dd[k] = int(v)
            blueprint[name] = (dd["ore"], dd["clay"], dd["obsidian"])
        blueprint["n"] = int(num)
        blueprint["costs"] = (blueprint["ore"], blueprint["clay"], blueprint["obsidian"], blueprint["geode"])
        blueprints[int(num)] = blueprint
    print(blueprints)


    tot = 1
    for k,blueprint in blueprints.items():
        m = maximize(k, (1,0,0,0), (0,0,0,0), 32) #24,32
        print("***>", k, m)
        tot *= m
        if (k == 3):
            break

    print(tot)
    return tot

if __name__ == '__main__':
    part1()
