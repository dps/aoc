from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def chomp(moves):
    while len(moves) > 0:
        ch, moves = moves[0], moves[1:]
        if ch in HEX_DIR:
            yield HEX_DIR[ch]
        else:
            ch, moves = ch + moves[0], moves[1:]
            yield HEX_DIR[ch]

def solve():
    tiles = defaultdict(bool)
    for moves in input:
        x,y = 0,0
        for dx,dy in chomp(moves):
            x += dx
            y += dy
        tiles[(x,y)] = not tiles[(x,y)]
    print("part 1:", sum([1 for _,v in tiles.items() if v==True]))

    count = 100
    while count > 0:
        candidates = set()
        for tile in tiles:
            candidates.add(tile)
            for n in HEX_NEIGHBORS:
                candidates.add((tile[0] + n[0], tile[1] + n[1]))

        new_tiles = defaultdict(bool)
        for c in candidates:
            nc = sum([1 for dx,dy in HEX_NEIGHBORS if tiles[(c[0]+dx, c[1]+dy)] == True])
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