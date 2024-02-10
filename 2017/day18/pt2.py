
from collections import deque, defaultdict

D = [i.strip() for i in open("input","r").readlines()]

def run(pid):
    regs = defaultdict(int)
    regs["p"] = pid
    pc = 0
    snd = None
    while True:
        line = D[pc]
        jumped = False

        op = line.split(" ")[0]
        if op == "snd":
            reg = line.split(" ")[1]
            snd = regs[reg]
            yield snd
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
            i = yield None
            regs[val] = i
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


qa,qb = deque(), deque()

a = run(0)
b = run(1)
c = 0

oa,ob = next(a),next(b)
if oa != None:
    qb.append(oa)
if ob != None:
    qa.append(ob)

while True:

    if len(qa) > 0 and oa == None:
        oa = a.send(qa.popleft())
    else:
        oa = next(a)
    if oa != None:
        qb.append(oa)
    
    if len(qb) > 0 and ob == None:
        ob = b.send(qb.popleft())
    else:
        ob = next(b)
    if ob != None:
        c += 1
        qa.append(ob)
    
    if oa == None and ob == None and len(qa) == 0 and len(qb) == 0:
        break

print(c)