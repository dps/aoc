import heapq
import math
from functools import partial

TARGET = {'A':0,'B':1,'C':2,'D':3}
COST = {'A':1, 'B':10, 'C':100, 'D':1000}

def clear_from_room_to_spot(r, s, z):
    if r == 0 and s == 0 : return not z[1] and not z[0], 3
    if r == 0 and s == 1 : return not z[1], 2
    if r == 0 and s == 2 : return not z[2], 2
    if r == 0 and s == 3 : return not z[2] and not z[3], 4
    if r == 0 and s == 4 : return not z[2] and not z[3] and not z[4], 6
    if r == 0 and s == 5 : return not z[2] and not z[3] and not z[4] and not z[5], 8
    if r == 0 and s == 6 : return not z[2] and not z[3] and not z[4] and not z[5] and not z[6], 9
    if r == 1 and s == 0 : return not z[2] and not z[1] and not z[0], 5
    if r == 1 and s == 1 : return not z[2] and not z[1], 4
    if r == 1 and s == 2 : return not z[2], 2
    if r == 1 and s == 3 : return not z[3], 2
    if r == 1 and s == 4 : return not z[3] and not z[4], 4
    if r == 1 and s == 5 : return not z[3] and not z[4] and not z[5], 6
    if r == 1 and s == 6 : return not z[3] and not z[4] and not z[5] and not z[6], 7
    if r == 2 and s == 0 : return not z[3] and not z[2] and not z[1] and not z[0], 7
    if r == 2 and s == 1 : return not z[3] and not z[2] and not z[1], 6
    if r == 2 and s == 2 : return not z[3] and not z[2], 4
    if r == 2 and s == 3 : return not z[3], 2
    if r == 2 and s == 4 : return not z[4], 2
    if r == 2 and s == 5 : return not z[4] and not z[5], 4
    if r == 2 and s == 6 : return not z[4] and not z[5] and not z[6], 5
    if r == 3 and s == 0 : return not z[4] and not z[3] and not z[2] and not z[1] and not z[0], 9
    if r == 3 and s == 1 : return not z[4] and not z[3] and not z[2] and not z[1], 8
    if r == 3 and s == 2 : return not z[4] and not z[3] and not z[2], 6
    if r == 3 and s == 3 : return not z[4] and not z[3], 4
    if r == 3 and s == 4 : return not z[4], 2
    if r == 3 and s == 5 : return not z[5], 2
    if r == 3 and s == 6 : return not z[5] and not z[6], 3

def clear_from_room_to_spot_exclusive(r, s, z):
    if r == 0 and s == 0 : return not z[1], 3
    if r == 0 and s == 1 : return True, 2
    if r == 0 and s == 2 : return True, 2
    if r == 0 and s == 3 : return not z[2], 4
    if r == 0 and s == 4 : return not z[2] and not z[3], 6
    if r == 0 and s == 5 : return not z[2] and not z[3] and not z[4], 8
    if r == 0 and s == 6 : return not z[2] and not z[3] and not z[4] and not z[5], 9
    if r == 1 and s == 0 : return not z[2] and not z[1], 5
    if r == 1 and s == 1 : return not z[2], 4
    if r == 1 and s == 2 : return True, 2
    if r == 1 and s == 3 : return True, 2
    if r == 1 and s == 4 : return not z[3], 4
    if r == 1 and s == 5 : return not z[3] and not z[4], 6
    if r == 1 and s == 6 : return not z[3] and not z[4] and not z[5], 7
    if r == 2 and s == 0 : return not z[3] and not z[2] and not z[1], 7
    if r == 2 and s == 1 : return not z[3] and not z[2], 6
    if r == 2 and s == 2 : return not z[3], 4
    if r == 2 and s == 3 : return True, 2
    if r == 2 and s == 4 : return True, 2
    if r == 2 and s == 5 : return not z[4], 4
    if r == 2 and s == 6 : return not z[4] and not z[5], 5
    if r == 3 and s == 0 : return not z[4] and not z[3] and not z[2] and not z[1], 9
    if r == 3 and s == 1 : return not z[4] and not z[3] and not z[2], 8
    if r == 3 and s == 2 : return not z[4] and not z[3], 6
    if r == 3 and s == 3 : return not z[4], 4
    if r == 3 and s == 4 : return True, 2
    if r == 3 and s == 5 : return True, 2
    if r == 3 and s == 6 : return not z[5], 3

