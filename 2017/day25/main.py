
from utils import *

D = [i.strip() for i in open("input","r").readlines()]

states = {}
state = D[0].split(" ")[-1][0]
cursor = 0
steps = ints(D[1])[0]

for rule in bundles(D[3:]):
    name = rule[0].split(" ")[-1][0]
    bits = {}
    for i, s in enumerate([2,6]):
        write = int(rule[s].split(" ")[-1][0])
        move = 1 if rule[s+1].split(" ")[-1][0] == 'r' else -1
        nxt = rule[s+2].split(" ")[-1][0]
        bits[i] = (write, move, nxt)
    states[name] = bits

tape = defaultdict(int)

for _ in range(steps):
    write, move, next_state = states[state][tape[cursor]]
    tape[cursor] = write
    cursor += move
    state = next_state

print(sum(tape.values()))