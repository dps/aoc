
from itertools import product
CDIR8 = [(1-1j), (-1-1j), (1+1j), (-1+1j), (1+0j), (-1+0j), -1j, 1j]

input = [i.strip() for i in open("input","r").readlines()]

def solve():
    symbols, symbolposes, pnums = set(), set(), []
    partial_num, p_num_pos = '', []

    def push_num():
        nonlocal pnums, partial_num, p_num_pos
        if partial_num != '':
            pnums.append((partial_num, p_num_pos))
        partial_num, p_num_pos = '', []

    for y, line in enumerate(input):
        for x, ch in enumerate(line + "."):
            if ch.isdigit():
                partial_num += ch
                p_num_pos.append(x + 1j*y)
            else:
                push_num()

            if not ch.isdigit() and ch != '.':
                symbols.add(x + 1j*y)
                symbolposes.add((ch, x + 1j*y))

    tot = 0
    for nstr, poses in pnums:
        for p,d in product(poses, CDIR8):
            if p+d in symbols:
                tot += int(nstr)
                break

    print("part1:", tot)

    tot = 0
    for ch,p in [s for s in symbolposes if s[0] == "*"]:
        c, ss = 0, []
        for pn in pnums:
            for pnn, d in product(pn[1], CDIR8):
                if pnn+d == p:
                    c += 1
                    ss.append(int(pn[0]))
                    break
        if c == 2:
            tot += ss[0] * ss[1]
    print("part2:", tot)

solve()
