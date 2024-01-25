from collections import defaultdict, deque

D = open("input","r").read()
G = (ch for ch in D)


world = defaultdict(lambda : set())

NSEW = {'N': (0,-1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
REV = {'N':'S','S':'N','E':'W','W':'E'}

def traverse(p):
    global G, world
    ch = None
    pos = p
    while ch != '$':
        ch = next(G)
        if ch in 'NSEW':
            d = NSEW[ch]
            np = (pos[0]+d[0], pos[1]+d[1])
            world[pos].add(ch)
            world[np].add(REV[ch])
            pos = np
        elif ch == '|':
            pos = p
        elif ch == '(':
            traverse(pos)
        elif ch == ')':
            return

traverse((0,0))

ml = 0
p2count = 0
Q, visited = deque([((0,0),0)]),set([0,0])
while Q:
    p,l = Q.popleft()
    if l >= 1000:
        p2count += 1
    if l > ml:
        ml = l
    for d in world[p]:
        dir = NSEW[d]
        np = (p[0] + dir[0], p[1] + dir[1])
        if np not in visited:
            visited.add(np)
            Q.append((np, l+1))

print(ml, p2count)