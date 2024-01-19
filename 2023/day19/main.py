import operator
from copy import copy
from functools import reduce

def bundles(inp):
    """
    Generator to turn input array from file with multi-line sequences divided by
    blank lines into something you can loop over.
    e.g.
    ```
    input = [i.strip() for i in open("input.txt","r").readlines()]

    max([sum(map(int, line)) for line in bundles(inp)])
    ```
    """
    r = []
    for line in inp:
        if line == "":
            yield r
            r = []
        else:
            r.append(line)
    yield (r)

D = [i.strip() for i in open("input", "r").readlines()]
tot = 0
workflows, parts = bundles(D)

wf = {}
for f in workflows:
    name = f.split("{")[0]
    steps = f.split("{")[1].split("}")[0].split(",")
    wf[name] = steps

# Part 1
for p in parts:
    xmas = {}
    for l, v in [x.split("=") for x in p[1:-1].split(",")]:
        xmas[l] = int(v)

    done = False
    state = "in"
    while not done:
        flow = wf[state]
        for step in flow:
            if ":" in step:
                opr = operator.lt if "<" in step else operator.gt
                ss = "<" if "<" in step else ">"
                cmp, next = step.split(":")
                var, val = cmp.split(ss)
                if opr(xmas[var], int(val)):
                    state = next
                    break
            else:
                state = step

        if state == "A" or state == "R":
            done = True
        if state == "A":
            tot += sum(xmas.values())

print("Part 1", tot)

# Part 2

# xmas
def pos(ch):
    return "xmas".index(ch)


R = ((1, 4000), (1, 4000), (1, 4000), (1, 4000))


def replace_range(pos, new_r, orig):
    return [orig[i] if i != pos else new_r for i in range(4)]


def dfs(ranges, node):
    if node == "A":
        return reduce(operator.mul, [(j - i) + 1 for i, j in ranges])
    if node == "R":
        return 0
    tot = 0
    rules = wf[node]
    new_ranges = copy(ranges)
    for rule in rules:
        if ":" in rule:
            ss = "<" if "<" in rule else ">"
            cmp, dest = rule.split(":")
            var, val = cmp.split(ss)
            rp = pos(var)
            rr = new_ranges[rp]
            val = int(val)
            if val >= rr[0] and val <= rr[1]:
                if ss == ">":
                    tot += dfs(replace_range(rp, (val + 1, rr[1]), new_ranges), dest)
                    new_ranges = replace_range(rp, (rr[0], val), new_ranges)
                if ss == "<":
                    tot += dfs(replace_range(rp, (rr[0], val - 1), new_ranges), dest)
                    new_ranges = replace_range(rp, (val, rr[1]), new_ranges)
        else:
            tot += dfs(new_ranges, rule)
    return tot


print("Part 2", dfs(R, "in"))
