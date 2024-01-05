| Problem | baseline (s) | CPU | runtime (s) | notes |
| --- | --- | --- | --- | --- |
|day01|0.126|96% cpu |0.044 | switched to a non-regex soln for 3x speedup |
|day02|0.040|97% cpu |0.039 |
|day03|0.211|96% cpu |0.030 |
|day04|0.035|96% cpu |0.034 |
|day05|0.037|96% cpu |0.037 |
|day06|0.140|96% cpu |0.032 |
|day07|0.088|96% cpu |0.082 | poker, minor speedups |
|day08|0.041|97% cpu |0.041 |
|day09|0.076|92% cpu |0.064 | copy vs deepcopy |
|day10|0.062|97% cpu |0.061 |
|day11|0.073|96% cpu |0.042 | minor speedups |
|day12|0.413|99% cpu |0.279 | DP, seems close to optimal, tried minor tweaks |
|day13|0.047|97% cpu |0.046 |
|day14|0.514|99% cpu |0.334 | stones roll on grid, soln optimized |
|day15|0.048|97% cpu |0.048 |
|day16|0.940|99% cpu|0.319 | beams, "." follow and don't enter from seen exits |
|day17|1.057|99% cpu |0.471 | Clumsy Crucible, BucketHeap 37% speedup |
|day18|0.040|96% cpu |0.033 |
|day19|0.065|95% cpu |0.045 | Already super fast |
|day20|0.188|98% cpu |0.107 | Algo tweaks |
|day21|8.463|97% cpu |0.108 | Huge speedup by reusing state from previous steps |
|day22|2.412|99% cpu|0.215 | New algo for pt2 - supports vs drop bricks |
|day23|16.810|99% cpu|0.327 | Remapped graph to ints, split search start -> end, end -> start |
|day24|1.110|99% cpu |0.252 | Moved to Z3, faster than sympy |
|day25|0.300|98% cpu |0.132 | Implemented Karger's instead of networkx |

`parallel ./run.sh {} > /dev/null  10.62s user 1.11s system 767% cpu 1.528 total`

