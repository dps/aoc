from utils import *
import sys
input = [i.strip() for i in open("input.txt","r").readlines()]

def manhattan(p, q):
    return abs(p.real - q.real) + abs(p.imag - q.imag)

def part1():
    w = {}
    mx = 0
    lx = sys.maxsize
    test_row = 2000000

    for row in input:
        p = ints(row)
        s = p[0] + (p[1])*1j
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
        t = False
        for p,s in w.items():
            if s == 0:
                continue
            if manhattan(x + test_row*1j, p) <= s:
                t = True
        if t:
            i+=1

    print(i)

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

        paint_around(s, int(mh + 1), candidates, max_dim)

    res = deepcopy(candidates)
    iter = 0
    for candidate in candidates:
        iter += 1
        if iter % 1000000 == 0:
            # input.txt completes in ~1 min... Which means there must be a more
            # efficient algorithm. Wrote this to make sure it wasn't a waste to
            # let it finish.
            print("progress>>>", (iter/len(candidates))*100)
        if candidate in w:
            res.remove(candidate)
            continue
        for p,s in w.items():
            if s == 0:
                continue
            if manhattan(candidate, p) <= s:
                if candidate in res:
                    res.remove(candidate)
                break
    
    res = [x for x in res if x.real <= max_dim and x.real >= 0 and x.imag <= max_dim and x.imag >= 0]
    print(res)
    print(int(4000000 * res[0].real + res[0].imag))




if __name__ == '__main__':
    #part1()
    part2()