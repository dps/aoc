
from utils import *

A,B = zip(*[ints(i) for i in open("input","r").readlines()])
A,B = sorted(A), sorted(B)
p1 = sum([abs(a - b) for a,b in zip(A,B)])
C = Counter(B)
p2 = sum([x * C[x] for x in A])

print(p1, p2)
