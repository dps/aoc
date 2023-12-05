
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def solve():
    seeds = D[0].split(":")[1].strip().split(" ")
    input = D[2:]
    dirs = defaultdict(str)
    maps = defaultdict(list)
    for bundle in bundles(input):
        bun = list(bundle)
        fro, _, to = bun[0].split()[0].split("-")
        dirs[fro] = to
        for line in bun[1:]:
            d_start, src_start, lenf = map(int, line.split())
            maps[(fro,to)].append((d_start, src_start, lenf))
    
    r = []
    for s in seeds:
        t,n = "seed", int(s)
        while t != "location":
            fnd = maps[t, dirs[t]]
            for ff in fnd:
                if n >= ff[1] and n < (ff[1]+ff[2]):
                    n = ff[0] + (n-ff[1])
                    break
            t = dirs[t]
        r.append(n)
    print("part1", min(r))

    r = []
    def pairs(ll):
        for x in range(0,len(ll),2):
            yield (ll[x], ll[x+1])
    for s,rg in pairs(lmap(int, seeds)):
        seed = s
        # We can skip forward each interval where there's nothing changing.
        while seed < s+rg:
            t = "seed"
            n = int(seed)
            canskip = math.inf
            while t != "location":
                fnd = maps[t, dirs[t]]
                for ff in fnd:
                    if n >= ff[1] and n < (ff[1]+ff[2]):
                        n = ff[0] + (n-ff[1])
                        canskip = min(canskip, ff[0]+ff[2]-n)
                        break
                t = dirs[t]
            r.append(n)
            assert(canskip != math.inf)
            seed += canskip
    print("part2", min(r))

solve()
