
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

board, moves = bundles(D)

grid = {x+1j*y:c for y,line in enumerate(board) for x,c in enumerate(line)}
p = [p for p, c in grid.items() if c == "@"][0]

for m in "".join(moves):
    move = {'<':-1, '>':1, '^':-1j, 'v':1j}[m]

    if grid[p+move] == "#":
        continue
    elif grid[p+move] == ".":
        grid[p] = "."
        grid[p+move] = "@"
        p += move
    elif grid[p+move] == "O":
        can_move = False
        collect = []
        q = p + move
        while q in grid and grid[q] == "O":
            collect.append((q, q+move))
            q += move
        if q in grid and grid[q] == ".":
            can_move = True
        if can_move:
            prev = '@'
            for c,new_c in collect:
                grid[new_c] = 'O'
                grid[c] = prev
                prev = 'O'
            grid[p] = "."
            p += move

tot = sum(p.real+100*p.imag for p in grid if grid[p] == 'O')
print(int(tot))
