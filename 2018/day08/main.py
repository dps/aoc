
gen = (int(i) for i in open("input","r").readlines()[0].split())
metadata = 0

def node_value():
    global gen, metadata
    children, mds = next(gen), next(gen)
    cvals, val = [], 0
    for _ in range(children):
        cvals.append(node_value())
    assert(len(cvals) == children)
    for _ in range(mds):
        m = next(gen)
        metadata += m
        if children == 0:
            val += m
        elif m > 0 and len(cvals) >= m:
            val += cvals[m-1]
    return val

root = node_value()
print("day08", metadata, root)

