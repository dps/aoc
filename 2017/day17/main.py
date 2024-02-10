from collections import deque

step = 380
buf = deque([0])
p = 0

for i in range(1,2018):
    p = ((p+step) % i) + 1
    buf.insert(p, i)
print(buf[buf.index(2017)+1])

p,ans = 0,None
for i in range(1,50000001):
    p = ((p+step) % i) + 1
    if p == 1:
        ans = i
print(ans)