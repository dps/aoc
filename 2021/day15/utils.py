import itertools
import math
import operator
import re
import sys
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, reduce
import heapq

sys.setrecursionlimit(100000)

def maxl(list):
    if len(list) == 0:
        return 0
    return max(list)

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

DIR = {'E': (1,0), 'W':(-1,0), 'N':(0,-1), 'S':(0,1) }
#DIR = {'R': (1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1) }
#DIR = {'>': (1,0), '<':(-1,0), '^':(0,-1), '.':(0,1) }
#DIR = {'>': (1,0), '<':(-1,0), '^':(0,-1), '.':(0,1) }
DIR8 = {'NE': (1, -1),
        'NW': (-1, -1),
        'SE': (1, 1),
        'SW': (-1, 1),
        'E': (1,0),
        'W':(-1,0),
        'N':(0,-1),
        'S':(0,1)}

CDIR8 = [p[0] + 1j*p[1] for _,p in DIR8.items()]
CDIR = [p[0] + 1j*p[1] for _,p in DIR.items()]

def manhattani(p, q):
    return abs(p.real - q.real) + abs(p.imag - q.imag)

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

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

def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

# sequence like 1,3,6,10,15
def triangle(n):
    return int((n/2)*(n+1))

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

def print_world(world):
    mix, miy = int(min([p.real for p in world])), int(min([p.imag for p in world]))
    mx, my = int(max([p.real for p in world])), int(max([p.imag for p in world]))
    for y in range(miy, my+1):
        print("".join(["🟧" if x+1j*y in world else "⬛️" for x in range(mix,mx+1)]))

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
                print(str(ch), " "[len(str(ch)):], end='')
            print()
        print()

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
        if dbg:
            print("peek", ch, self.right_wrap(self._cursor[0], right), self.down_wrap(self._cursor[1], down))
        return ch

    def g(self):
        return self._grid

    def right_wrap(self, x, steps=1):
        return (x + steps) #% self._width

    def left_wrap(self, x, steps=1):
        return (x - steps) #% self._width

    def up_wrap(self, y, steps=1):
        return (y - steps) #% self._height

    def down_wrap(self, y, steps=1):
        return (y + steps) #% self._height

def grid_from_strs(lines, spl=''):
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
            g[y][x] = ch
    return grid

def grid_ints_from_strs(lines, spl=''):
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
            g[y][x] = int(ch)
    return grid

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

def test_grid():
    g = grid_from_strs(["0122", "2111", "3113"])
    assert(g.g() == [['0', '1', '2', '2'], ['2', '1', '1', '1'], ['3', '1', '1', '3']])
    g.set("z")
    g.move(1,1)
    g.set("y")
    g.move(1,0)
    g.set("x")
    g.move(2,0)
    assert(g.get() == '2')
    g.set("w")
    assert(g.g() == [['z', '1', '2', '2'], ['w', 'y', 'x', '1'], ['3', '1', '1', '3']])
    g = grid_from_strs(["0,1,2,2", "2,1,1,1", "3,1,1,3"], spl=',')
    assert(g.g() == [['0', '1', '2', '2'], ['2', '1', '1', '1'], ['3', '1', '1', '3']])

if __name__ == "__main__":
    graph = {"start": [(1, "A")], "A": [(5, "B"), (2, "C")], "B": [(1, "end")], "C": [(1, "D")], "D": [(1,"end")], "end": []}
    print(dijkstra(graph, "start", "end"))
