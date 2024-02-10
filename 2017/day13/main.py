import re

def ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))

D = [i.strip() for i in open("input","r").readlines()]

layers = {}

mx = 0
for line in D:
    d,r = ints(line)
    layers[d] = r
    mx = max(mx, d)

def looplen(d):
    return (d-1)*2 if d > 1 else d

def probe(w):
    sev = 0
    for p in range(mx+1):
        if p in layers:
            if (p+w) % looplen(layers[p]) == 0:
                sev += p*layers[p]
    return sev

def probe_break_early(w):
    for p in range(mx+1):
        if p in layers:
            if (p+w)%looplen(layers[p]) == 0:
                return False
    return True

print(probe(0))

for i in range(10000000):
    if probe_break_early(i):
        print(i)
        break