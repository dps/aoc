input = [i.strip() for i in open("input.txt","r").readlines()]

def solve(ilen=4):
    last = []
    for i, ch in enumerate(input[0]):
        last.append(ch)
        if len(set(last[-ilen:])) == ilen:
            break
    print(i + 1)

if __name__ == '__main__':
    solve(4)
    solve(14)