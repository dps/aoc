
from utils import *

D = [i.strip() for i in open("input","r").readlines()]
grp = bundles(D)
R = [0,0,0,0,0,0]

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

P = []
for line in D[1:]:
    parsed = line.split(" ")
    P.append((INS[parsed[0]], int(parsed[1]), int(parsed[2]), int(parsed[3])))

R = [0,0,0,0,0,0]
ipr = ints(D[0])[0]
i = 0
part1 = None
seen = set()
state = set()
k=None
try:
    while True:
        ip = R[ipr]
        if ip == 28:
            if tuple(R) in state:
                break
            state.add(tuple(R))

            if part1 == None:
                part1 = R[1]
            if R[1] not in seen:
                seen.add(R[1])
                k=R[1]
        ins, a,b,c = P[ip]
        ins(a,b,c)
        R[ipr] += 1
        i += 1
except:
    pass

print(part1, k)