
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

bots = defaultdict(list)
outputs = defaultdict(list)
rules = {}

for line in D:
    toks = line.split(" ")
    vals = ints(line)
    if toks[0] == "value":
        bots[vals[1]].append(vals[0])
    elif toks[0] == "bot":
        rules[vals[0]] = ((vals[1],toks[5]),(vals[2],toks[10]))

part1_wants = {61,17}

while True:
    vv = [(b,a) for b,a in bots.items() if len(a) > 1]
    if len(vv) == 0:
        break
    b,vs = vv[0]
    bots[b] = []
    rule = rules[b]
    if vs[0] in part1_wants and vs[1] in part1_wants:
        print("Part 1", b)
    if rule[0][1] == "bot":
        bots[rule[0][0]].append(min(vs))
    else:
        outputs[rule[0][0]].append(min(vs))

    if rule[1][1] == "bot":
        bots[rule[1][0]].append(max(vs))
    else:
        outputs[rule[1][0]].append(max(vs))

print("Part 2", outputs[0][0]*outputs[1][0]*outputs[2][0])