
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

while True:
    # V maps node name to a list of nodes connected via edges (incl. repeats!) and a set
    # of the original nodes which have been merged in to n.
    V = {n: (list(v), set([n])) for n,v in vertices.items()}

    while len(V.keys()) > 2:
        e = random.choice(list(V.keys()))
        f = random.choice(V[e][0])
        
        u,v = V[e], V[f]

        for name,val in V.items():
            if name == e:
                V[name] = ([x for x in (u[0] + v[0]) if x != e and x != f], u[1]|v[1])
            elif name == f:
                continue
            else:
                V[name] = ([(e if d == f else d) for d in val[0]], val[1])

        del V[f]

    if len(list(V.values())[0][0]) == 3:
        aoc(reduce(operator.mul, [len(v[1]) for v in V.values()]))
        sys.exit(0)
