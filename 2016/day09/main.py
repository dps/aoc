
from utils import *

D = open("input","r").read().strip()

def expand(start, l, part=1):
    global D
    expanded = 0
    i = 0
    while i < l:
        ch = D[start + i]
        if ch == '(':
            ll = ""
            j,cha=0,None
            while cha != ")":
                cha = D[start+i+j]
                ll += cha
                j+=1
            length,rep = ints(ll)
            i+=j
            expanded += (length if part == 1 else expand(start+i,length)) * rep
            i+=length
        else:
            expanded += 1
            i+=1

    return expanded

print(expand(0,len(D),1))
print(expand(0,len(D),2))
        