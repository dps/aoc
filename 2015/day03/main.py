
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p, santa, robot = 0, 0, 0
visited, visited2 = set([0]), set([0])

for i,ch in enumerate(D[0]):
    d = CARROWS[ch]
    p += d
    visited.add(p)
    if i % 2 == 0:
        santa += d
        visited2.add(santa)
    else:
        robot += d
        visited2.add(robot)

print(len(visited), len(visited2))