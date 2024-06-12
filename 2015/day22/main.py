from utils import *

BOSS_HP = 71
BOSS_DAMAGE = 10

spells = {
    'Magic Missile': {'cost': 53, 'damage': 4, 'heal': 0, 'armor': 0, 'turns': 0, 'mana': 0},
    'Drain': {'cost': 73, 'damage': 2, 'heal': 2, 'armor': 0, 'turns': 0, 'mana': 0},
    'Shield': {'cost': 113, 'damage': 0, 'heal': 0, 'armor': 7, 'turns': 6, 'mana': 0},
    'Poison': {'cost': 173, 'damage': 3, 'heal': 0, 'armor': 0, 'turns': 6, 'mana': 0},
    'Recharge': {'cost': 229, 'damage': 0, 'heal': 0, 'armor': 0, 'turns': 5, 'mana': 101},
}

part2 = False

@cache
def dfs(player_hp, player_mana, boss_hp, players_turn, effects):
    armor = 0
    next_effects = set()
    for effect in effects:
        # A frozen set like (("Shield", 6),...)
        name, turns_remaining = effect
        if name == "Shield":
            armor += 7
        if name == "Poison":
            boss_hp -= 3
        if name == "Recharge":
            player_mana += 101
        turns_remaining -= 1
        if turns_remaining > 0:
            next_effects.add((name, turns_remaining))
    
    if boss_hp <= 0:
        return 0
    
    if not players_turn:
        player_hp -= max(1, BOSS_DAMAGE - armor)
        if (player_hp <= 0):
            return math.inf
        return dfs(player_hp, player_mana, boss_hp, True, frozenset(next_effects))
    else:
        if part2:
            player_hp -= 1
            if player_hp <= 0:
                return math.inf
        min_spend = math.inf
        for cast, spell_data in spells.items():
            spend = spell_data["cost"]
            if cast in ["Shield", "Poison", "Recharge"] and cast in [n for n,_ in next_effects]:
                continue
            if spell_data["cost"] > player_mana:
                continue
            if cast == "Shield":
                spend += dfs(player_hp, player_mana - spell_data["cost"], boss_hp, False, frozenset(next_effects | {("Shield", 6)}))
            if cast == "Magic Missile":
                # boss hp gets checked after effects on next turn, don't need to here?
                spend += dfs(player_hp, player_mana - spell_data["cost"], boss_hp-4, False, frozenset(next_effects))
            if cast == "Drain":
                spend += dfs(player_hp + 2, player_mana - spell_data["cost"], boss_hp - 2, False, frozenset(next_effects))
            if cast == "Poison":
                spend += dfs(player_hp, player_mana - spell_data["cost"], boss_hp, False, frozenset(next_effects | {("Poison", 6)}))
            if cast == "Recharge":
                spend += dfs(player_hp, player_mana - spell_data["cost"], boss_hp, False, frozenset(next_effects | {("Recharge", 5)}))
            if spend < min_spend:
                min_spend = spend
        return min_spend
    

print(dfs(50, 500, BOSS_HP, True, frozenset()))
part2 = True
dfs.cache_clear()
print(dfs(50, 500, BOSS_HP, True, frozenset()))

