from utils import *

D = [line.strip() for line in open("input")]

def cartesian3(p, q):
    return math.sqrt(
        abs(p[0] - q[0]) * abs(p[0] - q[0]) + abs(p[1] - q[1]) * abs(p[1] - q[1]) + abs(p[2] - q[2]) * abs(p[2] - q[2])
    )


points = set()
for line in D:
    x,y,z = map(int, line.split(","))
    points.add((x,y,z))

pairs = combinations(points, 2)
dists = sorted(map(lambda pair: (cartesian3(pair[0], pair[1]), pair[0], pair[1]), pairs))


for r in [1000, 10000]:
    in_circuit = {}
    circuits = defaultdict(set)
    next_circuit = 0

    for i in range(r):
        pair = dists[i][1], dists[i][2]
        circuit = None
        add = []
        if pair[0] in in_circuit:
            add.append(in_circuit[pair[0]])
        if pair[1] in in_circuit:
            add.append(in_circuit[pair[1]])

        if len(add) == 0:
            circuits[next_circuit].add(pair[0])
            circuits[next_circuit].add(pair[1])
            in_circuit[pair[0]] = next_circuit
            in_circuit[pair[1]] = next_circuit
            next_circuit += 1

        if len(add) == 1:
            circuits[add[0]].add(pair[0])
            circuits[add[0]].add(pair[1])
            in_circuit[pair[0]] = add[0]
            in_circuit[pair[1]] = add[0]

        if len(add) == 2:
            # Merge the circuits!
            dest = add[0]
            src = add[1]
            if dest == src:
                continue
            circuits[dest] |= circuits[src]
            for node in circuits[src]:
                in_circuit[node] = dest
            del circuits[src]
            circuits[dest].add(pair[0])
            circuits[dest].add(pair[1])
            in_circuit[pair[0]] = dest
            in_circuit[pair[1]] = dest

        if len(circuits) == 1:
            c = 0
            for p in points:
                if p not in in_circuit:
                    c += 1
            if c == 0:
                print(pair[0][0] * pair[1][0])
                exit(0)

    top3 = sorted(map(lambda x: (len(x), x), circuits.values()), reverse=True)[0:3]
    print(reduce(operator.mul, map(lambda x:x[0], top3)))