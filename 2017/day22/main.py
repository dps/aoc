
D = [i.strip() for i in open("input","r").readlines()]

def solve(part=1):
    world = {}

    for y, row in enumerate(D):
        for x, ch in enumerate(row):
            if ch == '#':
                world[(x+(1j*y))] = '#'

    p = (12+12j)
    d = -1j

    inf = 0
    # This could be optimized because it becomes a glider
    # at some point, but it's cheap enough to simulate the
    # whole thing
    for _ in range(10000 if part==1 else 10000000):
        if p not in world: # clean
            d = d * -1j
            if part == 1:
                world[p] = '#'
                inf += 1
            else:
                world[p] = 'W'
        else:
            t = world[p]
            if t == '#':
                d = d * 1j
                if part == 1:
                    del(world[p])
                else:
                    world[p] = 'F'
            elif t == 'W':
                world[p] = '#'
                inf += 1
            elif t == 'F':
                del(world[p])
                d = -d
        p = p + d

    print(inf)

solve(1)
solve(2)