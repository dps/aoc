input = [i.strip() for i in open("input", "r").readlines()]

def solve():
    dig = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

    p1,p2 = 0,0
    for line in input:
        ns1,ns2 = [],[]
        for i, ch in enumerate(line):
            if ch.isdigit():
                ns1.append(ch)
                ns2.append(ch)
            for dd,vv in dig.items():
                if line[i:].startswith(dd):
                    ns2.append(vv)
        p1 += int(ns1[0] + ns1[-1])
        p2 += int(ns2[0] + ns2[-1])
                
    print(p1, p2)

solve()
