
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]

dests = defaultdict(list)
types = defaultdict(str)
states = {}
inv_states = defaultdict(lambda : defaultdict(bool))
inputs = defaultdict(list)
for line in D:
    name,ds = line.split(" -> ")
    print(name)
    if name.startswith("%") or name.startswith("&"):
        tmp = name[0]
        name = name[1:]
        types[name] = tmp
        print("***", name, types[name])
    else:
        types[name] = "broadcast"
    states[name] = False
    dests[name] = [d.strip() for d in ds.split(",")]
    for d in dests[name]:
        inputs[d].append(name)
        inv_states[d][name] = False
types["output"] = None
types["output"] = None

print(dests, types)

Q = deque([])

# Flip-flop modules (prefix %) are either on or off; they are initially off.
# If a flip-flop module receives a high pulse, it is ignored and nothing happens.
# However, if a flip-flop module receives a low pulse, it flips between on and off.
# If it was off, it turns on and sends a high pulse. If it was on, it turns off and
# sends a low pulse.

# Conjunction modules (prefix &) remember the type of the most recent pulse received
# from each of their connected input modules; they initially default to remembering
# a low pulse for each input. When a pulse is received, the conjunction module first
# updates its memory for that input. Then, if it remembers high pulses for all
# inputs, it sends a low pulse; otherwise, it sends a high pulse.

lows,highs = 0,0

def tally(src, val, dest):
    print("tally", src, val, dest)
    global lows, highs
    if val:
        highs += 1
    else:
        lows += 1

for step in range(1000):
    Q.append(("broadcaster", False, None))
    lows += 1
    while Q:
        n,signal,from_ = Q.popleft()
        print("BUS", n,signal,from_)
        action = types[n]
        if action == "broadcast":
            for d in dests[n]:
                Q.append((d, signal, n))
                tally(n, signal, d)
        if action == "%":
            print("%%%%%%", n)
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

print(lows, highs, lows*highs)
                
