
from collections import defaultdict

D = [i.strip() for i in open("input","r").readlines()]

regs = defaultdict(int)
regs['a'] = 1
pc = 0
snd = None
e = 0
try:
    while True:
        line = D[pc]
        jumped = False

        def parse(aa):
            if not aa[1].isalpha():
                return aa[0], int(aa[1])
            else:
                return aa[0], regs[aa[1]]

        op, args = line.split(" ")[0], line.split(" ")[1:]
        if op == "set":
            dest, val = parse(args)
            regs[dest] = val
        elif op == "sub":
            dest, val = parse(args)
            regs[dest] -= val
        elif op == "mul":
            e += 1
            dest, val = parse(args)
            regs[dest] *= val
        elif op == "jnz":
            a, b = args
            if not b.isalpha():
                b = int(b)
            else:
                b = regs[b]
            if not a.isalpha():
                a = int(a)
            else:
                a = regs[a]
            if a != 0:
                pc += b
                jumped = True
        if not jumped:
            pc += 1
        print(regs)
except :
    pass

print(e)

### Part 2, by inspection
import sympy

c = 0
for i in range(105700, 122717, 17):
    if not sympy.isprime(i):
        c += 1

print(c)