
D = open("input","r").read().strip()

def make(a,l):
    while len(a) < l:
        b = "".join(reversed(a)).translate(str.maketrans("10","01"))
        a = a + "0" + b
    return a[0:l]

def pairs(s):
    flip = None
    for ch in s:
        if flip == None:
            flip = ch
        else:
            yield flip + ch
            flip = None

def chksm(s):
    while len(s) % 2 == 0:
        s = "".join(["1" if a[0]==a[1] else "0" for a in pairs(s)])
    return s

print(chksm(make(D, 272)))
print(chksm(make(D, 35651584)))