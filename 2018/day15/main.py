from collections import deque, Counter
import math

D = [i.strip() for i in open("input","r").readlines()]
G = list("".join(D))
N = len(G)
w,h = len(D[0]), len(D)

U = {}

def opponent(ch):
    return ('E' if ch == 'G' else 'G')

def hp_then_p(unit):
    p,_,hp,_,_ = unit
    return (hp,p)

def is_combat(unit):
    global G, U
    p,ch,_,_,_ = unit
    enemy = opponent(ch)
    could_fight = []
    for d in [-w,-1,1,w]:
        if 0 <= p+d < N and G[p+d] == enemy:
            could_fight.append(U[p+d])
    if len(could_fight) == 0:
        return False, None
    else:
        could_fight.sort(key=hp_then_p)
        return True, could_fight[0][0]

def move(unit):
    global G
    p,ch,_,_,_ = unit
    enemy = opponent(ch)
    Q, visited, found_at, found = deque([(p,0,None)]),set([p]),math.inf,[]
    while Q:
        q,l,first_step = Q.popleft()
        if l > found_at:
            continue
        for d in [-w,-1,1,w]:
            fs = d if first_step == None else first_step
            p_ = q + d
            if p_ not in visited and 0 <= p_ < N:
                if G[p_] == enemy and l <= found_at:
                    found_at = l
                    found.append((p_,fs))
                elif G[p_] == '.':
                    visited.add(p_)
                    Q.append((p_,l+1,fs))
    if len(found) == 0:
        return None
    found.sort()
    return found[0][1]


def battle(epower, stop_on_elf_death=False):
    global G, U
    G = list("".join(D))
    U = {}
    units = []
    for i,ch in enumerate(G):
        if ch == 'E' or ch == 'G':
            U[i] = (i,ch,200,3 if ch == 'G' else epower,i)
            units.append(U[i])

    rounds,p = 0,0
    while True:
        units.sort()
                
        to_delete = set()
        to_consider = set([v[4] for v in units])
        for u in units:
            if u[4] in to_delete:
                continue

            p,ch,hp,power,name = U[u[0]]
            
            combat, where = is_combat(u)
            if not combat:
                dir = move(u)
                if dir != None:
                    G[p],G[p+dir] = '.', ch
                    del(U[p])
                    U[p+dir] = (p+dir,ch,hp,power,name)
                    combat, where = is_combat(U[p+dir])

            if combat:
                p_,ch_,hp_,power_,name_ = U[where]
                assert(ch_ == opponent(ch))
                assert(p_ == where)
                U[where] = (p_,ch_,hp_-power,power_,name_)
                if hp_-power <= 0:
                    if stop_on_elf_death and ch_ == 'E':
                        return False, None
                    to_delete.add(name_)
                    to_consider -= {name_}
                    G[where] = '.'
                    del(U[where])
                    if len(Counter([v[1] for v in U.values()]).keys()) == 1:
                        final_vals = sum([v[2] for v in U.values()])
                        if len(to_consider) == 1:
                            return True, (rounds + 1) * final_vals
                        else:
                            return True, rounds * final_vals
            to_consider.remove(name)

        units = [u for u in U.values() if u[4] not in to_delete]
        rounds += 1

print("Part 1", battle(3, stop_on_elf_death=False)[1])

for elf_power in range(4,20):
    success, val = battle(elf_power, stop_on_elf_death=True)
    if success:
        print("Part 2", val)
        break
