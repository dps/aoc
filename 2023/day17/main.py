# With thanks to azzal07, who adapted my previous bucket queue solution to massively improve
# runtime. By:
# - Translating the grid into 1D coordinates (and making neighbors match with faster
#   math). It's very clever how (+/-) next_d = w//d gives the cw and ccw turns!
# - inlining a fixed size bucket queue inside the dijkstra impl.
# - using a fixed list for dijkstra mins instead of a dict.
# - unrolling neighbors in the hot loop
D = [i.strip() for i in open("input", "r").readlines()]

g = [int(ch) for row in D for ch in row]
h = len(D)
w = len(D[0])
end = len(g) - 1
MAX_SIZE = w * h * 9


def dynamic_dijkstra(minimum, maximum, end):
    seen, mins = set(), [[MAX_SIZE] * (w + 2) for _ in range(w * h)]
    bh = [[] for _ in range(MAX_SIZE)]
    for state in (0, 1), (0, w):
        for c, (yx, d) in neighbors(state, minimum, maximum):
            mins[yx][d] = c
            bh[c].append((yx, d))
    for cost, vs in enumerate(bh):
        for v in vs:
            if v in seen:
                continue

            if v[0] == end:
                return cost

            seen.add(v)

            yx, d = v
            next_d = w//d
            next_cost = cost
            for l in range(1, maximum):
                yx += d
                if yx < 0 or end < yx or (d == 1 and yx % w == 0) or (d == -1 and yx % w == (w-1)):
                    break

                next_cost += g[yx]
                if l >= minimum:
                    m = mins[yx]
                    if next_cost < m[next_d]:
                        m[next_d] = next_cost
                        bh[next_cost].append((yx, next_d))
                    if next_cost < m[-next_d]:
                        m[-next_d] = next_cost
                        bh[next_cost].append((yx, -next_d))


def neighbors(state, minimum, maximum):
    yx, d = state
    cc = 0
    for l in range(1, maximum):
        yx += d
        if yx < 0 or end < yx or (d == 1 and yx % w == 0) or (d == -1 and yx % w == (w-1)):
            break

        cc += g[yx]
        if l >= minimum:
            yield (cc, (yx, -w//d))
            yield (cc, (yx, w//d))



import time
START = time.time_ns()
print("day17", dynamic_dijkstra(1, 4, end), dynamic_dijkstra(4, 11, end))
print(">>>", (time.time_ns()-START)/1e9)