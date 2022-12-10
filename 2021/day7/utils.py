import re
import sys
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce
import operator

sys.setrecursionlimit(100000)

DIR = {'R': (1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1) }

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
        return [None for x in range(width)]

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._grid = [self._empty_row(width) for y in range(height)]
        self._cursor = (0, 0)

    def print(self):
        print("Grid ", self._width, self._height)
        for row in self._grid:
            for ch in row:
                print(ch, "  "[len(ch):], end='')
            print()
        print()

    def set_grid(self, g):
        assert(len(g) == self._height)
        assert(len(g[0]) == self._width)
        self._grid = g

    def set_cursor(self, x, y):
        self._cursor = (x, y)

    def get(self):
        return self._grid[self._cursor[1]][self._cursor[0]]

    def set(self, ch):
        self._grid[self._cursor[1]][self._cursor[0]] = ch

    def move(self, right, down):
        self.set_cursor(self.right_wrap(self._cursor[0], right),
                        self.down_wrap(self._cursor[1], down))
        return self._cursor

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
    test_grid()

    

