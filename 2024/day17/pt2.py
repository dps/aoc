target = [2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0]


def run(v):
    o = []
    A,B,C=v,0,0
    while True:
        B=A%8
        B=B^1
        C=A>>B
        B=B^C
        B=B^4
        A=A>>3
        o.append(B%8)
        if A==0:
            break
    return o

candidates = [0]
for pl in range(len(target)):
    cc = []
    for c in candidates:
        for i in range(8):
            nA = (c<<3) + i
            o = run(nA)
            if o == target[len(target)-pl-1:]:
                cc.append(nA)
    candidates = cc
print(min(candidates))
