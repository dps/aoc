# aoc

https://blog.singleton.io/posts/2023-01-14-advent-of-code/

## Utils

#### A bunch of useful imports
```python
import itertools
import math
import operator
import re
import sys
import heapq
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, reduce
```

#### `maxl(list)`
Returns the `max` element in an iterable, or 0 if the iterable is empty.

### Graph stuff

#### `floyd_warshall(graph, bidirectional=False)`
Given a graph `dict` of format `{vertex: [edges]}`, returns the shortest path between every pair of nodes in the graph.
𝚯( |V|^3 )
e.g.
```python
>>> graph = {'A':['B','C'],'B':['D'],'C':['B'],'D':['F'], 'E':['F', 'A'], 'F':[]}
>>> dict(floyd_warshall(graph))
{('A', 'B'): 1, ('A', 'C'): 1, ... , ('F', 'E'): inf, ('F', 'F'): inf}
>>> floyd_warshall(graph)[('E','B')]
2
```

#### `find_shortest_path(graph, start, end)`
Given the graph `dict` of format `{vertex: [edges]}` find the shortest path from node start to node end. Does a breadth first search. Returns the path as a list or `None`
```python
>>> find_shortest_path(graph, 'A', 'F')
['A', 'B', 'D', 'F']
```

#### `dijkstra(graph, start, end)`
Given a graph `dict` of format `{vertex: [(weight, neighbor), ...] }` finds the shortest path using Dijkstra's algorithm. Returns tuple `(sum(path weights), [path])`
```python
>>> grid, dim, _ = grid_ints_from_strs(["0000","9913", "9199", "5432"])
>>> graph = {(x,y): 
...             [(int(grid[n[1]][n[0]]),n) for n in grid_neighbors((x,y), dim)]
...           for x,y in itertools.product(range(dim), range(dim))}
>>> 
>>> start, end = (0,0), (dim-1, dim-1)
>>> dijkstra(graph, start, end)
(14, [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)])
```

#### `dynamic_dijkstra(neighbors, start, end)`
Given `neighbors` is a function which takes a node and returns a list of `(weight, neighbor)` pairs or `()` if no neighbors exist, finds the shortest path from `start` to `end` using Dijkstra's algorithm and returns `(sum(shortest path weights), [path])`

e.g.
```python
>>> neighbors = lambda ch:[(ord(ch), chr(ord('A') + ((ord(ch) - ord('A') + 1) % 26)))]
>>> dynamic_dijkstra(neighbors, 'C', 'B')
(1949, ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'])
```

#### `a_star(graph, start, end, heuristic)`
Given `graph` is a `dict` of `vertex: [(weight, neighbor), ...] `
`heuristic` is a function that takes in a vertex and returns an estimated cost to reach the end from that vertex, returns (sum(path weights), path) of the shortest path from start to end using the A* algorithm. `heuristic` must be _admissible_ i.e. it never overestimates the cost of reaching the goal.

```python
>>> grid, dim, _ = grid_ints_from_strs(["0000","9913", "9199", "5432"])
>>> graph = {(x,y): 
            [(int(grid[n[1]][n[0]]),n) for n in grid_neighbors((x,y), dim)]
          for x,y in itertools.product(range(dim), range(dim))}
>>> start, end = (0,0), (dim-1, dim-1)
>>> a_star(graph, start, end, lambda x,y:manhattan(x,y))
(14, [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)])
```

#### `dynamic_a_star(next_fn, start, end, heuristic)`
Verson of A* taking a `next_fn` to generate neighbors from current node. `next_fn` should take `vertex` => `[(weight, neighbor), ...]`

e.g.
```python
>>> # An arbitrary non-trivial weight space
>>> neighbors = lambda e: [(triangle(p[0])+p[1]*p[1], p) for p in grid_neighbors(e, 100)]
>>> dynamic_a_star(neighbors, (0,0), (99,99), manhattan)
>>> (902975, [(0, 0), (0, 1), (1, 1), ..., (99, 98), (99, 99)])
```


