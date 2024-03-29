
from collections import Counter

input = [i.strip() for i in open("input","r").readlines()]

order1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
order2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

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
        if part == 1:
            typ = Counter(hand)
        elif part == 2:
            h2 = best_joker(hand)
            typ = Counter(h2)
        nc = Counter(list(typ.values()))
        score = max(typ.values()) * 100 + 10 * (nc[2] if 2 in nc else 0)
        
        hands.append((score*10000000000000 + hand_to_val(hand, part), hand, bid))
    hands = sorted(hands)        
    print(sum([int(b[2])*int(r) for r,b in enumerate(hands, 1)]))

solve(1)
solve(2)