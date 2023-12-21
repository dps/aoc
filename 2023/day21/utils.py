"""
# utils

`Grid`
Linked lists: `Dll`, `Sll`

```
bin_search_fn(lower, upper, test)
`to_base(number, base)`
`aoc(data)`
`bundles(inp)`
`angle_from_vertical(c)`
`floyd_warshall(graph, bidirectional=False)`
`find_shortest_path(graph, start, end)`
`dynamic_find_shortest_path(neighbors, start, end)`
`dijkstra(graph, start, end)`
`dynamic_dijkstra(neighbors, start, end)`
`a_star(graph, start, end, heuristic)`
`dynamic_a_star(next_fn, start, end, heuristic)`
```

`manhattani(p, q)`, `manhattan(p, q)`
def manhattan3(p, q):
def hex_dir_alt(p, dir):
def wrap(p, max_x, max_y, min_x=0, min_y=0):
def cartesian(p, q):
def cartesiani(p, q):
def triangle(n):
# def flatten(list_of_lists):
def flatten(list_of_lists):
def sign(a):
def touching(a, b):
def lmap(func, *iterables):
def ints(s):
def positive_ints(s):
def floats(s):
def positive_floats(s):
def words(s):
    def _empty_row(self, width):
    def empty_row(self, ch):
    def __init__(self, width, height):
    def print(self):
    def set_grid(self, g):
    def set_cursor(self, x, y):
    def get_cursor(self):
    def get(self):
    def set(self, ch):
    def could_cursor(self, x, y):
    def move(self, right, down):
    def could_move(self, right, down):
    def peek_move(self, right, down):
    def g(self):
    def right_wrap(self, x, steps=1):
    def left_wrap(self, x, steps=1):
    def up_wrap(self, y, steps=1):
    def down_wrap(self, y, steps=1):
def grid_from_strs(lines, mapfn=lambda x:x, spl=''):
def grid_ints_from_strs(lines, spl=''):
def grid_neighbors(p, width, height=None):
def grid_wrap_neighbors(p, width, height=None):
def grid_8_neighbors(p, width, height=None):
def grid_wrap_8_neighbors(p, width, height=None):
def print_grid(g, spacing=0, markfn=lambda r,c,ch:""):
def print_world(world):
def print_dict_world(world):
    def parse(src, special_val=None, circular=True):
    def __init__(self, val, prv, nxt):
    def set_nxt(self, n):
    def set_prv(self, n):
    def nxt(self):
    def prv(self):
    def val(self):
    def parse(src, special_val=None, circular=True):
    def __init__(self, val, nxt):
    def set_nxt(self, n):
    def nxt(self):
    def val(self):
def toposort(leaves, graph):
"""
import itertools
import math
import operator
import re
import sys
import heapq
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, reduce
from itertools import combinations, permutations, product
import subprocess
import cmath

sys.setrecursionlimit(100000)


def data(filename="input", strip=True):
    """
    `[i.strip() if strip else i for i in open(filename,"r").readlines()]`
    """
    return [i.strip() if strip else i for i in open(filename, "r").readlines()]


def bin_search_fn(lower, upper, test):
    """
    Example: Find value where probe(x) is < 1T and probe(x+1) is >= 1T
    bin_search_fn(p_i, i, lambda x:probe(x) - 1000000000000)
    """
    while upper - lower > 1:
        mid = (lower + upper) // 2
        p = test(mid)
        if p < 0:
            lower = mid
        else:
            upper = mid
    return lower


base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


@cache
def to_base(number, base):
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"

@cache
def from_base(s, base):
    number = 0
    for char in s:
        value = base_string.index(char)
        number = number * base + value
    return number

def aoc(data):
    print(data)
    subprocess.run("pbcopy", text=True, input=str(data))


def bundles(inp):
    """
    Generator to turn input array from file with multi-line sequences divided by
    blank lines into something you can loop over.
    e.g.
    ```
    input = [i.strip() for i in open("input.txt","r").readlines()]

    max([sum(map(int, line)) for line in bundles(inp)])
    ```
    """
    r = []
    for line in inp:
        if line == "":
            yield r
            r = []
        else:
            r.append(line)
    yield (r)


def maxl(list):
    if len(list) == 0:
        return 0
    return max(list)


