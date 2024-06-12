
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

floor, p2 = 0, None
for i, ch in enumerate(D[0]):
    if ch == "(":
        floor += 1
    if ch == ")":
        floor -= 1
    if floor == -1 and p2 == None:
        p2 = i+1

print(floor, p2)