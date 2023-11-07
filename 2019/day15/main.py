from utils import *
from intcode import computer

input = [i.strip() for i in open("input","r").readlines()]


DIRS = {4: (1,0), 3:(-1,0), 1:(0,-1), 2:(0,1) }

destination_state = None

def part1():
    global destination_state
    program = [int(x) for x in input[0].split(",")]
    world = defaultdict(str)
    world[(0,0)] = '.'
    destination = None
        
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    n = None
    tries = deque()
    for d in range(1,4):
        tries.append(((0,0), (deepcopy(allmem), 0, 0), d))
    while len(tries) > 0:
        pos, state, dir = tries.popleft()
        mem, pc, relbase = state
        comp = computer(mem, pc, relbase, dir)
        explore_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        n, newstate = next(comp)
        if n == 0:
            world[explore_pos] = '#'
        if n == 1:
            world[explore_pos] = '.'
            if destination == None:
                for ndir, vec in DIRS.items():
                    npos = (explore_pos[0] + vec[0], explore_pos[1] + vec[1])
                    if npos not in world:
                        world[npos] = '?'
                        tries.append((explore_pos, deepcopy(newstate), ndir))
        if n == 2:
            world[explore_pos] = '.'
            destination = explore_pos
            destination_state = destination, deepcopy(mem), pc, relbase

    #print(destination)
    #print_dict_world(world)
    def neighbors(p):
        nonlocal world
        for d in DIRS.values():
            if world[(p[0]+d[0],p[1]+d[1])] == '.':
                yield((1, (p[0]+d[0],p[1]+d[1])))

    aoc(dynamic_dijkstra(neighbors, (0,0), destination)[0])

def part2():
    global destination_state
    world = defaultdict(str)
    destination = destination_state[0]
    world[destination] = '.'

    max_depth = 0

    n = None
    tries = deque()
    for d in range(1,4):
        tries.append((destination, (destination_state[1], destination_state[2], destination_state[3]), d, 1))
    while len(tries) > 0:
        pos, state, dir, depth = tries.popleft()
        mem, pc, relbase = state
        comp = computer(mem, pc, relbase, dir)
        explore_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        n, newstate = next(comp)
        if n == 0:
            world[explore_pos] = '#'
        if n > 0:
            world[explore_pos] = '.'
            if depth > max_depth:
                max_depth = depth
            for ndir, vec in DIRS.items():
                npos = (explore_pos[0] + vec[0], explore_pos[1] + vec[1])
                if npos not in world:
                    world[npos] = '?'
                    tries.append((explore_pos, deepcopy(newstate), ndir, depth+1))

    #print_dict_world(world)
    aoc(max_depth)

part1()
part2()





