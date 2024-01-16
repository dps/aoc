
gen = (int(i) for i in open("input","r").readlines()[0].split())

metadata = []
def node_value():
    global gen, metadata
    children, mds = next(gen), next(gen)
    cvals = []
    for _ in range(children):
        cvals.append(node_value())
    assert(len(cvals) == children)
    val = 0
    for _ in range(mds):
        m = next(gen)
        metadata.append(m)
        if children == 0:
            val += m
        else:
            if m == 0:
                continue
            elif len(cvals) >= m:
                val += cvals[m-1]
    return val

root = node_value()
print("day08", sum(metadata), root)

