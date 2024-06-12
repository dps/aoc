
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

# Alice would lose 82 happiness units by sitting next to David.

def solve(part=1):
    rules = defaultdict(list)
    people = set()

    for line in D:
        name, _, dir, num, _, _, _, _, _, _, partner = line.split()
        partner = partner[0:-1]
        d = int(num)
        if dir == "lose":
            d = -d

        rules[name].append((partner, d))
        people.add(name)

    mm = 0
    if part == 2:
        people.add("Me")
    for perm in permutations(people):
        val = 0
        seating = list(perm)
        seating = [seating[-1]] + seating + [seating[0]]
        for i in range(1, len(seating)-1):
            here = seating[i]
            left = seating[i-1]
            right = seating[i+1]
            val += sum(d for p,d in rules[here] if p == left or p == right)

        mm = max(val, mm)

    print(mm)

solve(1)
solve(2)