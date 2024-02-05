import re


def ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))


banks = ints(open("input", "r").readlines()[0])
L = len(banks)

seen = set()
c, p1 = 0, 0
again, p2 = None, 0
while True:
    if tuple(banks) in seen:
        if again == None:
            p1 = c
            again = tuple(banks)
        else:
            if tuple(banks) == again:
                p2 = c - p1
                break
    else:
        seen.add(tuple(banks))

    n = max(banks)
    b = banks.index(n)
    banks[b] = 0
    for i in range(n):
        banks[(b + i + 1) % L] += 1

    c += 1

print(p1, p2)
