
from utils import *

D = [ints(i.strip()) for i in open("input","r").readlines()]

print(sum([max(l) - min(l) for l in D]))

p2 = 0
for line in D:
    for a,b in combinations(line,2):
        n=max(a,b)
        d=min(a,b)
        if n%d == 0:
            p2 += n//d
            break
print(p2)

