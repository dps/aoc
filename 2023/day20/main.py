
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

dests = defaultdict(list)
types = defaultdict(str)
states = {}
inv_states = defaultdict(lambda : defaultdict(bool))
inputs = defaultdict(list)
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

Q = deque([])

lows,highs = 0,0

def tally(src, val, dest):
    global lows, highs
    if val:
        highs += 1
    else:
        lows += 1

critical_inputs = inputs[inputs["rx"][0]]
loops = {i:[] for i in critical_inputs}
step = 0
while True:  
    Q.append(("broadcaster", False, None))
    lows += 1
    while Q:
        n,signal,from_ = Q.popleft()
        if n in critical_inputs and signal == False:
            loops[n].append(step)
        if all([len(l) > 1 for _,l in loops.items()]):
            print("Part 2", math.lcm(*[l[1] - l[0] for l in loops.values()]))
            sys.exit(0)
        action = types[n]
        if action == "broadcast":
            for d in dests[n]:
                Q.append((d, signal, n))
                tally(n, signal, d)
        if action == "%":
            if not signal:
                states[n] = not states[n]
                for d in dests[n]:
                    Q.append((d,states[n],n))
                    tally(n, states[n], d)
        if action == "&":
            inv_states[n][from_] = signal
            if all([v == True for v in inv_states[n].values()]):
                for d in dests[n]:
                    Q.append((d,False,n))
                    tally(n, False, d)
            else:
                for d in dests[n]:
                    Q.append((d,True,n))
                    tally(n, True, d)
    if step == 999:
        print("Part 1", lows*highs)
    step += 1