
from collections import deque, defaultdict

D = [i.strip() for i in open("input","r").readlines()]

regs = defaultdict(int)
pc = 0
snd = None
while True:
    line = D[pc]
    jumped = False

    op = line.split(" ")[0]
    if op == "snd":
        reg = line.split(" ")[1]
        snd = regs[reg]
    elif op == "set":
        args = line.split(" ")[1:]
        dest, val = args
        if not val.isalpha():
            regs[dest] = int(val)
        else:
            regs[dest] = regs[val]
    elif op == "add":
        args = line.split(" ")[1:]
        dest, val = args
        if not val.isalpha():
            regs[dest] += int(val)
        else:
            regs[dest] += regs[val]
    elif op == "mul":
        args = line.split(" ")[1:]
        dest, val = args
        if not val.isalpha():
            regs[dest] *= int(val)
        else:
            regs[dest] *= regs[val]      
    elif op == "mod":
        args = line.split(" ")[1:]
        dest, val = args
        if not val.isalpha():
            regs[dest] %= int(val)
        else:
            regs[dest] %= regs[val]
    elif op == "rcv":
        args = line.split(" ")[1:]
        val = args[0]
        t = False
        if not val.isalpha():
            t = int(val) != 0
        else:
            t = regs[val] != 0
        if t:
            print("recover ", snd)
            break
    elif op == "jgz":
        args = line.split(" ")[1:]
        a, b = args
        if not b.isalpha():
            b = int(b)
        else:
            b = regs[b]
        if not a.isalpha():
            a = int(a)
        else:
            a = regs[a]
        if a > 0:
            pc += b
            jumped = True
    if not jumped:
        pc += 1

