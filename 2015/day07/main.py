
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def solve(b_override=None):
    vals = defaultdict(int)

    def getop(op):
        if op == "AND":
            return lambda x,y: x & y
        if op == "OR":
            return lambda x,y: x | y
        if op == "LSHIFT":
            return lambda x,y: x << y
        if op == "RSHIFT":
            return lambda x,y: x >> y    

    def getval(name_or_num):
        nonlocal vals
        if name_or_num.isdigit():
            return int(name_or_num)
        if name_or_num in vals:
            return vals[name_or_num]
        return None
    
    while True:
        if "a" in vals:
            return vals["a"]

        for line in D:
            toks = line.split()
            if len(toks) == 3:
                y = getval(toks[0])
                if y != None:
                    vals[toks[2]] = y

            # # x LSHIFT 2 -> f
            elif len(toks) == 5:
                x = getval(toks[0])
                y = getval(toks[2])
                op = getop(toks[1])
                if x != None and y != None:
                    vals[toks[4]] = op(x,y)

            # NOT y -> i
            elif len(toks) == 4:
                x = getval(toks[1])
                if x != None:
                    vals[toks[3]] = ~x

            if b_override != None:
                vals["b"] = b_override


p1 = solve()
p2 = solve(p1)
print(p1, p2)