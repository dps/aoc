
import sys
from collections import defaultdict
D = [i.strip() for i in open("input","r").readlines()]

toggled = defaultdict(bool)

TOGGLE = {"inc": "dec", "dec": "inc", "jnz": "cpy", "tgl": "inc", "cpy": "jnz"}

def run(a):
    pc = 0
    R = defaultdict(int)
    R['a'] = a
    while pc < len(D):
        ins = D[pc].split(" ")[0]
        if toggled[pc]:
            ins = TOGGLE[ins]
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
            if y[0].isalpha():
                y = R[y]
            else:
                y = int(y)
            if x != 0:
                pc += y - 1
        if ins == "tgl":
            x = D[pc].split(" ")[1]
            if x[0].isalpha():
                x = R[x]
            else:
                x = int(x)
            toggled[pc+x] = not toggled[pc+x]
        if ins == "out":
            x = D[pc].split(" ")[1]
            if x[0].isalpha():
                x = R[x]
            else:
                x = int(x)
            yield(x)


        pc += 1
    return R['a']

for i in range(1000):
    g = run(i)
    l,r = next(g),next(g)
    for j in range(1000):
        ll,rr = next(g),next(g)
        if ll != l or rr != r:
            break
        if j == 999:
            print(i)
            sys.exit(0)
