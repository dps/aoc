from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def incr_preceeding_num(lstr, inc_by):
    l = lstr
    found,o,p = False,-1,len(l)
    n = ""
    for i in range(len(l)-1, -1, -1):
        if found and not l[i].isdigit():
            o = i
            break
        elif l[i].isdigit():
            if not found:
                p = i
            found = True
            n = l[i] + n
    if found:
        return lstr[0:o+1] + str(int(n)+inc_by) + lstr[p+1:]
    return lstr

def incr_following_num(rstr, inc_by):
    r = rstr
    found,o,p,n = False,-1,-1,""
    for i in range(len(r)):
        if found and not r[i].isdigit():
            p = i
            break
        elif r[i].isdigit():
            if not found:
                o = i
            found = True
            n += r[i]
    if found:
        return rstr[0:o] + str(int(n)+inc_by) + rstr[p:]
    return rstr
         
def explode(sn):
    depth, explode_at = 0, -1
    for i, ch in enumerate(sn):
        if ch == '[':
            if depth == 4:
                explode_at = i
                break
            depth += 1
        elif ch == ']':
            depth -= 1
    if explode_at > 0:
        fwd = sn[explode_at:].index("]") + 1
        exploded = eval(sn[explode_at:explode_at+fwd])
        l,r = sn[0:explode_at],(sn[explode_at:])[sn[explode_at:].index("]")+1:]
        l = incr_preceeding_num(l, exploded[0])
        r = incr_following_num(r, exploded[1])
        return(l+"0"+r)
    else:
        return sn

def split(sn):
    l,n = 0, ""
    for i, ch in enumerate(sn):
        if ch.isdigit():
            n += ch
        else:
            if n != "":
                if (int(n) > 9):
                    return(sn[0:l+1]+ str([int(int(n)//2), int(math.ceil(int(n)/2))])+ sn[i:])
                n = ""
            else:
                l = i
    return sn


def snailfish_add(a, b):
    prev = [a, b]
    while True:
        a = eval(explode(str(prev).replace(" ","")))
        if a == prev:
            a = eval(split(str(a)))
        if a == prev:
            return a
        prev = a

def magnitude(sn):
    l,r = sn[0], sn[1]
    if type(l) == int and type(r) == int:
        return 3*l + 2*r
    if type(l) == list and type(r) == int:
        return 3 * magnitude(l) + 2*r
    if type(l) == int and type(r) == list:
        return 3 * l + 2* magnitude(r)
    if type(l) == list and type(r) == list:
        return 3 * magnitude(l) + 2* magnitude(r)

def part1():
    acc = eval(input[0])
    for line in input[1:]:
        v = eval(line)
        acc = snailfish_add(acc, v)
    print(magnitude(acc))

def part2():
    inp = [eval(i) for i in input]
    m = 0
    for a,b in itertools.combinations(inp, 2):
        m = max(m, magnitude(snailfish_add(a, b)))
        m = max(m, magnitude(snailfish_add(b, a)))
    print(m) 


#part1()
part2()