# aoc

## Cookbooks

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
```
Lists -- filter
```
oxy = [x for x in filter(lambda x : x[pos] == selected, oxy)]
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