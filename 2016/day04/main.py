
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

valid = []
c = 0
for line in D:
    l,chk = line.split("[")
    chk = chk[0:-1]
    sector = positive_ints(l)[0]
    l = words(l.replace('-',''))[0]
    ll = "".join([b for (_,b) in (sorted([(-b,a) for (a,b) in Counter(l).most_common()])[0:5])])
    if ll == chk:
        c += sector
        valid.append((l,sector))

print(c)

for enc,key in valid:
    dec = ""
    for ch in enc:
        s = ord(ch) - ord('a')
        s = s + key
        s = s % 26
        dec += chr(ord('a')+s)
    if dec == "northpoleobjectstorage":
        print(key)
        break
