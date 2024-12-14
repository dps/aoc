# Concise solution for day 14, I like my original solution better, but this
# is the way most people on the subreddit did it.
from utils import *

D = [i.strip() for i in open("input","r").readlines()]
W, H = 101, 103

robots = []
for line in D:
    robots.append(ints(line))

def part1(robots):
    q = [sum(1 for r in robots if r[0]<W//2 and r[1]<H//2),
         sum(1 for r in robots if r[0]<W//2 and r[1]>H//2),
         sum(1 for r in robots if r[0]>W//2 and r[1]<H//2),
         sum(1 for r in robots if r[0]>W//2 and r[1]>H//2)]
    print("Part 1:", q[0]*q[1]*q[2]*q[3])

for j in range(10000):
    new_robots, spots = [], set()
    for robot in robots:
        new_robots.append(((robot[0]+robot[2])%W, (robot[1]+robot[3])%H, robot[2], robot[3]))
        spots.add(((robot[0]+robot[2])%W, (robot[1]+robot[3])%H))
    robots = new_robots

    if j == 99:
        part1(robots)

    if len(spots) == len(robots):
        print("Part 2:", j+1)
        break