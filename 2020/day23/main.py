from utils import *

real = "853192647"
test = "389125467"
input = real

def move_cw(cups, spots):
    return cups[spots:] + cups[:spots]

def take(cups, n):
    return cups[:n], cups[n:]

def part1(moves=100):
    cups = [int(ch) for ch in input]
    min_l, max_l = min(cups), max(cups)
    while moves > 0:
        first = cups[0]
        cups = move_cw(cups, 1)
        removed, rest = take(cups, 3)
        pos = None
        look_for = first - 1
        while pos == None:
            try:
                pos = rest.index(look_for)
            except ValueError:
                look_for -= 1
                if look_for < min_l:
                    look_for = max_l
        cups = rest[:pos+1] + removed + rest[pos+1:]
        moves -= 1
    one = cups.index(1)
    print("".join([str(ch) for ch in cups[one+1:]+cups[:one]]))

class dll(object):

    def __init__(self, val, prv, nxt):
        self._val = val
        self._prv = prv
        self._nxt = nxt

    def set_nxt(self, n):
        self._nxt = n

    def set_prv(self, n):
        self._prv = n

    def nxt(self):
        return self._nxt

    def prv(self):
        return self._prv

    def val(self):
        return self._val

def part2(moves=10000000):
    cups = [int(ch) for ch in input]
    max_l = max(cups)
    cups = cups + list(range(max_l + 1,1000001))
    min_l, max_l = min(cups), max(cups)

    dmap = {}

    head = None
    one = None
    prev = None
    for v in cups:
        n = dll(v, prev, None)
        if not prev:
            head = n
        else:
            prev.set_nxt(n)
        prev = n
        if v == 1:
            one = n
        dmap[v] = n
    head.set_prv(prev) # Connect the ends
    prev.set_nxt(head)

    while moves > 0:
        first = head.val()
        a = head.nxt()
        b = a.nxt()
        c = b.nxt()
        
        # splice out taken
        head.set_nxt(c.nxt())
        c.nxt().set_prv(head)

        in_hand = {a.val(), b.val(), c.val()}

        look_for = first - 1
        if look_for < min_l:
            look_for = max_l

        while look_for in in_hand:
            look_for -= 1
            if look_for < min_l:
                look_for = max_l
        
        found = dmap[look_for]
        tmp = found.nxt()
        found.set_nxt(a)
        a.set_prv(found)

        c.set_nxt(tmp)
        tmp.set_prv(c)
        moves -= 1
        head = head.nxt()

    print(one.nxt().val() * one.nxt().nxt().val())

part1()
part2()