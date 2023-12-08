
from utils import *

#input = [int(i.strip()) for i in open("input","r").readlines()]
d = [i.strip() for i in open("input","r").readlines()]

print(d)
# LLRLRRRLRRRLRRLLRRRLLRRLLRLRLRRRLRRRLLRRRLLRRRLRRLRRLRLRRLLRRRLRRRLLRRRLRRLLLRRLRLLLRLRRRLRLRLLLRRLRRLLLRRRLLRRRLRLRLLRRLRLRRRLRLRLLRLRRLRRRLRRLRLRRRLRLRRLRRLRLRRLLRLRLRRLRLLRRLRRLRLRRLLRLRLLRRLLRLLLRRLRLRRRLRRRLRRRLRLRLRRRLLLRLRRLRLRRRLRRRLRRRLRLRRRLRRRLRRRLRRRR

# GLR = (SPQ, LKJ)
dirs= d[0]
D = d[2:]
left = {}
right = {}
for line in D:
    left[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[0][1:]
    right[line.split(" = ")[0]] = line[1:].split(" = ")[1].split(", ")[1][:-1]

curr = 'AAA'
steps = 0
i = 0
while curr != 'ZZZ':
    d = dirs[i]
    i+=1
    i = i % len(dirs)
    if d == 'L':
        curr = left[curr]
    if d == 'R':
        curr = right[curr]
    steps += 1
    

    
aoc(steps)
