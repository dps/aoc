from utils import *

p1_start = 10
p2_start = 9

die_rolls = 0

def roll():
    global die_rolls
    die_rolls += 1
    return((die_rolls-1) % 100) + 1

def part1():
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

p1_winning_states = []
p2_winning_states = []
@cache
def dfs(scores, positions, to_play, depth):
    if to_play != -1:
        if scores[0] >= 21:
            p1_winning_states.append(scores)
            return 1
        if scores[1] >= 21:
            p2_winning_states.append(scores)
            return 1j
    if to_play == -1:
        to_play = 0
    s = 0
    for roll, universes in [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]:
        if to_play == 0:
            new_pos = ((positions[0] + roll - 1) % 10) + 1
            s += universes * dfs((scores[0] + new_pos, scores[1]), (new_pos, positions[1]), 1, depth+1)
        else:
            new_pos = ((positions[1] + roll - 1) % 10) + 1
            s += universes * dfs((scores[0], scores[1] + new_pos), (positions[0], new_pos), 0, depth+1)
    return s



def part2():
    s = dfs((0,0),(p1_start,p2_start), -1, 0)
    print(max(s.real, s.imag))

part1()
part2()
