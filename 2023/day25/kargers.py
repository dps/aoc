
from utils import *
import random

D = [i.strip() for i in open("input","r").readlines()]

vertices = defaultdict(set)
for line in D:
    from_, to_ = line.split(":")
    to_ = to_.strip()
    vertices[from_].update(to_.split(" "))
    for e in to_.split(" "):
        vertices[e].add(from_)

def kargers(vertices):
    while True:
        # Implementation based on https://en.wikipedia.org/wiki/Karger%27s_algorithm
        # V maps node name to a list of nodes connected via edges (incl. repeats!) and a set
        # of the original nodes which have been merged in to n.
        V = {n: (list(v), set([n])) for n,v in vertices.items()}

        while len(V.keys()) > 2:
            e = random.choice(list(V.keys()))
            f = random.choice(V[e][0])

            u,v = V[e], V[f]

            for edge in v[0]:
                if edge != e and edge != f:
                    u[0].append(edge)
                    V[edge][0].remove(f)
                    V[edge][0].append(e)
            V[e] = ([d for d in u[0] if d != f], u[1]|v[1])

            del V[f]

        if len(list(V.values())[0][0]) == 3:
            return reduce(operator.mul, [len(v[1]) for v in V.values()])

print(kargers(vertices))