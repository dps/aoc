from utils import *

D = [line.strip() for line in open("input")]
O = D[len(D)-1]
D = D[:-1]

vv = defaultdict(list)
for line in D:
    vals = ints(line)
    for i, v in enumerate(vals):
        vv[i].append(v)

tot = 0
ops = []
for c in O:
    if c != ' ':
        ops.append(c)

for j, op in enumerate(ops):
    if op == '+':
        tot += sum(vv[j])
    elif op == '*':
        tot += reduce(lambda x, y: x * y, vv[j])

print(tot)