## Cardinal directions and grid stuff.
 
Most of these have two versions - one for complex number represention and one for tuple representation.

#### `COMPASS`
`{'E': (1,0), 'W':(-1,0), 'N':(0,-1), 'S':(0,1) }`

#### `COMPASS8`
```python
{'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1), 'E': (1,0), 'W':(-1,0), 'N':(0,-1), 'S':(0,1)}
```

#### `RLUD` "Right, Left, Up, Down"
```python
{'R': (1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1) }
```
#### `ARROWS`
```python
{'>': (1,0), '<':(-1,0), '^':(0,-1), 'v':(0,1) }
```

#### `DIR`
```python
[(1,0),(-1,0), (0,1), (0,-1)]
```
#### `DIR8`
```python
[(1, -1), (-1, -1), (1, 1), (-1, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]
```
#### `CDIR8`
`[p[0] + 1j*p[1] for p in DIR8]`
#### `CDIR`
`[p[0] + 1j*p[1] for p in DIR]`

## Distance stuff
#### `manhattan` and `manhattani(p, q)`
Returns the Manhattan distance between points in `(x,y)` tuple and imaginary number format respectively. `manhattan3(p, q)` for 3D (tuple only for obvious reasons).
#### `cartesian(p, q)`
`p` and `q` are `(x, y)` tuples. Returns the cartesian distance between `p` and `q` using Pythagoras' theorem. 



## Numeric

#### `triangle(n)`
Returns the `n`th triangular number - a sequence like `1,3,6,10,15`
```
>>> list(map(triangle, range(20)))
[0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190]
```

### `sign(a)`
Returns `-1` if a is negative, `0` if a is zero and `1` if a is positive. See also `math.copysign` and note that the semantics are different!
```
>>> sign(0)
0
>>> math.copysign(1,0)
1.0
```


## Input parsing stuff

First up, note that this is at the start of my default day template:
```
input = [i.strip() for i in open("input.txt","r").readlines()]
```

### Thanks mcpower!
### `ints(s)`, `positive_ints(s)`, `floats(s)`, `positive_floats(s)`, `words(s)`
Returns a list of all the ints, positive_ints etc in a string respectively.
```python
>>> ints("708,862 -> 100,862")
[708, 862, 100, 862]
>>> positive_ints("708,862 -> 100,-862")
[708, 862, 100, 862] # Note 862 is there but no sign!
>>> floats("0.0,1.2 -> 999.0,-3.1515")
[0.0, 1.2, 999.0, -3.1515]
>>> words("Returns a _list_ -- of all the ints. (foo)")
['Returns', 'a', 'list', 'of', 'all', 'the', 'ints', 'foo']
```

## flatten(list_of_lists)
Returns a single list of all of the elements from a list of arbitrarily nested lists at the same level:

```python
>>> flatten([[0,1],[2,3],[4,[5,6]]])
[0, 1, 2, 3, 4, 5, 6]
```

## Grid stuff

### `grid_from_strs(lines, mapfn=lambda x:x, spl='')`
`lines` is a list of strs, each one representing a row in a grid.
Returns `(2D array, width, height` 2D array is of grid rows, split on `spl` or each character by default. Optionally applies function `mapfn` to each element in the grid.

```python
>>> grid_from_strs(["1,2,3","4,5,6","7,8,9"], spl=",")
([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], 3, 3)
```

### `grid_ints_from_strs(lines, spl='')`
Given `lines` is a list of strs, each one representing a row in a grid, returns `(2D array of ints, width, height)`.

```python
>>> grid_ints_from_strs(["0000","9913", "9199", "5432"])
([[0, 0, 0, 0], [9, 9, 1, 3], [9, 1, 9, 9], [5, 4, 3, 2]], 4, 4)
```

