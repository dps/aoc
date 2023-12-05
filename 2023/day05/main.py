
from utils import *

D = [i.strip() for i in open("input","r").readlines()]
def part1():
    seeds = D[0].split(":")[1].strip().split(" ")
    print(seeds)
    input = D[2:]
    dirs = defaultdict(str)
    maps = defaultdict(list)
    for bundle in bundles(input):
        bun = list(bundle)
        print(bun)
        fro, _, to = bun[0].split()[0].split("-")
        print(fro, to)
        dirs[fro] = to
        for line in bun[1:]:
            print(line)
            d_start, src_start, lenf = map(int, line.split())
            print(lenf)
            maps[(fro,to)].append((d_start, src_start, lenf))
    
    print(dirs)
    r = []
    for s in seeds:
        t = "seed"
        n = int(s)
        while t != "location":
            print(t,n)
            fnd = maps[t, dirs[t]]
            for ff in fnd:
                if n >= ff[1] and n < (ff[1]+ff[2]):
                    n = ff[0] + (n-ff[1])
                    break
            t = dirs[t]
        print("***",t,n)
        r.append(n)
    aoc(min(r))


def part2():
    seeds = D[0].split(":")[1].strip().split(" ")
    print(seeds)
    input = D[2:]
    dirs = defaultdict(str)
    maps = defaultdict(list)
    for bundle in bundles(input):
        bun = list(bundle)
        print(bun)
        fro, _, to = bun[0].split()[0].split("-")
        print(fro, to)
        dirs[fro] = to
        for line in bun[1:]:
            print(line)
            d_start, src_start, lenf = map(int, line.split())
            print(lenf)
            maps[(fro,to)].append((d_start, src_start, lenf))
    
    M = {k:sorted(v) for k,v in maps.items()}
    
    print(M)
    r = []
    def pairs(ll):
        for x in range(0,len(ll),2):
            yield (ll[x], ll[x+1])
    for s,rg in pairs(lmap(int, seeds)):
        print(s,rg)
        seed = s
        # We can skip forward each interval where there's nothing changing.
        # let's sort the ranges
        while seed < s+rg:
            t = "seed"
            n = int(seed)
            canskip = math.inf
            while t != "location":
                fnd = maps[t, dirs[t]]
                for ff in fnd:
                    if n >= ff[1] and n < (ff[1]+ff[2]):
                        n = ff[0] + (n-ff[1])
                        canskip = min(canskip, ff[0]+ff[2]-n) #might be off 1
                        break
                t = dirs[t]
            r.append(n)
            assert(canskip != math.inf)
            seed += canskip
    aoc(min(r))

part2()
#part2()
