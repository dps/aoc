D = open("input","r").read()

score = 0
level = 0
skip = False
in_garbage = False
gc = 0
for ch in D:
    if skip:
        skip = not skip
        continue
    if in_garbage:
        if ch == '!':
            skip = True
        elif ch == '>':
            in_garbage = False
        else:
            gc += 1
    elif ch == '{':
        level += 1
    elif ch == '}':
        score += level
        level -= 1
    elif ch == '<':
        in_garbage = True

print(score, gc)