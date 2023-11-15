from utils import *
from string import *

input = [i.strip() for i in open("input","r").readlines()]

inputs = []
for i in range(50):
    inputs.append([])
print(inputs)

def computer(mem, _pc, _relbase, inputnum):
    global inputs

    def decode(cop):
        s = str(cop).zfill(5)
        return s[0],s[1],s[2],int(s[3:])

    pc = _pc
    op = None
    relbase = _relbase

    while True:
        l = 0
        md,my,mx,op = decode(mem[pc])

        def param(mode, p,):
            nonlocal relbase, mem
            if mode == '1':
                return p
            if mode == '0':
                return mem[p]
            if mode == '2':
                return mem[relbase + p]

        def dest(md, d):
            nonlocal relbase
            return d if md == '0' else relbase + d

        if op == 1:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[dest(md,d)] = param(mx, x) + param(my, y)
            l = 4
        elif op == 2:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[dest(md,d)] = param(mx, x) * param(my, y)
            l = 4
        elif op == 3: # input
            x = mem[pc+1]
            ii = -1
            if len(inputs[inputnum]) > 0:
                ii = inputs[inputnum][0]
                inputs[inputnum] = inputs[inputnum][1:]
                print(inputnum,"<-",ii)
            if ii == -1:
                yield "preempt"
            mem[dest(mx,x)] = ii
            l = 2
        elif op == 4: # output
            x = mem[pc+1]
            yield param(mx, x)
            l = 2
        elif op == 5: # jump-if-true
            x, y = mem[pc+1], mem[pc+2]
            if param(mx, x) != 0:
                pc = param(my, y)
            else:
                l = 3
        elif op == 6: # jump-if-false
            x, y = mem[pc+1], mem[pc+2]
            if param(mx, x) == 0:
                pc = param(my, y)
            else:
                l = 3
        elif op == 7: # <
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if param(mx, x) < param(my, y):
                mem[dest(md,d)] = 1
            else:
                mem[dest(md,d)] = 0
            l = 4
        elif op == 8: # ==
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if param(mx, x) == param(my, y):
                mem[dest(md,d)] = 1
            else:
                mem[dest(md,d)] = 0
            l = 4
        elif op == 9: # relbase
            x = mem[pc+1]
            relbase += param(mx, x)
            l = 2
        elif op == 99:
            break
        pc += l
    yield None

def part1():
    global inputs
    program = [int(x) for x in input[0].split(",")]    
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    computers = []
    for i in range(50):
        c = computer(deepcopy(allmem),0,0,i)
        computers.append(c)
        inputs[i].append(i)
    print(inputs)

    while True:
        for i in range(50):
            dest = next(computers[i])
            if dest == "preempt":
                #print(".",end="")
                continue
            x = next(computers[i])
            y = next(computers[i]) 
            print(dest, x, y)
            if dest == 255:
                aoc(y)
                return
            inputs[dest].append(x)
            inputs[dest].append(y)

def part2():
    global inputs
    program = [int(x) for x in input[0].split(",")]    
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    computers = []
    for i in range(50):
        c = computer(deepcopy(allmem),0,0,i)
        computers.append(c)
        inputs[i].append(i)
    print(inputs)

    nat_p2, nat_p = None, None
    nat_q = None
    while True:
        c=0
        for i in range(50):
            buffs = [len(x) for x in inputs]
            dest = next(computers[i])
            newbuffs = [len(x) for x in inputs]

            if buffs != newbuffs:
                c += 1

            if dest == "preempt":
                #print(".",end="")
                continue
            x = next(computers[i])
            y = next(computers[i]) 
            print(dest, x, y)
            if dest == 255:
                nat_q = (x,y)
            else:
                inputs[dest].append(x)
                inputs[dest].append(y)
        if c == 0:
            nat_p2 = nat_p
            inputs[0].append(nat_q[0])
            inputs[0].append(nat_q[1])
            nat_p = (nat_q[0],nat_q[1])

            if nat_p2 and nat_p[1] == nat_p2[1]:
                aoc(nat_p2[1])
                return




part2()

