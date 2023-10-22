from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    sections = bundles(input)

    fields = next(sections)
    all_vals = set()
    for line in fields:
        ns = positive_ints(line)
        all_vals.update(list(range(ns[0], ns[1]+1)))
        all_vals.update(list(range(ns[2], ns[3]+1)))

    _ = next(sections)

    valid_tickets = []
    tot = 0
    nearby = next(sections)
    for line in nearby:
        valid = True
        for i in positive_ints(line):
            if i not in all_vals:
                tot += i
                valid = False
        if valid:
            valid_tickets.append(line)

    aoc(tot)
    return valid_tickets

def part2():
    tickets = part1()
    sections = bundles(input)
    fields = next(sections)
    F = defaultdict(lambda:set())
    all_fields = set()

    for field in fields:
        ns = positive_ints(field)
        fn = field.split(":")[0]
        all_fields.add(fn)
        for x in range(ns[0],ns[1]+1):
            F[x].add(fn)
        for x in range(ns[2],ns[3]+1):
            F[x].add(fn)

    A = defaultdict(lambda:deepcopy(all_fields))

    for t in tickets[1:]:
        for p,v in enumerate(t.split(",")):
            A[p] = A[p] & F[int(v)]

    mapped = {}
    while len(mapped.keys()) < len(all_fields):
        B = deepcopy(A)
        for p,fields in B.items():
            if len(fields) == 1:
                mapped[p] = list(fields)[0]
                for q in A.keys():
                    A[q] = A[q] - {list(fields)[0]}
                break
    
    my_ticket = next(sections)[1]
    tot = 1
    for i,v in enumerate(my_ticket.split(",")):
        if 'departure' in mapped[i]:
            tot *= int(v)
    aoc(tot)

part2()
