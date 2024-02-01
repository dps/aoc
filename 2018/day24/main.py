
from utils import *

D = bundles([i.strip() for i in open("example","r").readlines()])

def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!

def weak_to(s):
    m = re.search(r"weak to ([^);]*)", s)
    if not m:
        return []
    return set([w.strip() for w in m.groups()[0].split(",")])

def immune_to(s):
    m = re.search(r"immune to ([^);]*)", s)
    if not m:
        return []
    return set([w.strip() for w in m.groups()[0].split(",")])

def does_damage(s):
    m = re.search(r"does [0-9]* ([^ ]*) damage", s)
    if not m:
        return []
    return set([w.strip() for w in m.groups()[0].split(",")])


immune, infection = next(D)[1:],next(D)[1:]

teams = defaultdict(list)

for i,team in enumerate([immune, infection]):
    for line in team:
        count,hp,damage,initiative = ints(line)
        units = (count*damage, initiative, count, hp, damage, weak_to(line), immune_to(line), does_damage(line).pop())
        teams[i].append(units)
print(teams)
def do_battle(teams):
    ts = [sorted(teams[0], reverse=True), sorted(teams[1], reverse=True)]

    # Target selection
    picked = defaultdict(set)
    game_plan = []
    for attack in [0,1]:
        attackers = ts[attack]
        defenders = ts[0 if attack == 1 else 1]
        for k,attacker in enumerate(attackers):
            ep, initiative, count, hp, damage, weak_to, immune_to,does = attacker
            can_do = {}
            for j, defender in enumerate(defenders):
                ep_, initiative_, count_, hp_, damage_, weak_to_, immune_to_,does_ = defender
                if does in immune_to_ or j in picked[attack]:
                    can_do[j] = (0, ep_, initiative_, j, attack, initiative)
                else:
                    can_do[j] = (ep * (2 if does in weak_to_ else 1), ep_, initiative_, (2 if does in weak_to_ else 1), k, j, attack, initiative)
            print(k,does,can_do)
            plan = sorted(can_do.values(), reverse=True)
            will_attack = (-math.inf,) if plan[0][0] == 0 else plan[0]
            if will_attack[0] != -math.inf:
                picked[attack].add(will_attack[-2])
            game_plan.append(tuple(reversed(will_attack)))

    # Attacking
    # During the attacking phase, each group deals damage to the target it selected, if any.
    # Groups attack in decreasing order of initiative, regardless of whether they are part of the
    # infection or the immune system. (If a group contains no units, it cannot attack.)
    game_plan.sort(reverse=True)
    print(game_plan)
    teams = deepcopy(ts)
    for attacker in game_plan:
        if attacker[0] == -math.inf:
            continue
        other_team = 0 if attacker[1] == 1 else 1
        ep_, initiative_, count_, hp_, damage_, weak_to_, immune_to_,does_ = teams[other_team][attacker[2]]
        count = teams[attacker[1]][attacker[3]][2]
        damage = teams[attacker[1]][attacker[3]][4]
        mult = attacker[4]
        damage_to_do = count*damage*mult
        print(count, damage,mult)
        units_destroyed = damage_to_do // hp_
        print(attacker[1],attacker[3],"attacks",other_team,attacker[2],damage_to_do, "destroying ",units_destroyed)
        count_ -= units_destroyed
        if count_ < 0: count_ = 0
        teams[other_team][attacker[2]] = (count_ * damage_, initiative_, count_, hp_, damage_, weak_to_, immune_to_,does_)
    print("--")
    ts = [[u for u in teams[0] if u[2] > 0], [u for u in teams[1] if u[2] > 0]]
    return ts

while len(teams[0])>0 and len(teams[1])>0:
    teams = do_battle(teams)

print(teams)