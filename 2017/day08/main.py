
from collections import defaultdict
D = [i.strip() for i in open("input","r").readlines()]

R = defaultdict(int)
mx = 0
for line in D:
    reg,op,n,if_,tr,cmp,val = line.split(" ")

    test = eval(f"R['{tr}'] {cmp} {val}")
    if test:
        if op == "inc":
            R[reg] += int(n)
        elif op == "dec":
            R[reg] -= int(n)
        mx = max(mx, R[reg])

print(max(R.values()), mx)