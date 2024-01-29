
from utils import *

depth = 7740
target = (12,763)

def elevel(n):
    return (n+depth)%20183

@cache
def geo_index(x,y):
    if (x,y) == (0,0) or (x,y) == target:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return ((geo_index(x-1,y)+depth)%20183) * ((geo_index(x,y-1)+depth)%20183)

print(sum(elevel(geo_index(x,y))%3 for x in range(target[0]+1) for y in range(target[1]+1)))

target = (12, 763, 1)
start = (0,0,1)

def neighbors(state):
    x,y,e = state
    stype = elevel(geo_index(x,y))%3

    for d in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx,ny = x + d[0], y + d[1]
        if nx < 0 or ny < 0:
            continue
        ntype = elevel(geo_index(nx,ny))%3
        if ntype == 0 and (e == 1 or e == 2):
            yield (1, (nx,ny,e))
        elif ntype == 1 and (e == 0 or e == 2):
            yield (1, (nx,ny,e))
        elif ntype == 2 and (e == 0 or e == 1):
            yield (1, (nx,ny,e))

    if stype == 0:
        yield (7, (x,y,2 if e == 1 else 1))
    elif stype == 1:
        yield (7, (x,y,0 if e == 2 else 2))
    elif stype == 2:
        yield (7, (x,y,1 if e == 0 else 0))

print(dynamic_a_star(neighbors, start,target, lambda z,e:manhattan((z[0],z[1]), target))[0])