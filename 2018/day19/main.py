
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

ipr = ints(D[0])[0]
try:
    while True:
        ip = R[ipr]
        ins, a,b,c = D[ip+1].split(" ")
        a,b,c = int(a), int(b), int(c)
        INS[ins](a,b,c)
        R[ipr] += 1
except:
    pass
print("part 1", R[0])


R = [1,0,0,0,0,0]
P = []
for line in D[1:]:
    parsed = line.split(" ")
    P.append((INS[parsed[0]], int(parsed[1]), int(parsed[2]), int(parsed[3])))

R = [1,0,0,0,0,0]
ipr = ints(D[0])[0]
bignum = 0
i = 0
try:
    while True:
        ip = R[ipr]
        if (ip == len(D)-2):
            bignum = R[5]
            break
        ins, a,b,c = P[ip]
        ins(a,b,c)
        R[ipr] += 1
        i += 1
except:
    pass

def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return sorted(divisors)

divisors = find_divisors(bignum)
print("part 2", sum(divisors))
