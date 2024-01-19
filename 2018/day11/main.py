
from utils import *

grid_serial = 7347

# https://en.wikipedia.org/wiki/Summed-area_table
grid = [0] * (301*301)
for y in range(1, 301):
    for x in range(1, 301):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += grid_serial
        power_level *= rack_id
        power_level = (power_level // 100) % 10
        power_level -= 5
        grid[y*300+x] = power_level + grid[y*300+x-1] + grid[(y-1)*300+x] - grid[(y-1)*300+x-1]

mp = -math.inf
mpx,mpy,mps = None,None,None

def get_power(x,y,size):
    # A---B
    # |   |
    # C---D
    # Sum = I(D)+I(A)-I(B)-I(C)
    a,b,c,d = grid[y*300+x],grid[y*300+x+size],grid[(y+size)*300+x],grid[(y+size)*300+x+size]
    return d+a-b-c

mp = -math.inf
mpx,mpy,mps = None,None,None

for size in range(1,300):
    for y in range(1,301-size):
        for x in range(1,301-size):
            s = get_power(x,y,size)
            if s > mp:
                mp = s
                mpx,mpy,mps = x+1,y+1,size
    if size == 3:
        print(f"Part 1: {mpx},{mpy}\t\t[{mp}]")        

print(f"Part 2: {mpx},{mpy},{mps}\t[{mp}]")