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
    top, deck_map, twentynineteen = Dll.init(length, specialval=2019)
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


def spos(top, special):
    i = 0
    n = top
    dir = top.dir()
    def inc():
        nonlocal n, dir
        if dir == 1:
            n = n.nxt()
        else:
            n = n.prv()
    while n != special:
        inc()
        i+=1
    return i

def part2():

    length = 10007
    top, deck_map, twentytwenty = Dll.init(length, specialval=2020)

    seen = set()
    prev = [None] * 5
    for i in range(975):
        for line in input:
            if "deal with increment" in line:
                incr = ints(line)[0]
                top = increment(top, incr, length)
            if "deal into new stack" in line:
                top = stack(top)
            if "cut" in line:
                cutn = ints(line)[0]
                top = cut(top, cutn)

        # p = spos(top, twentytwenty)
        # prev.append(p)
        # prev = prev[1:]
        # if tuple(prev) in seen:
        #     print("SEEN", i)
        #     break
        # seen.add(tuple(prev))
    # SEEN 5007
    # loops at 5002
    #>>> 101741582076661 % 5002
    #975
        aoc(spos(top, twentytwenty))
        # prev.append(p)
        # prev = prev[1:]
        # if tuple(prev) in seen:
        #     print("SEEN", i)
        #     break
        # seen.add(tuple(prev))

# def extended_euclidean(a, b):
#     """
#     Returns a pair of numbers (x, y) such that a * x + b * y = gcd(a, b)
#     """
#     if b == 0:
#         return (1, 0)
#     else:
#         (x, y) = extended_euclidean(b, a % b)
#         return (y, x - (a // b) * y)


#part2()
  
def multiplicative_inverse(a, m):
    """Find the multiplicative inverse of a modulo m."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        # q is quotient
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def solve_linear_congruence(a, b, L):
    """Solve the linear congruence ax ≡ b mod L."""
    d = gcd(a, L)
    if b % d != 0:
        return "No solution"

    a, b, L = a // d, b // d, L // d
    x = multiplicative_inverse(a, L) * b % L
    return x

DECK_LEN = 119315717514047

def prev_pos_increment(current_pos, increment):
    return solve_linear_congruence(increment, current_pos, DECK_LEN)

def prev_pos_stack(current_pos):
    return DECK_LEN - current_pos - 1

def prev_pos_cut(current_pos, cut):
    if cut > 0:
        if current_pos >= DECK_LEN - cut:
            return current_pos - (DECK_LEN - cut)
        if current_pos < DECK_LEN - cut:
            return current_pos + cut
    if cut < 0:
        if current_pos > (abs(cut) - 1):
            return current_pos + cut # remember cut is -ve
        else:
            return DECK_LEN - (abs(cut) - current_pos)

rules = []
for line in input[-1:0:-1]:
    if "deal with increment" in line:
        incr = ints(line)[0]
        rules.append((1,incr))
    if "deal into new stack" in line:
        rules.append((2,0))
    if "cut" in line:
        cutn = ints(line)[0]
        rules.append((3,cutn))

#history = [None] * 3
states = set()
def card_at_pos(pos, times=1):
    global history, states, rules
    seek = pos
    for i in range(times):
        for action,num in rules:
                if action == 1:
                    seek = prev_pos_increment(seek, num)
                if action == 2:
                    seek = prev_pos_stack(seek)
                if action == 3:
                    seek = prev_pos_cut(seek, num)
        #print(i, seek)
        #history.append(seek)
        #history = history[1:]
        if seek in states:
            print("REPEAT at ", i)
        states.add(seek)
    return seek

#unit tests with deck size == 10

# assert(prev_pos_cut(8, 3) == 1)  # should be 1
# assert(prev_pos_cut(7, 3) == 0)  # should be 0
# assert(prev_pos_cut(6, 3) == 9)  # should be 9

# assert(prev_pos_cut(4, -4) == 0) # should be 0
# assert(prev_pos_cut(5, -4) == 1) # should be 1
# assert(prev_pos_cut(3, -4) == 9) # should be 9

print(card_at_pos(2020, 10000000))