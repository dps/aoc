from utils import *

D = [line.strip() for line in open("input")]

@cache
def max_joltage(line, remaining):
    if remaining == 0:
        return ""

    if len(line) == remaining:
        return line
    max_j = 0
    max_str = ""
    for i, ch in enumerate(line):
        remain = line[i+1:]
        if len(remain) < remaining-1:
            break
        v = ch + max_joltage(remain, remaining - 1)
        if int(v) > max_j:
            max_j = int(v)
            max_str = v
    return max_str

print(sum(map(lambda x: int(max_joltage(x, 2)), D)))
print(sum(map(lambda x: int(max_joltage(x, 12)), D)))