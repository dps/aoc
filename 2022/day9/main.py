input = [i.strip() for i in open("input.txt","r").readlines()]


DIR = {'R': (1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1) }

def touching(a,b):
    return (a == b) or (a[0]==b[0] and abs(a[1]-b[1])==1) or (a[1]==b[1] and abs(a[0]-b[0])==1) or (abs(a[0]-b[0]) ==1 and abs(a[1]-b[1])==1)

def part1():
    head =(0,0)
    tail =(0,0)
    visited = set()
    for move in input:
        dir = move.split(' ')[0]
        steps = int(move.split(' ')[1])
        dx,dy = DIR[dir]
        for s in range(steps):
            head = (head[0] + dx, head[1] + dy)
            if not touching(head, tail):
                if tail[0] == head[0]:
                    tail = (tail[0], tail[1] + int((head[1]-tail[1])/abs(head[1]-tail[1])))
                elif tail[1] == head[1]:
                    tail = (tail[0] + int((head[0]-tail[0])/abs(head[0]-tail[0])), tail[1])
                else:
                    ddx = int((head[0]-tail[0])/abs(head[0]-tail[0]))
                    ddy = int((head[1]-tail[1])/abs(head[1]-tail[1]))
                    assert(ddx == -1 or ddx == 1)
                    assert(ddy == -1 or ddy == 1)
                    tail = (tail[0] + ddx, tail[1] + ddy)
            assert(touching(head, tail))
            visited.add(tail)
    print(len(visited))

def part2():
    knots = [(0,0) for x in range(10)]
    visited = set()
    for move in input:
        dir = move.split(' ')[0]
        steps = int(move.split(' ')[1])
        dx,dy = DIR[dir]
        for s in range(steps):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for k in range(1, 10):
                head = knots[k-1]
                tail = knots[k]
                if not touching(head, tail):
                    if tail[0] == head[0]:
                        tail = (tail[0], tail[1] + int((head[1]-tail[1])/abs(head[1]-tail[1])))
                    elif tail[1] == head[1]:
                        tail = (tail[0] + int((head[0]-tail[0])/abs(head[0]-tail[0])), tail[1])
                    else:
                        ddx = int((head[0]-tail[0])/abs(head[0]-tail[0]))
                        ddy = int((head[1]-tail[1])/abs(head[1]-tail[1]))
                        assert(ddx == -1 or ddx == 1)
                        assert(ddy == -1 or ddy == 1)
                        tail = (tail[0] + ddx, tail[1] + ddy)
                assert(touching(head, tail))
                if (k == 9):
                    visited.add(tail)
                knots[k] = tail
    print(len(visited))

if __name__ == '__main__':
    assert(touching((-2,-1),(-2,0)))
    part1()
    part2()