
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

greds = []
for line in D:
    c,d,f,t,v = ints(line)
    greds.append((c,d,f,t,v))

def solve(part=1):
    mm = 0
    for s in range(0, 101):
        for p in range(0, 100-s+1):
            for c in range(0, 100-(s+p)+1):
                l = 100 - (s+p+c)
                prod = 1
                recipe = (s,p,c,l)

                cals = 0
                for ingred in range(4):
                    cals += greds[ingred][4] * recipe[ingred]

                if part == 2 and cals != 500:
                    continue

                for property in range(4):
                    tot = 0
                    for ingred in range(4):
                        tot += greds[ingred][property] * recipe[ingred]

                    if tot < 0:
                        tot = 0

                    prod *= tot

                if prod > mm:
                    mm = prod
    return mm


print(solve(1), solve(2))