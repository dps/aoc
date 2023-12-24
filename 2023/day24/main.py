
from utils import *
import sympy as sym

#input = [int(i.strip()) for i in open("input","r").readlines()]
D = [i.strip() for i in open("input","r").readlines()]
tot = 0


def find_intersection(A, d1, B, d2):
    a = A
    b = (A[0]+d1[0], A[1]+d1[1])
    c = B
    d = (B[0]+d2[0], B[1]+d2[1])

    a1 = b[1]-a[1]
    b1 = a[0]-b[0]
    c1 = a1*a[0] + b1*a[1]

    a2 = d[1]-c[1]
    b2 = c[0]-d[0]
    c2 = a2*c[0] + b2*c[1]

    determinant = a1*b2 - a2*b1

    if (determinant == 0):
        return None
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
        return x,y

stones = []
for line in D:
    stones.append(ints(line))

for p,q in combinations(stones, 2):
    i = find_intersection((p[0], p[1]), (p[3], p[4]), (q[0],q[1]), (q[3], q[4]))
    if i != None and 200000000000000 <= i[0] <= 400000000000000 and 200000000000000 <= i[1] <= 400000000000000:
        n = (i[0] - p[0]) / p[3]
        m = (i[0] - q[0]) / q[3]
        if n > 0 and m > 0:
            tot += 1

print("Part 1", tot)

sx,sy,sz = sym.Symbol('sx'), sym.Symbol('sy'), sym.Symbol('sz')
dx,dy,dz = sym.Symbol('dx'), sym.Symbol('dy'), sym.Symbol('dz')

eqns = []
vars = [sx, sy, sz, dx, dy, dz]
for i,s in enumerate(stones[:3]):
    nn = sym.Symbol("n"+str(i))
    eqns.append(sym.Eq(sx + nn * dx, s[0] + nn * s[3]))
    eqns.append(sym.Eq(sy + nn * dy, s[1] + nn * s[4]))
    eqns.append(sym.Eq(sz + nn * dz, s[2] + nn * s[5]))
    vars.append(nn)

result = sym.solve_poly_system(eqns, *vars)[0]
print("Part 2", result[0]+result[1]+result[2])


