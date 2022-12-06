input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    score = 0
    last = []
    for ch in input[0]:
        score = score + 1
        last.append(ch)
        if len(set(last[-4:])) == 4:
            break
    print(score)

def part2():
    score = 0
    last = []
    for ch in input[0]:
        score = score + 1
        last.append(ch)
        if len(set(last[-14:])) == 14:
            break
    print(score)

if __name__ == '__main__':
    part1()
    part2()