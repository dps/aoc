D = open("input","r").readlines()[0].strip()

s = len(D)
h = s // 2

p1, p2, prev = 0,0, None
for i, ch in enumerate(D):
    n = int(ch)
    if n == int(D[(i+1) % s]):
        p1 += n
    if n == int(D[(i+h) % s]):
        p2 += n
    prev = n

print(p1,p2)