from utils import *
from string import *
from math import gcd

input = [i.strip() for i in open("input","r").readlines()]

class Dll(object):

    def init(length, specialval, circular=True):
        vmap = {}
        head = None
        special = None
        prev = None
        for v in range(length):
            n = Dll(v, prev, None)
            if not prev:
                head = n
            else:
                prev.set_nxt(n)
            prev = n
            if v == specialval:
                special = n
            vmap[v] = n
        if circular:
            head.set_prv(prev) # Connect the ends
            prev.set_nxt(head)
        return head, vmap, special 

    def __init__(self, val, prv, nxt, dir=1):
        self._val = val
        self._prv = prv
        self._nxt = nxt
        self._dir = dir

    def set_nxt(self, n):
        self._nxt = n

    def set_prv(self, n):
        self._prv = n

    def set_dir(self, dir):
        self._dir = dir

    def nxt(self):
        return self._nxt

    def prv(self):
        return self._prv

    def val(self):
        return self._val
    
    def dir(self):
        return self._dir
    
    def print(self):
        if self._dir == 1:
            n = self
            print(n.val(), end=" ")
            while n.nxt() != self:
                n = n.nxt()
                print(n.val(), end=" ")
            print()
        if self._dir == -1:
            n = self
            print(n.val(), end=" ")
            while n.prv() != self:
                n = n.prv()
                print(n.val(), end=" ")
            print()

def stack(top):
    #print("stack")
    if top.dir() == 1:
        newtop = top.prv()
        newtop.set_dir(-1)
        return newtop
    if top.dir() == -1:
        newtop = top.nxt()
        newtop.set_dir(1)
        return newtop

def cut(top, n):
    #print("cut", n)
    dir = top.dir()
    a = top
    if n >= 0:
        for _ in range(n):
            a = a.nxt() if dir == 1 else a.prv()
        a.set_dir(dir)
        return a
    else:
        for _ in range(abs(n)):
            a = a.prv() if dir == 1 else a.nxt()
        a.set_dir(dir)
        return a

def increment(top, incr, length):
    #print("increment", incr)
    table = [None] * length
    i = 0
    t = 0
    n = top
    dir = n.dir()
    def inc():
        nonlocal n, dir
        if dir == 1:
            n = n.nxt()
        else:
            n = n.prv()
    while t<length:
        table[i] = n
        i += incr
        if i > (length-1):
            i = i%length
        inc()
        t+=1
    top.set_dir(1)
    top.set_prv(table[-1])
    table[-1].set_nxt(top)
    for a,b in zip(table,table[1:]):
        a.set_nxt(b)
        b.set_prv(a)
    return top



def part1():

    length = 10007
    top, _, twentynineteen = Dll.init(length, specialval=2019)
    for line in input:
        if "deal with increment" in line:
            incr = ints(line)[0]
            top = increment(top, incr, length)
        if "deal into new stack" in line:
            top = stack(top)
        if "cut" in line:
            cutn = ints(line)[0]
            top = cut(top, cutn)

    i = 0
    n = top
    dir = top.dir()
    def inc():
        nonlocal n, dir
        if dir == 1:
            n = n.nxt()
        else:
            n = n.prv()
    while n != twentynineteen:
        inc()
        i+=1
    aoc(i)

DECK_LEN = 119315717514047
TIMES = 101741582076661

# (with some help)
# observe
def cut_pos(cut, pos, deck_size):
    return (pos - cut) % deck_size

def deal_with_increment_pos(incr, pos, deck_size):
    return (pos * incr) % deck_size

def deal_new_stack(x, deck_size):
    return deck_size - 1 - x

# These are all of the form
# a . pos + b mod deck_size
# cut => a = 1, b = -cut
# deal => a = incr, b = 0
# stack => a = -1, b = (deck_size - 1)

def forward(deck_size):
    a, b = 1, 0 # identity function to start
    for line in input:
        if "deal with increment" in line:
            incr = ints(line)[0]
            a *= incr
            b *= incr
        if "deal into new stack" in line:
            a *= -1
            b = deck_size - 1 - b
        if "cut" in line:
            cutn = ints(line)[0]
            b -= cutn
    return a,b

def part2():
    a,b = forward(DECK_LEN)
    # that's a function of shape (ax + b) mod N,
    # its inverse is a^-1 mod p . x + -b . a^-1 mod p
    c,d = pow(a, -1, DECK_LEN), -b * pow(a, -1, DECK_LEN)
    # now repeated application is a geometric series
    # 𝐹^𝑘(𝑥)=𝑎^𝑘𝑥+𝑏(1−𝑎^𝑘)/1−𝑎  mod 𝑚
    e = pow(c, TIMES, DECK_LEN)
    f = (e - 1) * pow(c-1, DECK_LEN - 2, DECK_LEN)
    aoc(((e * 2020) + d*f) % DECK_LEN)

part1()
part2()