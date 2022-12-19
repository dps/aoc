from utils import *

input = [i.strip() for i in open("simple.txt","r").readlines()]

blueprints = {}

@cache
def can_build(num, resources):
    costs = blueprints[num]["costs"]
    build = []
    for i,c in enumerate(costs):
        r = resources
        b = (0,0,0,0)

        # todo maybe can build more than one?
        if r[0] >= c[0] and r[1] >= c[1] and r[2] >= c[2]:
            b[i] = 1
            build.append((b,c))

    return build



#resource order: ore, clay, obsidian, geodes
@cache
def maximize(num, robots, resources, mins_remaining):
    if mins_remaining == 0:
        return resources[3]
    could_spend = can_build(num, resources)
    # Also include spending nothing
    could_spend.append(((0,0,0,0), (0,0,0)))
    # Each robot can collect 1 of its resource type per minute.
    # It also takes one minute for the robot factory to construct any type of robot,
    # although it consumes the necessary resources available when construction begins.
    possibilities = []
    for bom in could_spend:
        r = resources
        bots = robots
        for t in [0,1,2]:
            r[t] += robots[t] - bom[1][t]
        for t in [0,1,2, 3]:
            bots[t] += bom[0][t]
        possibilities.append(maximize(num, bots, r, mins_remaining-1))
    return max(possibilities)
    

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


    for k,blueprint in blueprints.items():
        m = maximize(k, (1,0,0,0), (0,0,0,0), 24)

    pass


if __name__ == '__main__':
    part1()
