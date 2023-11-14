from utils import *
from intcode import computer
from string import *

input = [i.strip() for i in open("input","r").readlines()]


def part1():
    program = [int(x) for x in input[0].split(",")]    
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    P = ["NOT A J",
         "NOT C T",
         "AND D T",
         "OR T J"]
    A = "WALK"

    # jump makes it 4 squares further than take off

    # #####.#..########
    #   ^ABCD

    ins = []
    for line in P:
        ins.extend([ord(i) for i in line])
        ins.append(10)
    ins.extend([ord(i) for i in A])
    ins.append(10)

    c = computer(allmem, 0, 0, ins)
    output = [ch for ch in c if ch]
    aoc(output[-1])

def part2():
    program = [int(x) for x in input[0].split(",")]    
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    P = [
        "OR E J", # J = E
        "AND I J", # J = E&&I
        "OR H J",  # J = (E&&I) || H
        "OR B T", # T = B
        "AND C T", # T = B&&C
        "NOT T T", # T = !(B&&C)
        "AND T J", # J = (!(B&C) && (H || (E&&I)))
        "AND D J", # J = ((!(B&C) && (H || (E&&I))) && D)
        "NOT A T",
        "OR T J",  # J = !A OR ((!(B&C) && (H || (E&&I))) && D)
    ]
    A = "RUN"

    # Collecting times I want to jump:
    # ###.###########
    #   ^ABCDEFGHI
    # #####.#..########
    #   ^ABCDEFGHI
    # #####.#..########
    #   ^ABCDEFGHI

    # BUT THAT LANDS US IN HOLE AT H, so require land at H
    # #####.#.##...####
    #   ^ABCDEFGHI
    #       ^ABCDEFGHI

    #   _ABCDEFGHI
    # ....@............
    # #####.###..#.####
    #     ^ABCdEFG*I    lands us in hole at H

    # ..@.............. did not want to jump here - require land at D
    # #####...#########
    #   ^ABCDEFGHI

    ins = []
    for line in P:
        ins.extend([ord(i) for i in line])
        ins.append(10)
    ins.extend([ord(i) for i in A])
    ins.append(10)

    c = computer(allmem, 0, 0, ins)
    output = [ch for ch in c if ch]
    #print("".join(output))
    aoc(output[-1])

part1()
part2()

