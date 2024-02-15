
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

screen = defaultdict(bool)
mx,my = 50,6
for line in D:
    cmd = line.split(" ")[0]
    if cmd == "rotate":
        cmd = line.split(" ")[1]
    vals = ints(line)

    if cmd == "rect":
        for y in range(vals[1]):
            for x in range(vals[0]):
                screen[(x,y)] = True
    
    if cmd == "column":
        x = vals[0]
        d = vals[1]
        new_screen = deepcopy(screen)
        for y in range(my):
            new_screen[(x,y)] = screen[(x, (y+my-d)%my)]
        screen = new_screen

    if cmd == "row":
        y = vals[0]
        d = vals[1]
        new_screen = deepcopy(screen)
        for x in range(mx):
            new_screen[(x,y)] = screen[((x+mx-d)%mx, y)]
        screen = new_screen

print(len([s for s in screen.values() if s]))
for y in range(my):
    for x in range(mx):
        print("#" if screen[(x,y)] else ".", end="")
    print()
