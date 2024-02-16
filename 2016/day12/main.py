
from collections import defaultdict
D = [i.strip() for i in open("input","r").readlines()]

def run(part):
    pc = 0
    R = defaultdict(int)
    if part == 2:
        R['c'] = 1
    while pc < len(D):
        ins = D[pc].split(" ")[0]
        if ins == "cpy":
            x,y = D[pc].split(" ")[1], D[pc].split(" ")[2]
            if x[0].isalpha():
                x = R[x]
            else:
                x = int(x)
            R[y] = x
        if ins == "inc":
            x = D[pc].split(" ")[1]
            R[x] += 1
        if ins == "dec":
            x = D[pc].split(" ")[1]
            R[x] -= 1
        if ins == "jnz":
            x,y = D[pc].split(" ")[1], D[pc].split(" ")[2]
            if x[0].isalpha():
                x = R[x]
            else:
                x = int(x)
            if x != 0:
                pc += int(y) - 1
        pc += 1
    return R['a']

print(run(1))
print(run(2))