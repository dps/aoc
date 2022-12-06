input = [i.strip() for i in open("input.txt","r").readlines()]

prev = []
count = 0
for x in input:
    prev.append(int(x))
    if (len(prev) < 4):
        continue
    if sum(prev[-3:]) > sum(prev[-4:][0:3]):
        count = count + 1
  
print(count)
