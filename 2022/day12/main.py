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

def delt(here, there):
    if there == 'S':
        return ord("a") - ord(here)
    if there == 'E':
        return ord("z") - ord(here)
    if here == 'S':
        return ord(there) - ord("a")
    if here == 'E':
        return ord(there) - ord("z")

    return ord(there) - ord(here)

def can_walk(r,c,ch):
    ret = []
    for _,i in DIR.items():
        if r + i[1] < len(input) and r + i[1] >= 0 and c + i[0] < len(input[0]) and c + i[0] >= 0:
            if delt(ch, input[r+i[1]][c + i[0]]) <= 1:
                ret.append(str(r+i[1])+","+str(c+i[0]))
    return ret

def solve2():
    graph = {}
    ayes = []
    start, end = None, None
    for r, row in enumerate(input):
        for c, ch in enumerate(row):
            key = str(r)+","+str(c)
            graph[key] = can_walk(r,c,ch)
            if ch == 'S':
                start = str(r)+","+str(c)
                ayes.append(str(r)+","+str(c))
            if ch == 'E':
                end = str(r)+","+str(c)
            if ch == 'a':
                ayes.append(str(r)+","+str(c))

    print(len(find_shortest_path(graph, start, end)) - 1)

    min_path = 9999999
    for a in ayes:
        path = find_shortest_path(graph, a, end)
        if path:
            t = len(path) - 1
            if t < min_path:
                min_path = t
    print(min_path)
            
    pass

if __name__ == '__main__':
    solve()
    solve2()