def angle_from_vertical(c):
    """
    ```           |    _c
               |Θ.-'
     origin -> .'
    ```
    c is a complex number with (CAREFUL!) y ^ up vertical as +1j direction
    opposite from how you usually read grids, but intuitive for trig.
    returns angle clockwise from vertical in degrees. Will return 315 not -45
    for close anticlockwise.
    """
    angle_from_horizontal = cmath.phase(c)
    angle_from_horizontal_degrees = math.degrees(angle_from_horizontal)
    angle_from_vertical_degrees = 90 - angle_from_horizontal_degrees
    if angle_from_vertical_degrees < 0:
        angle_from_vertical_degrees += 360
    return angle_from_vertical_degrees


## Graph stuff


def floyd_warshall(graph, bidirectional=False):
    """
    Given a graph dict of format {vertex: [edges]}
    returns the shortest path between every pair of nodes in the graph.
    """
    dist = defaultdict(lambda: math.inf)
    for node, edges in graph.items():
        for dest in edges:
            dist[(node, dest)] = 1  # use weight if weighted
            if bidirectional:
                dist[(dest, node)] = 1
    # for node in graph.keys():    # use if self connections important.
    #     dist[(node, node)] = 0
    for k in graph.keys():
        for i in graph.keys():
            for j in graph.keys():
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
    return dist


def find_shortest_path(graph, start, end):
    """
    Given a graph dict of format {vertex: [edges]}
    returns the shortest path between start and end. It's literally the whole route
    so to find its length do len(find_shortest_path)
    """
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist.get(end)


def dynamic_find_shortest_path(neighbors, start, end):
    """
    Given a graph defined by function `neighbors`
    returns the shortest path between start and end. It's literally the whole route
    so to find its length do len(find_shortest_path)
    """
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in neighbors(at):
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist.get(end)


def dijkstra(graph, start, end):
    """
    graph is a dict of vertex: [(weight, neighbor), ...] 
    returns (sum(path weights), path)
    """
    q, seen, mins = [(0, start, [])], set(), {start: 0}
    while q:
        (cost, v, path) = heapq.heappop(q)
        if v not in seen:
            seen.add(v)
            path = path + [v]
            if v == end:
                return (cost, path)

            for c, neighbor in graph.get(v, ()):
                if neighbor in seen:
                    continue
                prev = mins.get(neighbor, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[neighbor] = next
                    heapq.heappush(q, (next, neighbor, path))

    return math.inf, None


def dynamic_dijkstra(neighbors, start, end):
    """
    neighbors is a function which takes current node and returns a list of (weight, neighbor)
    pairs or () if no neighbors exist.
    returns (sum(path weights), path)
    """
    q, seen, mins = [(0, start, [])], set(), {start: 0}
    while q:
        (cost, v, path) = heapq.heappop(q)
        if v not in seen:
            seen.add(v)
            path = path + [v]
            if v == end:
                return (cost, path)

            for c, neighbor in neighbors(v):
                if neighbor in seen:
                    continue
                prev = mins.get(neighbor, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[neighbor] = next
                    heapq.heappush(q, (next, neighbor, path))

    return math.inf, None


def a_star(graph, start, end, heuristic):
    """
    graph is a dict of vertex: [(weight, neighbor), ...] 
    heuristic is a function that takes in a vertex and returns an estimated cost
    to reach the end from that vertex
    returns (sum(path weights), path)
    """

    # Initialize data structures
    distances = defaultdict(lambda: math.inf)
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    queue = []
    heapq.heappush(queue, (0, 0, start))

    # Loop until the queue is empty
    while queue:
        _, current_distance, current_vertex = heapq.heappop(queue)

        # End search if we have reached the end
        if current_vertex == end:
            break

        # Update the distances and previous vertices of the neighbors
        for weight, neighbor in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                priority = distance + heuristic(neighbor, end)
                heapq.heappush(queue, (priority, distance, neighbor))

    # Build the path
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]

    return (distances[end], path[::-1])


def dynamic_a_star(next_fn, start, end, heuristic):
    """
    next_fn is a funtion taking vertex => [(weight, neighbor), ...] 
    heuristic is a function that takes in a vertex and returns an estimated cost
    to reach the end from that vertex
    returns (sum(path weights), path)
    """

    # Initialize data structures
    distances = defaultdict(lambda: math.inf)
    distances[start] = 0
    previous = defaultdict(lambda: None)
    queue = []
    heapq.heappush(queue, (0, 0, start))

    # Loop until the queue is empty
    while queue:
        _, current_distance, current_vertex = heapq.heappop(queue)

        # End search if we have reached the end
        if current_vertex == end:
            break

        # Update the distances and previous vertices of the neighbors
        for weight, neighbor in next_fn(current_vertex):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                priority = distance + heuristic(neighbor, end)
                heapq.heappush(queue, (priority, distance, neighbor))

    # Build the path
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]

    return (distances[end], path[::-1])


