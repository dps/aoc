from collections import deque
from functools import cache
import sys
input = [i.strip() for i in open("input.txt","r").readlines()]

blizzards = deque([])
max_x, max_y = 0,0
global_min = 512

def wrap(p):
    q = p
    if p.real > max_x:
        q = 0 + q.imag * 1j
    if p.real < 0:
        q = max_x + q.imag * 1j
    if p.imag > max_y:
        q = q.real
    if p.imag < 0:
        q = q.real + 1j*max_y
    return q

MV = {'<': -1, '>': 1, '^': -1j, 'v': 1j, '$': 0}

@cache
def blizzards_at(mins):
    if mins == 0:
        return blizzards
    prev = blizzards_at(mins - 1)
    this_min = deque([])
    for blizzard in prev:
        mv = MV[blizzard[0]]
        this_min.append((blizzard[0], wrap(blizzard[1] + mv)))
    return this_min

@cache
def dfs(pos, goal, mins_elapsed):
    global global_min
    if mins_elapsed > global_min:
        return sys.maxsize
    blizz = blizzards_at(mins_elapsed + 1)
    best = sys.maxsize
    for move in MV.values():
        next = pos + move
        if next == goal:
            if (mins_elapsed + 1) < global_min:
                global_min = mins_elapsed + 1
            return mins_elapsed + 1
        if next.real < 0 or next.real > max_x or next.imag < 0 or next.imag > max_y:
            continue
        if not any([b[1] == next for b in blizz]):
            best = min(best, dfs(next, goal, mins_elapsed + 1))
    return best

def solve():
    global max_x, max_y, blizzards, global_min
    # Ignore the sides
    for y,row in enumerate(input):
        for x, ch in enumerate(row):
            if ch in "<>^v":
                blizzards.append((ch, (x-1)+(y-1)*1j))
    max_x = len(input[0]) - 3
    max_y = len(input) - 3

    pos = (0-1j)
    goal = max_x+(max_y+1)*1j

    initial_crossing = dfs(pos, goal, 2)
    print("Part 1 answer:", initial_crossing, "mins")

    blizzards = blizzards_at(initial_crossing)
    blizzards_at.cache_clear()
    dfs.cache_clear()
    global_min = 512

    return_journey = dfs(goal, pos, 1)
    print(return_journey)

    blizzards = blizzards_at(return_journey)
    blizzards_at.cache_clear()
    dfs.cache_clear()
    global_min = 512

    back_again = dfs(pos, goal, 1)
    print(back_again)
    print("Part 2 answer:", initial_crossing + return_journey + back_again, "mins")

if __name__ == '__main__':
    # input is 122x26 # Runtime: 54.58s
    solve()