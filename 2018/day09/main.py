import re

def ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))

D = open("input","r").read()

class Dll(object):
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

players, last_marble = ints(D)
take = (i for i in range((last_marble*100)+1))
scores = [0 for _ in range(players)]

def play(part1_limit):
    ## Implements game using doubly linked list class Dll
    circle = Dll(0, None, None)
    circle.set_nxt(circle)
    circle.set_prv(circle)
    current = circle
    for marble in take:
        if marble % 23 == 0:
            for _ in range(7):
                current = current.prv()
            scores[marble % players] += marble + current.val()
            current.prv().set_nxt(current.nxt())
            current.nxt().set_prv(current.prv())
            current = current.nxt()
        else:
            current = current.nxt()
            new = Dll(marble, current, current.nxt())
            current.nxt().set_prv(new)
            current.set_nxt(new)
            current = new
        if marble == part1_limit:
            print("Part 1", max(scores))

play(last_marble)
print("Part 2", max(scores))
