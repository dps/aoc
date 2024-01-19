
from utils import *

D = open("input","r").readlines()

w = len(D[0])
grid = "".join(D)

carts = []

for i,ch in enumerate(grid):
    if ch == "^": carts.append((i,-w,0,i))
    if ch == ">": carts.append((i,1,0,i))
    if ch == "v": carts.append((i,w,0,i))
    if ch == "<": carts.append((i,-1,0,i))

TURN_CORNER = {-w:1, -1:w, w:-1, 1:-w}
TURN_LEFT = {-w: -1, 1: -w, -1: w, w: 1}
TURN_RIGHT= {-1: -w, -w: 1, 1: w, w: -1}
seen_first_collision = False
while carts:
    carts.sort()
    new_carts = []
    to_delete = set()
    for n, cart in enumerate(carts):
        pos,dir,turn_clock,name = cart
        new_pos = pos + dir
        new_dir = dir
        if grid[new_pos] == "/":
            new_dir = TURN_CORNER[dir]
        elif grid[new_pos] == "\\":
            new_dir = -TURN_CORNER[dir]
        elif grid[new_pos] == "+":
            if turn_clock == 0:
                new_dir = TURN_LEFT[dir]
            elif turn_clock == 2:
                new_dir = TURN_RIGHT[dir]
            else:
                new_dir = dir
            turn_clock = (turn_clock + 1) % 3

        # Compute collisions with carts not yet moved on this tick.
        for k in range(n+1, len(carts)):
            if carts[k][0] == new_pos:
                to_delete.add(name)
                to_delete.add(carts[k][3])
        new_carts.append((new_pos, new_dir, turn_clock, name))
    carts = new_carts[:]

    # Compute collisions with carts collided on this tick before they move on.
    for a,b in combinations(carts, 2):
        if a[0] == b[0]:
            to_delete.add(a[3])
            to_delete.add(b[3])

    if len(to_delete) > 0:
        if not seen_first_collision:
            collided = [c for c in carts if c[3] in to_delete]
            print(f"Part 1: {collided[0][0] % w},{collided[0][0] // w}")
            seen_first_collision = True
        carts = [c for c in carts if c[3] not in to_delete]
            
    if len(carts) == 1:
        print(f"Part 2: {carts[0][0] % w},{carts[0][0] // w}")
        break