## Cardinal directions and grid stuff.
#
# Most of these have two versions - one for complex number represention and one for tuple
# representation.

COMPASS = {"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1)}
COMPASS8 = {
    "NE": (1, -1),
    "NW": (-1, -1),
    "SE": (1, 1),
    "SW": (-1, 1),
    "E": (1, 0),
    "W": (-1, 0),
    "N": (0, -1),
    "S": (0, 1),
}

RLUD = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
ARROWS = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
CRLUD = {"R": 1, "L": -1, "U": -1j, "D": 1j}
CARROWS = {">": 1, "<": -1, "^": -1j, "v": 1j}

DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DIR8 = [d[1] for d in COMPASS8.items()]

CDIR8 = [p[0] + 1j * p[1] for p in DIR8]
CDIR = [p[0] + 1j * p[1] for p in DIR]


def rotate_cw(g):
    return [list(x) for x in list(zip(*g[::-1]))]

def rotate_ccw(g):
    return [list(x)[::-1] for x in list(zip(*g[::-1]))][::-1]

def cw(d): return {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}[d]
def ccw(d): return {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}[d]

def manhattani(p, q):
    return abs(p.real - q.real) + abs(p.imag - q.imag)


def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def manhattan3(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])


# THERE ARE TWO TYPES OF HEX GRID - those with north/south
# and those with east/west
#          _____         _____         _____
#         /     \       /     \       /     \
#   _____/ -2,-1 \_____/  0,-1 \_____/  2,-1 \_____
#  /     \       /     \       /     \       /     \
# / -3,-1 \_____/ -1,-1 \_____/  1,-1 \_____/  3,-1 \
# \       /     \       /     \       /     \       /
#  \_____/ -2,0  \_____/  0,0  \_____/  2,0  \_____/
#  /     \       /     \  ***  /     \       /     \
# / -3,0  \_____/ -1,0  \_____/  1,0  \_____/  3,0  \
# \       /     \       /     \       /     \       /
#  \_____/ -2,1  \_____/  0,1  \_____/  2,1  \_____/
#  /     \       /     \       /     \       /     \
# / -3,1  \_____/ -1,1  \_____/  1,1  \_____/  3,1  \
# \       /     \       /     \       /     \       /
#  \_____/       \_____/       \_____/       \_____/
HEX_DIR_ALT_EVEN_X = {
    "n": (0, -1),
    "s": (0, 1),
    "ne": (1, -1),
    "se": (1, 0),
    "nw": (-1, -1),
    "sw": (-1, 0),
}
HEX_DIR_ALT_ODD_X = {
    "n": (0, -1),
    "s": (0, 1),
    "ne": (1, 0),
    "se": (1, 1),
    "nw": (-1, 0),
    "sw": (-1, 1),
}


def hex_dir_alt(p, dir):
    x, _ = p[0], p[1]
    if x % 2 == 0:
        return HEX_DIR_ALT_EVEN_X[dir]
    else:
        return HEX_DIR_ALT_ODD_X[dir]


#    /\   /\   /\
#   /  \ /  \ /  \
#  |    |0,-1|1,-1|
#  |    |    |    |
#   \  / \  / \  / \
#    \/   \/   \/   \
#    |-1,0| 0,0| 1,0|
#    |    | ** |    |
#   / \  / \  / \  /
#  /   \/   \/   \/
# |    |-1,1| 0,1|
# |    |    |    |
#  \  / \  / \  / \
#   \/   \/   \/   \


