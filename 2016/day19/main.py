
from utils import *

num = int(open("input","r").read())
p = deque()

def p1():
    for i in range(num):
        p.append((1,i))

    while len(p) > 1:
        t = p.popleft()
        g = p.popleft()
        p.append((t[0]+g[0],t[1]))

    print(p[0][1]+1)

def p2():
    first = Dll(1,None,None)
    prev = first
    opp = num//2 + 1
    mid = None
    for i in range(2,num+1):
        nxt = Dll(i,prev,None)
        prev.set_nxt(nxt)
        if i == opp:
            mid = nxt
        prev = nxt
    prev.set_nxt(first)
    first.set_prv(prev)

    l = num
    while first != mid:
        mid.prv().set_nxt(mid.nxt())
        mid.nxt().set_prv(mid.prv())
        l -= 1
        mid = mid.nxt()
        first = first.nxt()
        if l % 2 == 0:
            mid = mid.nxt()

    print(first.val())

p1()
p2()
