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

def bin_search_fn(lower, upper, test):
    # Example: Find value where probe(x) is < 1T and probe(x+1) is > 1T
    # bin_search_fn(p_i, i, lambda x:probe(x) - 1000000000000)
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

def aoc(data):
    print(data)
    subprocess.run("pbcopy", text=True, input=str(data))

def bundles(inp):
    r = []
    for line in inp:
        if line == '':
            yield(r)
            r = []
        else:
            r.append(line)
    yield(r)

def maxl(list):
    if len(list) == 0:
        return 0
    return max(list)

def angle_from_vertical(c):
    angle_from_horizontal = cmath.phase(c)
    angle_from_horizontal_degrees = math.degrees(angle_from_horizontal)
    angle_from_vertical_degrees = 90 - angle_from_horizontal_degrees
    if angle_from_vertical_degrees < 0:
        angle_from_vertical_degrees += 360
    return angle_from_vertical_degrees

## Graph stuff

def floyd_warshall(graph, bidirectional=False):
    # Given a graph dict of format {vertex: [edges]}
    # returns the shortest path between every pair of nodes in the graph.
    dist = defaultdict(lambda : math.inf)
    for node, edges in graph.items():
        for dest in edges:
            dist[(node, dest)] = 1 # use weight if weighted
            if bidirectional:
                dist[(dest, node)] = 1
    # for node in graph.keys():    # use if self connections important.
    #     dist[(node, node)] = 0
    for k in graph.keys():
        for i in graph.keys():
            for j in graph.keys():
                if dist[(i,j)] > dist[(i,k)] + dist[(k,j)]:
                    dist[(i,j)] = dist[(i,k)] + dist[(k,j)]
    return dist

def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist.get(end)

def dijkstra(graph, start, end):
    """
    graph is a dict of vertex: [(weight, neighbor), ...] 
    returns (sum(path weights), path)
    """
    q, seen, mins = [(0,start,[])], set(), {start: 0}
    while q:
        (cost,v,path) = heapq.heappop(q)
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
    q, seen, mins = [(0,start,[])], set(), {start: 0}
    while q:
        (cost,v,path) = heapq.heappop(q)
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

