from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                #dist[next] = [dist[at], next]
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist.get(end)

def delta(here, there):
    return (ord(there if there not in "SE" else {"S":"a","E":"z"}[there])
            -
            ord(here if here not in "SE" else {"S":"a","E":"z"}[here]))

def can_walk(r,c,ch):
    ret = []
    for _,i in DIR.items():
        if r + i[1] < len(input) and r + i[1] >= 0 and c + i[0] < len(input[0]) and c + i[0] >= 0:
            if delta(ch, input[r+i[1]][c + i[0]]) <= 1:
                ret.append((r + i[1], c + i[0]))
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
    print(min(len(x) - 1 for x in [v for v in [find_shortest_path(graph, a, end) for a in ayes] if v is not None]))


if __name__ == '__main__':
    solve()
