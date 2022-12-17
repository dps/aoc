from utils import *

input = [i.strip() for i in open("simple.txt","r").readlines()]

rocks = [
    {(2,0), (3,0), (4,0), (5,0)},       # -
    {(2,1),(3,1),(4,1), (3,0), (3,2)},  # +
    {(2,0), (3,0), (4,0), (4,1), (4,2)},# _|
    {(2,0),(2,1),(2,2),(2,3)},          # |
    {(2,0),(2,1),(3,0),(3,1)}           # square - those are the rocks that I got!
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

def top_twenty(world, wmax):
    res = ""
    for y in range(wmax, wmax-39, -1):
        o = set()
        for x in range(7):
            if (x,y) in world:
                o.add(x)
        res += str(o)
    return res

def top_til_line(world, wmax):
    res = ""
    y = wmax
    while True:
        o = 0
        for x in range(7):
            if (x,y) in world:
                o += pow(2, x)
        res += chr(65+o) #65 just makes it pretty to print
        if o == 127:
            break
        y -= 1
    return res

ALL_X = set([x for x in range(7)])

def top_til_every_xspot_seen(world, wmax):
    res = ""
    y = wmax
    s = set()
    while True:
        o = 0
        for x in range(7):
            if (x,y) in world:
                o += pow(2, x)
                s.add(x)
        res += chr(65+o) #65 just makes it pretty to print
        if s == ALL_X:
            break
        y -= 1
    return res

def part2():
    # My hypothesis is that the system loops after some length, you just have to find when it loops
    # that would be when the bottom half of the world is exactly equal to the top half of the world with the same next block falling
    # and on same move count.
    # OR there are a finite number of blocks and a finite number of moves so the height at num_blocks
    # * num_moves will repeat?
    # Let's find the height at num_blocks times num_moves? No, they don't neatly go into each other, so let's find how tall it is when
    # it loops

    # how about we grab move_idx, rock_idx and a bitmask of the top 20 lines and see how long until that loops?
    # that loops pretty quickly actually and the math doesn't quite work out for the simple input, so it must be harder than that.
    # >>> 1000000000000/2351
    # 425350914.5044662
    # >>> 1000000000000/62
    # 16129032258.064516
    # >>> 16129032258.064516 * 100
    # 1612903225806.4517 <<--- should be 1514285714288, close but not perfect
    
    # So... go back more lines? Since no blocks can fall past a full line across that seems like the most conservative approach.
    # Trying that... Not found a loop after 21000 iterations in simple.txt, but it also seems like overkill to have to look back that far
    # it's more like as soon as the full path across the grid is blocked?
    # e.g. this should count:
    # |.....##|
    # |..####.|
    # |####...|
    # no blocks can fall past this pattern.
    # There are definitely degenerate inputs (e.g. if you blow the blocks always to the left), but we don't seem to have one of these.
    #
    # Hmm... this loops after 63 blocks with stack height 102 (very similar to the prev)
    # >>> 1000000000000/63
    # 15873015873.015873
    # >>> 15873015873.015873 * 102
    # 1619047619047.6191

    # Let's go back to top 20 and do some visualization


    seen_before = set()
    wmaxes_seen = {}
    blocks_seen = {}

    moves = [m for m in input[0].strip()]
    #print(len(moves)) # 10091 for input
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
    start_decr = False
    nblock = 999
    before_extra_wm = 0
    almost_there = 0
    heights = []
    while nblock > 0:
        state = top_twenty(world, world_max)
        heights.append(world_max)

        if (start_decr):
            nblock -= 1

        r += 1
        if (r % 1000 ==0):
            print(r, len(state))
        if not start_decr and (move_idx, rock_idx, state) in seen_before:
            print("SEEN BEFORE!", r, world_max, wmaxes_seen[(move_idx, rock_idx, state)], blocks_seen[(move_idx, rock_idx, state)])
            print_top_of_world(world_max, world_max)

            #Between blocks_seen[(move_idx, rock_idx, state)] nBLOCKS and r we have a cycle
            cycle_blocks = r - blocks_seen[(move_idx, rock_idx, state)]
            print("cycle blocks=", cycle_blocks)
            #Before the next block fell at the start of this cycle, we had a tower of height
            start_blocks = blocks_seen[(move_idx, rock_idx, state)]
            print("start num blocks before cycle=", blocks_seen[(move_idx, rock_idx, state)])
            print("orig tower h=", wmaxes_seen[(move_idx, rock_idx, state)])
            # height of the cycle is
            cycle_height = world_max-wmaxes_seen[(move_idx, rock_idx, state)]
            print("cycle height=", cycle_height)
            # we'll also need to simulate the remaining falling on top. How many blocks?
            print("heights", heights[-cycle_blocks:]) #.  <<<-- the first of these should be the same as next line 
            print("hs ", heights[blocks_seen[(move_idx, rock_idx, state)]])
            # blocks after start bit
            nblocks = 1000000000000 - blocks_seen[(move_idx, rock_idx, state)] - cycle_blocks
            # middle part is cycles

            print("height after one cycle (incl start)", heights[start_blocks+cycle_blocks])
            after_first_cycle = heights[start_blocks+cycle_blocks]
            remainder = (nblocks / cycle_blocks) % 1

            more_blocks = round(remainder * cycle_blocks)
            print("more blocks", more_blocks)
            almost_there = after_first_cycle + ((nblocks/cycle_blocks) - 1 ) * cycle_height
            print("height before final blocks:", almost_there)
            print("wmax now", world_max)
            before_extra_wm = world_max
            # print(r)
            # print(top_twenty(world, wmaxes_seen[(move_idx, rock_idx, state)]))
            # print_top_of_world(world_max, wmaxes_seen[(move_idx, rock_idx, state)])
            # print()
            hh = heights[-cycle_blocks:]
            nblock = 0
            print("height added at start of cycle by that number extras:", hh[more_blocks]-hh[0])
            start_decr = True

        if start_decr:
            print("In start_decr ", r, world_max)
        
        seen_before.add((move_idx, rock_idx, state))
        wmaxes_seen[(move_idx, rock_idx, state)] = world_max
        blocks_seen[(move_idx, rock_idx, state)] = r
        #print(r)
        next_rock = rocks[rock_idx]
        rock_idx += 1
        rock_idx = rock_idx % len(rocks)
        rock = set()
        for point in next_rock:
            rock.add((point[0], point[1] + world_max + 4))
        #print_world()

        while True:
            move = moves[move_idx]
            move_idx += 1
            move_idx = move_idx % len(moves)
            rock = shift(world, rock, move)
            #print_world()
            if stop_rock(world, rock):
                #print("STOP")
                #print_world()
                world = world.union(rock)
                world_max = max([p[1] for p in world])
                break
            else:
                rock = drop_rock(rock)
                #print_world()

    print(world_max)
    print(almost_there + (world_max-before_extra_wm))

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
        #print(r)
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
            #print_world()
            if stop_rock(world, rock):
                #print("STOP")
                #print_world()
                world = world.union(rock)
                world_max = max([p[1] for p in world])
                break
            else:
                rock = drop_rock(rock)
                #print_world()

    print(world_max)



if __name__ == '__main__':
    part2()
