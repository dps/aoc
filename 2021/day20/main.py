input = [i.strip() for i in open("input.txt","r").readlines()]

def grid_set_from_strs(lines):
    g = set()
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                g.add(x+y*1j)
    return g

def solve(part=1):
    enhance = [i == '#' for i in input[0]]
    image = grid_set_from_strs(input[2:])

    POS = [-1-1j, -1j, 1-1j, -1, 0, 1, -1+1j, 1j, 1+1j]
    
    for i in range(2 if part==1 else 50):
        min_x,min_y = int(min([p.real for p in image])), int(min([p.imag for p in image]))
        max_x,max_y = int(max([p.real for p in image])), int(max([p.imag for p in image]))
        next_image = set()
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                acc = 0
                for v in POS:
                    acc = acc << 1
                    if (x+v.real) > max_x or (x+v.real) < min_x or (y+v.imag > max_y) or (y+v.imag < min_y):
                        acc += 1 if (enhance[0] and (i % 2 == 1)) else 0
                    if (x+y*1j + v) in image:
                        acc += 1
                if enhance[acc]:
                    next_image.add(x+y*1j)
        image = next_image

    print(len(image))


solve(part=1)
solve(part=2)