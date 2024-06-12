
from utils import *

input = "3113322113"
i2 = [(1, 3), (1, 1), (1, 1), (1, 3), (1, 3), (1, 2), (1, 2), (1, 1), (1, 1), (1, 3)]

def looksay(ll):
    ans = []
    prev_count, prev_val = None, None
    for cnt,val in ll:
        if prev_val == None:
            prev_val = val
            prev_count = cnt
        elif val == prev_val:
            prev_count += cnt
        else:
            ans.append((1, prev_count))
            ans.append((1, prev_val))
            prev_val = val
            prev_count = cnt

    ans.append((1, prev_count))
    ans.append((1, prev_val))

    return ans

s = i2
for i in range(50):
    s = looksay(s)
    if i == 39: # Part 1
        print(sum([c for c,_ in s]))        

print(sum([c for c,_ in s]))