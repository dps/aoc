from utils import *
from intcode import computer

input = [i.strip() for i in open("input","r").readlines()]


def part1():
    program = [int(x) for x in input[0].split(",")]    
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    acc = 0
    for x in range(0,50):
        for y in range(0, 50):
            c = computer(deepcopy(allmem), 0, 0, [x,y])
            acc += next(c)
    aoc(acc)

def part2():
    program = [int(x) for x in input[0].split(",")]    
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    def check(x,y):
        return next(computer(deepcopy(allmem), 0, 0, [x,y]))

    world = set()
    sqsize = 100
    cur_row = 16
    # Pick a line far enough out to skip the empty sections, and find its bounds.
    bnds = [check(x,cur_row-1) for x in range(20)]
    line = list(zip(bnds,[0]+bnds))
    prev_bounds = (line.index((1,0)),line.index((0,1))-1)

    bounds = {}
    overflow = None
    while True:
        left_bound = prev_bounds[0]
        while check(left_bound,cur_row) == 0:
            left_bound += 1
        right_bound = prev_bounds[1]
        while check(right_bound,cur_row) == 1:
            right_bound += 1
        right_bound -= 1
        bounds[cur_row] = (left_bound, right_bound)
        world.add(left_bound+1j*cur_row)
        world.add(right_bound+1j*cur_row)
        prev_bounds = bounds[cur_row]
        if overflow == None and (cur_row - (sqsize - 1)) in bounds and left_bound >= bounds[cur_row - (sqsize - 1)][0] and left_bound <= bounds[cur_row - (sqsize - 1)][1] and (left_bound+(sqsize-1)) <= bounds[cur_row - (sqsize-1)][1]:
            for x in range(left_bound, left_bound+sqsize):
                for y in range(cur_row-(sqsize-1),cur_row+1):
                    world.add(x+1j*y)
            aoc(10000 * left_bound + (cur_row - (sqsize - 1)))
            overflow = sqsize//10
        cur_row += 1
        if type(overflow) == type(1):
            overflow -= 1
            if overflow < 0:
                break
    #print_world(world)

#part1()
part2()
