
D = [i.strip() for i in open("input","r").readlines()]

def solve(part):
    pad = "123456789" if part == 1 else "  1   234 56789 ABC   D  "
    p,w = 4 if part == 1 else 10,3 if part == 1 else 5

    move = {'R': 1, 'L': -1, 'U': -w, 'D': w}
    code = ""
    for line in D:
        for ch in line:
            if ch == 'L' and p % w == 0:
                continue
            if ch == 'R' and p % w == 2:
                continue
            if ch == 'U' and p - w < 0:
                continue
            if ch == 'D' and p + w >= w*w:
                continue
            if pad[p + move[ch]] == ' ':
                continue
            p += move[ch]
        code += pad[p]

    print(code)

solve(1)
solve(2)