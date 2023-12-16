
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

def hashfn(str):
    r = 0
    for ch in str:
        r = ((r + ord(ch)) * 17) % 256
    return r

print("Part 1", sum(hashfn(v) for v in D[0].split(",")))

boxes = defaultdict(lambda:{})
for instr in D[0].split(","):
    box, label = hashfn(words(instr)[0]), words(instr)[0]
    op = ("remove", None) if instr[-1] == "-" else ("set", int(instr.split("=")[1]))

    if op[0] == "set":
        boxes[box][label] = op[1]
    elif op[0] == "remove":
        try:
            del(boxes[box][label])
        except:
            pass

tot = 0
for box, ll in boxes.items():
    for slot,label in enumerate(ll, 1):
        tot += (box+1) * slot * boxes[box][label]
print("Part 2", tot)