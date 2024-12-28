
from utils import *
from tqdm import tqdm

D = [i.strip() for i in open("input","r").readlines()]
p1, p2 = 0,0

start, end = None, None
grid = {}
for y, line in enumerate(D):
    for x, c in enumerate(line):
        if c == "S":
            start = (x,y,0, [])
        elif c == "E":
            end = (x,y,0,[])
        grid[(x,y)] = c

dist = {}

grid[(end[0], end[1])] = '.'
grid[(start[0], start[1])] = '.'


def bfs(start, end):
    global cheat_at
    Q, visited = deque([start]), {(start[0], start[1])}
    while Q:
        x,y,depth, path = Q.popleft()
        dist[(x,y)] = depth

        if (x,y) == (end[0],end[1]):
            return depth, path
        for dx,dy in DIR:
            if ((x+dx, y+dy) not in visited and (x+dx, y+dy) in grid) and grid[(x+dx,y+dy)] == '.':
                visited.add((x+dx,y+dy))
                Q.append((x+dx,y+dy,depth+1, path+[(x+dx,y+dy)]))
    return math.inf, []


baseline,_ = bfs(end, start)

for LL in [2, 20]:
    counts = defaultdict(int)
    best_cheats = defaultdict(int) # ((start),(end)): saves

    visited = set()
    def dfs(s, p, max_cheat):
        global visited
        d = LL - max_cheat
        if max_cheat == 0:
            if grid[p] == ".":
                saves = dist[s] - dist[p] - d
                best_cheats[(s,p)] = max(best_cheats[(s,p)], saves)
            return

        assert max_cheat > 0
        stop_now = dist[s] - dist[p] - d if grid[p] == "." else -math.inf
        best_cheats[(s,p)] = max(best_cheats[(s,p)], stop_now)
        x,y = p
        for dx,dy in DIR:
            q = (x+dx, y+dy)
            if q in grid and (q,d) not in visited:
                visited.add((q,d))
                dfs(s, q, max_cheat-1)

    for p, v in tqdm(grid.items()):
        ox,oy = p
        if v == '.':
            visited.clear()
            dfs(p, p, LL)
        
    for k,v in best_cheats.items():
        counts[v] += 1

    print(sum(v for k,v in counts.items() if k >= 100))
