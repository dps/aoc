from utils import *

real = "853192647"
test = "389125467"
input = real

def solve(moves=10000000, part2=True):
    cups = [int(ch) for ch in input]
    max_l = max(cups)
    if part2:
        cups = cups + list(range(max_l + 1,1000001))
    min_l, max_l = min(cups), max(cups)

    #dmap = {} # O(1) lookup for any val.

    # head = None
    # one = None
    # prev = None
    # for v in cups:
    #     n = Dll(v, prev, None)
    #     if not prev:
    #         head = n
    #     else:
    #         prev.set_nxt(n)
    #     prev = n
    #     if v == 1:
    #         one = n
    #     dmap[v] = n
    # head.set_prv(prev) # Connect the ends
    # prev.set_nxt(head)

    head, dmap, one = Sll.parse(cups, 1)

    while moves > 0:
        first = head.val()
        a = head.nxt()
        b = a.nxt()
        c = b.nxt()
        
        # splice out taken
        head.set_nxt(c.nxt())

        in_hand = {a.val(), b.val(), c.val()}

        look_for = first - 1
        if look_for < min_l:
            look_for = max_l

        while look_for in in_hand:
            look_for -= 1
            if look_for < min_l:
                look_for = max_l
        
        found = dmap[look_for]
        tmp = found.nxt()
        found.set_nxt(a)

        c.set_nxt(tmp)
        moves -= 1
        head = head.nxt()

    if part2:
        print(one.nxt().val() * one.nxt().nxt().val())
    else:
        s = ""
        n = one.nxt()
        while n != one:
            s += str(n.val())
            n = n.nxt()
        print(s)

solve(moves=100, part2=False)
solve()