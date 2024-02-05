from copy import copy

D = [int(i.strip()) for i in open("input","r").readlines()]
N = len(D)

def solve(part, D):
    i = 0
    c = 0
    while 0 <= i < N:
        j = i + D[i]
        if part == 1:
            D[i] = D[i] + 1
        else:
            D[i] = D[i] + 1 if D[i] < 3 else D[i] - 1
        i = j
        c += 1
    return c

print(solve(1, copy(D)), solve(2, copy(D)))