COMPASS = {'E': (1,0), 'W':(-1,0), 'N':(0,-1), 'S':(0,1) }
COMPASS8 = {'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1), 'E': (1,0), 'W':(-1,0), 'N':(0,-1), 'S':(0,1)}

RLUD = {'R': (1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1) }
ARROWS = {'>': (1,0), '<':(-1,0), '^':(0,-1), 'v':(0,1) }

DIR = [(1,0),(-1,0), (0,1), (0,-1)]
DIR8 = [d[1] for d in COMPASS8.items()]

CDIR8 = [p[0] + 1j*p[1] for p in DIR8]
CDIR = [p[0] + 1j*p[1] for p in DIR]

def manhattani(p, q):
    return abs(p.real - q.real) + abs(p.imag - q.imag)

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def manhattan3(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + + abs(p[2] - q[2])


def wrap(p, max_x, max_y, min_x=0, min_y=0):
    q = p
    if p.real > max_x:
        q = min_x + q.imag * 1j
    if p.real < min_x:
        q = max_x + q.imag * 1j
    if p.imag > max_y:
        q = q.real + min_y * 1j
    if p.imag < min_y:
        q = q.real + 1j*max_y
    return q

def cartesian(p, q):
    return math.sqrt(abs(p[0] - q[0])*abs(p[0] - q[0]) + abs(p[1] - q[1]) * abs(p[1] - q[1]))

def cartesiani(p, q):
    return math.sqrt(abs(p.real - q.real)*abs(p.real - q.real) + abs(p.imag - q.imag) * abs(p.imag - q.imag))

# sequence like 1,3,6,10,15
def triangle(n):
    return int((n/2)*(n+1))

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
    return (a == b) or (a[0]==b[0] and abs(a[1]-b[1])==1) or (a[1]==b[1] and abs(a[0]-b[0])==1) or (abs(a[0]-b[0]) ==1 and abs(a[1]-b[1])==1)

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

    # def print(self):
    #     print("Grid ", self._width, self._height)
    #     for row in self._grid:
    #         for ch in row:                    
    #             print(str(ch), " "[len(str(ch)):], end='')
    #         print()
    #     print()

    def set_grid(self, g):
        assert(len(g) == self._height)
        assert(len(g[0]) == self._width)
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
        if x > self._width -1 or y > self._height -1 or x < 0 or y < 0:
            return False
        return True

    def move(self, right, down):
        return  self.set_cursor(self.right_wrap(self._cursor[0], right),
                        self.down_wrap(self._cursor[1], down))

    def could_move(self, right, down, dbg=False):
        return  self.could_cursor(self.right_wrap(self._cursor[0], right),
                        self.down_wrap(self._cursor[1], down))

    def peek_move(self, right, down, dbg=False):
        ch = self._grid[self.down_wrap(self._cursor[1], down)][self.right_wrap(self._cursor[0], right)]
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

def grid_from_strs(lines, mapfn=lambda x:x, spl=''):
    l = lines[0].strip()
    if spl != '':
        l = re.sub(' +', ' ', l)
        l = l.split(spl)
    w = len(l)
    h = len(lines)
    grid = Grid(w, h)
    g = grid.g()
    for y, line in enumerate(lines):
        if spl != '':
            line = re.sub(' +', ' ', line)
            line = line.split(spl)
        for x, ch in enumerate(line):
            g[y][x] = mapfn(ch)
    return grid, w, h

def grid_ints_from_strs(lines, spl=''):
    return grid_from_strs(lines, mapfn=int, spl=spl)

def grid_neighbors(p, width, height=None):
    height = width if not height else height
    for d in DIR:
        q = (p[0] + d[0], p[1] + d[1])
        if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
            continue
        yield(q)

def grid_8_neighbors(p, width, height=None):
    height = width if not height else height
    for d in DIR8:
        q = (p[0] + d[0], p[1] + d[1])
        if q[0] < 0 or q[1] < 0 or q[0] >= width or q[1] >= height:
            continue
        yield(q)

def print_grid(g, spacing=0, markfn=lambda r,c,ch:""):
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            print(str(ch)+markfn(r,c,ch)+" "*(spacing-len(str(ch))-len(markfn(r,c,ch))), end="")
        print()

def print_world(world):
    mix, miy = int(min([p.real for p in world])), int(min([p.imag for p in world]))
    mx, my = int(max([p.real for p in world])), int(max([p.imag for p in world]))
    for y in range(miy, my+1):
        print("".join(["#" if x+1j*y in world else "." for x in range(mix,mx+1)]))

def print_dict_world(world):
    mix = int(min([k[0] for k in world.keys()]))
    miy = int(min([k[1] for k in world.keys()]))
    mx = int(max([k[0] for k in world.keys()]))
    my = int(max([k[1] for k in world.keys()]))

    for y in range(miy, my+1):
        for x in range(mix, mx+1):
            if (x,y) in world:
                print(world[(x,y)][0], end='')
            else:
                print(" ", end='')
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
            head.set_prv(prev) # Connect the ends
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

if __name__ == "__main__":
    assert(set(grid_neighbors((0,0), 4)) == set([(1,0), (0,1)]))
    assert(set(grid_neighbors((3,3), 4)) == set([(2,3), (3,2)]))
    assert(set(grid_8_neighbors((0,0), 4)) == set([(1,0), (0,1), (1,1)]))

    graph = {'A':['B','C'],'B':['D'],'C':['B'],'D':['F'], 'E':['F', 'A'], 'F':[]}
    assert(floyd_warshall(graph)[('E','B')] == 2)
    neighbors = lambda ch:[(ord(ch), chr(ord('A') + ((ord(ch) - ord('A') + 1) % 26)))]
    assert(dynamic_dijkstra(neighbors, 'C', 'B')[0] == 1949)

    grid, dim, _ = grid_ints_from_strs(["0000","9913", "9199", "5432"])
    graph = {(x,y): 
                [(int(grid[n[1]][n[0]]),n) for n in grid_neighbors((x,y), dim)]
             for x,y in itertools.product(range(dim), range(dim))}
    start, end = (0,0), (dim-1, dim-1)
    assert(a_star(graph, start, end, lambda x,y:manhattan(x,y))) #[0] == 14)
    print("utils OK")
    # An arbitrary non-trivial weight space
    neighbors = lambda e: [(triangle(p[0])+p[1]*p[1], p) for p in grid_neighbors(e, 100)]
    assert(dynamic_a_star(neighbors, (0,0), (99,99), manhattan)[0] == 902975)
