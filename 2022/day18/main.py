from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

FACES = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

droplet = set()
min_x,min_y,min_z,max_x,max_y,max_z = 0,0,0,0,0,0

def points_facing_sides(voxel):
    # a voxel has 6 sides each facing a voxel with the returned coords
    return [(voxel[0] + f[0], voxel[1] + f[1], voxel[2] + f[2]) for f in FACES]

def in_bound(x, min_x, max_x):
    return x >= -1 and x <= max_x + 1

def not_enclosed():
    outside_droplet = set()
    queue = deque([(0,0,0)])
    while len(queue) > 0:
        vox = queue.popleft()
        for q in points_facing_sides(vox):
            if q in outside_droplet:
                continue
            elif q in droplet:
                continue
            elif in_bound(q[0], min_x, max_x) and in_bound(q[1], min_y, max_y) and in_bound(q[2], min_z, max_z):
                outside_droplet.add(q)
                queue.append(q)
    return outside_droplet

def part1():
    # Surface area of connected voxels
    droplet = set()
    for line in input:
        droplet.add(tuple(ints(line)))
    faces = []
    for voxel in droplet:
        adj = points_facing_sides(voxel)
        for p in adj:
            if p not in droplet:
                faces.append(adj)
    print(len(faces))
    return len(faces)

def part2():
    global min_x,min_y,min_z, max_x,max_y,max_z
    # Find the enclosed bubbles and ignore them!
    for line in input:
        droplet.add(tuple(ints(line)))
    
    # find droplet bounds.
    min_x,min_y,min_z = min([p[0] for p in droplet]), min([p[1] for p in droplet]), min([p[2] for p in droplet])
    max_x,max_y,max_z = max([p[0] for p in droplet]), max([p[1] for p in droplet]), max([p[2] for p in droplet])

    # Better algorithm h/t robertying
    outside_droplet = not_enclosed()

    faces = []
    for voxel in droplet:
        adj = points_facing_sides(voxel)
        for p in adj:
            if p in outside_droplet:
                faces.append(adj)
    print(len(faces))
    return len(faces)

if __name__ == '__main__':
    assert(part1() == 4580)
    assert(part2() == 2610)