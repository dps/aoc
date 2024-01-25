from collections import defaultdict, deque

D = (ch for ch in open("input","r").read())
NSEW = {'N': -1j, 'S': 1j, 'E': 1, 'W': -1}
REV = {'N':'S','S':'N','E':'W','W':'E'}

world = defaultdict(lambda : set())

def traverse(p):
    global D, world
    pos = p
    while True:
        ch = next(D)
        if ch in NSEW:
            world[pos].add(ch)
            pos += NSEW[ch]
            world[pos].add(REV[ch])
        elif ch == '|':
            pos = p
        elif ch == '(':
            traverse(pos)
        elif ch == ')' or ch == '$':
            return

traverse(0)

Q, visited, all = deque([(0,0)]),set([0]),{}
while Q:
    p,l = Q.popleft()
    all[p] = l
    for door in world[p]:
        d = NSEW[door]
        np = p + d
        if np not in visited:
            visited.add(np)
            Q.append((np, l+1))

print(max(all.values()), len([v for v in all.values() if v >= 1000]))