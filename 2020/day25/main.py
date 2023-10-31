from utils import *

divisor = 20201227
# card = 5764801
# door = 17807724
card = 18356117
door = 5909654

def xform(subj, loops):
    return pow(subj, loops, divisor)

def findx(subj, to_find):
    val = 1
    loops = 0
    while True:
        val *= subj
        val %= divisor
        loops += 1
        if val == to_find:
            return loops

res = findx(7, card)
aoc(xform(door, res))