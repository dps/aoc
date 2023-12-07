
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

order1 = list(reversed(list("AKQJT98765432")))
order2 = list(reversed(list("AKQT98765432J")))

def hand_to_val(hand, part=1):
    d = 0
    for k in hand:
        d += (order1 if part==1 else order2).index(k)
        d *= 100
    return d

def best_joker(hand):
    typ = Counter(hand)
    if hand == "JJJJJ":
        h2 = "AAAAA"
    else:
        mc = typ.most_common()
        if mc[0][0] == "J":
            mc = mc[1:]
        
        top = [n for n in mc if n[1] == mc[0][1]]
        tn = sorted([(order2.index(n[0]),n) for n in top])
        r = tn[-1][1][0]
        h2 = hand.replace("J", r)
    return h2

def solve(part=1):
    hands=[]
    for line in input:
        hand, bid = line.split()
        typ = Counter(hand)
        if part == 2:
            h2 = best_joker(hand)
            typ = Counter(h2)
        nc = Counter(list(typ.values()))
        score = max(typ.values()) * 100 + 10 * (nc[2] if 2 in nc else 0)
        
        hands.append((score*10000000000000 + hand_to_val(hand, part), hand, bid))
    hands = sorted(hands)        
    aoc(sum([int(b[2])*int(r) for r,b in enumerate(hands, 1)]))

solve(1)
solve(2)