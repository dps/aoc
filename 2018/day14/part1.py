
from utils import *

rounds = 846021

S = [3,7]
a,b = 0,1

seen = set()
while True:
    comb = str(S[a]+ S[b])
    next = [int(comb[0])] if len(comb)==1 else [int(comb[0]), int(comb[-1])]
    S.extend(next)
    m = len(S)
    a = (a + (S[a] + 1)) % m
    b = (b + (S[b] + 1)) % m
    if len(S) >= rounds+10:
        break

print("".join(str(s) for s in S[rounds:rounds+10]))


