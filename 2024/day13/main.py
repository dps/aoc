from utils import *
from z3 import *

D = [i.strip() for i in open("input","r").readlines()]

A, B = 3, 1
machines = bundles(D)

def optimize(a, b, p):
    opt = Optimize()
    press_a = Int('press_a')
    press_b = Int('press_b')
    opt.add(press_a * a[0] + press_b * b[0] == p[0])
    opt.add(press_a * a[1] + press_b * b[1] == p[1])
    opt.add(press_a >= 0)
    opt.add(press_b >= 0)

    total_cost = press_a * A + press_b * B
    opt.minimize(total_cost)

    if opt.check() == sat:
        model = opt.model()
        a_presses = model[press_a].as_long()
        b_presses = model[press_b].as_long()
        final_cost = (a_presses * A) + (b_presses * B)
        return final_cost
    else:
        return 0


p1, p2 = 0, 0
for m in machines:
    p1 += optimize(ints(m[0]), ints(m[1]), ints(m[2]))
    p2 += optimize(ints(m[0]), ints(m[1]), [10000000000000+x for x in ints(m[2])])

print(p1, p2)
