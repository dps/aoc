from utils import *
import operator

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve():
    i = bundles(input)
    rules, messages = next(i), next(i)

    rs = {}
    for rule in rules:
        rs[rule.split(":")[0].strip()] = rule.split(":")[1].strip()

    def construct(r):
        if r[0] == '"':
            return r[1]
        if "|" in r:
            parts = r.split("|")
            return "((" + construct(parts[0].strip()) + ")|(" + construct(parts[1].strip()) + "))"
        cons = ""
        for tok in r.split(" "):
            cons += construct(rs[tok.strip()])
        return cons
    
    regex = construct(rs["0"])
    aoc(sum([1 if re.fullmatch(regex, m) != None else 0 for m in messages]))

solve()
