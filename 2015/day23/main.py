from utils import *


# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

D = [i.strip() for i in open("input","r").readlines()]

def solve(part=1):
    R = defaultdict(int)

    def run():
        pc = 0
        while True:
            toks = D[pc].split(" ")
            ins = toks[0]

            if ins == "hlf":
                R[toks[1]] = R[toks[1]] // 2
            elif ins == "tpl":
                R[toks[1]] = R[toks[1]] * 3
            elif ins == "inc":
                R[toks[1]] = R[toks[1]] + 1
            elif ins == "jmp":
                d = int(toks[1])
                pc += d
                continue
            elif ins == "jie":
                r = toks[1][0]
                if R[r] % 2 == 0:
                    pc += int(toks[2])
                    continue
            elif ins == "jio":
                r = toks[1][0]
                if R[r] == 1:
                    pc += int(toks[2])
                    continue
            
            pc += 1

    try:
        if part == 2:
            R["a"] = 1
        run()
    except:
        print(R["b"])

solve(1)
solve(2)