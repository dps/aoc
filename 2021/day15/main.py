from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    grid = grid_ints_from_strs(input).g()
    graph = {}
    dim = len(grid[0])
    for y in range(dim):
        for x in range(dim):
            p = (x, y)
            neighbors = []
            for d in DIR.values():
                q = (p[0]+d[0], p[1]+d[1])
                if q[0] < 0 or q[1] < 0 or q[0] >= dim or q[1] >= dim:
                    continue
                neighbors.append((grid[q[1]][q[0]], q))
            graph[p] = neighbors
    start = (0,0)
    end = (dim-1, dim-1)
    return(dijkstra(graph, start, end)[0])

def part2():
    grid = grid_ints_from_strs(input).g()
    dim = len(grid[0])
    def grid_at(x, y):
        return (((grid[y % dim][x % dim]-1) + x//dim + y//dim) % 9) + 1
    graph = {}
    for y in range(dim*5):
        for x in range(dim*5):
            p = (x, y)
            neighbors = []
            for d in DIR.values():
                q = (p[0]+d[0], p[1]+d[1])
                if q[0] < 0 or q[1] < 0 or q[0] >= dim*5 or q[1] >= dim*5:
                    continue
                neighbors.append((grid_at(q[0], q[1]), q))
            graph[p] = neighbors
    start = (0,0)
    end = ((dim*5)-1, (dim*5)-1)
    return(dijkstra(graph, start, end)[0])

assert(part1() == 398)
assert(part2() == 2817)