from utils import *
from functools import cmp_to_key

scanners = []

def manhattan12space(p, q):
    return abs(p[0]*12 - q[0]) + abs(p[1]*12 - q[1]) + abs(p[2]*12 - q[2])

def fingerprints(num):
    global scanners
    scanner = scanners[num]
    fps = set()
    points = []
    for c in itertools.combinations(scanner, 12):
        centroid = [e for e in reduce(lambda a,b: (a[0]+b[0],a[1]+b[1],a[2]+b[2]), c)]
        dists = sorted([manhattan12space(p,centroid) for p in c])
        fps.add(tuple(dists))
        points.append((tuple(dists), c))
    return fps, points

def merge_points_into_left_coord_space(pair, lpoints, rpoints, scanners_in_r):
    # {l,r}points contains the points in the overlap set in {l,r} space

    centroid_r = [e for e in reduce(lambda a,b: (a[0]+b[0],a[1]+b[1],a[2]+b[2]), rpoints)]
    centroid_l = [e for e in reduce(lambda a,b: (a[0]+b[0],a[1]+b[1],a[2]+b[2]), lpoints)]

    # Pair up the points in left and right so that their manhattan distances from centroid match
    # These are the same points in different coordinate spaces!
    merged = [(pair[0][1], pair[1][1]) for pair in
        zip(
            sorted([(manhattan12space(p, centroid_l), p) for p in lpoints]),
            sorted([(manhattan12space(p, centroid_r), p) for p in rpoints])
            )
        ]
    mapper = []

    # sort by lspace x increasing, then y increasing, then z increasing
    # as we iterate the resulting list there will be one axis that is monotonic, find it and
    # figure out its direction.
    for xyz in [0,1,2]:
        dir = [None, None, None]
        prev = None
        p = set([0,1,2])
        for _, r in sorted(merged, key=cmp_to_key(lambda a,b: a[0][xyz] - b[0][xyz])):
            if prev == None:
                prev = list(r)
            elif dir[0] == None:
                dir = sign(r[0]-prev[0]), sign(r[1]-prev[1]), sign(r[2]-prev[2])
            else:
                if sign(r[0]-prev[0]) != 0 and sign(r[0]-prev[0]) != dir[0]:
                    if 0 in p : p.remove(0)
                if sign(r[1]-prev[1]) != 0 and sign(r[1]-prev[1]) != dir[1]:
                    if 1 in p : p.remove(1)
                if sign(r[2]-prev[2]) != 0 and sign(r[2]-prev[2]) != dir[2]:
                    if 2 in p : p.remove(2)
            prev = list(r)

        axis = p.pop()
        mapper.append((axis, dir[axis]))

    l_point, r_point = merged[0]
    r_point_xf = []
    for ax in mapper:
        r_point_xf.append(r_point[ax[0]] * ax[1])
    # r_in_l is the scanner position of the right scanner in left co-ord space.
    r_in_l = (l_point[0]-r_point_xf[0], l_point[1]-r_point_xf[1], l_point[2]-r_point_xf[2])

    def r_to_l(t_point):
        p=[]
        for i, ax in enumerate(mapper):
            p.append(t_point[ax[0]] * ax[1] + r_in_l[i])
        return(tuple(p))

    l_points = set(scanners[pair[0]])
    r_points = scanners[pair[1]]

    for point in r_points:
        l_points.add(r_to_l(point))

    scanners_in_l = [(0,0,0), r_in_l] + [r_to_l(s) for s in scanners_in_r]
    return l_points, scanners_in_l


def solve(do_fingerprinting=False):
    global scanners, sinter
    total = 0
    data = open("input.txt","r").read().split("\n\n")
    for scanner in data:
        lines = scanner.split("\n")
        s = set()
        for l in lines[1:]:
            s.add(tuple(ints(l)))
        scanners.append(s)
        total += len(s)

    if do_fingerprinting:
        nums = range(len(scanners))
        pairs = list(itertools.combinations(nums, 2))
        
        result = []
        for i, pair in enumerate(pairs):
            print(i, "of", len(pairs))
            lfp, lps = fingerprints(pair[0])
            rfp, rps = fingerprints(pair[1])
            isect = lfp.intersection(rfp)
            if len(isect) > 0:
                for k, isect_fingerprint in enumerate(isect):
                    found = [pair]
                    print("Scanners", pair, "overlap ", k)
                    for lp in lps:
                        if lp[0] == isect_fingerprint:
                            found.append(lp[1])
                            break
                    for rp in rps:
                        if rp[0] == isect_fingerprint:
                            found.append(rp[1])
                            break
                    result.append(found)
        sinter = result
    else:
        import precomputed
        sinter = precomputed.sinter

    graph = defaultdict(lambda : [])
    for l,r in [x[0] for x in sinter]:
        graph[r].append((1,l))
        graph[l].append((1,r))

    paths = []
    for a in range(1, 38):
        paths.append(dijkstra(graph, a,0))
    paths = sorted(paths, reverse=True)

    all_scanners = set()

    sintermap = {s[0]:(s[1],s[2]) for s in sinter}
    sintermap.update({(s[0][1],s[0][0]):(s[2],s[1]) for s in sinter})
    for path in paths:
        scanners_in_r = []
        for l,r in zip(path[1][1:], path[1]):
            merged, scanners_in_r = merge_points_into_left_coord_space((l,r), sintermap[(l,r)][0], sintermap[(l,r)][1], scanners_in_r)
            scanners[l] = merged
        all_scanners.update(scanners_in_r)

    print("Part 1 answer:", len(scanners[0]))
    max_d = 0
    for a in all_scanners:
        for b in all_scanners:
            max_d = max(max_d, manhattan3(a,b))
    print("Part 2 answer:", max_d)
        

solve()