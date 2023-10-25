from utils import *
import operator

input = [i.strip() for i in open("input.txt","r").readlines()]

def symbol_to_op(sym):
    return {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}[sym]

def eval_flattened_plus_precedence(flat):
    while "+" in flat:
        pp = flat.index("+")
        l = flat[pp-1]
        r = flat[pp+1]
        res = int(l) + int(r)
        flat.insert(pp+2, res)
        flat.pop(pp-1)
        flat.pop(pp-1)
        flat.pop(pp-1)
    return eval(" ".join(map(str, flat)))

def eval_flattened_left_precedence(flat):
    acc = int(flat[0])
    op = None
    for tok in flat[1:]:
        if str(tok).isnumeric():
            acc = op(acc, int(tok))
        else:
            op = symbol_to_op(tok)
    return acc

def calc(toks, ev):
    i = 0
    flat = []
    while i < len(toks):
        t = toks[i]
        if t == "(":
            v,c = calc(toks[i+1:], ev)
            i += c
            flat.append(v)
        elif t == ")":
            return ev(flat), i+1
        else:
            flat.append(t)
        i += 1
    return ev(flat)

def solve(ev):
    sum = 0
    for line in input:
        line = line.replace("(", "( ")
        line = line.replace(")", " )")
        res = calc(line.split(" "), ev)
        sum += res
    aoc(sum)

solve(eval_flattened_left_precedence)
solve(eval_flattened_plus_precedence)
