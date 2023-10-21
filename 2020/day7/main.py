from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

def part1():
    res = 0
    hgraph = defaultdict(lambda :[])
    for line in input:
        host = line.split(' bags contain ')[0]
        contents = line.split(' bags contain ')[1].split(',')
        if 'no other' in line.split(' bags contain ')[1]:
            continue
        else:
            conn = []
            for cont in contents:
                num = ints(cont)[0]
                color = ' '.join(cont.split('bag')[0].strip().split(' ')[1:])
                conn.append((num, color))
                hgraph[color].append(host)

    containers = set()
    tovisit = ['shiny gold']
    while len(tovisit) > 0:
        n = tovisit.pop()
        containers.add(n)
        tovisit.extend(hgraph[n])

    aoc(len(containers) - 1)

graph = {}

@cache
def dfs(bag):
    if bag not in graph.keys():
        return 1
    else:
        tot = 1
        for num, color in graph[bag]:
            tot += num * dfs(color)
        return tot

def part2():
    res = 0
    for line in input:
        host = line.split(' bags contain ')[0]
        contents = line.split(' bags contain ')[1].split(',')
        if 'no other' in line.split(' bags contain ')[1]:
            continue
        else:
            conn = []
            for cont in contents:
                num = ints(cont)[0]
                color = ' '.join(cont.split('bag')[0].strip().split(' ')[1:])
                conn.append((num, color))
            graph[host] = conn

    tot = dfs('shiny gold') - 1

    aoc(tot)

part1()
part2()
