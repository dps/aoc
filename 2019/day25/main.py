from utils import *
from string import *

prompt = [i.strip() for i in open("input","r").readlines()]

inputs = [[]]

def computer(mem, _pc, _relbase, inputnum):
    global inputs

    def decode(cop):
        s = str(cop).zfill(5)
        return s[0],s[1],s[2],int(s[3:])

    pc = _pc
    op = None
    relbase = _relbase

    while True:
        l = 0
        md,my,mx,op = decode(mem[pc])

        def param(mode, p,):
            nonlocal relbase, mem
            if mode == '1':
                return p
            if mode == '0':
                return mem[p]
            if mode == '2':
                return mem[relbase + p]

        def dest(md, d):
            nonlocal relbase
            return d if md == '0' else relbase + d

        if op == 1:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[dest(md,d)] = param(mx, x) + param(my, y)
            l = 4
        elif op == 2:
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            mem[dest(md,d)] = param(mx, x) * param(my, y)
            l = 4
        elif op == 3: # input
            x = mem[pc+1]
            ii = -1
            if len(inputs[inputnum]) > 0:
                ii = inputs[inputnum][0]
                inputs[inputnum] = inputs[inputnum][1:]
                #print(inputnum,"<-",ii)
            if ii == -1:
                yield "preempt"
            mem[dest(mx,x)] = ii
            l = 2
        elif op == 4: # output
            x = mem[pc+1]
            yield param(mx, x)
            l = 2
        elif op == 5: # jump-if-true
            x, y = mem[pc+1], mem[pc+2]
            if param(mx, x) != 0:
                pc = param(my, y)
            else:
                l = 3
        elif op == 6: # jump-if-false
            x, y = mem[pc+1], mem[pc+2]
            if param(mx, x) == 0:
                pc = param(my, y)
            else:
                l = 3
        elif op == 7: # <
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if param(mx, x) < param(my, y):
                mem[dest(md,d)] = 1
            else:
                mem[dest(md,d)] = 0
            l = 4
        elif op == 8: # ==
            x, y, d = mem[pc+1], mem[pc+2], mem[pc+3]
            if param(mx, x) == param(my, y):
                mem[dest(md,d)] = 1
            else:
                mem[dest(md,d)] = 0
            l = 4
        elif op == 9: # relbase
            x = mem[pc+1]
            relbase += param(mx, x)
            l = 2
        elif op == 99:
            break
        pc += l
    yield None

def part1():
    global inputs
    program = [int(x) for x in prompt[0].split(",")]    
    allmem = defaultdict(int)
    for i, v in enumerate(program):
        allmem[i] = v

    c = computer(deepcopy(allmem),0,0,0)


    moves = ['west', 'take space law space brochure', 'north', 'take loom', 'south', 'south', 'take hologram', 'west', 'take manifold', 'north', 'south', 'east', 'east', 'north', 'east', 'north', 'take mutex', 'south', 'south', 'take cake', 'west', 'south', 'take easter egg', 'south', 'inv', '$']
    items = ['space law space brochure', 'loom', 'hologram', 'manifold', 'mutex', 'cake', 'easter egg']

    # Uncomment to play the game interactively.
    # inpbuffer = []
    # buffer = []
    # try:
    #     while True:
    #         ch = next(c)
    #         buffer.append(chr(ch))
    #         print(chr(ch), end="")
    #         if "".join(buffer[-(len("Command?")):]) == "Command?":
    #             cmd = input()
    #             inputs[0].extend([ord(c) for c in list(cmd)] + [10])
    #             inpbuffer.append(cmd)
    # except EOFError:
    #     print(inpbuffer)
    # exit(0)

    def execute():
        nonlocal moves
        buffer = ""
        while len(moves) > 0:
            ch = next(c)
            if ch == None:
                return buffer
            buffer += chr(ch)
            #print(chr(ch), end="")
            if "".join(buffer[-(len("Command?")):]) == "Command?":
                cmd = moves[0]
                #print(cmd)
                moves = moves[1:]
                inputs[0].extend([ord(c) for c in list(cmd)] + [10])
        return buffer

    execute()
    # We are now at the checkpoint holding all the items


    # This was really mean - it turns out some of the items are lighter than "air"
    # i.e. have negative weight.

    # for cc in combinations(deepcopy(items), 1):
    #     moves = []
    #     for im in items:
    #         moves.append("drop " + im)
    #     for im in cc:
    #         moves.append("take " + im)
    #     moves.append("south")
    #     moves.append("$")
    #     result = execute()
    #     if "lighter" in result:
    #         items.remove(cc[0])
    #         print(cc[0], "is too heavy alone")

    # print("****", items)

    maxl = len(items)

    for num in range(1,maxl):
        for cc in combinations(items, num):
            moves = []
            for im in items:
                moves.append("drop " + im)
            for im in cc:
                moves.append("take " + im)
            moves.append("south")
            moves.append("$")
            result = execute()
            if "Alert" not in result:
                aoc(result)
                return

    # A loud, robotic voice says "Analysis complete! You may proceed." and you enter the cockpit.
    # Santa notices your small droid, looks puzzled for a moment, realizes what has happened, and radios your ship directly.
    # "Oh, hello! You should be able to get in by typing XXXXXX on the keypad at the main airlock."


part1()

