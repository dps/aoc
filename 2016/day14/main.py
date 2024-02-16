
from utils import *
import hashlib

salt = open("input","r").read().strip()
print(salt)

@cache
def mdn(n):
    s = hashlib.md5((salt+str(n)).encode()).hexdigest()
    for _ in range(2016):
        s = hashlib.md5(s.encode()).hexdigest()
    return s

c = 0
k = len(mdn(0))
for i in range(100000000):
    h = mdn(i)
    ch = None
    for j in range(2,k):
        if h[j-2] == h[j-1] and h[j-1] == h[j]:
            ch = h[j-1]
            break
    if ch != None:
        needle = ch * 5
        for j in range(1,1001):
            h = mdn(i+j)
            if h.find(needle) >= 0:
                c += 1
                if c == 64:
                    print(i)
                    sys.exit(0)

