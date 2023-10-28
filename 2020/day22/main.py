from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    bundl = bundles(input)
    decks = []
    for b in bundl:
        d = []
        for card in b[1:]:
            d.append(int(card))
        decks.append(d)

    while len(decks[0]) > 0 and len(decks[1]) > 0:
        o,t = decks[0][0], decks[1][0]
        if o > t:
            decks[0].extend([o, t])
        else:
            decks[1].extend([t, o])
        decks[1] = decks[1][1:]
        decks[0] = decks[0][1:]

    winner = decks[0] if len(decks[0]) > 0 else decks[1]

    aoc(sum([l * r for (l,r) in zip(range(1, len(winner)+1), reversed(winner))]))

def state(o,t):
    return ",".join([str(i) for i in o]) + "|" + ",".join([str(i) for i in t])

def recurse(o,t):
    states = set()
    while len(o) > 0 and len(t) > 0:
        s = state(o,t)
        l,r = o.pop(0),t.pop(0)
        winner = None
        if s in states:
            winner = 0
            return 0, [l] + o
        else:
            if len(o) >= l and len(t) >= r:
                winner, _ = recurse(o[0:l],t[0:r])
            else:
                winner = 0 if l>r else 1
        states.add(s)
        if winner == 0:
            o.extend([l,r])
        else:
            t.extend([r, l])
    if len(o) > 0:
        return 0, o
    else:
        return 1, t


def part2():
    bundl = bundles(input)
    decks = []
    for b in bundl:
        d = []
        for card in b[1:]:
            d.append(int(card))
        decks.append(d)
    _, winner = recurse(decks[0], decks[1])
    aoc(sum([l * r for (l,r) in zip(range(1, len(winner)+1), reversed(winner))]))


part1()
part2()