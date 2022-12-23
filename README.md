# aoc

## Cookbooks

A hashable `set`
```
s = frozenset([1,2])
t = set(s)
t.add(3)
t = frozenset(t)
>>> t
frozenset({1, 2, 3})
```

##### `functools.cache`
```
@cache
def expensive_fn(hashable_args):
  expensive()
```

Binary => decimal
```
int("1001", 2)
```

Defaultdicts
```
from collections import defaultdict

acc = defaultdict(int)
acc['z'] += 1
```
Defaultdicts of defaultdicts
```
from collections import defaultdict

acc = defaultdict(lambda : defaultdict(int))
acc['a']['circle'] += 1
```

Copy
```
import copy

c = copy.deepcopy(input)
```

Lists -- sum elements matching filter
```
ones = sum(map(lambda x : x == "1", list_var))
# more pythonic
ones = sum([x == "1" for x in list_var])
# simpler
ones = list_var.count("1")
```
Lists -- filter
```
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

## My setup

```
[browser window][VS Code           ]
[terminal A][terminal B][terminal C]
```

* Terminal A is in `~/Downloads` and running `watchexec -- cp input.txt [path to current day problem]`
   * This means as soon as I right click to download input.txt in Chrome it gets copied to the right place without me messing with the finder window. Most other folks going for speed seem to just select the content and copy to the clipboard then paste in the editor so maybe that's faster.
* Terminal B is in the current day working directory running a python REPL.
   * I use this for trying little code fragments
* Terminal C is in the current day working directory running `watchexec -- python3.10 main.py`
   * This is the one that matters - re-runs my code every time I save the source code
### Get `watchexec`
`brew install watchexec`
