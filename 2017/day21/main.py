
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def rotate_cw(g):
    return tuple([tuple(x) for x in list(zip(*g[::-1]))])

def flip_h(g):
    return tuple([tuple(reversed(x)) for x in g])

def flip_v(g):
    return tuple(g[::-1])

board = [".#.","..#","###"]
board = tuple(tuple(l) for l in board)

rules = {}
for line in D:
    ##.#/.#./#.# => ..#./##.#/..../....
    l,r = line.split(" => ")
    dest = tuple(tuple(s) for s in r.split("/"))
    o = [tuple(s) for s in l.split("/")]
    rules[tuple(o)] = dest
    rules[flip_h(o)] = dest
    rules[flip_v(o)] = dest
    for deg in [90,180,270]:
        o = rotate_cw(o)
        rules[tuple(o)] = dest
        rules[flip_h(o)] = dest
        rules[flip_v(o)] = dest

world = set()
for x, row in enumerate(board):
    for y, ch in enumerate(row):
        if ch == '#':
            world.add((x,y))

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
                for y, row in enumerate(expand):
                    for x, ch in enumerate(row):
                        if ch == "#":
                            new_world.add((ix*m+x,iy*m+y))
    world = new_world
    w += w//d
    h += h//d
    if iter == 4:
        print("Part 1",len(world))

print("Part 2", len(world))
