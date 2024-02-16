
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

discs = []
for line in D:
    d = ints(line)
    discs.append(d)
discs.append([7,11,0])
p1_done = False
for i in range(10000000):
    broke = None
    for j,ds in enumerate(discs, 1):
        if (ds[-1]+i+j)%ds[1] != 0:
            broke=j
            break
    if broke == len(D) and not p1_done:
        print("p1", i)
        p1_done = True
    if broke==None:
        print("p2", i)
        break


