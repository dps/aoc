
D = [i.strip() for i in open("input","r").readlines()]

p1, p2 = 0,0
for line in D:
    prev = []
    inb = 0
    candidate = False
    block = False
    has_aba = set()
    has_bab = set()
    for ch in line:
        if ch == "[":
            inb += 1
        if ch == "]":
            inb -= 1
        prev.append(ch)
        if inb == 0 and len(prev)>=4 and prev[-1] == prev[-4] and prev[-2] == prev[-3] and prev[-2] != prev[-1]:
            candidate = True
        if inb > 0 and len(prev)>=4 and prev[-1] == prev[-4] and prev[-2] == prev[-3] and prev[-2] != prev[-1]:
            block = True
        if inb > 0 and len(prev)>=3 and prev[-1] == prev[-3] and prev[-2] != prev[-1]:
            has_bab.add("".join(prev[-3:]))
        if inb == 0 and len(prev)>=3 and prev[-1] == prev[-3] and prev[-2] != prev[-1]:
            has_aba.add("".join(prev[-3:]))


    if candidate and not block:
        p1 += 1
    for a in has_aba:
        if (a[1]+a[0]+a[1]) in has_bab:
            p2 += 1
            break

print(p1, p2)