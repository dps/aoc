
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def solve():
    cap = {"red": 12, "green": 13, "blue": 14}
    p1,p2 = 0, 0
    for game, line in enumerate(input, 1):
            if all([not any(x>mm for x in map(int, re.findall(f"(\d+) {color}", line))) for color,mm in cap.items()]):
                p1 += game
            p2 += reduce(operator.mul, [max(map(int, re.findall(f"(\d+) {color}", line))) for color in cap.keys()])
    print(p1, p2)

solve()
