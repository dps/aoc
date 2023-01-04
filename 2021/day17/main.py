from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()][0]
min_x, max_x, min_y, max_y = ints(input)

@cache
def simulate(vx,vy):
    x,y = 0,0
    sim_max_y = 0
    while True:
        x += vx
        y += vy
        vx -= sign(vx)
        vy -= 1
        sim_max_y = max(sim_max_y, y)
        if y < min_y:
            return False, sim_max_y, x<min_x, x>max_x, vy
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
            return True, sim_max_y

def part1():
    print(((min_y+1)*min_y)//2)
    # mh = 0
    # for vy in range(1,-min_y):
    #     for vx in range(1,max_x):
    #         h = simulate(vx,vy)
    #         if h[0] == True:
    #             mh = max(h[1], mh)
    #         else:
    #             _, _, too_short, too_long, _ = h
    #             if too_long:
    #                 break 
    # print(mh)

def part2():
    t = 0
    min_x_search = int((min_x * 2) ** 0.5 - 1)
    for vy in range(min_y,-min_y):
        for vx in range(min_x_search, max_x+1):
            h = simulate(vx,vy)
            if h[0] == True:
                t+=1
    print(t)

part1()
part2()