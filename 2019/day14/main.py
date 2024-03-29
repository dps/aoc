from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def probe(probeamt):
    reactions = []
    back_graph = {}
    for line in input:
        reagents, output = line.split(' => ')[0], line.split(' => ')[1]
        rs = []
        for r in reagents.split(","):
            n = int(r.strip().split(' ')[0])
            a = r.strip().split(' ')[1]
            rs.append((n,a))
        n,a = int(output.strip().split(' ')[0]), output.strip().split(' ')[1]
        reactions.append((rs, (n,a)))
        back_graph[a] = (n, rs)

    needed = defaultdict(int)
    needed['FUEL'] = probeamt
    surplus = defaultdict(int)
    while list(needed.keys()) != ['ORE']:
        choose = (set(needed.keys()) - {'ORE'}).pop()
        amt = needed[choose]
        del(needed[choose])

        if surplus[choose] > 0:
            if surplus[choose] >= amt:
                surplus[choose] -= amt
                continue
            else:
                amt -= surplus[choose]
                surplus[choose] = 0

        react_produces, react = back_graph[choose]
        times = 1
        remain = 0
        if times * react_produces < amt:
            times = math.ceil(amt / react_produces)

        remain = (times * react_produces) - amt
        surplus[choose] += remain

        for reagent in react:
            needed[reagent[1]] += times * reagent[0]

    return(needed['ORE'])

def part1():
    aoc(probe(1))

def part2():
    p_i = 0
    i = 1
    needed = 0
    while needed < 1000000000000:
        p_i = i
        i *= 2
        needed = probe(i)

    #binary search between p_i and i
    aoc(bin_search_fn(p_i, i, lambda x:probe(x) - 1000000000000))

part1()
part2()