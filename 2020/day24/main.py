from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def chomp(moves):
    while len(moves) > 0:
        ch = moves[0]
        if ch == 'e':
            yield 1,0
            moves = moves[1:]
            continue
        if ch == 'w':
            yield -1,0
            moves = moves[1:]
            continue
        ch += moves[1]
        if ch == 'se':
            yield 0,1
            moves = moves[2:]
            continue
        if ch == 'sw':
            yield -1,1
            moves = moves[2:]
            continue
        if ch == 'ne':
            yield 1,-1
            moves = moves[2:]
            continue
        if ch == 'nw':
            yield 0,-1
            moves = moves[2:]
            continue

def solve():
    tiles = defaultdict(bool)
    neighbors = [(1,0),(-1,0),(0,1),(-1,1),(1,-1),(0,-1)]
    for moves in input:
        x,y = 0,0
        for dx,dy in chomp(moves):
            x += dx
            y += dy
        tiles[(x,y)] = not tiles[(x,y)]
    print("part 1:", sum([1 for k,v in tiles.items() if v==True]))

    count = 100
    while count > 0:
        candidates = set()
        for tile in tiles:
            candidates.add(tile)
            for n in neighbors:
                candidates.add((tile[0] + n[0], tile[1] + n[1]))

        new_tiles = defaultdict(bool)
        for c in candidates:
            nc = sum([1 for dx,dy in neighbors if tiles[(c[0]+dx, c[1]+dy)] == True])
            if tiles[c] == True:
                # black
                if nc == 0 or nc > 2:
                    new_tiles[c] = False
                else:
                    new_tiles[c] = True
            elif tiles[c] == False:
                if nc == 2:
                    new_tiles[c] = True
                else:
                    new_tiles[c] = False
        tiles = new_tiles
        count -= 1

    print("part 2:", sum([1 for _,v in tiles.items() if v==True]))


solve()