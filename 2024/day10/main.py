
D = [i.strip() for i in open("input","r").readlines()]

C, R = len(D[0]), len(D)
p1, p2 = 0, 0

paths, ends = set(), set()

def dfs(p, visited):
    global paths
    visited.append(p)

    if D[int(p.imag)][int(p.real)] == "9":
        paths.add("|".join(str(int(i.real)) + "," + str(int(i.imag)) for i in visited))
        ends.add(p)
        return
    for d in [1, -1, 1j, -1j]:
        np = p + d
        if np.real < 0 or np.real >= C or np.imag < 0 or np.imag >= R:
            continue
        if int(D[int(np.imag)][int(np.real)]) == int(D[int(p.imag)][int(p.real)]) + 1:
            dfs(np, visited)


heads = []
for y, line in enumerate(D):
    for x, ch in enumerate(line):
        if ch == "0":
            heads.append((x+1j*y))

for head in heads:
    ends = set()
    dfs(head, [])
    p1 += len(ends)

paths = set()
for head in heads:
    dfs(head, [])
    p2 += len(paths)
    paths = set()

print(p1, p2)