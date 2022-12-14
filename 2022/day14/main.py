from utils import *
input = [i.strip() for i in open("input.txt","r").readlines()]

def draw_line(g, x, y, px, py):
    assert(g.set_cursor(px, py) != None)
    g.set("#")
    if x == px:
        for _ in range(abs(y - py)):
            g.move(0, sign(y - py))
            g.set("#")
    if y == py:
        for _ in range(abs(x - px)):
            g.move(sign(x - px), 0)
            g.set("#")

def drop_sand(g, max_y, part):
    sx, sy = 500, 0
    g.set_cursor(sx,sy)
    if (g.get() == "o"):
        return "full"
    while True:
        if part == 1 and sy > max_y -1:
            return "end"
        g.set_cursor(sx, sy)
        if g.peek_move(0, 1) == ".":
            sy += 1
        elif g.peek_move(-1, 1) == ".":
            sy += 1
            sx -= 1
        elif g.peek_move(1, 1) == ".":
            sy += 1
            sx += 1
        else:
            g.set("o")
            return "rest"

def solve(part=1):
    max_y, max_x = 0,0
    for line in input:
        for point in line.split(" -> "):
          x, y = int(point.split(",")[0]), int(point.split(",")[1])
          if y > max_y:
            max_y = y
          if x > max_x:
            max_x = x
    g = Grid(max(500, max_x*2) + 1, max_y + 3)
    for line in input:
        px, py = None, None
        for point in line.split(" -> "):
          x, y = int(point.split(",")[0]), int(point.split(",")[1])
          if px and py:
            draw_line(g, x,y,px,py)
          px, py = x, y
    g._grid[max_y+2] = g.empty_row("#")
    iter = 0
    while drop_sand(g, max_y, part) == "rest":
        iter += 1
    print(iter)       

if __name__ == '__main__':
    solve(1)
    solve(2)
