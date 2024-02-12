
D = [i.strip() for i in open("input","r").readlines()]

def rotate_cw(g):
    return tuple([tuple(x) for x in list(zip(*g[::-1]))])

def flip_h(g):
    return tuple([tuple(reversed(x)) for x in g])

def flip_v(g):
    return tuple(g[::-1])

rules = {}
for line in D:
    ##.#/.#./#.# => ..#./##.#/..../....
    l,r = line.split(" => ")
    dest = set()
    for y, row in enumerate(r.split("/")):
        for x, ch in enumerate(row):
            if ch == '#':
                dest.add((x,y))

    o = tuple(tuple(s) for s in l.split("/"))
    rules[o] = dest
    rules[flip_h(o)] = dest
    rules[flip_v(o)] = dest
    for deg in [90,180,270]:
        o = rotate_cw(o)
        rules[o] = dest
        rules[flip_h(o)] = dest
        rules[flip_v(o)] = dest

world = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
w,h = 3,3

for iter in range(18):
    d = 2 if (w % 2 == 0) else 3
    m = 4 if d == 3 else 3

    new_world = set()
    for iy in range(h//d):
        for ix in range(w//d):
            xx,yy = ix*d,iy*d
            tile = []
            for y in range(d):
                r = []
                for x in range(d):
                    if (xx+x,yy+y) in world:
                        r.append("#")
                    else:
                        r.append(".")
                tile.append(tuple(r))

            tile = tuple(tile)
            if tile in rules:
                expand = rules[tile]
                for (x,y) in expand:
                    new_world.add((ix*m+x,iy*m+y))
    world = new_world
    w += w//d
    h += h//d
    if iter == 4:
        print("Part 1",len(world))

print("Part 2", len(world))
