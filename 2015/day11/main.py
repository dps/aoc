
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def increment(password):
    s = list(password)
    for i in range(len(s)-1, -1, -1):
        if s[i] != 'z':
            s[i] = chr(ord(s[i]) + 1)
            break
        else:
            s[i] = 'a'
    return "".join(s)

def valid(password):
    bad = ["i", "o", "l"]
    for b in bad:
        if b in password:
            return False
    prevprev, prev = None, None
    straight = False
    pairs = set()
    pair_banned = 0
    for ch in password:
        if prevprev and prev and ord(prevprev) == ord(prev) - 1 and ord(ch) == ord(prev) + 1:
            straight = True
        if prev == ch and not (pair_banned > 0):
            pairs.add(ch)
            pair_banned = 2
        pair_banned -= 1
        prevprev = prev
        prev = ch

    return straight and len(pairs) >= 2

passw = D[0]
while not valid(passw):
    passw = increment(passw)

print(passw)
passw = increment(passw)
while not valid(passw):
    passw = increment(passw)

print(passw)
