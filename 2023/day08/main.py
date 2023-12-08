
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

dirs = input[0]
D = input[2:]
left, right = {}, {}
starts = []
for line in D:
    origin = line.split(" = ")[0]
    if origin.endswith("A"):
        starts.append(origin)

    left[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[0][1:]
    right[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[1][:-1]

print(len(dirs))


#263
# 19199
# 0 BPA 11309
# 0 BVA 17621
# 0 NDA 20777
# 0 AAA 16043
# 0 QCA 15517

prime = 263
cycles = [19199, 11309, 17621, 20777, 16043, 15517]
mods = [x % 263 for x in cycles]
print(mods)

def extended_euclidean(a, b):
    """
    Returns a pair of numbers (x, y) such that a * x + b * y = gcd(a, b)
    """
    if b == 0:
        return (1, 0)
    else:
        (x, y) = extended_euclidean(b, a % b)
        return (y, x - (a // b) * y)

def chinese_remainder_theorem(nr):
    """
    Solve the system of linear congruences:
    x ≡ rems[0] (mod nums[0])
    x ≡ rems[1] (mod nums[1])
    ...
    x ≡ rems[k] (mod nums[k])

    Where nums are pairwise coprime.
    """
    # Calculate the product of all nums
    N = 1
    for n,_ in nr:
        N *= n

    result = 0
    for n, r in nr:
        m = N // n
        inv_m, _ = extended_euclidean(m, n)
        result += r * inv_m * m

    return result % N

# is it a coprime modulus problem?
for i,start in enumerate(starts):
    c = start
    i = 0
    steps = 0
    for j in range(1):
        while not c.endswith("Z"):
            d = dirs[i]
            i+=1
            i = i % len(dirs)
            if d == 'L':
                c = left[c]
            if d == 'R':
                c = right[c]
            steps += 1
        print(i,start,steps)
print("----")
curr = 'AAA'
steps = 0
i = 0
zz = 0
while not zz == len(starts):
    zz = 0
    d = dirs[i]
    i+=1
    i = i % len(dirs)
    new = deepcopy(starts)
    for o,x in enumerate(starts):
        if d == 'L':
            x = left[x]
        if d == 'R':
            x = right[x]
        if x.endswith("Z"):
            zz += 1
        new[o] = x
    starts = new
    steps += 1
    


    
aoc(steps)
