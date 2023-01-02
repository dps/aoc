from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve(part=1):
    sequence = input[0]
    pair_counts = defaultdict(int)

    for l,r in zip(sequence, sequence[1:]):
        pair_counts[l+r] += 1

    xform = {}
    for line in input[2:]:
        xform[line.split(" -> ")[0]] = line.split(" -> ")[1]

    start_str = sequence[0:2]
    end_str = sequence[-2:]
    
    for i in range(40 if part == 2 else 10):
        new_pairs = deepcopy(pair_counts)
        for pair, count in pair_counts.items():
            if pair in xform:
                # LR -> LXR
                new_pairs[pair] -= count
                if new_pairs[pair] == 0:
                    del(new_pairs[pair])
                new_pairs[pair[0] + xform[pair]] += count
                new_pairs[xform[pair] + pair[1]] += count
        pair_counts = new_pairs
        if start_str in xform:
            start_str = start_str[0] + xform[start_str]
        if end_str in xform:
            end_str = xform[start_str] + end_str[1]
    
    cnts = defaultdict(int)
    for pair, count in pair_counts.items():
        cnts[pair[0]] += count
    cnts[end_str[1]] += 1
    
    l = [(c,k) for k,c in cnts.items()]
    l.sort()
    print(res := l[-1][0]-l[0][0])
    return(res)
    
assert(solve(part=1) == 2657)
assert(solve(part=2) == 2911561572630)
