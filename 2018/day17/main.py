
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

clay = set()

def ranges(s, coord):
    return list(map(int, re.findall(coord + r"=[0-9.]*", s)[0].split("=")[1].split("..")))

for line in D:
    xr, yr = ranges(line, "x"), ranges(line, "y")
    for x in range(xr[0],xr[-1]+1):
        for y in range(yr[0],yr[-1]+1):
            clay.add((x,y))

mix = int(min([k[0] for k in clay]))
miy = int(min([k[1] for k in clay]))
mx = int(max([k[0] for k in clay]))
my = int(max([k[1] for k in clay]))

spring = (500, 0)

settled = set()
visited = set()

def can_settle(p,dx):
    i = 0
    while True:
        i += 1
        if (p[0]+i*dx,p[1]) in clay:
            return True
        if ((p[0]+i*dx,p[1]+1) not in clay) and ((p[0]+i*dx,p[1]+1) not in settled):
            return False

prev_settled, prev_visited = 0,0
while True:
    p = spring
    Q,local_visited = deque([p]),set()
    while Q:
        p = Q.popleft()
        if p[1] >= miy and p[1] <= my:
            visited.add(p)
        if p[1] > my:
            continue

        local_visited.add(p)

        # First, always try to move down
        q = (p[0], p[1]+1)
        if q not in settled and q not in clay:
            Q.append(q)
            continue

        # We couldn't go down, so try to go left, then right in that order
        for dx in [-1, 1]:
            q = (p[0]+dx, p[1])
            if q in local_visited:
                continue
            if q in clay or q in settled:
                if can_settle(p,-dx):
                    settled.add(p)
                continue
            Q.append(q)

    if prev_settled == len(settled) and prev_visited == len(visited):
        break
    prev_settled = len(settled)
    prev_visited = len(visited)

vs = list(visited)
vs.sort()
for p in vs:
    if (p[0]-1,p[1]) in settled:
        i = 1
        q = (p[0]+i,p[1])
        while q in visited and q not in settled:
            i += 1
            q = (p[0]+i,p[1])
        if q in settled:
            settled.add(p)

print(len(settled | visited))
print(len(settled))
