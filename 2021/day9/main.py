from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    score = 0
    g = grid_from_strs(input)
    for y in range(g.height()):
        for x in range(g.width()):
            g.set_cursor(x,y)
            v = int(g.get())
            is_low_point = True
            for _,d in DIR.items():
                if g.could_move(d[0], d[1]):
                    if int(g.peek_move(d[0], d[1])) <= v:
                        is_low_point = False
            if is_low_point:
                score += (v + 1)
    print(score)
    return score

def find_basins(g, lps):
    basins = []
    for lp in lps:
        q = deque([lp])
        basin_size = -1
        checked = set((lp[0], lp[1]))
        while len(q) > 0:
            p = q.popleft()
            g.set_cursor(p[0], p[1])
            if int(g.get()) < 9:
                basin_size += 1
                for _,d in DIR.items():
                    if g.could_move(d[0], d[1]) and (p[0]+d[0], p[1]+d[1]) not in checked:
                        q.append((p[0]+d[0], p[1]+d[1]))
                        checked.add((p[0]+d[0], p[1]+d[1]))
        basins.append(basin_size)
    return sorted(basins, reverse=True)



def part2():
    score = 0
    g = grid_from_strs(input)
    lps = []
    for y in range(g.height()):
        for x in range(g.width()):
            g.set_cursor(x,y)
            v = int(g.get())
            is_low_point = True
            for _,d in DIR.items():
                if g.could_move(d[0], d[1]):
                    if int(g.peek_move(d[0], d[1])) <= v:
                        is_low_point = False
            if is_low_point:
                lps.append((x,y))
    basins = find_basins(g, lps)
    print(basins)
    print(reduce(lambda x,y:x*y, basins[0:3],1))
    return score


if __name__ == '__main__':
    #assert(part1() == 526)
    part2()
