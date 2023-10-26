from utils import *
import operator

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve(part=1):
    i = bundles(input)
    rules, messages = next(i), next(i)

    rs = {}
    for rule in rules:
        rs[rule.split(":")[0].strip()] = rule.split(":")[1].strip()

    def construct(r):
        if r[0] == '"':
            return r[1]
        if "|" in r:
            parts = r.split(" | ")
            return "((" + construct(parts[0]) + ")|(" + construct(parts[1]) + "))"
        cons = ""
        for tok in r.split(" "):
            if part == 2 and tok == "8":
                cons += construct(rs[tok]) + "+"
            elif part == 2 and tok == "11":
                l = construct(rs["42"])
                r = construct(rs["31"])
                # 4 levels deep is all that was required to fully match my input.
                cons += "((" + l + r + ")|(" + 2*l + 2*r + ")|(" + 3*l + 3*r + ")|(" + 4*l + 4*r + "))"
            else:
                cons += construct(rs[tok])
        return cons
    
    regex = construct(rs["0"])
    aoc(sum([1 for m in messages if re.fullmatch(regex, m) != None]))

solve(1)
solve(2)