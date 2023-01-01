from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    graph = defaultdict(lambda : [])
    for line in input:
        graph[line.split("-")[0]].append(line.split("-")[1])
        graph[line.split("-")[1]].append(line.split("-")[0])

    q = deque()
    paths = 0
    q.append(("start", [], set()))
    while len(q) > 0:
        node, path, small_visited = q.popleft()
        small_visited = deepcopy(small_visited)
        if node[0].islower():
            small_visited.add(node)
        path = (path[:])
        path.append(node)
        for next in graph[node]:
            if next == "end":
                paths += 1
            elif next[0].islower() and next in small_visited:
                continue
            else:
                q.append((next, path, small_visited))
    return paths

def part2():
    graph = defaultdict(lambda : [])
    littles = set()
    for line in input:
        left = line.split("-")[0]
        right = line.split("-")[1]
        graph[left].append(right)
        graph[right].append(left)
        if left[0].islower() and left not in ["start", "end"]:
            littles.add(left)
        if right[0].islower() and right not in ["start", "end"]:
            littles.add(right)


    q = deque()
    for little in littles:
        q.append(("start", [], set(), little))
    
    pathstrs = set()
    while len(q) > 0:
        node, path, small_visited, allowed_little = q.popleft()
        small_visited = deepcopy(small_visited)
        if node[0].islower():
            if node == allowed_little:
                allowed_little = None
            else:
                small_visited.add(node)
        path = path[:]
        path.append(node)
        for next in graph[node]:
            if next == "end":
                pathstrs.add(",".join(path + ["end"]))
            elif next[0].islower() and next in small_visited:
                continue
            else:
                q.append((next, path, small_visited, allowed_little))
    return len(pathstrs)


print(part1())
print(part2())