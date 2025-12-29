from utils import *

D = [line for line in open("input")]
O = D[len(D)-1]
D = D[:-1]
tot = 0

currentop = O[0]
nums = []
for i, ch in enumerate(O):
    v = ''
    for row in D:
        v += row[i]
    v = v.strip()
    if v == '':
        tot += sum(nums) if currentop == '+' else reduce(lambda x, y: x * y, nums)
        nums = []
    else:
        nums.append(int(v))
    if ch == '+' or ch == '*':
        currentop = ch
tot += sum(nums) if currentop == '+' else reduce(lambda x, y: x * y, nums)

print(tot)