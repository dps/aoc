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
    for line in lines:
        m = line.strip()
        half = int(len(m) / 2)
        print(half)
        in_first= {}
        left = m[0:half]
        right = m[half:]
        print(m)
        print(len(left)," ",len(right))
        print()
        for char in left:
            in_first[char] = True
        for char in right:
            if char in in_first:
                score = score + char_to_score(char)
                break
    print(score)

def second():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    score = 0

    sack = 0
    common = {}
    for line in lines:
        m = line.strip()
        for char in set(m):
            if not char in common:
                common[char] = 1
            else:
                common[char] = common[char] + 1
        sack = sack + 1

        if sack == 3:
            for k in common:
                print(k, common[k])
                if common[k] == 3:
                    score = score + char_to_score(k)
                    print(k)
                    break
            sack = 0
            common = {}
    print(score)

if __name__ == '__main__':
    second()
