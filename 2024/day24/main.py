
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

vals, wires = bundles(D)

F = {
    'AND': lambda a,b: a & b,
    'OR': lambda a,b: a | b,
    'XOR': lambda a,b: a ^ b,
}

deps = {}
W = {}
V = set()

def simulate():

    for line in vals:
        name, v = line.split(": ")
        v = int(v)
        W[name] = v
        V.add(name)

    change = True
    while change:
        change = False
        for line in wires:
            inp, oup = line.split(" -> ")
            if oup in W:
                continue
            a,op,b = inp.split(" ")
            deps[oup] = (a,op,b)
            if a in W and b in W:
                W[oup] = F[op](W[a],W[b])
                change = True

    return sum(2**i * W[j] for i,j in enumerate(sorted([w for w in W.keys() if w.startswith("z")])))

actual_z = simulate() # 59364044286798
print("Part 1", actual_z)

#part2
x = sum(2**i * W[j] for i,j in enumerate(sorted([w for w in W.keys() if w.startswith("x")])))
y = sum(2**i * W[j] for i,j in enumerate(sorted([w for w in W.keys() if w.startswith("y")])))
expected_z = x + y #59398404285134
ezb = to_base(expected_z, 2)#'1101100000010111000100110010011010001011001110'
azb = to_base(actual_z, 2)  #'1101011111110111000100110001011010101101001110'


# Adder
#        C  
#    1 0 1 1
#    0 1 1 0
#    -------
#  1 0 0 0 1

# out bit is XOR (immediate sum, carry_bit)

def wire(prefix, n):
    return f"{prefix}{n:02}"

def check_out_bit(n):
    print("cob", n)
    a,op,b = deps[wire("z",n)]
    if op != "XOR":
        print("!! not xor", a,op,b,'->', wire("z",n))
        return False
    if n == 0:
        return sorted([a,b]) == [wire("x",n), wire("y",n)]
    else:
        # can be add and carry or carry and add in either order
        return (check_sum(a, n) and check_carry(b, n)) or (check_sum(b, n) and check_carry(a, n))
    
def check_sum(w, n):
    a,op,b = deps[w]
    print("cs", w, n, a, op, b)
    if op != "XOR":
        print("!! not xor", a,op,b,'->', w)
        return False
    return sorted([a,b]) == [wire("x",n), wire("y",n)]

def check_carry(w, n):
    print("cc", w, n)
    a,op,b = deps[w]
    if n == 1:
        if op != "AND":
            return False
        return sorted([a,b]) == [wire("x",0), wire("y",0)]
    if op != "OR":
        print("!! not or", a,op,b,'->', w)
        return False
    # We now have two possibilities again - a can be the immediate carry and b the propagated carry
    # or the otehr way around
    return check_immediate_carry(a, n-1) and check_propagated_carry(b, n-1) or check_immediate_carry(b, n-1) and check_propagated_carry(a, n-1)

def check_immediate_carry(w, n):
    print("cic", w, n)
    a,op,b = deps[w]
    if op != "AND":
        print("!! not and", a,op,b,'->', w)
        return False
    return sorted([a,b]) == [wire("x",n), wire("y",n)]

def check_propagated_carry(w, n):
    print("cpc", w, n)
    a,op,b = deps[w]
    if op != "AND":
        return False
    return check_sum(a, n) and check_carry(b, n) or check_sum(b, n) and check_carry(a, n)

for i in range(46):
    v = check_out_bit(i)
    print(i, v)
    if not v:
        break
#print(check_out_bit(19))
# y07 AND x07 -> z07
# wrong ^ should be the immediate carry bit for z08
## rkw XOR whp -> z08
#print(check_out_bit(8))

# gmt and z07 are swapped

# Now 11 breaks
# x11 AND y11 -> cbj
# should be XOR
# x11 AND y11 is the immediate carry bit for z12

#print(check_out_bit(12))
# qjj is wrong, so cbj and qjj are swapped

# 18 breaks
# khk OR stg -> z18
# inspection:
# y18 XOR x18 -> hch
# nff AND hch -> stg
# khk OR stg -> z18
# !! not or hch XOR nff -> dmn
# z18 and dmn are swapped

#breaks at 35
# !! not xor qnm AND rfk -> z35
# 35 False
#print(check_out_bit(36))
# cfk and z35 are swapped

# Inspection:
# cbj,cfk,dmn,gmt,qjj,z07,z18,z35