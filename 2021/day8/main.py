from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    # 1,4,7,8 => 2, 4, 3, 7
    count = 0
    seg_counts = [2, 4, 3, 7]
    for line in input:
        right = line.split("|")[1]
        count += len([a for a in right.split(" ") if len(a) in seg_counts])
    print(count)

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


REV = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "acdeg": 2,
    "acdfg": 3,
    "abdfg": 5,
    "abdefg": 6,
    "abcdfg": 9,
    "abcefg": 0,
    "abcdefg": 8
}

def decode(examples, test_cases):
    # 1 => c,f ... 6 has an f but no c, 5 has an f but no c
    # 7 => a,c,f ... 4 has an f but no a so that pins down "a" definitively
    examples_by_length = defaultdict(list)
    for e in examples:
        s = examples_by_length[len(e)]
        s.append(e)
    mappings = {}

    assert(len(examples_by_length[3]) == 1)
    assert(len(examples_by_length[2]) == 1)

    seven = set(examples_by_length[3][0])
    one = set(examples_by_length[2][0])
    assert(len(seven.difference(one)) == 1)
    mappings["a"] = seven.difference(one).pop()

    # b and e are only in one each  of the len 5 examples (5)
    len_five = examples_by_length[5]
    str_five = reduce(lambda acc,x: acc + x, flatten(len_five), "")
    b_and_e = [k for k,v in Counter(str_five).items() if v == 1]
    four = set(examples_by_length[4].pop())
    mappings["b"] = four.intersection(b_and_e).pop()
    mappings["e"] = set(b_and_e).difference(set(mappings["b"])).pop()
    
    len_six = examples_by_length[6]
    for s in len_six:
        s.remove(mappings["a"])
        s.remove(mappings["b"])
        if mappings["e"] in s:
            s.remove(mappings["e"])

    str_six = reduce(lambda acc,x: acc + x, flatten(len_six), "")
    d_and_c = [k for k,v in Counter(str_six).items() if v == 2]

    mappings["c"] = one.intersection(set(d_and_c)).pop()
    mappings["f"] = one.difference(set(mappings["c"])).pop()

    for s in len_six:
        if mappings["c"] in s:
            s.remove(mappings["c"])
        if mappings["f"] in s:
            s.remove(mappings["f"])
    str_six = reduce(lambda acc,x: acc + x, flatten(len_six), "")
    mappings["g"] = [k for k,v in Counter(str_six).items() if v == 3][0]
    mappings["d"] = [k for k,v in Counter(str_six).items() if v == 2][0]

    invert = {v:k for k,v in mappings.items()}
    result = 0
    for case in test_cases:
        result *= 10
        dig = "".join(sorted([invert[x] for x in case]))
        result += int(REV[dig])

    return(result)

def part2():
    total = 0
    for line in input:
        examples = [sorted(x) for x in line.split("|")[0].strip().split(" ")]
        test_cases = [sorted(x) for x in line.split("|")[1].strip().split(" ")]
        total += decode(examples, test_cases)
    print(total)

if __name__ == '__main__':
    part1()
    part2()
