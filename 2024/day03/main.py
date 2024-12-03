
from utils import *

D = open("input").read()

p1, p2 = 0, 0
p = []

for m in re.finditer(r"mul\((\d+),(\d+)\)", D):
    p.append((m.start(), [m.group(1), m.group(2)]))
    p1 += int(m.group(1)) * int(m.group(2))

for m in re.finditer(r"do\(\)", D):
    p.append((m.start(), True))

for m in re.finditer(r"don't\(\)", D):
    p.append((m.start(), False))

p = sorted(p, key=lambda x: x[0])

enabled = True
for e in p:
    if e[1] == True:
        enabled = True
    elif e[1] == False:
        enabled = False
    else:
        p2 += int(e[1][0]) * int(e[1][1]) if enabled else 0
    
print(p1, p2)
