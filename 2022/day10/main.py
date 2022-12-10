input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    X = 1
    cycle = 0
    sigs = []
    def push_significant(cycle, x):
        if cycle in [20, 60, 100, 140, 180, 220]:
            sigs.append(x * cycle)
    
    for line in input:
        toks = line.split(" ")
        if toks[0] == "noop":
            cycle += 1
            push_significant(cycle, X)
        if toks[0] == "addx":
            cycle += 1
            push_significant(cycle, X)
            cycle += 1
            push_significant(cycle, X)
            X = X + int(toks[1])
    print(sum(sigs))

def part2():
    X = 1
    cycle = 0
    def draw(cycle, x):
        if (cycle % 40) in [x-1,x,x+1]:
            print('#', end='')
        else:
            print('.', end='')
        if (cycle % 40) == 39:
            print()
    
    for line in input:
        toks = line.split(" ")
        if toks[0] == "noop":
            draw(cycle, X)
            cycle += 1
        if toks[0] == "addx":
            draw(cycle, X)
            cycle += 1
            draw(cycle, X)
            cycle += 1
            X = X + int(toks[1])

if __name__ == '__main__':
    part1()
    part2()