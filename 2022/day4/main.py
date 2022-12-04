def char_to_score(ch):
    t = ord(ch)
    if t >= ord('a') and t <= ord('z'):
        return t - ord('a') + 1
    if t >= ord('A') and t <= ord('Z'):
        return t - ord('A') + 27

def first():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    score = 0
    for l in lines:
        line = l.strip()
        pairs = line.split(',')
        first = [i for i in range(int(pairs[0].split('-')[0]), int(pairs[0].split('-')[1])+1)]
        second = [i for i in range(int(pairs[1].split('-')[0]), int(pairs[1].split('-')[1])+1)]
        all_f_in_s = True
        all_s_in_f = True
        for a in first:
            if not a in second:
                all_f_in_s = False
                break
        for a in second:
            if not a in first:
                all_s_in_f = False
                break
        if (all_f_in_s or all_s_in_f):
            score = score + 1
    print(score)

def second():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    score = 0
    for l in lines:
        line = l.strip()
        pairs = line.split(',')
        first = [i for i in range(int(pairs[0].split('-')[0]), int(pairs[0].split('-')[1])+1)]
        second = [i for i in range(int(pairs[1].split('-')[0]), int(pairs[1].split('-')[1])+1)]
        any_f_in_s = False
        any_s_in_f = False
        for a in first:
            if a in second:
                any_f_in_s = True
        for a in second:
            if a in first:
                any_s_in_f = True
        if (any_f_in_s or any_s_in_f):
            score = score + 1
    print(score)


if __name__ == '__main__':
    second()
