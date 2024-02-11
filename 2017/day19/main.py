
D = [i for i in open("input","r").readlines()]
w,h = len(D[0]), len(D)
s, d = None, (0,1)

for x, ch in enumerate(D[0]):
    if ch == '|':
        s = (x,0)
        break

path = ""
p, i = s, 1
while True:
    n = (p[0]+d[0], p[1]+d[1])
    if D[n[1]][n[0]].isalpha():
        path += D[n[1]][n[0]]
    elif D[n[1]][n[0]] not in "-|+":
        break
    elif D[n[1]][n[0]] == "+":
        for dd in [(0,1),(0,-1),(-1,0),(1,0)]:
            q = (n[0]+dd[0],n[1]+dd[1])
            if q == p or q[0] < 0 or q[0] >= w or q[1] < 0 or q[1] >= h:
                continue
            elif D[q[1]][q[0]] != ' ':
                d = dd
                break
    p = n
    i+=1

print(path, i)