
from utils import *


D = [i.strip() for i in open("input","r").readlines()]
p1 = 0

R = [0,0,0]
regs, program = bundles(D)
print(regs, program)

for r in regs:
    r = r.replace("Register ", "")
    V, v = r.split(": ")
    R[int(ord(V[0])-ord('A'))] = int(v)
print(R)
program = program[0].split(": ")[1]
print(program)
instr = list(map(int, program.split(",")))
print(instr)


def combo(v):
    # Combo operands 0 through 3 represent literal values 0 through 3.
    # Combo operand 4 represents the value of register A.
    # Combo operand 5 represents the value of register B.
    # Combo operand 6 represents the value of register C.
    # Combo operand 7 is reserved and will not appear in valid programs.
    if v == 4:
        return R[0]
    elif v == 5:
        return R[1]
    elif v == 6:
        return R[2]
    else:
        return v

out = []
pc = 0
while pc < len(instr):
    op = instr[pc]
    if op == 0:
        # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
        num = R[0]
        denom = 2**combo(instr[pc+1])
        R[0] = num // denom
        pc += 2
    elif op == 1:
        # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
        B = R[1]
        lit = instr[pc+1]
        R[1] = B ^ lit
        pc += 2
    elif op == 2:
        # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
        R[1] = combo(instr[pc+1]) % 8
        pc += 2
    elif op == 3:
        # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        if R[0] != 0:
            pc = instr[pc+1]
        else:
            pc += 2
    elif op == 4:
        # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
        B = R[1]
        C = R[2]
        R[1] = B ^ C
        pc += 2
    elif op == 5:
        # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
        out.append(combo(instr[pc+1]) % 8)
        pc += 2
    elif op == 6:
        # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
        num = R[0]
        denom = 2**combo(instr[pc+1])
        R[1] = num // denom
        pc += 2
    elif op == 7:
        # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
        num = R[0]
        denom = 2**combo(instr[pc+1])
        R[2] = num // denom
        pc += 2
    else:
        print("Unknown opcode", op)
        break

print(",".join([str(i) for i in out]))

