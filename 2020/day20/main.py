from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def rot90cw(tile):
    h = len(tile)
    w = len(tile[0])
    newtile = []
    for x in range(w):
      row = ""
      for y in range(h-1, -1, -1):
          row += tile[y][x]
      newtile.append(row)
    return newtile

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

        tfp = int("".join(reversed(tile[0])),2)
        bfp = int("".join(reversed(tile[h-1])),2)
        lfp = right
        rfp = left

        edges.extend([(top, right, bottom, left),
                      (tflipped, rflipped, bflipped, lflipped),
                      (tfp, rfp, bfp, lfp)])
        tile = rot90cw(tile)
    return frozenset(edges)


def check(names, placement, w):
    # dbg = False
    # if names == [1951,2311,3079,2729]:
    #     print("CHECK!")
    #     dbg = True
    if len(placement) == 1:
        return True
    left = None if len(placement) % w == 1 else placement[-2][1] 
    above = None if len(placement) <= w else placement[-(w+1)][2]
    # if dbg:
    #   print(left, above, placement[-1][3], placement[-1][0])
    if left:
        if not placement[-1][3] == left:
            return False
    if above:
        if not placement[-1][0] == above:
            return False
    # if (dbg):
    #     print("CHECK TRUE")
    return True


def dfs(names, placed, remaining, w):
    #print("dfs", names, len(remaining), w)
    if len(remaining) == 0:
        print("DONE", names)
        print(names[0]*names[w-1]*names[w*w-1]*names[w*w-w])
    else:
        for tile in remaining:
            for rot in tile[1]:
                if check(names + [tile[0]], placed + [rot], w):
                    dfs(names + [tile[0]], placed + [rot], remaining - {tile}, w)

def solve(part=1):

    tiles = set()
    
    for tile in bundles(input):
        num = positive_ints(tile[0])[0]
        data = [l.replace(".", "0").replace("#", "1") for l in tile[1:]]
        edges = permute_edges(data)
        tiles.add((num, edges))
    print(tiles)

    w = int(math.sqrt(len(tiles)))
    print(w)

    dfs([], [], tiles, w)

    aoc(0)

solve(1)
