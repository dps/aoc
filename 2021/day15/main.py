from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

import heapq

def a_star(graph, start, end, heuristic):
    """
    graph is a dict of vertex: [(weight, neighbor), ...] 
    heuristic is a function that takes in a vertex and returns an estimated cost
    to reach the end from that vertex
    returns (sum(path weights), path)
    """
    
    # Initialize data structures
    distances = defaultdict(lambda: math.inf)
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    queue = []
    heapq.heappush(queue, (0, 0, start))
    
    # Loop until the queue is empty
    while queue:
        _, current_distance, current_vertex = heapq.heappop(queue)
        
        # End search if we have reached the end
        if current_vertex == end:
            break
            
        # Update the distances and previous vertices of the neighbors
        for weight, neighbor in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                priority = distance + heuristic(neighbor, end)
                heapq.heappush(queue, (priority, distance, neighbor))
    
    # Build the path
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    
    return (distances[end], path[::-1])

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
    return(a_star(graph, start, end, lambda x,y:manhattan(x,y))[0])

assert(solve(1) == 398)
assert(solve(2) == 2817)