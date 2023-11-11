from utils import *
import string

grid = [i.strip() for i in open("input","r").readlines()]
keys = {}
doors = {}

best = math.inf

# Idea for how to go faster:
# Use bfs / floyd w to make a list of min distances between every key pair (and doors you need to be able to go through)
# DFS key-wise for all possible key paths without doing the bfs every time

@cache
def reachable_keys(pos, collected_keys):
    def reachable_key_neighbors(p):
        for dx,dy in DIR:
            ch = grid[p[1]+dy][p[0]+dx]
            if ch == '.' or ch in string.ascii_lowercase or (ch in string.ascii_uppercase and ch.lower() in collected_keys):
                yield (p[0]+dx, p[1]+dy)

    reachable_keys = []
    q, visited = deque([(pos,0)]), set()
    while len(q):
        tr,ll = q.popleft()
        visited.add(tr)
        for n in reachable_key_neighbors(tr):
            if n in visited:
                continue
            ch = grid[n[1]][n[0]]
            if ch not in collected_keys and ch in string.ascii_lowercase:
                reachable_keys.append((ch, (n[0],n[1]), ll+1))
            q.append(((n[0],n[1]), ll+1))
    return reachable_keys
    
@cache
def dfs(pos, remaining_keys, collected_keys, pl):
    global best
    #print("dfs", pos, remaining_keys, collected_keys, pl)
    if len(remaining_keys) == 0:
        best = min(pl, best)
        print(pl, best)
        return pl
    if pl > best:
        return math.inf
    min_dist = math.inf

    for nk,pos,apl in reachable_keys(pos, collected_keys):
        atmpt = dfs(keys[nk], frozenset(set(remaining_keys) - {nk}), frozenset(set(collected_keys) | {nk}), pl + apl)
        min_dist = min(atmpt, min_dist)
    return min_dist

@cache
def reachable_keys2(poses, collected_keys):
    def reachable_key_neighbors2(p):
        for dx,dy in DIR:
            ch = grid[p[1]+dy][p[0]+dx]
            if ch == '.' or ch in string.ascii_lowercase or (ch in string.ascii_uppercase and ch.lower() in collected_keys):
                yield (p[0]+dx, p[1]+dy)

    reachable_keys = []
    for i, pos in enumerate(poses):
        q, visited = deque([(pos,0)]), set()
        while len(q):
            tr,ll = q.popleft()
            visited.add(tr)
            for n in reachable_key_neighbors2(tr):
                if n in visited:
                    continue
                ch = grid[n[1]][n[0]]
                if ch not in collected_keys and ch in string.ascii_lowercase:
                    reachable_keys.append((ch, (n[0],n[1]), ll+1, i))
                q.append(((n[0],n[1]), ll+1))
    return reachable_keys

@cache
def dfs2(poses, remaining_keys, collected_keys, pl):
    global best
    #print("dfs2", pos, remaining_keys, collected_keys, pl)
    if len(remaining_keys) == 0:
        best = min(pl, best)
        print(pl, best)
        return pl
    if pl > best:
        return math.inf
    min_dist = math.inf

    for nk,pos,apl,i in reachable_keys2(poses, collected_keys):
        nposes = tuple(poses[j] if j !=i else pos for j in range(4))
        atmpt = dfs2(nposes, frozenset(set(remaining_keys) - {nk}), frozenset(set(collected_keys) | {nk}), pl + apl)
        min_dist = min(atmpt, min_dist)
    return min_dist

def part1():
    print(grid)
    pos = None
    for y,row in enumerate(grid):
        for x,ch in enumerate(row):
            if ch in string.ascii_lowercase:
                keys[ch] = (x,y)
            if ch in string.ascii_uppercase:
                doors[ch] = (x,y)
            if ch == '@':
                pos = (x,y)
                grid[y] = grid[y].replace("@", ".")

    remaining_keys = frozenset(keys.keys())
    collected_keys = frozenset()
    print(dfs(pos, remaining_keys, collected_keys, 0))

def part2():
    global grid
    # I wrote the extra # squares in manually
    grid = [i.strip() for i in open("input2","r").readlines()]
    print(grid)
    pos = None
    for y,row in enumerate(grid):
        for x,ch in enumerate(row):
            if ch in string.ascii_lowercase:
                keys[ch] = (x,y)
            if ch in string.ascii_uppercase:
                doors[ch] = (x,y)
            if ch == '@':
                pos = ((x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1, y+1))
                grid[y] = grid[y].replace("@", "#")

    remaining_keys = frozenset(keys.keys())
    collected_keys = frozenset()
    print(dfs2(pos, remaining_keys, collected_keys, 0))

part2() #took 14m8s
