
from utils import *

D = [i.strip() for i in open("input", "r").readlines()]

p1, p2 = 0, 0

grid = {(x + 1j*y): c for y, row in enumerate(D) for x, c in enumerate(row)}
proc = grid.copy()

while len(proc) > 0:
    k,v = proc.popitem()

    queue, visited = deque([k]), set([k])
    sides = set()

    while queue:
        k = queue.popleft()
        
        for d in [1, -1, 1j, -1j]:
            if (k + d in grid and grid[k + d] != v) or (k + d not in grid):
                sides.add((str(d), k.real, k.imag))

            nk = k + d
            if nk in grid and nk not in visited and grid[nk] == v:
                queue.append(nk)
                visited.add(nk)

    for p in visited:
        if p in proc:
            del proc[p]

    p1 += len(visited) * len(sides)
    
    ms = defaultdict(list)
    for s in sides:
        ms[s[0]].append(s[1:])

    def count_direction(direction, sort_key):
        points = ms[str(direction)]
        points.sort(key=sort_key)
        count = 1
        prev = points[0]
        
        for curr in points[1:]:
            is_vertical = direction in [1j, -1j]
            coord_index = 1 if is_vertical else 0            
            if prev[coord_index] != curr[coord_index] or abs(prev[1-coord_index] - curr[1-coord_index]) != 1:
                count += 1
            prev = curr
        return count
    
    vertical_key = lambda x: x[1]*1000000 + x[0]
    horizontal_key = lambda x: x[0]*1000000 + x[1]
    
    side_count = sum([
        count_direction(1, horizontal_key),
        count_direction(-1, horizontal_key),
        count_direction(1j, vertical_key),
        count_direction(-1j, vertical_key)
    ])
        
    p2 += len(visited) * side_count

print(p1, p2)
