from utils import *
from intcode import computer

input = [i.strip() for i in open("input","r").readlines()]


DIRS = {4: (1,0), 3:(-1,0), 1:(0,-1), 2:(0,1) }

destination_state = None
world = defaultdict(str)

def part1():
    global destination_state, world
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
        tries.append(((0,0), (deepcopy(allmem), 0, 0), d, 1))
    while len(tries) > 0:
        pos, state, dir, depth = tries.popleft()
        mem, pc, relbase = state
        comp = computer(mem, pc, relbase, dir)
        explore_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        n, newstate = next(comp)
        if n == 0:
            world[explore_pos] = '#'
        if n == 1:
            world[explore_pos] = '.'
            for ndir, vec in DIRS.items():
                npos = (explore_pos[0] + vec[0], explore_pos[1] + vec[1])
                if npos not in world:
                    world[npos] = '?'
                    tries.append((explore_pos, deepcopy(newstate), ndir, depth + 1))
        if n == 2:
            world[explore_pos] = '.'
            destination = explore_pos
            print(depth)
            destination_state = destination, deepcopy(mem), pc, relbase

def part2():
    global destination_state, world
    max_depth = 0

    bfs, visited = deque([(destination_state[0], 0)]), {destination_state[0]}
    while bfs:
        pos, depth = bfs.popleft()
        if pos in world and world[pos] != '#':
            if depth > max_depth:
                max_depth = depth
            for d in DIRS.values():
                g = (pos[0]+d[0],pos[1]+d[1])
                if g not in visited:
                    bfs.append((g, depth + 1))
                    visited.add(g)

    aoc(max_depth)

part1()
part2()





