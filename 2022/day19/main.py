from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

blueprints = {}
global_best = 0

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

    return build

@cache
def max_cost(num, resource_num):
    costs = blueprints[num]["costs"]
    m = 0
    for v in costs:
        m = max(m, v[resource_num])
    return m

@cache
def max_geodes_from_new_bots_in_remaining(mins):
    if mins <= 1:
        return 0
    elif mins == 2:
        return 1
    else:
        return triangle(mins - 1)

#resource order: ore, clay, obsidian, geodes
@cache
def maximize(num, robots, resources, mins_remaining):
    global global_best
    if mins_remaining == 0:
        if resources[3] > global_best:
            global_best = resources[3]
        return resources[3]

    if (resources[3] + robots[3] * mins_remaining + max_geodes_from_new_bots_in_remaining(mins_remaining)) < global_best:
        return 0
    could_spend = can_build(num, resources)

    to_prune = []
    if len(could_spend) > 1:
        for option in could_spend:
            if robots[option[2]] * mins_remaining + resources[option[2]] > mins_remaining * max_cost(num, option[2]):
                to_prune.append(option)

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
    

def solve(part=1):
    global global_best
    for i, line in enumerate(input):
        blueprint = {}
        #Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.

        num = ints(line.split(":")[0])[0]
        robot_descs = line.split(":")[1].split(".")
        for robot in robot_descs:
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

    tot = 0 if part == 1 else 1
    for k,blueprint in blueprints.items():
        global_best = 0
        m = maximize(k, (1,0,0,0), (0,0,0,0), 24 if part==1 else 32)
        print("***>", k, m)
        if part == 1:
            tot += k * m
        else:
            tot *= m
        if (part == 2 and k == 3):
            break

    print(tot)
    return tot


if __name__ == '__main__':
    assert(solve(1) == 1404)
    assert(solve(2) == 5880)
