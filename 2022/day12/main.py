from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def delt(here, there):
    if there == 'S':
        return ord("a") - ord(here)
    if there == 'E':
        return ord("z") - ord(here)
    if here == 'S':
        return ord(there) - ord("a")
    if here == 'E':
        return ord(there) - ord("z")

    return ord(there) - ord(here)

def can_walk(r,c,ch):
    ret = []
    for _,i in DIR.items():
        if r + i[1] < len(input) and r + i[1] >= 0 and c + i[0] < len(input[0]) and c + i[0] >= 0:
            if delt(ch, input[r+i[1]][c + i[0]]) <= 1:
                ret.append((r+i[1], c+i[0]))
    return ret

def solve():
    graph = {}
    ayes = []
    start, end = None, None
    for r, row in enumerate(input):
        for c, ch in enumerate(row):
            key = (r, c)
            graph[key] = can_walk(r,c,ch)
            if ch == 'S':
                start = key
                ayes.append(key)
            if ch == 'E':
                end = key
            if ch == 'a':
                ayes.append(key)

    print(len(find_shortest_path(graph, start, end)) - 1)

    min_path = 9999999
    for a in ayes:
        path = find_shortest_path(graph, a, end)
        if path:
            t = len(path) - 1
            if t < min_path:
                min_path = t
    print(min_path)

if __name__ == '__main__':
    solve()
