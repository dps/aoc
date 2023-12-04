
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def solve():
    p1 = 0
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    cards = defaultdict(int)
    for num, line in enumerate(input, 1):
        want = set(lmap(int, line.split("|")[0].split(":")[1].strip().split()))
        have = set(lmap(int, line.split("|")[1].strip().split()))
        cards[num] = len(want & have)
        if len(want & have) > 0:
            p1 += pow(2, len(want & have) - 1)

    print("part1", p1)
    
    wins = defaultdict(int)

    def countup(num):
        nonlocal cards, wins
        tt = cards[num]
        for card_num in range(num + 1, num + tt + 1):
            wins[card_num] += 1
            countup(card_num)
    
    for num, line in enumerate(input, 1):
        wins[num] += 1
        countup(num)

    print("part2", sum(wins.values()))

solve()
