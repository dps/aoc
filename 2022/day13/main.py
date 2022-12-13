import itertools
import functools

def validate(left, right):
    for (l,r) in itertools.zip_longest(left, right):
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            if l > r:
                return False
        cmp = None
        if isinstance(l, list) and isinstance(r, list):
            cmp = validate(l, r)
        if isinstance(l, list) and isinstance(r, int):
            cmp = validate(l, [r])
        if isinstance(l, int) and isinstance(r, list):
            cmp = validate([l], r)

        if l is None and not r is None:
            return True
        if r is None and not l is None:
            return False

        if cmp == True or cmp ==False:
            # can also be None to continue comparing
            return cmp

    return None

def wrap_validate(l,r):
    t = validate(l,r)
    if t == True:
        return -1
    elif t == False:
        return 1
    else:
        return 0

def part1():
    input = open("input.txt","r").read().split("\n\n")
    idx = 1
    sum = 0
    for lines in input:
        pair = lines.split('\n')
        left = eval(pair[0].strip())
        right = eval(pair[1].strip())
        if validate(left, right):
            sum = sum + idx
        idx += 1
    print(sum)

def part2():
    input = [eval(i.strip()) for i in open("input.txt","r").readlines() if i.startswith("[")]
    input.append([[2]])
    input.append([[6]])

    input = sorted(input, key=functools.cmp_to_key(wrap_validate))
    print((input.index([[2]])+1) *(input.index([[6]])+1))

if __name__ == '__main__':
    part1()
    part2()
