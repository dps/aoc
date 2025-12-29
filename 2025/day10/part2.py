from utils import *
from z3 import *

D = [line.strip() for line in open("input")]

def solve(buttons, joltage):
    opt = Optimize()

    # Create one variable per button (how many times we press it)
    button_vars = []
    for i, button in enumerate(buttons):
        var = Int(f"button_{i}")
        button_vars.append(var)
        opt.add(var >= 0)  # Can't press negative times
    
    for pos in range(len(joltage)):
        contributions = []
        for i, button in enumerate(buttons):
            if pos in button:
                contributions.append(button_vars[i])
        
        if contributions:
            opt.add(Sum(contributions) == joltage[pos])
        else:
            opt.add(joltage[pos] == 0)
    
    # Minimize the total number of button presses
    total_presses = Sum(button_vars)
    opt.minimize(total_presses)
    
    if opt.check() == sat:
        model = opt.model()
        # Return total button presses
        total = sum(model.eval(var).as_long() for var in button_vars)
        return total
    else:
        return math.inf


tot = 0
for line in D:
    parts = line.split(' ')
    dest = [x == '#' for x in parts[0].strip('[]')]
    initial_state = tuple([0] * len(dest))
    buttons = tuple(map(lambda x: tuple(map(int, x.strip('()').split(','))), parts[1:-1]))
    joltage = tuple(map(int, parts[-1].strip('{}').split(',')))
    press = solve(buttons, joltage)
    tot += press

print(tot)