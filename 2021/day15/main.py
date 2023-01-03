from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve(part=1):
    grid, dim, _ = grid_ints_from_strs(input)
    ldim = dim*5 if part == 2 else dim
    def grid_at(x, y):
        return (((grid[y % dim][x % dim]-1) + x//dim + y//dim) % 9) + 1
    graph = {}
    for y in range(ldim):
        for x in range(ldim):
            p = (x, y)
            graph[p] = [(grid_at(q[0], q[1]), q) for q in grid_neighbors(p, ldim)]
    start = (0,0)
    end = (ldim-1, ldim-1)
    return(dijkstra(graph, start, end)[0])

assert(solve(1) == 398)
assert(solve(2) == 2817)