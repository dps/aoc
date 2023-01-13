import heapq
import math
from functools import partial
from collections import defaultdict

TARGET = {'A':0,'B':1,'C':2,'D':3}
COST = {'A':1, 'B':10, 'C':100, 'D':1000}

def clear_from_room_to_spot(r, s, z):
    if r == 0 and s == 0 : return z[1]=='' and z[0]=='', 3
    elif r == 0 and s == 1 : return z[1]=='', 2
    elif r == 0 and s == 2 : return z[2]=='', 2
    elif r == 0 and s == 3 : return z[2]=='' and z[3]=='', 4
    elif r == 0 and s == 4 : return z[2]=='' and z[3]=='' and z[4]=='', 6
    elif r == 0 and s == 5 : return z[2]=='' and z[3]=='' and z[4]=='' and z[5]=='', 8
    elif r == 0 and s == 6 : return z[2]=='' and z[3]=='' and z[4]=='' and z[5]=='' and z[6]=='', 9
    elif r == 1 and s == 0 : return z[2]=='' and z[1]=='' and z[0]=='', 5
    elif r == 1 and s == 1 : return z[2]=='' and z[1]=='', 4
    elif r == 1 and s == 2 : return z[2]=='', 2
    elif r == 1 and s == 3 : return z[3]=='', 2
    elif r == 1 and s == 4 : return z[3]=='' and z[4]=='', 4
    elif r == 1 and s == 5 : return z[3]=='' and z[4]=='' and z[5]=='', 6
    elif r == 1 and s == 6 : return z[3]=='' and z[4]=='' and z[5]=='' and z[6]=='', 7
    elif r == 2 and s == 0 : return z[3]=='' and z[2]=='' and z[1]=='' and z[0]=='', 7
    elif r == 2 and s == 1 : return z[3]=='' and z[2]=='' and z[1]=='', 6
    elif r == 2 and s == 2 : return z[3]=='' and z[2]=='', 4
    elif r == 2 and s == 3 : return z[3]=='', 2
    elif r == 2 and s == 4 : return z[4]=='', 2
    elif r == 2 and s == 5 : return z[4]=='' and z[5]=='', 4
    elif r == 2 and s == 6 : return z[4]=='' and z[5]=='' and z[6]=='', 5
    elif r == 3 and s == 0 : return z[4]=='' and z[3]=='' and z[2]=='' and z[1]=='' and z[0]=='', 9
    elif r == 3 and s == 1 : return z[4]=='' and z[3]=='' and z[2]=='' and z[1]=='', 8
    elif r == 3 and s == 2 : return z[4]=='' and z[3]=='' and z[2]=='', 6
    elif r == 3 and s == 3 : return z[4]=='' and z[3]=='', 4
    elif r == 3 and s == 4 : return z[4]=='', 2
    elif r == 3 and s == 5 : return z[5]=='', 2
    elif r == 3 and s == 6 : return z[5]=='' and z[6]=='', 3

