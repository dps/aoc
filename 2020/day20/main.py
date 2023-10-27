from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def rot90cw(tile):
    return [''.join(row) for row in zip(*tile[::-1])]

def vflip(tile):
    return tile[-1::-1]

def permute_edges(tile):
    # Returns a list of tuples of 10 bit numbers (top,right,bottom,left)
    # flipped and unflipped for each rotation
    edges = []
    h = len(tile)
    w = len(tile[0])

    for _ in range(4):
        top = int(tile[0], 2)
        bottom = int(tile[h-1], 2)
        left = int("".join([t[0] for t in tile]), 2)
        right = int("".join([t[w-1] for t in tile]), 2)

        tflipped = bottom
        bflipped = top
        lflipped = int("".join(reversed([t[0] for t in tile])),2)
        rflipped = int("".join(reversed([t[w-1] for t in tile])), 2)

        edges.extend([(top, right, bottom, left, ",".join(tile)),
                      (tflipped, rflipped, bflipped, lflipped, ",".join(vflip(tile)))])
        tile = rot90cw(tile)
    return frozenset(edges)

def count_sea_monsters(placed, w):
    merged = []
    rem = []
    for tile in placed:
        chop_top_bottom = tile[4].split(",")[1:-1]
        rem.append([chop[1:-1] for chop in chop_top_bottom])
    tile_width = len(rem[0][0])
    for y in range(w):
        row_tiles = rem[y*w:((y+1)*w)]
        for line_n in range(tile_width):
            row = ""
            for tile in row_tiles:
                row += tile[line_n]
            merged.append(row)
    c, roughness = find_sea_monsters(merged)
    # if c > 0:
    #   print("\n".join(merged).replace("0",".").replace("1","#"))
    return c, roughness

def find_sea_monsters(image):
    count = 0
    sea_monster =["..................1..",
                  "1....11....11....111.",
                  ".1..1..1..1..1..1..."]
    for r in range(len(image)):
        for c in range(len(image[0])):
            m = 0
            for rs in range(len(sea_monster)):
                for cs in range(len(sea_monster[0])):
                    try:
                        if sea_monster[rs][cs] == ".":
                            continue
                        else:
                            if image[r+rs][c+cs] == "1":
                                m += 1
                    except IndexError:
                        break
            if m == 15:
                count += 1

    return count, sum([1 for ch in "".join(image) if ch == "1"]) - (count)*15

def check(placement, w):
    if len(placement) == 1:
        return True
    left = None if len(placement) % w == 1 else placement[-2][1] 
    above = None if len(placement) <= w else placement[-(w+1)][2]
    if left:
        if not placement[-1][3] == left:
            return False
    if above:
        if not placement[-1][0] == above:
            return False
    return True

def dfs(names, placed, remaining, w):
    if len(remaining) == 0:
        monsters, roughness = count_sea_monsters(placed, w)
        if (monsters > 0):
            print("Part 1 corners:", names[0]*names[w-1]*names[w*w-1]*names[w*w-w])
            print("Part 2 roughness:", roughness)
            exit(0)
    else:
        for tile in remaining:
            for rot in tile[1]:
                if check(placed + [rot], w):
                    dfs(names + [tile[0]], placed + [rot], remaining - {tile}, w)

def solve():

    tiles = set()
    
    for tile in bundles(input):
        num = positive_ints(tile[0])[0]
        data = [l.replace(".", "0").replace("#", "1") for l in tile[1:]]
        edges = permute_edges(data)
        tiles.add((num, edges))

    w = int(math.sqrt(len(tiles)))

    dfs([], [], tiles, w)

solve()
