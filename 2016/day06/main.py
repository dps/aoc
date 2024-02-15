from collections import defaultdict, Counter

D = [i.strip() for i in open("input","r").readlines()]

chars = defaultdict(list)
for line in D:
    for i,ch in enumerate(line):
        chars[i].append(ch)

p1 = ""
p2 = ""
for j in sorted(chars.keys()):
    p1 += (Counter(chars[j]).most_common()[0][0])
    p2 += (Counter(chars[j]).most_common()[-1][0])

print(p1,p2)
