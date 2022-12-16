from utils import *
import networkx as nx
from networkx.algorithms import tournament

input = [i.strip() for i in open("simple.txt","r").readlines()]

flow = {}
connect = {}
tvalves = 0

memo = {}

def dfs(here, mins_remaining, opened):
    #print(here, mins_remaining, opened)
    if (here, mins_remaining, opened) in memo:
        return memo[(here, mins_remaining, opened)]
    acc = 0
    if mins_remaining <= 1: # it takes a min to open a valve
        memo[(here, mins_remaining, opened)] = 0
        return 0
    nowopened = opened


    #print("NO", nowopened)
    ## Run past case!
    best = max([dfs(c, mins_remaining-1, nowopened) for c in connect[here]])

    ## Hmm, you can also run past
    if flow[here] > 0 and not here in opened:
        acc = (mins_remaining-1) * flow[here]
        nowopened = opened + (here,)
        nowopened = tuple(sorted(nowopened)) # gah need to make them equal like sets!
        mins_remaining -= 1 # It takes a min to open the valve
        if len(nowopened) == tvalves:
            memo[(here, mins_remaining, opened)] = acc
            return acc
        # It takes a min to traverse the tunnel
        best = max(best, acc + max([dfs(c, mins_remaining-1, nowopened) for c in connect[here]]))

    memo[(here, mins_remaining, opened)] = best
    return best

def dfs_with_elephant(here, elephant, mins_remaining, opened):
    #(here, elephant, mins_remaining, opened)
    if (here, elephant, mins_remaining, opened) in memo:
        return memo[(here, elephant, mins_remaining, opened)]
    if mins_remaining <= 1: # it takes a min to open a valve
        memo[(here, elephant, mins_remaining, opened)] = 0
        return 0
    nowopened = opened

    best = 0
    # Can now be:
    # m e
    # R R
    # R O
    # O R
    # O O

    # * == stay here and open the valve
    places_for_me_to_go = connect[here]
    if flow[here] > 0 and not here in opened:
        places_for_me_to_go = places_for_me_to_go + ["*"]
    places_for_elephant_to_go = connect[elephant]
    if flow[elephant] > 0 and not elephant in opened:
        places_for_elephant_to_go = places_for_elephant_to_go + ["*"]

    combos = [x for x in itertools.product(places_for_me_to_go, places_for_elephant_to_go) if x[0] == "*" or x[1] == "*" or x[0] != x[1]]

    #print(combos)

    # 0 is what I do, 1 is elephant
    for x in combos:
        if x[0] == "*" and x[1] == "*":
            acc = (mins_remaining - 1) * flow[here] + (mins_remaining - 1) * flow[elephant]
            nowopened = opened + (here,elephant)
            nowopened = tuple(sorted(nowopened)) # gah need to make them equal like sets!
            if len(nowopened) == tvalves:
                memo[(here, elephant, mins_remaining, opened)] = acc
                return acc
            best = max(best, acc + dfs_with_elephant(here, elephant, mins_remaining-1, nowopened))

        elif x[0] == "*":
            acc = (mins_remaining - 1) * flow[here]
            nowopened = opened + (here,)
            nowopened = tuple(sorted(nowopened)) # gah need to make them equal like sets!
            if len(nowopened) == tvalves:
                memo[(here, elephant, mins_remaining, opened)] = acc
                return acc
            best = max(best, acc + dfs_with_elephant(here, x[1], mins_remaining-1, nowopened))
        elif x[1] == "*":
            acc = (mins_remaining - 1) * flow[elephant]
            nowopened = opened + (elephant,)
            nowopened = tuple(sorted(nowopened)) # gah need to make them equal like sets!
            if len(nowopened) == tvalves:
                memo[(here, elephant, mins_remaining, opened)] = acc
                return acc
            best = max(best, acc + dfs_with_elephant(x[0], elephant, mins_remaining-1, nowopened))
        else:
            best = max(best, dfs_with_elephant(x[0], x[1], mins_remaining-1, nowopened))

    memo[(here, mins_remaining, opened)] = best
    return best

def part1():
    global tvalves
    graph = nx.DiGraph()

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
        graph.add_node(valve)
        for tunnel in tunnels:
            graph.add_edge(valve, tunnel)

    #print(tvalves)
    # # Idea 1: DFS stopping at 30 mins... big input has 60 valves
    max = dfs("AA", 30, ())
    print(max)


    # Idea 2 -- turn the whole thing into a graph, then find longest path

    #print([p for p in nx.all_simple_paths(graph, "AA", "BB")])

def part2():
    global tvalves
    graph = nx.DiGraph()

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
        graph.add_node(valve)
        for tunnel in tunnels:
            graph.add_edge(valve, tunnel)

    #print(tvalves)
    # # Idea 1: DFS stopping at 30 mins... big input has 60 valves
    max = dfs_with_elephant("AA", "AA", 26, ())
    print(max)


if __name__ == '__main__':
    #part1()
    part2()