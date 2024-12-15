
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

board, moves = bundles(D)

grid = {}
for y,line in enumerate(board):
    for x, ch in enumerate(line):
        grid[(x*2)+1j*y] = ch
        grid[(x*2+1)+1j*y] = ch
        if ch == "@":
            grid[(x*2)+1j*y] = '@'
            grid[(x*2+1)+1j*y] = '.'
        if ch == "O":
            grid[(x*2)+1j*y] = '['
            grid[(x*2+1)+1j*y] = ']'

p = [p for p, c in grid.items() if c == "@"][0]

for m in "".join(moves):
    move = {'<':-1, '>':1, '^':-1j, 'v':1j}[m]

    if grid[p+move] == "#":
        continue
    elif grid[p+move] == ".":
        grid[p] = "."
        grid[p+move] = "@"
        p += move
    elif grid[p+move] in ['[', ']'] and move in [1, -1]:
        pgrid = grid.copy()
        can_move = False
        collect = []
        q = p + move
        while q in grid and (grid[q] == "[" or grid[q] == "]"):
            collect.append((q, q+move))
            q += move
        if q in grid and grid[q] == ".":
            can_move = True
        if can_move:
            prev = '@'
            for c,new_c in collect:
                grid[new_c] = pgrid[c]
            grid[p] = "."
            grid[p+move] = "@"
            p += move
    elif grid[p+move] in ['[', ']'] and move in [1j, -1j]:
        pgrid = grid.copy()
        can_move = True
        collect = []
        Q, visited = deque([p+move]), set()
        while Q:
            o = Q.popleft()
            if o in visited:
                continue
            visited.add(o)
            if pgrid[o] == "[":
                collect.append((o, o+move))
                collect.append((o+1, o+1+move))
                if pgrid[o+move] == "#" or pgrid[o+1+move] == "#":
                    can_move = False
                    break
                Q.append(o+move)
                Q.append(o+1+move)
            elif pgrid[o] == "]":
                collect.append((o, o+move))
                collect.append((o-1, o-1+move))
                if pgrid[o+move] == "#" or pgrid[o-1+move] == "#":
                    can_move = False
                    break
                Q.append(o+move)
                Q.append(o-1+move)
        if can_move:
            for c, new_c in reversed(collect):
                grid[new_c] = pgrid[c]
                grid[c] = '.'
            grid[p] = "."
            grid[p+move] = "@"
            p += move

tot = sum(p.real+100*p.imag for p in grid if grid[p] == '[')
print(int(tot))
