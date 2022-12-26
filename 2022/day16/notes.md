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