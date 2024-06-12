
from utils import *

D = [i.strip() for i in open("input","r").readlines()]


p1, p2 = 0, 0

for line in D:
    s = eval(line)
    p1 += len(line) - len(s)
    ss = Counter(line)
    enclen = 2 + ss["\""] + ss["\\"] + len(line)
    p2 += (enclen - len(line))

print(p1, p2)