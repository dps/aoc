from utils import *

# do it like sieve of erastothenes
D = [i.strip() for i in open("input","r").readlines()]
target = int(D[0])

def solve(part=1):
    houses = defaultdict(int)

    for i in range(1, target//10):
        n = 0
        for j in range(i, target//10, i):
            houses[j] += (10 if part == 1 else 11) * i
            n += 1
            if part == 2 and n >= 50:
                break

    for i in range(target):
        if houses[i] >= target:
            print(i)
            return

solve(1)
solve(2)

