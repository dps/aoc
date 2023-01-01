from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve():
    world = set()
    read_folds = False
    folds = []
    for line in input:
        if len(line) == 0:
            read_folds = True
            continue
        if read_folds:
            folds.append((line.split("=")[0][-1], int(line.split("=")[1])))
            continue
        world.add(int(line.split(",")[0]) + int(line.split(",")[1])*1j)

    for i, fold in enumerate(folds):
        new_world = set()
        if fold[0] == 'y':
            for p in world:
                new_world.add(p.real + 1j * (p.imag if p.imag < fold[1] else fold[1] - (p.imag - fold[1])))
        if fold[0] == 'x':
            for p in world:
                new_world.add(1j* p.imag + (p.real if p.real < fold[1] else fold[1] - (p.real - fold[1])))
        world = new_world
        if i == 0:
            print("Part 1:", len(world))
    
    mx, my = int(max([p.real for p in world])), int(max([p.imag for p in world]))
    for y in range(my+1):
        for x in range(mx+1):
            print("#" if x+1j*y in world else " ", end="")
        print()

solve()
