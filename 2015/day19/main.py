
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

patterns, medicine = bundles(D)
medicine = medicine[0]

BACKWARDS = defaultdict(list)

possible = set()

for line in patterns:
    # Al => ThF
    p,r = line.split(" => ")
    BACKWARDS[r].append(p)

    for match in re.finditer(p, medicine):
        possible.add(medicine[0:match.start()] + r + medicine[match.end():])

# Part 1
print(len(possible))

# This was my original solution, which worked on my input.
# It uses a greedy algorithm, but while it looks pretty, I learned it doesn't
# work on all input. It's a bit mean that the greedy algo works with some input
# but not all. 

# try longer matches first, going backwards
REPL = sorted(BACKWARDS.items(), key=lambda item: len(item[0]), reverse=True)

def neighbors(molecule):
    for r,ps in REPL:
        for p in ps:
            for match in re.finditer(r, molecule):
                replacement = molecule[0:match.start()] + p + molecule[match.end():]
                yield 1, replacement
                return # greedy algo


#print(dynamic_dijkstra(neighbors, medicine, "e")[0])

# This is the real solution. It depends on inspection of the input to realize that
# Rn, Y and Ar are like ( , ) and only on the RHS and the other rules are
# X => X(X) | X(X,X) | X(X,X,X)  OR e => XX OR X => XX
# I didn't figure this out myself as I was exposed to the idea that greedy doesn't
# work and the solution at the same time.

def tokenize(s):
    prev = None
    for ch in s:
        if ch.islower():
            yield prev + ch
            prev = None
        if ch.isupper():
            if prev != None:
                yield prev
            prev = ch

c = Counter(list(tokenize(medicine)))
aoc(len(list(tokenize(medicine))) - c['Rn'] - c['Ar'] - 2*c['Y'] - 1)
