from collections import defaultdict
import copy
input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    acc = defaultdict(list)
    for x in input:
        for i, b in enumerate(x):
            acc[i].append(b)
        gamma = ""
        epsilon = ""
        for k in range(len(acc.keys())):
            ones = sum(map(lambda x : x == "1", sorted(acc[k])))
            zeroes = sum(map(lambda x : x == "0", sorted(acc[k])))
            if ones > zeroes:
                gamma = gamma + "1"
                epsilon = epsilon + "0"
            else:
                gamma = gamma + "0"
                epsilon = epsilon + "1"
    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    acc = defaultdict(list)
    o = None
    c = None
    oxy = copy.deepcopy(input)
    coo = copy.deepcopy(input)
    for pos in range(len(input[0])):
        acc = [0,0]
        for num in oxy:
            acc[int(num[pos])] += 1
        selected = "1" if acc[1] >= acc[0] else "0"
        oxy = [x for x in filter(lambda x : x[pos] == selected, oxy)]
        if len(oxy) == 1:
            print("oxy", int(oxy[0],2))
            o = int(oxy[0],2)
        acc = [0,0]
        for num in coo:
            acc[int(num[pos])] += 1
        selected = "0" if acc[1] >= acc[0] else "1"
        coo = [ x for x in filter(lambda x : x[pos] == selected, coo)]
        if len(coo) == 1:
            print("coo", int(coo[0],2))
            c = int(coo[0],2) 
    print(o*c)
        

part1()
part2()
