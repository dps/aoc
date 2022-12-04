input = [i.strip() for i in open("input.txt","r").readlines()]
print(input)
count = 0
for x in input:
    z = [[int(z) for z in y.split('-')] for y in x.split(',')]
    r = [set(range(x[0],x[1]+1)) for x in z]
    i = r[0].intersection(r[1])
    if len(i) > 0: #== len(r[0]) or len(i) == len(r[1]):
        count = count + 1
print(count)