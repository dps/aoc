from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

MDIR8 = [p[0] + 1j*p[1] for _,p in DIR8.items()]

def solve(max_rounds):
    world = set()
    moves = deque([ ((-1j,1-1j,-1-1j), -1j, "N"),
                    ((1j,1+1j,-1+1j), 1j, "S"),
                    ((-1,-1+1j,-1-1j), -1, "W"),
                    ((1,1+1j,1-1j), 1, "E")])

    for y, row in enumerate(input):
        for x, ch in enumerate(row):
            if ch == '#':
                world.add(x+y*1j)

    for round in range(max_rounds):
        proposed = defaultdict(int)
        elf_mv = {}
        for elf in world:
            if not any([(elf + e) in world for e in MDIR8]):
                continue

            for mv in moves:
                if (elf + mv[0][0] not in world and
                    elf + mv[0][1] not in world and
                    elf + mv[0][2] not in world):
                    proposed[elf + mv[1]] += 1
                    elf_mv[elf] = elf + mv[1]
                    break

        if len(elf_mv.keys()) == 0:
            print("pt2 DONE at round", round+1)
            return(round+1)
        for elf, proposed_mv in elf_mv.items():
            if proposed[proposed_mv] == 1:
                world.remove(elf)
                world.add(proposed_mv)
        moves.rotate(-1)

    mix,mxx = int(min([x.real for x in world])), int(max([x.real for x in world]))
    miy,myy = int(min([x.imag for x in world])), int(max([x.imag for x in world]))

    space = 0
    for y in range(miy,myy+1):
        for x in range(mix,mxx+1):
            if (x+y*1j) not in world:
                space += 1
    print("pt1 spaces after max_rounds", space)
    return(space)

if __name__ == '__main__':
    assert(solve(10) == 3800)   # 0.14s
    assert(solve(1000) == 916)  # 3.95s