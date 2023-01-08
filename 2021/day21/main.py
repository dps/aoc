from utils import *
#input = [i.strip() for i in open("input.txt","r").readlines()]

die_rolls = 0

def roll():
    global die_rolls
    die_rolls += 1
    return((die_rolls-1) % 100) + 1

def part1():
    p1_start = 10 #4 #ints(input[0])[1]
    p2_start = 9  #8 #ints(input[1])[1]

    scores = [0, 0]
    positions = [p1_start, p2_start]
    playing = 0

    while True:
        tot = roll()+roll()+roll()
        positions[playing] = ((positions[playing] + tot - 1) % 10) + 1
        scores[playing] += positions[playing]
        if scores[playing] >= 1000:
            break
        playing = 0 if playing == 1 else 1
    
    print(scores[0 if playing == 1 else 1] * die_rolls)


part1()
