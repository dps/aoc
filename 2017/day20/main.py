
from utils import *

D = [i.strip() for i in open("input","r").readlines()]


def solve(part):
    particles = []
    cycles = 0
    for line in D:
        p = ints(line)
        particles.append(p)
        cycles = max(cycles, max([abs(x) for x in p[0:3]]))

    for _ in range(cycles):
        world = defaultdict(list)
        for i,p in enumerate(particles):
            px,py,pz,vx,vy,vz,ax,ay,az = p
            vx += ax
            vy += ay
            vz += az
            px += vx
            py += vy
            pz += vz
            particles[i] = [px,py,pz,vx,vy,vz,ax,ay,az]
            world[(px,py,pz)].append(i)
        if part == 2:
            to_del = set()
            for idx in flatten([l for l in world.values() if len(l) > 1]):
                to_del.add(idx)
                #print(k)
            particles = [p for i,p in enumerate(particles) if i not in to_del]

    if part == 1:
        mi,mii = math.inf, None
        for i,p in enumerate(particles):
            px,py,pz,vx,vy,vz,ax,ay,az = p
            d = manhattan3((0,0,0), (px,py,pz))
            if d < mi:
                mi = d
                mii = i

        print(mii)
    else:
        print(len(particles))

solve(1)
solve(2)