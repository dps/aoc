
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

# Step P must be finished before step F can begin.

def ntoposort(leaves, graph, nworkers=4):
    res = []
    s = leaves
    time = 0
    workers = [(0, '.')] * nworkers
    while len(s) > 0 or any([w[0] > 0 for w in workers]):
        # any work? any available workers?
        while len(s) > 0 and any([w[0] == 0 for w in workers]):
            for i, w in enumerate(workers):
                if w[0] == 0:
                    n = sorted(list(s))[0]
                    s.remove(n)
                    workers[i] = (60 + (ord(n) - ord('A') + 1), n)
                    break

        # advance time
        completed = set()
        next_workers = [None] * nworkers
        for i, w in enumerate(workers):
            if w[0] == 0:
                next_workers[i] = w
            if w[0] == 1:
                completed.add(w[1])
                next_workers[i] = (0, '.')
            elif w[0] > 1:
                next_workers[i] = (w[0] - 1, w[1])
        workers = next_workers
        time += 1

        for n in completed:
            res.append(n)
            for dep_k, dep_v in [(k, v) for k, v in graph.items() if n in v]:
                dep_v.remove(n)
                if len(dep_v) == 0:
                    s.add(dep_k)      

    return time, "".join(res)

def solve():
    lefts = set()
    rights = set()
    order = defaultdict(list)
    for line in input:
        l,r = line.split(" must be")[0][-1], line.split(" can begin")[0][-1]
        lefts.add(l)
        rights.add(r)
        order[r].append(l)

    # Part 1
    aoc(ntoposort(lefts - rights, deepcopy(order), 1)[1])
    # Part 2
    aoc(ntoposort(lefts - rights, order)[0])

solve()
