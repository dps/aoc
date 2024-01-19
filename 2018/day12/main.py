
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

init = D[0].split(" ")[2]
D = D[2:]

rules = {}
for line in D:
    rule_, result_ = line.split(" => ")
    rule = int("".join(["1" if i == "#" else "0" for i in rule_]), 2)
    result = True if result_ == "#" else False
    rules[rule] = result

world = defaultdict(bool)
for i in range(len(init)):
    world[i] = True if init[i] == "#" else False

prev_pattern = None
pattern = None
for j in range(1,200):
    l = min(world.keys())
    r = max(world.keys())
    new_world = defaultdict(bool)
    for p in range(l-5,r+6):
        rule = 0
        for i in range(p-2,p+3):
            rule = (rule << 1) + world[i]
        val = rules[rule] if rule in rules else False
        if val:
            new_world[p] = True
    world = new_world
    if j == 20:
        print("Part 1",sum(i for i in world if world[i]))

    l = min(world.keys())
    r = max(world.keys())

    pattern = "".join("#" if world[i] else "." for i in range(l,r+1))
    if pattern == prev_pattern:
        break
    prev_pattern = pattern

sub = j - min(world.keys())
j = 50000000000
print("Part 2", sum(i + j-sub for i,ch in enumerate(pattern) if ch == "#"))