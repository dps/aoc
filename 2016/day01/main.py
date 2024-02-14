
def manhattani(p, q):
    return int(abs(p.real - q.real) + abs(p.imag - q.imag))

D = [i.strip() for i in open("input","r").readlines()]

pos = 0
d = -1j
p2_done = False
visited = set()
visited.add(pos)
for move in D[0].split(", "):
    turn, steps = move[0], int(move[1:])
    if turn == "R":
        d *= 1j
    if turn == "L":
        d *= -1j

    for _ in range(steps):
        pos += d
        if pos in visited and not p2_done:
            print("part 2", manhattani(0, pos))
            p2_done = True
        visited.add(pos)

print("part 1", manhattani(0, pos))
