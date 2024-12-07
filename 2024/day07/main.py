
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0


def dfs(vals, acc, target, operators):
    if len(vals) == 0:
        return acc == target
    for op in operators:
        if op == "+":
            if dfs(vals[1:], acc + vals[0], target, operators):
                return True
        elif op == "||":
            if dfs(vals[1:], int(str(acc) + str(vals[0])), target, operators):
                return True
        else:
            if dfs(vals[1:], acc * vals[0], target, operators):
                return True
    return False

for line in D:
    target, acc, *vals = ints(line)
    if dfs(vals, acc, target, ["+", "*"]):
        p1 += target
    if dfs(vals, acc, target, ["+", "*", "||"]):
        p2 += target

print(p1, p2)
