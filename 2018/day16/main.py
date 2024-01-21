
from utils import *

D = [i.strip() for i in open("input","r").readlines()]
grp = bundles(D)

R = [0,0,0,0]

def addr(a,b,c): R[c] = R[a] + R[b]
def addi(a,b,c): R[c] = R[a] + b
def mulr(a,b,c): R[c] = R[a] * R[b]
def muli(a,b,c): R[c] = R[a] * b
def banr(a,b,c): R[c] = R[a] & R[b]
def bani(a,b,c): R[c] = R[a] & b
def borr(a,b,c): R[c] = R[a] | R[b]
def bori(a,b,c): R[c] = R[a] | b
def setr(a,_,c): R[c] = R[a]
def seti(a,_,c): R[c] = a
def gtir(a,b,c): R[c] = 1 if a > R[b] else 0
def gtri(a,b,c): R[c] = 1 if R[a] > b else 0
def gtrr(a,b,c): R[c] = 1 if R[a] > R[b] else 0
def eqir(a,b,c): R[c] = 1 if a == R[b] else 0
def eqri(a,b,c): R[c] = 1 if R[a] == b else 0
def eqrr(a,b,c): R[c] = 1 if R[a] == R[b] else 0

INS = {"addr":addr, "addi":addi, "mulr":mulr, "muli":muli, "banr":banr, "bani":bani, "borr":borr, "bori":bori,
       "setr":setr, "seti":seti, "gtir":gtir, "gtri":gtri, "gtrr":gtrr, "eqir":eqir, "eqri":eqri, "eqrr":eqrr}

CODES = defaultdict(list)
p1 = 0
for b in grp:
    if b == []:
        break
    before = list(map(int, b[0].split("[")[1].split("]")[0].split(",")))
    instruction = list(map(int, b[1].split(" ")))
    after = list(map(int, b[2].split("[")[1].split("]")[0].split(",")))

    pl = set()
    for name,op in INS.items():
        R = before[:]
        op(*instruction[1:])
        if R == after:
            pl.add(name)
    CODES[instruction[0]].append(pl)
    if len(pl) >= 3:
        p1 += 1


MAPPED = {}

while CODES:
    del_op,del_ins = set(),set()
    for op, lls in CODES.items():
        lls.sort(key=lambda l:len(l))
        for poss in lls:
            if len(poss) == 1:
                MAPPED[op] = poss.pop()
                del_op.add(op)
                del_ins.add(MAPPED[op])
    for dop in del_op:
        del(CODES[dop])
    for op,lls in CODES.items():
        CODES[op] = [s-del_ins for s in lls]

second_half = False
R = [0,0,0,0]
for b in grp:
    if b == []:
        second_half = True
    if not second_half or b == []:
        continue
    
    for line in b:
        ins = list(map(int, line.split(" ")))
        INS[MAPPED[ins[0]]](*ins[1:])

print("day 16", p1, R[0])
