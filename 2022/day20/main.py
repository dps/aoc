from utils import *
import random
from math import ceil

input = [int(i.strip()) for i in open("input.txt","r").readlines()]

zero = None

class dll(object):

    def __init__(self, val, op, prv, nxt):
        self._val = val
        self.op = op
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

    def _splice_out(self):
        self.nxt().set_prv(self.prv())
        self.prv().set_nxt(self.nxt())
        return self

    def move_n(self, rel):
        if rel == 0:
            return
        
        # Question was unclear if I should count myself when going back past start or not,
        # turns out by trial and error that I should not count myself.
        me = self._splice_out()
        new_left = self
        if rel < 0:
            for _ in range(abs(rel)+1):
                new_left = new_left.prv()
        if rel > 0:
            for _ in range(abs(rel)):
                new_left = new_left.nxt()

        right = new_left.nxt()
        new_left.set_nxt(me)
        right.set_prv(me)
        self.set_nxt(right)
        self.set_prv(new_left)

    def print(self):
        print(self._val, end=">")
        n = self
        while True:
            n = n.nxt()
            print(n._val, end=">")
            if n == self or n == None:
                break
        print()

    def get_score(self, key=1):
        s = 0
        n = self
        for _ in range(3):
            for _ in range(1000):
                n = n.nxt()
            s += n.val() * key
        return s
            

def solve(part=1):
    key = 1 if part == 1 else 811589153
    head = None
    prev = None
    n = None
    ogs = []
    for i,v in enumerate(input):
        n = dll(v, i, prev, None)
        ogs.append(n)
        if not prev:
            head = n
        else:
            prev.set_nxt(n)
        prev = n
    # Connect the ends
    head.set_prv(prev)
    prev.set_nxt(head)
    for _ in range(1 if part==1 else 10):
        for v in ogs:
            v.move_n(sign(v.val()) * (abs(v.val()) * key) % (len(input)-1))
                
            if v.val() == 0:
                zero = v
    score = zero.get_score(key)
    print(score)
    return score

if __name__ == '__main__':
    assert(solve(1) == 872)
    assert(solve(2) == 5382459262696)
