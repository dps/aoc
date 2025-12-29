D = [line.strip() for line in open("input")]

d = 50
p1,p2 = 0, 0
for line in D:
    dir = line[0]
    num = int(line[1:])
    od = d
    if dir == 'L':
        d -= num
    elif dir == 'R':
        d += num
    
    d = d % 100

    if d == 0:
        p1 += 1
        p2 += 1

    if num > 100:
        p2 += (num // 100)
    num = num % 100

    if od != 0:
        if dir == 'L':
            if num > od: 
                p2 += 1
        elif dir == 'R':
            if num > (100 - od):
                p2 += 1

print(p1,p2)