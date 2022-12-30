from utils import *
import sys
input = [i.strip() for i in open("input.txt","r").readlines()]

def manhattan(p, q):
    return abs(p.real - q.real) + abs(p.imag - q.imag)

def part1():
    w = {}
    mx, lx = 0, sys.maxsize
    test_row = 2000000

    for row in input:
        p = ints(row)
        s = p[0] + p[1]*1j
        b = p[2] + p[3]*1j
        mh = manhattan(s, b)
        if p[0]+mh > mx:
            mx = int(p[0]+mh)
        if p[0]-mh < lx:
            lx = int(p[0]-mh)

        if s.imag + mh < test_row:
            continue
        if s.imag - mh > test_row:
            continue

        w[s]=int(mh)
        w[b]=int(0)

    i = 0
    for x in range(lx,mx):
        if x + test_row*1j in w:
            continue
        for p,s in w.items():
            if s == 0:
                continue
            if manhattan(x + test_row*1j, p) <= s:
                i += 1
                break

    print(i)
    return i

def paint_around(p, dist, c, stop):
    res = []
    y=dist
    x=0
    for i in range(dist):
        if p.real+x > 0 and p.real+x < stop and p.imag - y >0 and p.imag -y < stop:
            c.add(p +x - y*1j)
        if p.real-x > 0 and p.real-x < stop and p.imag - y >0 and p.imag -y < stop:
            c.add(p -x - y*1j)
        if p.real+x > 0 and p.real+x < stop and p.imag + y >0 and p.imag +y < stop:
            c.add(p +x + y*1j)
        if p.real-x > 0 and p.real-x < stop and p.imag + y >0 and p.imag +y < stop:
            c.add(p -x + y*1j)
        y-=1
        x+=1
    return res


def part2():
    w = {}
    candidates = set()
    max_dim = 4000000

    for row in input:
        p = ints(row)
        s = p[0] + (p[1])*1j
        b = (p[2] + p[3]*1j)
        mh = abs(s.real - b.real) + abs(s.imag - b.imag)
        w[s]=int(mh)
        w[b]=int(0)

    checked = set()
    for s1,r1 in w.items():
        for s2, r2 in w.items():
            if not (s1.real+s2.real,s2.imag+s1.imag) in checked:
                if manhattan(s1, s2) == r1 + r2 + 2:
                    paint_around(s1, int(r1 + 1), candidates, max_dim)
                    checked.add((s1.real+s2.real,s2.imag+s1.imag))
                    break

    for candidate in candidates:
        keep = True
        if candidate in w:
            keep = False
            continue
        for p,s in w.items():
            if s == 0:
                continue
            if manhattan(candidate, p) <= s:
                keep = False
                break
        if keep:
            print(int(4000000 * candidate.real + candidate.imag))
            return(int(4000000 * candidate.real + candidate.imag))


if __name__ == '__main__':
    assert(part1() == 5525990)
    assert(part2() == 11756174628223)