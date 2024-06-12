from utils import *

# Hit Points: 100
# Damage: 8
# Armor: 2
boss = {"hp": 109, "damage": 8, "armor": 2}

weapons = [
    (8, 4, 0),  # Dagger
    (10, 5, 0), # Shortsword
    (25, 6, 0), # Warhammer
    (40, 7, 0), # Longsword
    (74, 8, 0)  # Greataxe
]

# Armor:      Cost  Damage  Armor
armor = [
    (13, 0, 1),  # Leather
    (31, 0, 2),  # Chainmail
    (53, 0, 3),  # Splintmail
    (75, 0, 4),  # Bandedmail
    (102, 0, 5)  # Platemail
]

# Rings:      Cost  Damage  Armor
rings = [
    (25, 1, 0),   # Damage +1
    (50, 2, 0),   # Damage +2
    (100, 3, 0),  # Damage +3
    (20, 0, 1),   # Defense +1
    (40, 0, 2),   # Defense +2
    (80, 0, 3)    # Defense +3
]

# You must buy exactly one weapon; no dual-wielding.
# Armor is optional, but you can't use more than one.
# You can buy 0-2 rings (at most one for each hand).
# You must use any items you buy.
# The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.


def battle(equipment):
    bb = deepcopy(boss)
    me = {"hp": 100, "damage": sum(e[1] for e in equipment), "armor": sum(e[2] for e in equipment)}
    while bb["hp"] > 0 and me["hp"] > 0:
        # take a turn
        bb["hp"] = bb["hp"] - max(1, me["damage"]-bb["armor"])
        if bb["hp"] <= 0:
            break
        me["hp"] = me["hp"] - max(1, bb["damage"] - me["armor"])
        if me["hp"] <= 0:
            break

    return me["hp"] > 0

minspend = math.inf
maxspend = -math.inf

for weapon in weapons: # must choose one
    for arm in armor + [(0,0,0)]: # must choose one or none
        for lr in rings + [(0,0,0)]:
            for rr in rings + [(0,0,0)]:
                if rr == lr:
                    continue
                gold = weapon[0] + arm[0] + lr[0] + rr[0]
                equipment = [weapon, arm, lr, rr]
                if battle(equipment):
                    minspend = min(minspend, gold)
                else:
                    maxspend = max(maxspend, gold)

print(minspend, maxspend)