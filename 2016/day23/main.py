
from collections import defaultdict
D = [i.strip() for i in open("input","r").readlines()]

toggled = defaultdict(bool)

TOGGLE = {"inc": "dec", "dec": "inc", "jnz": "cpy", "tgl": "inc", "cpy": "jnz"}

def run(part):
    pc = 0
    R = defaultdict(int)
    if part == 1:
        R['a'] = 7
    if part == 2:
        R['a'] = 12
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

        pc += 1
    return R['a']


def pt2(eggs):
    # By analysis of the program, making some assumptions about what
    # might be different in other people's input, obviously.
    a = eggs*(eggs-1)
    b = 10
    c = 20
    for _ in range(b,1,-1):
        a *= (c//2)
        c -= 2
    a += int(D[19].split(" ")[1]) * int(D[20].split(" ")[1])
    print(a)

print(run(1))
pt2(12)