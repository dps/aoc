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
    return(int(state["root"]))

def part2():
    leaves = set()
    formulae = {}
    for row in input:
        key = row.split(":")[0].strip()
        v = row.split(":")[1].strip()
        if " " in v:
            match = re.match(r"([a-zA-Z]+) ([+-/*]) ([a-zA-Z]+)", v).groups()
            l = match[0]
            op = match[1]
            r = match[2]
            formulae[key] = (l,r,op)
            graph[key] = [l, r]
            state[key] = 'state["' + l + '"]' + op + 'state["' + r + '"]'
        else:
            state[key] = v
            leaves.add(key)

    # break into two sub-graphs - the one with human at leaf and the other one
    # Human subgraph 
    to_check = set(["humn"])
    in_humn_branch = {}
    while len(to_check) > 0:
        n = to_check.pop()
        nodes = [(k,v) for k,v in graph.items() if n in v]
        for k,v in nodes:
            in_humn_branch[k] = v
            to_check.add(k)
    leaves.remove("humn")
    
    # Forward compute the non-human parts of the graph
    order = toposort(deepcopy(leaves), graph)
    for node in order:
        if state[node] not in leaves:
            state[node] = eval(state[node])

    # Go _backwards_ through human branch order undoing operations
    human_order = toposort(set(["humn"]), in_humn_branch)
    human_order.reverse()

    f = formulae["root"]
    state["root"] = state[f[0]] if f[1] in human_order else state[f[1]]
    human_order.remove("root")
    acc = state["root"]
    for cell in human_order:
        if cell == "humn":
            print(acc)
            return(acc)
        formula = formulae[cell]
        op = formula[2]
        operand = None
        if type(state[formula[0]]) == str and type(state[formula[1]]) != str:
            operand = state[formula[1]]
            if op == "*": #unk * num == acc; acc = acc / num
                acc /= operand
            elif op == "/": #unk / num == acc; unk = acc * num 
                acc *= operand
            elif op == "-": #unk - num == acc; unk = acc + num
                acc += operand
            elif op == "+": #unk + num == acc; unk = acc - num
                acc -= operand
        elif type(state[formula[1]]) == str and type(state[formula[0]]) != str:
            operand = state[formula[0]]
            if op == "*": #unk * num == acc; acc = acc / num
                acc /= operand
            elif op == "/": #num / unk == acc 3/x = 4  x = 3/4 
                acc = operand / acc
            elif op == "-": #num - unk == acc; -unk = (acc - num)
                acc = operand - acc
            elif op == "+": #num + unk == acc; unk = 
                acc -= operand
        else:
            assert(False)


if __name__ == '__main__':
    assert(part1() == 49288254556480)
    assert(part2() == 3558714869436)
