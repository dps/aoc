from utils import *
from functools import cache

input = [i.strip() for i in open("input.txt","r").readlines()]

flow = {}
connect = {}
tvalves = 0

@cache
def dfs(here, mins_remaining, opened):
    acc = 0
    if mins_remaining <= 1: # it takes a min to open a valve
        return 0

    ## Run past case!
    best = max([dfs(c, mins_remaining-1, opened) for c in connect[here]])

    ## Open valve case
    if flow[here] > 0 and not here in opened:
        nowopened = set(opened)
        acc = (mins_remaining-1) * flow[here]
        nowopened.add(here)
        nowopened = frozenset(nowopened)
        mins_remaining -= 1 # It takes a min to open the valve
        if len(nowopened) == tvalves:
            return acc
        # It takes a min to traverse the tunnel
        best = max(best, acc + max([dfs(c, mins_remaining-1, nowopened) for c in connect[here]]))

    return best


@cache
def dfs_with_elephant(here, mins_remaining, opened):
    acc = 0
    if mins_remaining <= 1: # it takes a min to open a valve
        # Let the elephant run from the top
        return dfs("AA", 26, opened)

    ## Run past case!
    best = max([dfs_with_elephant(c, mins_remaining-1, opened) for c in connect[here]])

    ## Open valve case
    if flow[here] > 0 and not here in opened:
        nowopened = set(opened)
        acc = (mins_remaining-1) * flow[here]
        nowopened.add(here)
        nowopened = frozenset(nowopened)
        mins_remaining -= 1 # It takes a min to open the valve
        if len(nowopened) == tvalves:
            return acc
        # It takes a min to traverse the tunnel
        best = max(best, acc + max([dfs_with_elephant(c, mins_remaining-1, nowopened) for c in connect[here]]))

    return best

def solve(part=1):
    global tvalves

    for row in input:
        # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
        valve = row.split(" ")[1]
        rate = int(row.split("rate=")[1].split(";")[0])
        if rate > 0:
            tvalves += 1
        if "lead to valves " in row:
            tunnels = row.split("lead to valves ")[1].split(", ")
        else:
            tunnels = [row.split("leads to valve ")[1]]
        flow[valve] = rate
        connect[valve] = tunnels

    if part == 1:
        return(dfs("AA", 30, frozenset()))
    if part == 2:
        return(dfs_with_elephant("AA", 26, frozenset()))


if __name__ == '__main__':
    assert(solve(1) == 2320)
    assert(solve(2) == 2967)


# Without frozenset:
## time python main.py 
## python main.py  95.10s user 1.09s system 99% cpu 1:36.24 total
# With frozenset:
## python main.py  55.31s user 1.35s system 99% cpu 56.710 total