def dynamic_dijkstra(neighbors, start, end):
    """
    neighbors is a function which takes current node and returns a list of (weight, neighbor)
    pairs or () if no neighbors exist.
    returns (sum(path weights), path)
    """
    q, seen, mins = [(0,start,[])], set(), {start: 0}
    while q:
        (cost,v,path) = heapq.heappop(q)
        if v not in seen:
            seen.add(v)
            path = path + [v]
            if v == end:
                return (cost, path)

            for c, neighbor in neighbors(v):
                if neighbor in seen:
                    continue
                prev = mins.get(neighbor, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[neighbor] = next
                    heapq.heappush(q, (next, neighbor, path))

    return math.inf, None

start_state = None
end_state = None

def next_states(room_size, s):
    next_states = []
    for room in range(4):
        if s[room] != end_state[room] and len(s[room]) > 0:
            # We only need to look at moves to buffer spots on the way out (next phase will bring in)
            in_doorway = s[room][0]
            for spot in range(7):
                clear, steps = clear_from_room_to_spot(room, spot, s[4])
                if clear:
                    now_in_room = s[room][1:]
                    next_rooms = tuple(s[i] if i != room else now_in_room for i in range(4))
                    next_hallway = tuple(s[4][i] if i != spot else in_doorway for i in range(7))
                    next_state = next_rooms + (next_hallway,)
                    steps += room_size - len(s[room])
                    cost = steps * COST[in_doorway]
                    next_states.append((cost, next_state))
    # Now look at clearing the hallway
    for spot in range(7):
        if s[4][spot] != '':
            in_spot = s[4][spot]
            target_room = TARGET[in_spot]
            # "and that room contains no amphipods which do not also have that room as their own destination."
            has_space = len(s[target_room]) < room_size and all([a == in_spot for a in s[target_room]])
            if has_space:
                clear, steps = clear_from_room_to_spot_exclusive(target_room, spot, s[4])
                if clear:
                    now_in_room = (in_spot,) + s[target_room]
                    next_rooms = tuple(s[i] if i != target_room else now_in_room for i in range(4))
                    next_hallway = tuple(s[4][i] if i != spot else '' for i in range(7))
                    next_state = next_rooms + (next_hallway,)
                    steps += room_size - 1 - len(s[target_room])
                    cost = steps * COST[in_spot]
                    next_states.append((cost, next_state))

    return next_states if len(next_states) else ()

def part1():
    global start_state, end_state
    start_state = (('B', 'C'), ('B', 'A'), ('D', 'A'), ('D','C'), ('', '', '', '', '', '', ''))
    end_state = (('A','A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('', '', '', '', '', '', ''))
    print(dynamic_dijkstra(partial(next_states, 2), start_state, end_state)[0])

def part2():
    global start_state, end_state
    end_state = (('A','A','A','A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'), ('', '', '', '', '', '', ''))
    start_state = (('B', 'D', 'D', 'C'), ('B', 'C', 'B', 'A'), ('D', 'B', 'A', 'A'), ('D', 'A', 'C', 'C'), ('', '', '', '', '', '', ''))
    print(dynamic_dijkstra(partial(next_states, 4), start_state, end_state)[0])

part1() # 10607, dijkstra - 1.49s
part2() # 59071, dijkstra - 1.3s

#### "Appendix"

def write_my_code(): # This writes the code for clear_from_room_to_spot
    data = [0, 1, "0", 2, "1", 3, "2", 4, "3", 5 ,6]
    for room in "0123":
        left = []
        right = []

        found = False
        for x in data:
            if x == room:
                found = True
            if type(x) == int:
                if not found:
                    left.append(x)
                else:
                    right.append(x)
        left.reverse()
        for spot in range(7):
            v = ""
            if spot in left:
                for z in left:
                    if len(v) > 0: v += " and "
                    v += "not z[" + str(z) + "]"
                    if z == spot:
                        break
                print("if r ==", room, "and s ==", spot, ": return " + v)
            if spot in right:
                for z in right:
                    if len(v) > 0: v += " and "
                    v += "not z[" + str(z) + "]"
                    if z == spot:
                        break

                print("if r ==", room, "and s ==", spot, ": return " + v)

#write_my_code()