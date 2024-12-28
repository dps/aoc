
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def mix(val, secret):
    return val ^ secret

def prune(secret):
    return secret % 16777216

def evolve(secret):
    secret = prune(mix(secret*64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret

deltas = defaultdict(dict)
sums = defaultdict(int)

p1 = 0
for i, line in enumerate(D):
    secret = int(line)
    prevs, prev = [], secret%10
    for _ in range(2000):
        secret = evolve(secret)
        prevs.append((secret%10)-prev)
        prevs = prevs[-4:]
        if tuple(prevs) not in deltas[i]:
            deltas[i][tuple(prevs)] = secret % 10
            sums[tuple(prevs)] += secret % 10
        prev = secret % 10
    p1 += secret

print(p1)
print(max(sums.values()))
