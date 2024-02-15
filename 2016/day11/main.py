
from utils import *

# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

# An elerium generator.
# An elerium-compatible microchip.
# A dilithium generator.
# A dilithium-compatible microchip.
start = (frozenset({"el-g", "el-c", "di-g","di-c","pr-g", "pr-c", "e"}), frozenset({"co-g", "cu-g", "ru-g", "pl-g"}),
         frozenset({"co-c", "cu-c", "ru-c", "pl-c"}), frozenset())
end = (frozenset(),frozenset(),frozenset(),frozenset({"pr-g", "pr-c", "e","co-g", "cu-g", "ru-g", "pl-g","co-c", "cu-c", "ru-c", "pl-c", "el-g", "el-c", "di-g","di-c"}))

floor_neighbors = {0: {1}, 1:{0,2}, 2:{1,3}, 3:{2}}

@cache
def valid(items):
    if all([e[-1] == "g" for e in items]):
        return True
    if all([e[-1] == "c" for e in items]):
        return True
    for i in items:
        ele,typ = i.split("-")
        if typ == "c":
            if f"{ele}-g" not in items:
                return False
    return True

@cache
def neighbors(state):
    #print("neigbors ", state)
    floor,items = [(f,s) for f,s in enumerate(state) if "e" in s][0]
    next_floors = list(floor_neighbors[floor])
    brings = list(combinations((items - {"e"}), 2)) + list(combinations((items - {"e"}), 1))
    candidates = list(product(next_floors, brings))
    #print(candidates)
    for next_floor, bring in candidates:
        if len(bring) > 1:
            if bring[0][-1] != bring[1][-1] and bring[0][0:2] != bring[1][0:2]:
                continue
        nxt = frozenset(state[next_floor] | set(bring))
        current = frozenset(state[floor] - {"e"} - set(bring))
        if valid(nxt) and valid(current):
            nxt = frozenset(nxt | {"e"})
            ss = tuple(i if (f != floor and f != next_floor) else nxt if f==next_floor else current for f,i in enumerate(state))
            #print("--->", ss)
            yield (1, ss)
            

# for i in neighbors(start):
#     print(i)

print(dynamic_dijkstra(neighbors, start, end)[0])
