
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def scramble(password):
    for line in D:
        toks = line.split(" ")
        vals = ints(line)

        if toks[0] == "rotate":
            if toks[1] == "left":
                password = password[vals[0]:] + password[0:vals[0]]
            if toks[1] == "right":
                password = password[-vals[0]:] + password[0:-vals[0]]
            if toks[1] == "based":
                ch = toks[6]
                i = password.index(ch)
                r = i + 1 + (1 if i >= 4 else 0)
                r = r%len(password)
                password = password[-r:] + password[0:-r]

        if toks[0] == "swap":
            if toks[1] == "position":
                t = password[vals[0]]
                password[vals[0]] = password[vals[1]]
                password[vals[1]] = t
            if toks[1] == "letter":
                password = [toks[2] if p == toks[5] else toks[5] if p == toks[2] else p for p in password]

        if toks[0] == "reverse":
            password = password[:vals[0]] + list(reversed(password[vals[0]:vals[1]+1])) + password[vals[1]+1:]

        if toks[0] == "move":
            x,y = vals[0],vals[1]
            ch = password.pop(x)
            password.insert(y, ch)

    return password


print("".join(scramble(list("abcdefgh"))))

seeds = permutations(list("abcdefgh"))
dest = list("fbgdceah")
for s in seeds:
    if scramble(list(s)) == dest:
        print("".join(s))
        break