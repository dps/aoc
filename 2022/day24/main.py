from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

blizzards = deque([])
max_x, max_y = 0,0

def wrap(p):
    q = p
    if p.real > max_x:
        q = 0 + q.imag * 1j
    if p.real < 0:
        q = max_x + q.imag * 1j
    if p.imag > max_y:
        q = q.real
    if p.imag < 0:
        q = q.real + 1j*max_y
    return q

MV = {'<': -1, '>': 1, '^': -1j, 'v': 1j, '$': 0}

@cache
def blizzards_at(mins):
    if mins == 0:
        return blizzards
    prev = blizzards_at(mins - 1)
    this_min = deque([])
    for blizzard in prev:
        mv = MV[blizzard[0]]
        this_min.append((blizzard[0], wrap(blizzard[1] + mv)))
    return this_min

def bfs(pos, goal):
    q = deque([(pos, 0)])
    visited = set()
    while len(q) > 0:
        p = q.popleft()
        blizz = blizzards_at(p[1] + 1)
        for move in MV.values():
            next = p[0] + move
            if next == goal:
                return p[1] + 1
            if next != pos and (next.real < 0 or next.real > max_x or next.imag < 0 or next.imag > max_y):
                continue
            if not any([b[1] == next for b in blizz]):
                if (next, p[1] + 1) not in visited:
                    q.append((next, p[1] + 1))
                    visited.add((next, p[1] + 1))
    return sys.maxsize

def solve():
    global max_x, max_y, blizzards, global_min
    # Ignore the sides
    for y,row in enumerate(input):
        for x, ch in enumerate(row):
            if ch in "<>^v":
                blizzards.append((ch, (x-1)+(y-1)*1j))
    max_x = len(input[0]) - 3
    max_y = len(input) - 3

    pos = (0-1j)
    goal = max_x+(max_y+1)*1j

    initial_crossing = bfs(pos, goal)
    print("Part 1 answer:", initial_crossing, "mins")

    blizzards = blizzards_at(initial_crossing)
    blizzards_at.cache_clear()

    return_journey = bfs(goal, pos)

    blizzards = blizzards_at(return_journey)
    blizzards_at.cache_clear()

    back_again = bfs(pos, goal)
    print(back_again)
    print("Part 2 answer:", initial_crossing + return_journey + back_again, "mins")

if __name__ == '__main__':
    # Runtime: DFS 54.58s -> 40.86s [added manhattan stop] -> 18.09s [BFS]
    # input is 122x26
    solve()