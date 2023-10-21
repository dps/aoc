from utils import *

input = [i.strip() for i in open("test.txt","r").readlines()]

def part1():
    g,w,h = grid_from_strs(input)
    g = g.g()
    seats = set()
    occupied = set()
    for x in range(w):
        for y in range(h):
            if g[y][x] == 'L':
                seats.add((x,y))

    poccupied = None
    while poccupied != occupied:
        poccupied = deepcopy(occupied)
        new_occupied = set()
        for x in range(w):
            for y in range(h):
                if (x,y) not in seats:
                    continue
                adj = 0
                for c in DIR8:
                    if (x+c[0], y+c[1]) in occupied:
                        adj += 1
                if (x,y) in occupied:
                    if adj < 4:
                        new_occupied.add((x,y))
                else:
                    if adj == 0:
                        new_occupied.add((x, y))
        occupied = new_occupied
    aoc(len(occupied))

def part2():
    g,w,h = grid_from_strs(input)
    g = g.g()
    seats = set()
    occupied = set()
    for x in range(w):
        for y in range(h):
            if g[y][x] == 'L':
                seats.add((x,y))

    poccupied = None
    while poccupied != occupied:
        poccupied = deepcopy(occupied)
        new_occupied = set()
        for x in range(w):
            for y in range(h):
                if (x,y) not in seats:
                    continue
                adj = 0
                for c in DIR8:
                    if (x+c[0], y+c[1]) in occupied:
                        adj += 1
                if (x,y) in occupied:
                    if adj < 4:
                        new_occupied.add((x,y))
                else:
                    if adj == 0:
                        new_occupied.add((x, y))
        occupied = new_occupied
    aoc(len(occupied))

#part1()
part2()
