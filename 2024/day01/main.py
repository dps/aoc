
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0, 0
a,b = [], []
for line in D:
    ii = ints(line)
    a.append(ii[0])
    b.append(ii[1])

a = sorted(a)
b = sorted(b)
c = Counter(b)

for i, x in enumerate(a):
    p1 += abs(a[i] - b[i])
    p2 += x * c[x]

print(p1, p2)