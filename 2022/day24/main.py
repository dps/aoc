from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

blizzards = deque([])
return_blizzards = None
max_x, max_y = 0,0
global_min = 1000 #sys.maxsize

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

@cache
def dfs(pos, goal, mins_elapsed):
    global global_min
    if mins_elapsed > global_min:
        return sys.maxsize
    blizz = blizzards_at(mins_elapsed + 1)
    best = sys.maxsize
    for move in MV.values():
        next = pos + move
        if next == goal:
            if (mins_elapsed + 1) < global_min:
                global_min = mins_elapsed + 1
            return mins_elapsed + 1
        if next.real < 0 or next.real > max_x or next.imag < 0 or next.imag > max_y:
            continue
        if not any([b[1] == next for b in blizz]):
            best = min(best, dfs(next, goal, mins_elapsed + 1))
    return best


    

def solve():
    global max_x, max_y, blizzards
    # Ignore the sides
    for y,row in enumerate(input):
        for x, ch in enumerate(row):
            if ch in "<>^v":
                blizzards.append((ch, (x-1)+(y-1)*1j))
    max_x = len(input[0]) - 3
    max_y = len(input) - 3

    pos = (0-1j)
    goal = max_x+(max_y+1)*1j

    blizzards = blizzards_at(518)
    blizzards_at.cache_clear()

    # goal = (0-1j)
    # pos = max_x+(max_y+1)*1j

    # for r in range(10):
    #     blizz = blizzards_at(r)
    #     for y in range(max_y + 1):
    #         for x in range(max_x + 1):
    #             bz = [b for b in blizz if b[1] == x+y*1j]
    #             if len(bz) > 1:
    #                 print(str(len(bz))[0], end="")
    #             elif len(bz) == 1:
    #                 print(bz[0][0], end="")
    #             else:
    #                 print(".", end="")
    #         print()
    #     print()

    print("dfs", dfs(pos, goal, 1))
    # print("dfs", dfs(pos, goal, 2))

    # 255 mins to get from pos -> goal
    # back again 263 #518
    # 

    # Return blizz = 

    score = 0
    print(score)
    return score

if __name__ == '__main__':
    # input is 122x26
    solve()