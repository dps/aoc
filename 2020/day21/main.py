from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def solve():
    all_ingredients = set()
    ingredient_count = Counter()
    allergens_to_ingreds = defaultdict(list)

    for line in input:
        
        ingredients = line.split(" (contains ")[0].split(" ")
        ingredient_count.update(ingredients)
        allergens = line.split(" (contains ")[1].replace(", ",",").replace(")","").split(",")
        all_ingredients.update(ingredients)
        for allergen in allergens:
            allergens_to_ingreds[allergen].append(set(ingredients))


    a_g = defaultdict(set)
    greds = deepcopy(all_ingredients)
    for allergen in allergens_to_ingreds.keys():
        u = set.intersection(*allergens_to_ingreds[allergen])
        a_g[allergen] = u
        for x in u:
            greds -= {x}

    print(sum([ingredient_count[g] for g in greds]))

    mapped = {}
    ordered = []
    while len(a_g.keys()) > 0:
        for a in a_g.keys():
            if len(a_g[a]) == 1:
                mapped[a] = a_g[a].pop()
                ordered.append((a,mapped[a]))
                for v in a_g.keys():
                    a_g[v] = a_g[v] - {mapped[a]}
                del(a_g[a])
                break

    print(",".join([v for k,v in sorted(ordered)]))


solve()
