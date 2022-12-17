from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

rocks = [
    {(2,0), (3,0), (4,0), (5,0)},       # -
    {(2,1),(3,1),(4,1), (3,0), (3,2)},  # +
    {(2,0), (3,0), (4,0), (4,1), (4,2)},# _|
    {(2,0),(2,1),(2,2),(2,3)},          # |
    {(2,0),(2,1),(3,0),(3,1)}           # square - those are all the rocks that I got!
]

sm = {">": 1, "<": -1}

def xminmax(rock):
    xmin = 9999
    xmax = -1
    for p in rock:
        if p[0] < xmin:
            xmin = p[0]
        if p[0] > xmax:
            xmax = p[0]
    return xmin, xmax
    
def shift(world, rock, move):
    min, max = xminmax(rock)
    if min == 0 and move == "<":
        return rock
    if max == 6 and move == ">":
        return rock
    r = set()
    d = sm[move]
    for p in rock:
        r.add((p[0] + d, p[1]))
    if len(world.intersection(r)) > 0:
        return rock
    return r

def drop_rock(rock):
    r = set()
    for p in rock:
        r.add((p[0], p[1] - 1))
    return r

def stop_rock(world, rock):
    drop = drop_rock(deepcopy(rock))
    return len(world.intersection(drop)) > 0

def hash_top_lines(world, wmax):
    res = ""
    for y in range(wmax, wmax-39, -1): #39 needed for input.txt, 14 enough for simple
        o = set()
        for x in range(7):
            if (x,y) in world:
                o.add(x)
        res += str(o)
    return res

def part2():
    # The system loops after some length, you just have to find when it loops

    seen_before = set()
    wmaxes_seen = {}
    blocks_seen = {}

    moves = [m for m in input[0].strip()]
    move_idx = 0
    rock_idx = 0
    world = set([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)])
    world_max = 0
    def print_top_of_world(wmax, owmax):
        delta = wmax - owmax
        for y in range(wmax,wmax-39,-1):
            for x in range(7):
                if (x,y) in world:
                    print("#", end="")
                else:
                    print(".", end="")
            print("      ", end="")
            for x in range(7):
                if (x,y-delta) in world:
                    print("#", end="")
                else:
                    print(".", end="")            
            print()
    r = -1
    heights = [0]
    deltas = []
    while True:
        state = hash_top_lines(world, world_max)
        heights.append(world_max)
        deltas.append(heights[-1] - heights[-2])

        r += 1
        if (move_idx, rock_idx, state) in seen_before:
            # We found a cycle
            cycle_blocks = r - blocks_seen[(move_idx, rock_idx, state)]
            cycle_height = world_max-wmaxes_seen[(move_idx, rock_idx, state)]
            remain = 1000000000000 - r
            tot = world_max
            i = 0
            add_cycles = remain // cycle_blocks
            tot += add_cycles * cycle_height
            remain -= add_cycles * cycle_blocks
            while remain > 0:
                if (remain % 10000000000) == 0:
                    print(remain)
                tot += deltas[-cycle_blocks:][i]
                remain -= 1
                i += 1
                i = i % cycle_blocks

            print(tot)
            return tot

        
        seen_before.add((move_idx, rock_idx, state))
        wmaxes_seen[(move_idx, rock_idx, state)] = world_max
        blocks_seen[(move_idx, rock_idx, state)] = r
        next_rock = rocks[rock_idx]
        rock_idx += 1
        rock_idx = rock_idx % len(rocks)
        rock = set()
        for point in next_rock:
            rock.add((point[0], point[1] + world_max + 4))

        while True:
            move = moves[move_idx]
            move_idx += 1
            move_idx = move_idx % len(moves)
            rock = shift(world, rock, move)
            if stop_rock(world, rock):
                world = world.union(rock)
                world_max = max([p[1] for p in world])
                break
            else:
                rock = drop_rock(rock)


def part1():
    moves = [m for m in input[0].strip()]
    move_idx = 0
    rock_idx = 0
    world = set([(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)])
    world_max = 0
    def print_world():
        return
        for y in range(30,-1,-1):
            for x in range(7):
                if (x,y) in world.union(rock):
                    print("#", end="")
                else:
                    print(".", end="")
            print()
    for r in range(2022):
        next_rock = rocks[rock_idx]
        rock_idx += 1
        rock_idx = rock_idx % len(rocks)
        rock = set()
        for point in next_rock:
            rock.add((point[0], point[1] + world_max + 4))
        print_world()

        while True:
            move = moves[move_idx]
            move_idx += 1
            move_idx = move_idx % len(moves)
            rock = shift(world, rock, move)
            if stop_rock(world, rock):
                world = world.union(rock)
                world_max = max([p[1] for p in world])
                break
            else:
                rock = drop_rock(rock)

    print(world_max)
    return(world_max)



if __name__ == '__main__':
    assert(part1() == 3153)
    assert(part2() == 1553665689155)
