
from utils import *


D = [i.strip() for i in open("input","r").readlines()]
p1 = 0

R = [0,0,0]
regs, program = bundles(D)

for r in regs:
    r = r.replace("Register ", "")
    V, v = r.split(": ")
    R[int(ord(V[0])-ord('A'))] = int(v)
program = program[0].split(": ")[1]
instr = list(map(int, program.split(",")))


def combo(v):
    if v == 4:
        return R[0]
    elif v == 5:
        return R[1]
    elif v == 6:
        return R[2]
    else:
        return v

out = []
pc = 0
while pc < len(instr):
    op = instr[pc]
    if op == 0:
        R[0] = R[0] >> combo(instr[pc+1])
    elif op == 1:
        R[1] = R[1] ^ instr[pc+1]
    elif op == 2:
        R[1] = combo(instr[pc+1]) % 8
    elif op == 3 and R[0] != 0:
        pc = instr[pc+1] - 2
    elif op == 4:
        R[1] = R[1] ^ R[2]
    elif op == 5:
        out.append(combo(instr[pc+1]) % 8)
    elif op == 6:
        R[1] = R[0] >> combo(instr[pc+1])
    elif op == 7:
        R[2] = R[0] >> combo(instr[pc+1])
    else:
        print("Unknown opcode", op)
        break
    pc += 2

print(",".join([str(i) for i in out]))

target = ints(program)

def run(v):
    o = []
    A,B,C=v,0,0
    while True:
        B=A%8
        B=B^1
        C=A>>B
        B=B^C
        B=B^4
        A=A>>3
        o.append(B%8)
        if A==0:
            break
    return o

candidates = [0]
for pl in range(len(target)):
    cc = []
    for c in candidates:
        for i in range(8):
            nA = (c<<3) + i
            o = run(nA)
            if o == target[len(target)-pl-1:]:
                cc.append(nA)
    candidates = cc
print(min(candidates))