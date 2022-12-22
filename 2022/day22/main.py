input = [i for i in open("inp.txt","r").readlines()]


def move_gen(move):
    gen = None
    for tok in move:
        if (not gen or type(gen) == str) and tok.isdigit():
            if gen:
                yield(gen)
            gen = int(tok)
        elif tok in "LR":
            yield(gen)
            gen = tok
        else:
            gen *= 10
            gen += int(tok)
    yield(gen)

def turn(facing, dir):
    print("turn", dir)
    if dir == "R":
        return facing * 1j
    else:
        return facing / 1j

score = {
    1: 0,
    0 + 1j: 1,
    -1: 2,
    -1j: 3
}

def part1():
    world = set()
    block = {}

    move = None
    origin = None

    for y, row in enumerate(input):
        if row[0].isdigit():
            move = row.strip()
            break
        for x, ch in enumerate(row):
            if ch == '\n':
                continue
            if ch != ' ':
                if not origin:
                    origin = x + y*1j
                world.add(x + y*1j)
                if (ch == "%"):
                    print(x, y)
                    return
                block[x + y*1j] = ch
    print(origin, move)
    pos = origin
    facing = 1

    def loop(pos, facing):
        if facing == 1:
            return min([x.real for x in world if x.imag == pos.imag]) + 1j*pos.imag
        if facing == 1j:
            return pos.real + min([x.imag for x in world if x.real == pos.real]) * 1j
        if facing == -1:
            return max([x.real for x in world if x.imag == pos.imag]) + 1j*pos.imag
        if facing == -1j:
            return pos.real + max([x.imag for x in world if x.real == pos.real]) * 1j

    def advance(pos, n, facing):
        while n > 0:
            print("advance", n, pos, facing)
            p = pos + facing
            if p not in world:
                # loop
                p = loop(pos, facing)
                print("loop", pos, facing, "->", p)
            if block[p] == '.':
                pos = p
            else:
                print("[" + block[p] + "]")
                assert(block[p] == '#')
                return pos
            n -= 1
        return pos

    for mv in move_gen(move):
        if type(mv) == str:
            facing = turn(facing, mv)
        else:
            pos = advance(pos, mv, facing)
    print(1000 * (pos.imag+1) + 4 * (pos.real + 1) + score[facing])




if __name__ == '__main__':
    part1()
