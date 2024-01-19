
from utils import *


# Find the fuel cell's rack ID, which is its X coordinate plus 10.
# Begin with a power level of the rack ID times the Y coordinate.
# Increase the power level by the value of the grid serial number (your puzzle input).
# Set the power level to itself multiplied by the rack ID.
# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
# Subtract 5 from the power level.

grid_serial = 7347

grid = [0] * (301*301)
for y in range(1, 301):
    for x in range(1, 301):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += grid_serial
        power_level *= rack_id
        power_level = (power_level // 100) % 10
        power_level -= 5
        grid[y*300+x] = power_level

mp = -math.inf
mpx,mpy,mps = None,None,None

DP = {}

def get_power(x,y,size):
    if (x,y,size) in DP:
        return DP[(x,y,size)]
    if size == 1:
        DP[(x,y,size)] = grid[y*300+x]
        return DP[(x,y,size)]
    init = get_power(x,y,size-1)
    for dy in range(size):
        init += grid[(y+dy)*300+(x+size-1)]
    for dx in range(size-1):
        init += grid[(y+size-1)*300+(x+dx)]
    DP[(x,y,size)] = init
    return init

for size in range(1,300,1):
    for y in range(1,301-size):
        for x in range(1,301-size):
            s = get_power(x,y,size)
            if s > mp:
                mp = s
                mpx,mpy,mps = x,y,size

print(f"{mpx},{mpy},{mps}")