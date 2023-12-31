from utils import *

D = [i.strip() for i in open("input", "r").readlines()]

g, w, h, _ = grid_ints_from_strs(D)
end = ((w - 1), (h - 1))

class BucketHeap:
    def __init__(self):
        self.heap = defaultdict(list)
        self.min_bucket = math.inf

    def insert(self, element):
        self.heap[element[0]].append(element)
        if element[0] < self.min_bucket:
            self.min_bucket = element[0]

    def delete_min(self):
        min_element = self.heap[self.min_bucket][0]
        if len(self.heap[self.min_bucket]) > 1:
            self.heap[self.min_bucket] = self.heap[self.min_bucket][1:]
        else:
            del self.heap[self.min_bucket]
            try:
                self.min_bucket = min(self.heap.keys())
            except:
                self.min_bucket = math.inf
        return min_element

def dynamic_dijkstra(neighbors, start, end):
    seen, mins = set(), {start: 0}
    bh = BucketHeap()
    bh.insert((0, start))
    while True:
        (cost, v) = bh.delete_min() #heapq.heappop(q)
        if v not in seen:
            seen.add(v)
            if v[0] == end:
                return cost

            for c, neighbor in neighbors(v):
                if neighbor in seen:
                    continue
                prev = mins.get(neighbor, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[neighbor] = next
                    bh.insert((next, neighbor))
                    #heapq.heappush(q, (next, neighbor))


def cw(d): return {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}[d]
def ccw(d): return {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}[d]

def in_bounds(p, d): return 0 <= p[0] + d[0] < w and 0 <= p[1] + d[1] < h
def cost(p, d): return g[p[1] + d[1]][p[0] + d[0]]

def neighbors1(state):
    r = []
    for p, d in [((0, 0), (1, 0)), ((0, 0), (0, 1))] if state == ("start") else [state]:
        cc = 0
        for l in range(1, 4):
            dl = (l * d[0], l * d[1])
            if in_bounds(p, dl):
                cc += cost(p, dl)
                r.append((cc, ((p[0] + l * d[0], p[1] + l * d[1]), {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}[d])))
                r.append((cc, ((p[0] + l * d[0], p[1] + l * d[1]), {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}[d])))
            else:
                break
    return r

def neighbors2(state):
    r = []
    for p, d in [((0, 0), (1, 0)), ((0, 0), (0, 1))] if state == ("start") else [state]:
        cc = 0
        for l in range(1, 11):
            dl = (l * d[0], l * d[1])
            if in_bounds(p, dl):
                cc += cost(p, dl)
                if l >= 4:
                    r.append((cc, ((p[0] + l * d[0], p[1] + l * d[1]), {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}[d])))
                    r.append((cc, ((p[0] + l * d[0], p[1] + l * d[1]), {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}[d])))
            else:
                break
    return r

# pypy3 main.py  1.16s user 0.02s system 99% cpu 1.187 total
print(dynamic_dijkstra(neighbors1, ("start"), end))
print(dynamic_dijkstra(neighbors2, ("start"), end))
