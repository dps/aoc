
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

tot = 0
#max_sum = max([sum(map(int, lines)) for lines in bundles(D)])

workflows, parts = bundles(D)


wf={}
for f in workflows:
    name = f.split("{")[0]
    steps = f.split("{")[1].split("}")[0].split(",")
    wf[name] = steps

# xmas
def pos(ch):
    return "xmas".index(ch)
R = ((1,4000),(1,4000),(1,4000),(1,4000))

def replace_range(pos, new_r, orig):
    return [orig[i] if i != pos else new_r for i in range(4)]

# jxc{m>787:hk,a>3653:sk,a<3299:A,R}

def dfs(ranges, node):
    print("dfs", node, ranges)
    if node == "A":
        return reduce(operator.mul, [(j-i)+1 for i,j in ranges])
    if node == "R":
        return 0
    tot = 0
    rules = wf[node]
    new_ranges = deepcopy(ranges)
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
                    tot += dfs(replace_range(rp, (val+1,rr[1]), new_ranges), dest)
                    new_ranges = replace_range(rp, (rr[0],val), new_ranges)
                if ss == "<":
                    tot += dfs(replace_range(rp, (rr[0],val-1), new_ranges), dest)
                    new_ranges = replace_range(rp, (val,rr[1]), new_ranges)
        else:
            tot += dfs(new_ranges, rule)
    return tot

print(dfs(R,"in"))

                    





sys.exit(0)

for p in parts:
    print(p)
    xmas = {}
    for l,v in [x.split("=") for x in p[1:-1].split(",")]:
        xmas[l] = int(v)
    
    done = False
    state = "in"
    states = set()
    while not done:
        if state in states:
            print("loop", state)
            continue
        states.add(state)
        flow = wf[state]
        for step in flow:
            if ":" in step:
                opr = operator.lt if "<" in step else operator.gt #check
                ss = "<" if "<" in step else ">"
                print(opr, step.split(":")[0].split(ss)[0], xmas[step.split(":")[0].split(ss)[0]], int(step.split(":")[0].split(ss)[1]))
                if opr(xmas[step.split(":")[0].split(ss)[0]], int(step.split(":")[0].split(ss)[1])):
                    print("true")
                    state = step.split(":")[1]
                    if state == "A" or state == "R":
                        done = True
                    if state == "A":
                        tot += sum(xmas.values())
                    print("moving to", state)
                    break
                else:
                    print("false")
            else:
                print("else moving to", step)
                state = step
                if state == "A" or state == "R":
                    done = True
                if state == "A":
                    tot += sum(xmas.values())
            


    
aoc(tot)
