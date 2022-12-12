from utils import *
import string
input = [i.strip() for i in open("input.txt","r").readlines()]

def delta(here, there):
    if there == 'S':
        return ord(here[0]) - ord("a")
    return ord(here[0]) - ord(there[0])

def track_back_from_end(g, here, val):
    moves_to_recurse = []
    start = g.get_cursor()
    for k,v in DIR.items():
        if g.could_move(v[0], v[1]):
            there = g.peek_move(v[0], v[1])
            if (isinstance(there, str) and delta(here, there) <= 1):
                g.move(v[0], v[1])
                g.set((val + 1, there))
                moves_to_recurse.append((there, (v[0], v[1]), val + 1))
                g.set_cursor(start[0], start[1])
            if (not isinstance(there, str)) and (delta(here, there[1]) <= 1 and there[0] > val + 1):
                g.move(v[0], v[1])
                g.set((val + 1, there[1]))
                moves_to_recurse.append((there[1], (v[0], v[1]), val + 1))
                g.set_cursor(start[0], start[1])

    for move in moves_to_recurse:
        g.set_cursor(start[0], start[1])
        g.move(move[1][0], move[1][1])
        track_back_from_end(g, move[0], val + 1)


def solve():
    grid = input
    start = None
    end = None
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            if col == 'S':
                start = (c, r)
            if col == 'E':
                end = (c, r)
    g = grid_from_strs(input)
    g.set_cursor(end[0], end[1])

    track_back_from_end(g, "z", 0)

    g.set_cursor(start[0], end[1])
    print(g.get())

    min = 9999999999
    for i in flatten(g.g()):
        if not isinstance(i, str):
            if i[1] == "a" and i[0] < min:
                min = i[0]
    print(min)


if __name__ == '__main__':
    solve()
