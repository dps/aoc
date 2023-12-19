
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}
tot = 0
#max_sum = max([sum(map(int, lines)) for lines in bundles(D)])

workflows, parts = bundles(D)

wf = {}
for f in workflows:
    name = f.split("{")[0]
    steps = f.split("{")[1].split("}")[0].split(",")
    wf[name] = steps

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
