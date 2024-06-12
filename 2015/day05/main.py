
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def nice(s):
    v_count = 0
    twice_count = 0

    bad = ["ab", "cd", "pq", "xy"]
    for b in bad:
        if b in s:
            return False
    
    prev = None
    for ch in s:
        if ch in "aeiou":
            v_count += 1
        if ch == prev:
            twice_count += 1
        prev = ch
    return v_count >= 3 and twice_count >= 1


def nice2(s):
    twice_count = 0
    xyx_count = 0

    prev = None
    prevprev = None
    for i,ch in enumerate(s):
        if prev:
            match = prev+ch
            if match in (s[0:i-1] + "|" + s[i+1:]):
                twice_count += 1
        if prevprev == ch:
            xyx_count += 1
        prevprev = prev
        prev = ch

    return xyx_count >= 1 and twice_count >= 1

print(len([word for word in D if nice(word)]))
print(len([word for word in D if nice2(word)]))

