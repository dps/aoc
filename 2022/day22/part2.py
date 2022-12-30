input = [i for i in open("input.txt", "r").readlines()]

FACES = {
    1: 1,
    2: 2,
    1 + 1j: 3,
    2j: 4,
    1 + 2j: 5,
    3j: 6
}


def face(p, face_width):
    return FACES[p.real // face_width + 1j * (p.imag // face_width)]


def loop(pos, facing, face_width):
    p, new_facing = None, None
    fac = face(pos, face_width)
    x_on_face, y_on_face = int(
        pos.real) % face_width, int(pos.imag) % face_width

    # 1 up goes to 6 coming in from left
    if fac == 1 and facing == -1j:
        y_on_new_face = x_on_face
        p = (3 * face_width + y_on_new_face) * 1j
        new_facing = 1
    # 1 left goes to 4 coming in from left (inv)
    if fac == 1 and facing == -1:
        y_on_new_face = face_width - y_on_face - 1
        p = (2 * face_width + y_on_new_face) * 1j
        new_facing = 1
    # 2 up goes to 6 from btm
    if fac == 2 and facing == -1j:
        p = (4 * face_width - 1) * 1j + x_on_face
        new_facing = -1j
    # 2 right -> 5 coming in from right inv
    if fac == 2 and facing == 1:
        y_on_new_face = face_width - y_on_face - 1
        p = (2 * face_width - 1) + (2 * face_width + y_on_new_face) * 1j
        new_facing = -1
    # 2 down -> 3 coming in from right
    if fac == 2 and facing == 1j:
        y_on_new_face = x_on_face
        p = (2 * face_width) - 1 + (face_width + y_on_new_face) * 1j
        new_facing = -1
    # 3 left -> 4 down from top
    if fac == 3 and facing == -1:
        x_on_new_face = y_on_face
        p = x_on_new_face + (2 * face_width) * 1j
        new_facing = 1j
    # 3 right -> 2 coming up from btm
    if fac == 3 and facing == 1:
        x_on_new_face = y_on_face
        p = 2 * face_width + x_on_new_face + (face_width - 1) * 1j
        new_facing = -1j
    # 4 up -> 3 from left
    if fac == 4 and facing == -1j:
        y_on_new_face = x_on_face
        p = face_width + (face_width + y_on_new_face) * 1j
        new_facing = 1
    # 4 left -> 1 from left (inv)
    if fac == 4 and facing == -1:
        y_on_new_face = face_width - y_on_face - 1
        p = face_width + y_on_new_face * 1j
        new_facing = 1
    # 5 right -> 2 coming in from left inv
    if fac == 5 and facing == 1:
        y_on_new_face = face_width - y_on_face - 1
        p = (3 * face_width) - 1 + y_on_new_face * 1j
        new_facing = -1
    # 5 down -> 6 coming in right
    if fac == 5 and facing == 1j:
        y_on_new_face = x_on_face
        p = (1 * face_width) - 1 + (3 * face_width + y_on_new_face) * 1j
        new_facing = -1
    # 6 left -> 1 coming in top
    if fac == 6 and facing == -1:
        x_on_new_face = y_on_face
        p = face_width + x_on_new_face
        new_facing = 1j
    # 6 right -> 5 in bottom
    if fac == 6 and facing == 1:
        x_on_new_face = y_on_face
        p = face_width + x_on_new_face + (3 * face_width - 1) * 1j
        new_facing = -1j
    # 6 down -> 2 coming in top
    if fac == 6 and facing == 1j:
        x_on_new_face = x_on_face
        p = (2 * face_width) + x_on_new_face
        new_facing = 1j

    return (p, new_facing)


def move_gen(move):
    gen = None
    for tok in move:
        if (not gen or isinstance(gen, str)) and tok.isdigit():
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


def solve():
    world, block = set(), {}
    move, origin, facing = None, None, 1

    for y, row in enumerate(input):
        if row[0].isdigit():
            move = row.strip()
            break
        for x, ch in enumerate(row):
            if ch == '\n':
                continue
            if ch != ' ':
                if not origin:
                    origin = x + y * 1j
                world.add(x + y * 1j)
                block[x + y * 1j] = ch
    pos = origin

    def advance(pos, n, facing, face_width):
        while n > 0:
            new_facing = facing
            p = pos + facing
            if p not in world:
                p, new_facing = loop(pos, facing, face_width)
            if block[p] == '.':
                pos = p
                facing = new_facing
            else:
                assert(block[p] == '#')
                return (pos, facing)
            n -= 1
        return (pos, facing)

    for mv in move_gen(move):
        if isinstance(mv, str):
            facing = turn(facing, mv)
        else:
            pos, facing = advance(pos, mv, facing, 50)
    print(1000 * (pos.imag + 1) + 4 * (pos.real + 1) + score[facing])


if __name__ == '__main__':
    solve()

    # assert(loop(2, -1j, 2) == (6j, 1))
    # assert(loop(3, -1j, 2) == (7j, 1))

    # assert(loop(2, -1, 2) == (5j, 1))
    # assert(loop(2+1j, -1, 2) == (4j, 1))

    # assert(loop(4, -1j, 2) == (0+7j, -1j))
    # assert(loop(5, -1j, 2) == (1+7j, -1j))

    # assert(loop(5, 1, 2) == (3+5j, -1))
    # assert(loop(5+1j, 1, 2) == (3+4j, -1))

    # assert(loop(4+1j, 1j, 2) == (3+2j), -1)
    # assert(loop(5+1j, 1j, 2) == (3+3j), -1)

    # assert(loop(2+2j, -1,2) == (4j, 1j))
    # assert(loop(2+3j, -1,2) == (1+4j, 1j))

    # assert(loop(3+2j, 1, 2) == (4+1j, -1j))
    # assert(loop(3+3j, 1, 2) == (5+1j, -1j))
    # # 4 up -> 3 from left

    # assert(loop(4j, -1j, 2) == (2+2j, 1))
    # assert(loop(1+4j, -1j, 2) == (2+3j, 1))

    # # 4 left
    # assert(loop(4j, -1, 2) == (2+1j, 1))
    # assert(loop(5j, -1, 2) == (2, 1))

    # # 5 right
    # assert(loop(3+4j, 1, 2) == (5+1j, -1))
    # assert(loop(3+5j, 1, 2) == (5, -1))

    # # 5 down -> 6 coming in right
    # assert(loop(2+5j, 1j, 2) == (1+6j, -1))
    # assert(loop(3+5j, 1j, 2) == (1+7j, -1))

    # # 6 left -> 1 coming in top
    # assert(loop(6j, -1, 2) == (2, 1j))
    # assert(loop(7j, -1, 2) == (3, 1j))

    # # 6 right -> 5 in bottom
    # assert(loop(1+6j, 1, 2) == (2+5j, -1j))
    # assert(loop(1+7j, 1, 2) == (3+5j, -1j))
    # # 6 down -> 2 coming in top
    # assert(loop(7j, 1j, 2) == (4, 1j))
    # assert(loop(1+7j, 1j, 2) == (5, 1j))

# FACES_EXAMPLE = {
#     (2): 1,
#     (0+1j): 2, (1+1j): 3, (2+1j): 4,
#     (2+2j): 5, (3+2j): 6,
# }

# def loop_example(pos, facing, face_width):
#     p = None
#     new_facing = None
#     fac = face(pos, face_width)
#     x_on_face = int(pos.real) % face_width
#     y_on_face = int(pos.imag) % face_width
#
#     # 1 up goes to 2 coming down from top facing \/
#     if fac == 1 and facing == -1j:
#         x_on_new_face = face_width - x_on_face - 1
#         p = x_on_new_face + (face_width * 1j)
#         new_facing = 1j
#     # 1 left goes to 3 coming down from top facing \/
#     if fac == 1 and facing == -1:
#         p = (face_width + y_on_face) + (face_width * 1j)
#         new_facing = 1j
#     # 1 right goes to 6 coming in from right facing <
#     if fac == 1 and facing == 1:
#         y_on_new_face = face_width - y_on_face - 1
#         p = ((face_width*4) - 1) + (face_width * 2 + y_on_new_face)*1j
#         new_facing = -1
#     # 2 up goes to 1 coming in from top facing down
#     if fac == 2 and facing == -1j:
#         x_on_new_face = face_width - x_on_face - 1
#         p = 2 * face_width + x_on_new_face
#         new_facing = 1j
#     # 2 left goes to 6 coming up from bottom facing ^
#     if fac == 2 and facing == -1:
#         x_on_new_face = face_width - y_on_face - 1
#         p = 3*face_width + x_on_new_face + (3j * face_width) - 1j
#         new_facing = -1j
#     # 2 down goes to 5 coming up from bottom facing ^
#     if fac == 2 and facing == 1j:
#         x_on_new_face = face_width - x_on_face - 1
#         p = 2*face_width + x_on_new_face + (3j * face_width) - 1j
#         new_facing = -1j
#     # 3 up goes to 1 coming in from left facing >
#     if fac == 3 and facing == -1j:
#         y_on_new_face = x_on_face
#         p = 2*face_width + y_on_new_face * 1j
#         new_facing = 1
#     # 3 down goes to 5 coming in from left facing >
#     if fac == 3 and facing == 1j:
#         y_on_new_face = face_width - x_on_face - 1
#         p = 2*face_width + y_on_new_face * 1j + (2j * face_width)
#         new_facing = 1
#     # 4 right goes to 6 coming in from top facing \/
#     if fac == 4 and facing == 1:
#         x_on_new_face = face_width - y_on_face - 1
#         p = x_on_new_face + 3*face_width + (2j * face_width)
#         new_facing = 1j
#     # 5 left goes to 3 coming in from bottom facing ^
#     if fac == 5 and facing == -1:
#         x_on_new_face = face_width - y_on_face - 1
#         p = x_on_new_face + 1*face_width + (2j * face_width) - 1j
#         new_facing = -1j
#     # 5 down goes to 2 coming up from bottom facing ^
#     if fac == 5 and facing == 1j:
#         x_on_new_face = face_width - x_on_face - 1
#         p = x_on_new_face + (2j * face_width) - 1j
#         new_facing = -1j
#     # 6 up goes to 4 coming in from right facing <
#     if fac == 6 and facing == -1j:
#         y_on_new_face = face_width - x_on_face - 1
#         p = (3*face_width) -1 + y_on_new_face *1j + (1j * face_width)
#         new_facing = -1
#     # 6 down goes to 2 coming in from left facing >
#     if fac == 6 and facing == 1j:
#         y_on_new_face = face_width - x_on_face - 1
#         p = 1j * face_width + y_on_new_face *1j
#         new_facing = 1
#     # 6 right goes to 1 coming in from right facing <
#     if fac == 6 and facing == 1:
#         y_on_new_face = face_width - y_on_face - 1
#         p = (3*face_width)-1 + y_on_new_face *1j
#         new_facing = -1
#     print("LOOP ",pos,p,new_facing)
#     return (p, new_facing)
