# inp a - Read an input value and write it to variable a.
# add a b - Add the value of a to the value of b, then store the result in variable a.
# mul a b - Multiply the value of a by the value of b, then store the result in variable a.
# div a b - Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
# mod a b - Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
# eql a b - If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.


def alu(inp, program):
    registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    def lookup(tok):
        if tok in 'wxyz':
            return int(registers[tok])
        else:
            return int(tok)

    for line in program:
        tokens = line.strip().split(' ')
        instruction = tokens[0]
        match instruction:
            case "inp":
                registers[tokens[1]] = inp.pop(0)
                print(registers['z'])
                print()
                print("--- ", registers[tokens[1]])
            case "add":
                registers[tokens[1]] = registers[tokens[1]] + lookup(tokens[2])
            case "mul":
                registers[tokens[1]] = registers[tokens[1]] * lookup(tokens[2])
            case "div":
                registers[tokens[1]] = registers[tokens[1]] // lookup(tokens[2])
            case "mod":
                registers[tokens[1]] = registers[tokens[1]] % lookup(tokens[2])
            case "eql":
                if registers[tokens[1]] == lookup(tokens[2]):
                    registers[tokens[1]] = 1
                else:
                    registers[tokens[1]] = 0
    
    return registers['z']

def find_first_plausible_digit(program):
    for dig in range(1,10):
        print(dig)
        inp = [dig]
        registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
        def lookup(tok):
            if tok in 'wxyz':
                return int(registers[tok])
            else:
                return int(tok)

        for line in program:
            tokens = line.strip().split(' ')
            instruction = tokens[0]
            match instruction:
                case "inp":
                    if len(inp) > 0:
                        registers[tokens[1]] = inp.pop(0)
                    else:
                        print("out of input")
                        break
                case "add":
                    registers[tokens[1]] = registers[tokens[1]] + lookup(tokens[2])
                case "mul":
                    registers[tokens[1]] = registers[tokens[1]] * lookup(tokens[2])
                case "div":
                    registers[tokens[1]] = registers[tokens[1]] // lookup(tokens[2])
                case "mod":
                    registers[tokens[1]] = registers[tokens[1]] % lookup(tokens[2])
                case "eql":
                    if registers[tokens[1]] == lookup(tokens[2]):
                        registers[tokens[1]] = 1
                    else:
                        registers[tokens[1]] = 0
        
        print(registers)

def compare_digit_programs():
    inp = open('input.txt', 'r')
    lines = inp.readlines()
    progs =  [[] for _ in range(14)]
    prog = -1
    i = 0
    for line in lines:
        if line.strip().split(' ')[0] == 'inp':
            prog = prog + 1
        progs[prog].append(line.strip())

    for l in range(len(progs[0])):
      for i in range(14):
        print(progs[i][l], end=' ' * (16- len(progs[i][l])))
      print()





def first():
    inp = open('input.txt', 'r')
    lines = inp.readlines()

    #find_first_plausible_digit(lines)

    # It's far too slow to enumerate all!

    # for a in range(99999999999999, 11111111111111, -1):
    #     if '0' in str(a):
    #         continue
    #     z = alu(list(str(a)), lines)
    #     print(a,z)
    #     if (a % 99999 == 0):
    #         print(" .   ", a)

    # Checking paper work -->
    #z = alu(list(str(79197919993985)), lines)
    z = alu(list(str(13191913571211)), lines)
    print(z)
        

if __name__ == '__main__':
    first()
