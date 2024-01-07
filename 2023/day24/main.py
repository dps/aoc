
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

# sx + t0 dx = s00 + t0 s03
# sy + t0 dy = s01 + t0 s04

# From (1)
# t0 (dx - s03) = s00 - sx
# t0 = (s00 - sx) / (dx - s03) (3)

# From (2)
# t0 (dy - s04) = s01 - sy
# t0 = (s01 - sy) / (dy - s04) (4)

# (3) == (4)
# (s00 - sx) / (dx - s03) = (s01 - sy) / (dy - s04)
# Cross-multiply
# (dy - s04)(s00 - sx) = (s01 - sy)(dx - s03)
# dy s00 - dy sx - s04 s00 + s04 sx = s01 dx - s01 s03 - sy dx + sy s03
# Rearrange (- RHS from both sides)

# dy s00 - dy sx - s04 s00 + s04 sx - s01 dx + s01 s03 + sy dx - sy s03 = 0  (3)
# same for second hailstone:
# dy s10 - dy sx - s14 s10 + s14 sx - s11 dx + s11 s13 + sy dx - sy s13 = 0  (4)

# (3) - (4); dy . sx etc terms cancel, making it linear!

# dy s00 - s04 s00 + s04 sx - s01 dx + s01 s03 - sy s03 - dy s10 + s14 s10 - s14 sx + s11 dx - s11 s13 + sy s13 = 0

# collect sx,sy,dx,dy

#sx: s04 - s14
#sy: s13 - s03 
#dx: s11 - s01
#dy: s00 - s10   == s04 s00 - s01 s03 - s14 s10 + s11 s13

#From stones 1 & 0 => 
# sx (s04 - s14) + sy (s13 - s03) + dx (s11 - s01) + dy (s00 - s10) = s04 s00 - s01 s03 - s14 s10 + s11 s13
#From stones 2 & 1 =>
# sx (s14 - s24) + sy (s23 - s13) + dx (s21 - s11) + dy (s10 - s20) = s14 s10 - s11 s13 - s24 s20 + s21 s23
#From stones 3 & 2 =>
# sx (s24 - s34) + sy (s33 - s23) + dx (s31 - s21) + dy (s20 - s30) = s24 s20 - s21 s23 - s34 s30 + s31 s33
#From stones 4 & 3 =>
# sx (s34 - s44) + sy (s43 - s33) + dx (s41 - s31) + dy (s30 - s40) = s34 s30 - s31 s33 - s44 s40 + s41 s43

# These form a system of linear equations of the form Ax = b so we can use any linalg solver / Gaussian elim
# or Cramer's method.

# numpy yields a correct but inexact answer:
# x = np.linalg.solve(a, b)
# print(x)
# [ 2.70392224e+14  4.63714142e+14  2.60000000e+01 -3.31000000e+02]

# import numpy as np

# A = np.array([[s[0][4] - s[1][4], s[1][3] - s[0][3], s[1][1] - s[0][1], s[0][0] - s[1][0]],
#     [s[1][4] - s[2][4], s[2][3] - s[1][3], s[2][1] - s[1][1], s[1][0] - s[2][0]],
#     [s[2][4] - s[3][4], s[3][3] - s[2][3], s[3][1] - s[2][1], s[2][0] - s[3][0]],
#     [s[3][4] - s[4][4], s[4][3] - s[3][3], s[4][1] - s[3][1], s[3][0] - s[4][0]]], dtype=np.double)
# b = np.array([s[0][4] * s[0][0] - s[0][1] * s[0][3] - s[1][4] * s[1][0] + s[1][1] * s[1][3],
#      s[1][4] * s[1][0] - s[1][1] * s[1][3] - s[2][4] * s[2][0] + s[2][1] * s[2][3],
#      s[2][4] * s[2][0] - s[2][1] * s[2][3] - s[3][4] * s[3][0] + s[3][1] * s[3][3],
#      s[3][4] * s[3][0] - s[3][1] * s[3][3] - s[4][4] * s[4][0] + s[4][1] * s[4][3]], dtype=np.double)

# x = np.linalg.solve(A, b)

# mpmath gives an exact answer
import mpmath

s = stones

A = mpmath.matrix([[s[0][4] - s[1][4], s[1][3] - s[0][3], s[1][1] - s[0][1], s[0][0] - s[1][0]],
    [s[1][4] - s[2][4], s[2][3] - s[1][3], s[2][1] - s[1][1], s[1][0] - s[2][0]],
    [s[2][4] - s[3][4], s[3][3] - s[2][3], s[3][1] - s[2][1], s[2][0] - s[3][0]],
    [s[3][4] - s[4][4], s[4][3] - s[3][3], s[4][1] - s[3][1], s[3][0] - s[4][0]]])
b = mpmath.matrix([s[0][4] * s[0][0] - s[0][1] * s[0][3] - s[1][4] * s[1][0] + s[1][1] * s[1][3],
     s[1][4] * s[1][0] - s[1][1] * s[1][3] - s[2][4] * s[2][0] + s[2][1] * s[2][3],
     s[2][4] * s[2][0] - s[2][1] * s[2][3] - s[3][4] * s[3][0] + s[3][1] * s[3][3],
     s[3][4] * s[3][0] - s[3][1] * s[3][3] - s[4][4] * s[4][0] + s[4][1] * s[4][3]])

x = mpmath.lu_solve(A, b)

sx, sy, dx, dy = x

# From above.
t0 = (s[0][0] - sx) / (dx - s[0][3])
t1 = (s[1][0] - sx) / (dx - s[1][3])

# This is just the equation for velocity between positions given time
# elapsed.
dz = ((s[1][2] + t1*s[1][5]) - (s[0][2] + t0*s[0][5])) / (t1 - t0)

# sz + t1 dz - s12 - t1 s15 = 0
# sz = -t1 dz +s12 + t1 s15
sz = -t1 * dz + s[1][2] + t1*s[1][5]

print("day24", tot, int(sx)+int(sy)+int(sz))