def clear_from_room_to_spot_exclusive(r, s, z):
    if r == 0 and s == 0 : return z[1]=='', 3
    elif r == 0 and s == 1 : return True, 2
    elif r == 0 and s == 2 : return True, 2
    elif r == 0 and s == 3 : return z[2]=='', 4
    elif r == 0 and s == 4 : return z[2]=='' and z[3]=='', 6
    elif r == 0 and s == 5 : return z[2]=='' and z[3]=='' and z[4]=='', 8
    elif r == 0 and s == 6 : return z[2]=='' and z[3]=='' and z[4]=='' and z[5]=='', 9
    elif r == 1 and s == 0 : return z[2]=='' and z[1]=='', 5
    elif r == 1 and s == 1 : return z[2]=='', 4
    elif r == 1 and s == 2 : return True, 2
    elif r == 1 and s == 3 : return True, 2
    elif r == 1 and s == 4 : return z[3]=='', 4
    elif r == 1 and s == 5 : return z[3]=='' and z[4]=='', 6
    elif r == 1 and s == 6 : return z[3]=='' and z[4]=='' and z[5]=='', 7
    elif r == 2 and s == 0 : return z[3]=='' and z[2]=='' and z[1]=='', 7
    elif r == 2 and s == 1 : return z[3]=='' and z[2]=='', 6
    elif r == 2 and s == 2 : return z[3]=='', 4
    elif r == 2 and s == 3 : return True, 2
    elif r == 2 and s == 4 : return True, 2
    elif r == 2 and s == 5 : return z[4]=='', 4
    elif r == 2 and s == 6 : return z[4]=='' and z[5]=='', 5
    elif r == 3 and s == 0 : return z[4]=='' and z[3]=='' and z[2]=='' and z[1]=='', 9
    elif r == 3 and s == 1 : return z[4]=='' and z[3]=='' and z[2]=='', 8
    elif r == 3 and s == 2 : return z[4]=='' and z[3]=='', 6
    elif r == 3 and s == 3 : return z[4]=='', 4
    elif r == 3 and s == 4 : return True, 2
    elif r == 3 and s == 5 : return True, 2
    elif r == 3 and s == 6 : return z[5]=='', 3

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
                    next_rooms = s[:room] + (now_in_room,) + s[room+1:-1]
                    next_state = next_rooms + ((s[4][:spot] + (in_doorway,) + s[4][spot+1:]),)
                    steps += room_size - len(s[room])
                    cost = steps * COST[in_doorway]
                    next_states.append((cost, next_state))
    # Now look at clearing the hallway
    for spot in range(7):
        if s[4][spot] != '':
            in_spot = s[4][spot]
            target_room = ord(in_spot)-65#TARGET[in_spot]
            # "and that room contains no amphipods which do not also have that room as their own destination."
            has_space = len(s[target_room]) < room_size and all([a == in_spot for a in s[target_room]])
            if has_space:
                clear, steps = clear_from_room_to_spot_exclusive(target_room, spot, s[4])
                if clear:
                    now_in_room = (in_spot,) + s[target_room]
                    next_rooms = s[:target_room] + (now_in_room,) + s[target_room+1:-1]
                    next_state = next_rooms + ((s[4][:spot] + ('',) + s[4][spot+1:]),)
                    steps += room_size - 1 - len(s[target_room])
                    cost = steps * COST[in_spot]
                    next_states.append((cost, next_state))

    return next_states

def dynamic_a_star(next_fn, start, end, heuristic):
    """
    next_fn is a funtion taking vertex => [(weight, neighbor), ...] 
    heuristic is a function that takes in a vertex and returns an estimated cost
    to reach the end from that vertex
    returns (sum(path weights), path)
    """
    
    # Initialize data structures
    distances = defaultdict(lambda: math.inf)
    distances[start] = 0
    previous = defaultdict(lambda: None)
    queue = []
    heapq.heappush(queue, (0, 0, start))
    
    # Loop until the queue is empty
    while queue:
        _, current_distance, current_vertex = heapq.heappop(queue)
        
        # End search if we have reached the end
        if current_vertex == end:
            break
            
        # Update the distances and previous vertices of the neighbors
        for weight, neighbor in next_fn(current_vertex):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                priority = distance + heuristic(neighbor, end)
                heapq.heappush(queue, (priority, distance, neighbor))
    
    # Build the path
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    
    return (distances[end], path[::-1])

def heuristic(n,_):
    acc = 0
    for room in range(4):
        for c in n[room]:
            if TARGET[c] != room:
                acc += abs(TARGET[c]-room)*3*COST[c]
    for spot in range(7):
        if n[4][spot] != '': acc += COST[n[4][spot]]*abs(TARGET[n[4][spot]]-spot)
    return acc

def part1():
    global start_state, end_state
    start_state = (('B', 'C'), ('B', 'A'), ('D', 'A'), ('D','C'), ('', '', '', '', '', '', ''))
    end_state = (('A','A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('', '', '', '', '', '', ''))
    print(dynamic_a_star(partial(next_states, 2), start_state, end_state, heuristic)[0])

def part2():
    global start_state, end_state
    end_state = (('A','A','A','A'), ('B', 'B', 'B', 'B'), ('C', 'C', 'C', 'C'), ('D', 'D', 'D', 'D'), ('', '', '', '', '', '', ''))
    start_state = (('B', 'D', 'D', 'C'), ('B', 'C', 'B', 'A'), ('D', 'B', 'A', 'A'), ('D', 'A', 'C', 'C'), ('', '', '', '', '', '', ''))
    print(dynamic_a_star(partial(next_states, 4), start_state, end_state, heuristic)[0])

part1() # 10607, dijkstra - 1.49s, A* - 0.785
part2() # 59071, dijkstra - 1.3s, A* - 1.041

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
                    v += "z[" ==''+ str(z) + "]"
                    if z == spot:
                        break
                print("if r ==", room, "and s ==", spot, ": return " + v)
            if spot in right:
                for z in right:
                    if len(v) > 0: v += " and "
                    v += "z[" ==''+ str(z) + "]"
                    if z == spot:
                        break

                print("if r ==", room, "and s ==", spot, ": return " + v)

#write_my_code()