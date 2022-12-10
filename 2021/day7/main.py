from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def part1():
    starting = lmap(int, input[0].split(","))
    minf = sys.maxsize
    for pos in range(max(starting)):
        fuel = sum([abs(x-pos) for x in starting])
        if fuel < minf:
            minf = fuel
    print(minf)

def triangle(n):
    return int((n/2)*(n+1))

def part2():
    starting = lmap(int, input[0].split(","))
    minf = sys.maxsize
    for pos in range(max(starting)):
        fuel = sum([triangle(abs(x-pos)) for x in starting])
        if fuel < minf:
            minf = fuel
    print(minf)

if __name__ == '__main__':
    part1()
    part2()