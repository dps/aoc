from utils import *

D = [line.strip() for line in open("input")]


def solve(dest, initial_state, buttons):
    choices = range(0, len(buttons))
    # bfs with queue of (state, cost)
    queue = deque([(initial_state, 0)])
    visited = set()
    visited.add(tuple(initial_state))
    while len(queue):
        state, cost = queue.popleft()
        if state == dest:
            return cost
        for choice in choices:
            new_state = state[:]
            for pos in buttons[choice]:
                new_state[pos] = not new_state[pos]
            if tuple(new_state) in visited:
                continue
            visited.add(tuple(new_state))
            queue.append((new_state, cost + 1))
    return -1

tot = 0
for line in D:
    parts = line.split(' ')
    dest = [x == '#' for x in parts[0].strip('[]')]
    initial_state = [False] * len(dest)
    buttons = list(map(lambda x: list(map(int, x.strip('()').split(','))), parts[1:-1]))
    joltage = parts[-1]
    tot += solve(dest, initial_state, buttons)

print(tot)