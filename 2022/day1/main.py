def first():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    elf = 0
    totals = []
    max = 0
    max_elf = -1
    sum = 0
    for line in lines:
        if line == '\n':
            totals.append(sum)
            if sum > max:
                max = sum
                max_elf = elf
            elf = elf + 1
            sum = 0
        else:
            sum = sum + int(line)

    print(max, max_elf)

def second():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    elf = 0
    totals = []
    max = 0
    max_elf = -1
    sum = 0
    for line in lines:
        if line == '\n':
            totals.append(sum)
            if sum > max:
                max = sum
                max_elf = elf
            elf = elf + 1
            sum = 0
        else:
            sum = sum + int(line)

    totals.sort(reverse=True)
    print(totals[0] + totals[1] + totals[2])

if __name__ == '__main__':
    second()


