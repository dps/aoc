
from utils import *

rounds = 846021
digits = tuple(int(d) for d in str(rounds))

S = [3,7] + [0] * 100000000
a,b = 0,1

i = 0
m = 2

while True:
    comb = S[a] + S[b]
    if comb > 9:
        S[m] = comb // 10
        S[m+1] = comb % 10
        m += 2
    else:
        S[m] = comb
        m += 1
    a = (a + (S[a] + 1)) % m
    b = (b + (S[b] + 1)) % m
    if m == rounds + 10:
        print("Part 1:", "".join(str(s) for s in S[rounds:rounds+10]))

    # This unrolling improves runtime by 20% ish.
    if S[m-1] == digits[-1] and S[m-2] == digits[-2] and S[m-3] == digits[-3] and S[m-4] == digits[-4] and S[m-5] == digits[-5] and S[m-6] == digits[-6]:
        break

    if S[m-2] == digits[-1] and S[m-3] == digits[-2] and S[m-4] == digits[-3] and S[m-5] == digits[-4] and S[m-6] == digits[-5] and S[m-7] == digits[-6]:
        break

    i+=1

print("Part 2:", m-len(digits) - (0 if tuple(S[m-len(digits):m]) == digits else 1))


