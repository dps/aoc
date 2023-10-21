from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def vm(program):
    res = 0

    pc = 0
    acc = 0
    executed = set()
    while pc < len(program):
        if pc in executed:
            return ('loop', acc)
        executed.add(pc)
        line = program[pc]
        instruction, val = line.split(' ')
        val = ints(val)[0]

        if instruction == 'jmp':
            pc = pc + val
            continue
        elif instruction == 'acc':
            acc += val
        elif instruction == 'nop':
            pass
        pc += 1
    return ('terminated', acc)

def part1():
    _, acc = vm(input)
    aoc(acc)

def part2():
    for i in range(len(input)):
        program = input.copy()
        line = program[i]
        instruction, val = line.split(' ')
        if instruction == 'jmp':
            program[i] = 'nop ' + val
        elif instruction == 'nop':
            program[i] = 'jmp ' + val
        else:
            continue
        res, acc = vm(program)
        if res == 'terminated':
            aoc(acc)
            return

part1()
part2()
