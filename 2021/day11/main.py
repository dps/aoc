from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve(part=1):
    grid = grid_ints_from_strs(input).g()
    width = len(grid)

    flashes = 0
    iter = 0
    for _ in range(100 if part == 1 else 1000):
        iter += 1
        q = deque()
        flashed = set()

        for r in range(width):
            for c in range(width):
                grid[r][c] += 1
                if (grid[r][c] > 9):
                    q.append((r,c))
                    flashed.add((r,c))
        while len(q) > 0:
            octo = q.popleft()
            r,c = octo
            flashes += 1
            for pos in DIR8.values():
                rr,cc = (r+pos[0], c+pos[1])
                if (rr,cc) in flashed:
                    continue
                if rr < 0 or rr >= width or cc < 0 or cc >= width:
                    continue
                grid[rr][cc] += 1
                if grid[rr][cc] > 9:
                    q.append((rr,cc))
                    flashed.add((rr,cc))
        for (r,c) in flashed:
            grid[r][c] = 0
        if part==2 and len(flashed) == width*width:
            return(iter)
    return(flashes)

assert(solve(part=1) == 1634)
assert(solve(part=2) == 210)