### `grid_neighbors(p, width, height=None)`, `grid_8_neighbors(p, width, height=None)`
Given `p` is a point `(x,y)` in a grid of `width` x `height`, generates the up to four/eight neighbors of `p` that also lie within the grid. Clips at the edges of the grid, which is why this is useful!
```R
8  4  8
 \ | /
4--p--4
 / | \
8  4  8
```

*Note - `x` `y` not `row`, `col`... Matters for non-square grids*

```python
>>> list(grid_neighbors((0,0),2))
[(1, 0), (0, 1)]
>>> list(grid_neighbors((1,1),400))
[(2, 1), (0, 1), (1, 2), (1, 0)]
>>> list(grid_8_neighbors((1,1),400))
[(2, 0), (0, 0), (2, 2), (0, 2), (2, 1), (0, 1), (1, 0), (1, 2)]
```

#### `wrap(p, max_x, max_y, min_x=0, min_y=0)`
Wraps an imaginary coordinate `x + y*1j` back into a grid of size `max_x, max_y` etc. Does no modular arithmetic - i.e. `max+2 => 0`


#### print_grid(g, spacing=0, markfn=lambda r,c,ch:""):
Given `g` is a grid - a 2D array as above, print the grid. Optionally add spacing (shorter values get padded so print out is tidy). Optionally use `markfn` to apply a _mark_ to certain elements (e.g. to show a path through a grid or similar)
```python
>>> grid, _, _ = grid_from_strs(["123","456","789"])
>>> print_grid(grid, spacing=3, markfn=lambda r,c,ch:"*" if int(ch)%2==0 else "")
1  2* 3  
4* 5  6* 
7  8* 9 
```
#### print_world(world)
Given `world` is a set of imaginary numbers representing points in a 2D plane of form `x+y*1j`, prints the set as a matrix of orange (present) and black (absent) squares.
```python
>>> print_world(world)
🟧⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️🟧⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️🟧⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️🟧⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️🟧⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️🟧
```
## Cookbooks

A hashable `set`
```python
s = frozenset([1,2])
t = set(s)
t.add(3)
t = frozenset(t)
>>> t
frozenset({1, 2, 3})
```

##### `functools.cache`
```python
@cache
def expensive_fn(hashable_args):
  expensive()
```

Binary => decimal
```python
int("1001", 2)
```

Defaultdicts
```python
from collections import defaultdict

acc = defaultdict(int)
acc['z'] += 1
```
Defaultdicts of defaultdicts
```python
from collections import defaultdict

acc = defaultdict(lambda : defaultdict(int))
acc['a']['circle'] += 1
```

Copy
```python
import copy

c = copy.deepcopy(input)
```

Lists -- sum elements matching filter
```python
ones = sum(map(lambda x : x == "1", list_var))
# more pythonic
ones = sum([x == "1" for x in list_var])
# simpler
ones = list_var.count("1")
```
Lists -- filter
```python
oxy = [x for x in filter(lambda x : x[pos] == selected, oxy)]
# more pythonic
oxy = [x for x in oxy if x[pos] == selected]
```

`itertools`
https://docs.python.org/3/library/itertools.html

`groupby` -- start with a sorted string
```
>>> [list(g) for k,g in itertools.groupby('AABBBBA')]
[['A', 'A'], ['B', 'B', 'B', 'B'], ['A']] 
```

Char positions
```
>>> list(zip(itertools.count(), 'David')) 
[(0, 'D'), (1, 'a'), (2, 'v'), (3, 'i'), (4, 'd')]
```

## References
https://gist.github.com/mcpower/87427528b9ba5cac6f0c679370789661

https://www.youtube.com/watch?v=IIaj7MSFEcU&list=PLZhotmgEsCQNhE-X5bkcVvlyAMzcCqAEw

https://blog.vero.site/post/advent-leaderboard

## Notes

*Write less code*. The best/fastest competitors all have short solutions - less code equals less bugs.
