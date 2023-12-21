
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

# The graph
dests, inputs, types = defaultdict(list), defaultdict(list), defaultdict(str)

# State tracking
states, inv_states = {}, defaultdict(lambda : defaultdict(bool))

for line in D:
    name,ds = line.split(" -> ")
    if name.startswith("%") or name.startswith("&"):
        tmp = name[0]
        name = name[1:]
        types[name] = tmp
    else:
        types[name] = "broadcast"
    states[name] = False
    dests[name] = [d.strip() for d in ds.split(",")]
    for d in dests[name]:
        inputs[d].append(name)
        inv_states[d][name] = False

Q, lows, highs = deque([]), 0, 0

def transmit(dests, val, src):
    global Q, lows, highs
    for dest in dests:
        Q.append((dest, val, src))
        if val:
            highs += 1
        else:
            lows += 1

critical_inputs = inputs[inputs["rx"][0]]
loops = {i:[] for i in critical_inputs}
step = 0
while True:
    transmit(["broadcaster"], False, "button")
    while Q:
        n,signal,from_ = Q.popleft()
        if n in critical_inputs and signal == False:
            loops[n].append(step)
        if all([len(s) > 1 for _,s in loops.items()]):
            print("Part 2", math.lcm(*[l[1] - l[0] for l in loops.values()]))
            sys.exit(0)
        action = types[n]
        if action == "broadcast":
            transmit(dests[n],signal,n)
        if action == "%":
            if not signal:
                states[n] = not states[n]
                transmit(dests[n],states[n],n)
        if action == "&":
            inv_states[n][from_] = signal
            if all([v == True for v in inv_states[n].values()]):
                transmit(dests[n], False, n)
            else:
                transmit(dests[n], True, n)
    if step == 999:
        print("Part 1", lows*highs)
    step += 1