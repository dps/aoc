from utils import *

divisor = 20201227
# card = 5764801
# door = 17807724
card = 18356117
door = 5909654

def xform(subj, loops):
    val = 1
    while loops > 0:
        val *= subj
        val %= divisor
        loops -= 1
    return val

def findx(subj, to_find):
    val = 1
    loops = 0
    res = {}
    while len(to_find) > 0:
        val *= subj
        val %= divisor
        loops += 1
        if val in to_find:
            res[val] = loops
            to_find.remove(val)
    return res

res = findx(7, [card, door])
aoc(xform(door, res[card]))