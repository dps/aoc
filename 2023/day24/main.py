
from utils import *
from z3 import *

stones = lmap(ints, [i.strip() for i in open("input","r").readlines()])
tot = 0

def isect_sympy(s1,s2):
    # Eqns computed by sympy as follows:
    # n1,n2 = sym.Symbol('n1'), sym.Symbol('n2')
    # s1x,s1y,s2x,s2y = sym.Symbol('s1x'),sym.Symbol('s1y'),sym.Symbol('s2x'),sym.Symbol('s2y')
    # s1dx,s1dy,s2dx,s2dy = sym.Symbol('s1dx'),sym.Symbol('s1dy'),sym.Symbol('s2dx'),sym.Symbol('s2dy')

    # ex = sym.Eq(s1x + n1 * s1dx, s2x + n2 * s2dx)
    # ey = sym.Eq(s1y + n1 * s1dy, s2y + n2 * s2dy)
    # result = sym.solve([ex, ey], n1, n2)
    # print(result)
    # #n,m = (eval(str(result[n1])),eval(str(result[n2])))
    s1x,s1y,_,s1dx,s1dy,_ = s1
    s2x,s2y,_,s2dx,s2dy,_ = s2
    
    try:
        n1 = (-s1x*s2dy + s1y*s2dx - s2dx*s2y + s2dy*s2x)/(s1dx*s2dy - s1dy*s2dx)
        n2 = (s1dx*s1y - s1dx*s2y - s1dy*s1x + s1dy*s2x)/(s1dx*s2dy - s1dy*s2dx)
        ix = s1x + n1 * s1dx
        iy = s1y + n1 * s1dy
        return ix,iy,n1,n2
    except ZeroDivisionError:
        return None

for p,q in combinations(stones, 2):
    i = isect_sympy(p,q)
    if i != None and 200000000000000 <= i[0] <= 400000000000000 and 200000000000000 <= i[1] <= 400000000000000:
        n,m = i[2], i[3]
        if n > 0 and m > 0:
            tot += 1

print("Part 1", tot)

sx,sy,sz,dx,dy,dz = Real('sx'),Real('sy'),Real('sz'),Real('dx'),Real('dy'),Real('dz')
T = [Real(f't{i}') for i in range(3)]
solver = Solver()
for i in range(3):
  solver.add(sx + T[i]*dx - stones[i][0] - T[i]*stones[i][3] == 0)
  solver.add(sy + T[i]*dy - stones[i][1] - T[i]*stones[i][4] == 0)
  solver.add(sz + T[i]*dz - stones[i][2] - T[i]*stones[i][5] == 0)
res = solver.check()
model = solver.model()
print("Part 2", model.eval(sx+sy+sz))
