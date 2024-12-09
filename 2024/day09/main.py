
from utils import *

D = open("input","r").read()

disk = defaultdict(int)
free = set()
chunks = {}
fmap = {}

p = 0
for i, ch in enumerate(D):
    if i % 2 == 0:
        fmap[i//2] = (p, int(ch)) 
        for _ in range(int(ch)):
            disk[p] = i//2
            p += 1
    else:
        chunks[p] = int(ch)
        for _ in range(int(ch)):
            free.add(p)
            p += 1

orig_disk = disk.copy()

# Part 1
while len(free) > 0 and min(free) < max(disk.keys()):
    dest = min(free)
    mv = max(disk.keys())
    disk[dest] = disk[mv]
    free.remove(dest)
    del disk[mv]

print(sum(k*v for k,v in disk.items()))
# Part 2
disk = orig_disk
mf = max(disk.values())
for fn in range(mf, 0, -1):
    cm = [(p,s) for p,s in chunks.items()]
    cm.sort(key=lambda x: x[0])

    start, size = fmap[fn]
    for cs, cz in cm:
        if cz >= size and cs < start:
            # the file moves
            for i in range(size):
                disk[cs + i] = fn
                del disk[start+i]
            rem = cz - size
            del chunks[cs]
            if rem > 0:
                chunks[cs+size] = rem
            break


print(sum(k*v for k,v in disk.items()))
