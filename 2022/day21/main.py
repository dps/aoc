from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

state = {}
graph = {}

def toposort(leaves, graph):
    # Kahn's algorithm
    res = []
    s = leaves
    while len(s) > 0:
        n = s.pop()
        res.append(n)
        for dep_k,dep_v in [(k,v) for k,v in graph.items() if n in v]:
            dep_v.remove(n)
            if len(dep_v) == 0:
                s.add(dep_k)

    return res

def part1():
    leaves = set()
    for row in input:
        key = row.split(":")[0].strip()
        v = row.split(":")[1].strip()
        if " " in v:
            match = re.match(r"([a-zA-Z]+) ([+-/*]) ([a-zA-Z]+)", v).groups()
            l = match[0]
            op = match[1]
            r = match[2]
            graph[key] = [l, r]
            state[key] = 'state["' + l + '"]' + op + 'state["' + r + '"]'
        else:
            state[key] = v
            leaves.add(key)
    order = toposort(deepcopy(leaves), graph)
    for node in order:
        if state[node] not in leaves:
            state[node] = eval(state[node])
    print(state["root"])


if __name__ == '__main__':
    part1()
