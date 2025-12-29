D = [line.strip() for line in open("input")]

def part1():
    global D
    tot = 0
    for r in D[0].split(','):
        a, b = r.split('-')
        a = int(a)
        b = int(b)
        for i in range(a, b + 1):
            str_i = str(i)
            if len(str_i)%2 == 0:
                left,right = str_i[:len(str_i)//2], str_i[len(str_i)//2:]
                if left == right:
                    tot += i

    print(tot)

def repeats(i):
    str_i = str(i)
    L = len(str_i)
    for i,j in enumerate(range(len(str_i)//2)):
        start = str_i[:j+1]
        if str_i == start * int(L/(i+1)):
            return True
    return False

def part2():
    global D
    tot = 0
    for r in D[0].split(','):
        a, b = r.split('-')
        a = int(a)
        b = int(b)
        for i in range(a, b + 1):
            if repeats(i):
                tot += i
    print(tot)

part1()
part2()

