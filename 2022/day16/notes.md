# How it works

1. The graph is sparse in terms of nodes that have valves with non-zero flow, so find the distance between all pairs of nodes using Floyd-Warshall, and use a graph that contains only those nodes (and "AA" where we start).
2. We will track the valves opened at each step using a bitmask (more compact to store and faster to access than a `set`). So remap the positive flow string node ids (e.g. "AA") to integers, so we can use them as bit positions in that bitmask. Also compute the bitmask equivalent to every valve being open.
3. Run a depth-first search jumping from node containing a just-opened valve to each other node containing an unopened valve which we can reach in the remaining time.
4. At every step of the DFS, store the currently accumulated outflow in a state map of the currently opened valves if it is greater than we've seen already for the same set of opened valves (i.e. value of the bitmask)
5. At each node, open the valve and add the new outflow (`mins remaining * flow at this valve`) to `accumulated`
6. If all valves are open or we've run out of time, stop the DFS search tree.

The answer to part 1 is then simply the maximum outflow value we've seen across all bitmask values.

The answer to part 2 depends on the observation that you and the elephant must open disjoint sets of valves in the optimal solution. Therefore, the valves that you opened don't matter to the elephant. We've actually _already_ calculated all possible sets of valves that can be opened in the time limit in part 1 so the answer to part 2 is the maximum value of the combined outflow rates where the bitmasks are non-overlapping.

```
part2 = max([v1 + v2 for bitmask1, v1 in B.items() for bitmask2, v2 in B.items() if not bitmask1 & bitmask2])
```

This version runs part 2 *faster* than part 1 as it only needs to explore 26 mins worth of the state space. 🤯.

# Progress
## Initial DFS implementation without frozenset:
`95.10s user 1.09s system 99% cpu 1:36.24 total`
## With frozenset:
`55.31s user 1.35s system 99% cpu 56.710 total`
## With pypy:
`40.93s user 1.75s system 99% cpu 42.686 total`
## Remove non-flow valves (BFS dist table)
`39.15s user 0.39s system 99% cpu 39.555 total`
## int bitmask instead of frozenset
`34.73s user 0.48s system 99% cpu 35.222 total`
## floyd-warshall instead of BFS
`31.14s user 0.55s system 99% cpu 31.733 total`
## opened valves statemap !!!
`1.48s user 0.12s system 98% cpu 1.624 total`