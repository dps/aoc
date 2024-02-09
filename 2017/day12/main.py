D = [i.strip() for i in open("input","r").readlines()]

groups = []

for line in D:
    l,r = line.split(" <-> ")
    src = int(l)
    dests = list(map(int, r.split(",")))
    aa = set(dests) | {src}
    to_merge = []
    for i,g in enumerate(groups):
        if len(aa & g):
            g.update(aa)
            to_merge.append(i)
    if len(to_merge) == 0:
        groups.append(aa)
    elif len(to_merge) > 1:
        keep = groups[to_merge[0]]
        for k,j in enumerate(to_merge[1:]):
            keep.update(groups[j-k])
            groups.pop(j-k)

print([len(g) for g in groups if 0 in g][0], len(groups))