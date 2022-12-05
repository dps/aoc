import re

input = [i for i in open("input.txt","r").readlines()]
phase = "stacks"
stacks = {}
num_stacks = (len(input[0]) + 1) // 4

for i in range(1, num_stacks + 1):
    stacks[i] = []
for x in input:
    if len(x) == 1:
        phase = "moves"
        continue
    if phase == "stacks":
        for a in range(1, num_stacks + 1):
            crate = x[(a*4)-3]
            if crate.isalpha():
                stacks[a].append(crate)
    else:
        # Each line is like: move 1 from 8 to 7
        mvs = re.findall(r'\d+', x)
        move = [stacks[int(mvs[1])].pop(0) for i in range(int(mvs[0]))]
        #move.reverse() # use for pt 1, commented out for part 2
        stacks[int(mvs[2])] = move + stacks[int(mvs[2])]

a=""
for i in range(1,num_stacks + 1):
    a=a+stacks[i][0]

print(a)