HEX_DIR = {
    "e": (1, 0),
    "w": (-1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "ne": (1, -1),
    "nw": (0, -1),
}
HEX_NEIGHBORS = [(1, 0), (-1, 0), (0, 1), (-1, 1), (1, -1), (0, -1)]


def wrapi(p, max_x, max_y, min_x=0, min_y=0):
    q = p
    if p.real > max_x:
        q = min_x + q.imag * 1j
    if p.real < min_x:
        q = max_x + q.imag * 1j
    if p.imag > max_y:
        q = q.real + min_y * 1j
    if p.imag < min_y:
        q = q.real + 1j * max_y
    return q

def wrap(p, max_x, max_y, min_x=0, min_y=0):
    q = p[0] + 1j*p[1]
    q = wrapi(q, max_x, max_y, min_x, min_y)
    return int(q.real), int(q.imag)


def cartesian(p, q):
    return math.sqrt(
        abs(p[0] - q[0]) * abs(p[0] - q[0]) + abs(p[1] - q[1]) * abs(p[1] - q[1])
    )


def cartesiani(p, q):
    return math.sqrt(
        abs(p.real - q.real) * abs(p.real - q.real)
        + abs(p.imag - q.imag) * abs(p.imag - q.imag)
    )


# sequence like 1,3,6,10,15
def triangle(n):
    return int((n / 2) * (n + 1))


# def flatten(list_of_lists):
#     if len(list_of_lists) == 0:
#         return list_of_lists
#     if isinstance(list_of_lists[0], list):
#         return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
#     return list_of_lists[:1] + flatten(list_of_lists[1:])


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list(list_of_lists)
    if isinstance(list_of_lists[0], tuple):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list(list_of_lists[:1]) + list(flatten(list_of_lists[1:]))


def sign(a):
    if a == 0:
        return 0
    return a // abs(a)


def touching(a, b):
    return (
        (a == b)
        or (a[0] == b[0] and abs(a[1] - b[1]) == 1)
        or (a[1] == b[1] and abs(a[0] - b[0]) == 1)
        or (abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 1)
    )


# Thanks mcpower!
def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!


def positive_ints(s):
    return lmap(int, re.findall(r"\d+", s))  # thanks mserrano!


def floats(s):
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def positive_floats(s):
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def words(s):
    return re.findall(r"[a-zA-Z]+", s)


class Grid(object):
    def _empty_row(self, width):
        return ["." for x in range(width)]

    def empty_row(self, ch):
        return [ch for x in range(self._width)]

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = [self._empty_row(width) for y in range(height)]
        self._cursor = (0, 0)

    def print(self):
        print("Grid ", self._width, self._height)
        for row in self._grid:
            for ch in row:
                print(str(ch), " "[len(str(ch)) :], end="")
            print()
        print()

    def set_grid(self, g):
        assert len(g) == self._height
        assert len(g[0]) == self._width
        self._grid = g

    def set_cursor(self, x, y):
        if x > self._width - 1 or y > self._height - 1 or x < 0 or y < 0:
            return None
        self._cursor = (x, y)
        return self._cursor

    def get_cursor(self):
        return self._cursor

    def get(self):
        return self._grid[self._cursor[1]][self._cursor[0]]

    def set(self, ch):
        self._grid[self._cursor[1]][self._cursor[0]] = ch

    def could_cursor(self, x, y):
        if x > self._width - 1 or y > self._height - 1 or x < 0 or y < 0:
            return False
        return True

    def move(self, right, down):
        return self.set_cursor(
            self.right_wrap(self._cursor[0], right),
            self.down_wrap(self._cursor[1], down),
        )

    def could_move(self, right, down):
        return self.could_cursor(
            self.right_wrap(self._cursor[0], right),
            self.down_wrap(self._cursor[1], down),
        )

    def peek_move(self, right, down):
        ch = self._grid[self.down_wrap(self._cursor[1], down)][
            self.right_wrap(self._cursor[0], right)
        ]
        return ch

    def g(self):
        return self._grid

    def right_wrap(self, x, steps=1):
        return (x + steps) % self._width

    def left_wrap(self, x, steps=1):
        return (x - steps) % self._width

    def up_wrap(self, y, steps=1):
        return (y - steps) % self._height

    def down_wrap(self, y, steps=1):
        return (y + steps) % self._height


def grid_from_strs(lines, mapfn=lambda x: x, find=None, spl=""):
    l = lines[0].strip()
    found = None
    if spl != "":
        l = re.sub(" +", " ", l)
        l = l.split(spl)
    w = len(l)
    h = len(lines)
    grid = Grid(w, h)
    g = grid.g()
    for y, line in enumerate(lines):
        if spl != "":
            line = re.sub(" +", " ", line)
            line = line.split(spl)
        for x, ch in enumerate(line):
            g[y][x] = mapfn(ch)
            if find and ch == find:
                found = (x,y)
    return g, w, h, found

def grid_ints_from_strs(lines, spl=""):
    return grid_from_strs(lines, mapfn=int, spl=spl)


def grid_neighbors(p, width, height=None):
    height = width if not height else height
    for d in DIR:
        q = (p[0] + d[0], p[1] + d[1])
        if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
            continue
        yield (q)


def grid_wrap_neighbors(p, width, height=None):
    height = width if not height else height
    for d in DIR:
        q = (p[0] + d[0]) % width, (p[1] + d[1]) % height
        yield (q)


def grid_8_neighbors(p, width, height=None):
    height = width if not height else height
    for d in DIR8:
        q = (p[0] + d[0], p[1] + d[1])
        if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
            continue
        yield (q)


def grid_wrap_8_neighbors(p, width, height=None):
    height = width if not height else height
    for d in DIR8:
        q = (p[0] + d[0]) % width, (p[1] + d[1]) % height
        yield (q)


def print_grid(g, spacing=0, markfn=lambda r, c, ch: ""):
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            print(
                str(ch)
                + markfn(r, c, ch)
                + " " * (spacing - len(str(ch)) - len(markfn(r, c, ch))),
                end="",
            )
        print()


def print_world(world):
    mix, miy = int(min([p.real for p in world])), int(min([p.imag for p in world]))
    mx, my = int(max([p.real for p in world])), int(max([p.imag for p in world]))
    for y in range(miy, my + 1):
        print(
            "".join(["#" if x + 1j * y in world else "." for x in range(mix, mx + 1)])
        )


def print_dict_world(world):
    mix = int(min([k[0] for k in world.keys()]))
    miy = int(min([k[1] for k in world.keys()]))
    mx = int(max([k[0] for k in world.keys()]))
    my = int(max([k[1] for k in world.keys()]))

    for y in range(miy, my + 1):
        for x in range(mix, mx + 1):
            if (x, y) in world:
                print(world[(x, y)][0], end="")
            else:
                print(" ", end="")
        print()


class Dll(object):
    def parse(src, special_val=None, circular=True):
        vmap = {}
        head = None
        special = None
        prev = None
        for v in src:
            n = Dll(v, prev, None)
            if not prev:
                head = n
            else:
                prev.set_nxt(n)
            prev = n
            if v == special_val:
                special = n
            vmap[v] = n
        if circular:
            head.set_prv(prev)  # Connect the ends
            prev.set_nxt(head)
        return head, vmap, special

    def __init__(self, val, prv, nxt):
        self._val = val
        self._prv = prv
        self._nxt = nxt

    def set_nxt(self, n):
        self._nxt = n

    def set_prv(self, n):
        self._prv = n

    def nxt(self):
        return self._nxt

    def prv(self):
        return self._prv

    def val(self):
        return self._val


class Sll(object):
    def parse(src, special_val=None, circular=True):
        vmap = {}
        head = None
        special = None
        prev = None
        for v in src:
            n = Dll(v, prev, None)
            if not prev:
                head = n
            else:
                prev.set_nxt(n)
            prev = n
            if v == special_val:
                special = n
            vmap[v] = n
        if circular:
            prev.set_nxt(head)
        return head, vmap, special

    def __init__(self, val, nxt):
        self._val = val
        self._nxt = nxt

    def set_nxt(self, n):
        self._nxt = n

    def nxt(self):
        return self._nxt

    def val(self):
        return self._val


def toposort(leaves, graph):
    """
    Returns list of leaves topologically sorted according to graph
    ```
    leaves: set of leaves
    graph: dict of vertex => dependencies

    graph={'A':['B', 'C'], 'C': ['D']}
    print(toposort({'A','B','C','D'}, graph))
    ['D', 'C', 'B', 'A']
    ```
    """
    # Kahn's algorithm
    res = []
    s = leaves
    while len(s) > 0:
        n = s.pop()
        res.append(n)
        for dep_k, dep_v in [(k, v) for k, v in graph.items() if n in v]:
            dep_v.remove(n)
            if len(dep_v) == 0:
                s.add(dep_k)
    return res

def test():
    assert set(grid_neighbors((0, 0), 4)) == set([(1, 0), (0, 1)])
    assert set(grid_neighbors((3, 3), 4)) == set([(2, 3), (3, 2)])
    assert set(grid_8_neighbors((0, 0), 4)) == set([(1, 0), (0, 1), (1, 1)])

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["B"],
        "D": ["F"],
        "E": ["F", "A"],
        "F": [],
    }
    assert floyd_warshall(graph)[("E", "B")] == 2
    neighbors = lambda ch: [(ord(ch), chr(ord("A") + ((ord(ch) - ord("A") + 1) % 26)))]
    assert dynamic_dijkstra(neighbors, "C", "B")[0] == 1949

    grid, dim, _ = grid_ints_from_strs(["0000", "9913", "9199", "5432"])
    graph = {
        (x, y): [(int(grid[n[1]][n[0]]), n) for n in grid_neighbors((x, y), dim)]
        for x, y in itertools.product(range(dim), range(dim))
    }
    start, end = (0, 0), (dim - 1, dim - 1)
    assert a_star(graph, start, end, lambda x, y: manhattan(x, y))  # [0] == 14)

    # An arbitrary non-trivial weight space
    neighbors = lambda e: [
        (triangle(p[0]) + p[1] * p[1], p) for p in grid_neighbors(e, 100)
    ]
    assert dynamic_a_star(neighbors, (0, 0), (99, 99), manhattan)[0] == 902975

    print(list(grid_wrap_8_neighbors((0, 0), 8, 8)))

    print(angle_from_vertical(-1 + 1j))

    xx = sum([x for x, _ in [HEX_DIR[c] for c in ["ne", "se", "sw", "w", "ne"]]])
    yy = sum([y for _, y in [HEX_DIR[c] for c in ["ne", "se", "sw", "w", "ne"]]])
    assert (xx, yy) == (0, 0)

    seq = ["ne", "se", "sw", "w", "nw", "nw", "e", "se"]
    xx = sum([x for x, _ in [HEX_DIR[c] for c in seq]])
    yy = sum([y for _, y in [HEX_DIR[c] for c in seq]])
    assert (xx, yy) == (0, 0)

    xx, yy = 0, 0
    seq = ["ne", "s", "sw", "nw", "nw", "ne", "se"]
    for s in seq:
        dx, dy = hex_dir_alt((xx, yy), s)
        xx += dx
        yy += dy

    assert (xx, yy) == (0, 0)

    print(bin_search_fn(0, 1000000000000000, lambda x: x - 987665454321))
    print(to_base(999, 5))

    inp = ["12", "13", "14", "", "4", "99", "", "1234"]
    assert max([sum(map(int, line)) for line in bundles(inp)]) == 1234

    graph = {"A": ["B", "C"], "C": ["D"]}
    print(toposort({"A", "B", "C", "D"}, graph))

TEMPLATE = """
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]

def part1():
    global D
    tot = 0
    #max_sum = max([sum(map(int, lines)) for lines in bundles(D)])
    
    for line in D:
        print(line)
        
    aoc(tot)

part1()
#part2()
"""

def make_template():
    import argparse
    import os
    import shutil
    parser = argparse.ArgumentParser(
                    prog='utils',
                    description='AoC utils for dps',
                    epilog='May the elves be with you')
    parser.add_argument('day_num')
    args = parser.parse_args()
    print(args.day_num)
    directory = f"day{str(args.day_num).zfill(2)}"
    os.mkdir(f"day{str(args.day_num).zfill(2)}")
    os.chdir(directory)
    shutil.copyfile("../../utils.py", "utils.py")
    t = open("main.py","w")
    t.write(TEMPLATE)
    t.close()
    print(f"Now run aoc download --year 2023 --day {args.day_num}")
    print("watchexec -- \"clear;pypy3 main.py\"")

if __name__ == "__main__":
    make_template()