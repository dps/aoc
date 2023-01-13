from utils import *
from itertools import *

scanners = []

def fingerprints_two(num):
    global scanners
    scanner = scanners[num]
    fps = set()
    for c in itertools.combinations(scanner, 2):
        fps.add(manhattan3(c[0], c[1]))
    return fps

@cache
def align(b, cnum):
    base = scanners[b]
    c = scanners[cnum]
    signs = [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
    rots = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

    for axis in rots:
        for sign in signs:
            cc = [(sign[0] * p[axis[0]], sign[1] * p[axis[1]], sign[2] * p[axis[2]]) for p in c]

            for o in base:
                for p in cc:
                    # guess that o and p are the same point
                    xlat = (p[0]-o[0], p[1]- o[1], p[2] - o[2])
                    translated = {(q[0]-xlat[0], q[1]-xlat[1], q[2]-xlat[2]) for q in cc}
                    if len(base & translated) >= 12:
                        return translated, xlat
    return None, None

def solve():
    data = open("input.txt","r").read().split("\n\n")
    for scanner in data:
        lines = scanner.split("\n")
        s = set()
        for l in lines[1:]:
            s.add(tuple(ints(l)))
        scanners.append(s)

    pairs = list(itertools.combinations(range(len(scanners)), 2))
    
    graph = defaultdict(lambda : [])
    for pair in pairs:
        lfp = fingerprints_two(pair[0])
        rfp = fingerprints_two(pair[1])
        isect = lfp.intersection(rfp)
        if len(isect) >= 66:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])


    world = set()
    next = [ 0 ]
    aligned = set()
    locs = set()
    while len(next):
        t = next.pop()
        to_align = graph[t]
        for process in to_align:
            if process in aligned: continue
            translated, scanner_loc = align(t, process)
            assert(translated != None)
            locs.add(scanner_loc)
            world.update(translated)
            scanners[process] = translated #scanners[process] data is now in scanner[0] space
            next.append(process)
            aligned.add(process)

    print("Part 1 answer:", len(world))
    max_d = 0
    for a in locs:
        for b in locs:
            max_d = max(max_d, manhattan3(a,b))
    print("Part 2 answer:", max_d)

solve()