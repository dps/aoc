from utils import *

D = [int(i.strip()) for i in open("input","r").readlines()]

def solve(parts=3):
    S = sum(D)
    T = S//parts
    assert(T*parts == S)

    min_c = []

    for i in range(7):
        found = False
        for c in combinations(D, i):
            if sum(c) == T:
                found = True
                min_c.append((reduce(operator.mul, c), c))

    # Sort by QE
    min_c = sorted(min_c)

    def can_partition(nums, target):
        for i in range(2, len(nums) - 2):
            for p in combinations(nums, i):
                if sum(p) == target:
                    return True
        return False


    for c in min_c:
        d = deepcopy(D)
        qe, ns = c
        for n in ns:
            d.remove(n)
        if can_partition(d, T):
            print(qe)
            break
    
solve(3)
solve(4)