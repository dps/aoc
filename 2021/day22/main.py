from utils import *
from dataclasses import dataclass

input = [i.strip() for i in open("simple.txt","r").readlines()]


def part1():
    procedure = []
    for line in input:
        action = line.split(" ")[0]
        ranges = ints(line)
        if ranges[0] < -500:
            break
        procedure.append((action, ranges))

    switches = set()
    for action, ranges in procedure:
        for x in range(ranges[0], ranges[1]+1):
            for y in range(ranges[2], ranges[3]+1):
                for z in range(ranges[4], ranges[5]+1):
                    if action == "on":
                        switches.add((x,y,z))
                    if action == "off" and (x,y,z) in switches:
                        switches.remove((x,y,z))

    tot = 0
    for x in range(-50,51):
        for y in range(-50,51):
            for z in range(-50,51):
                if (x,y,z) in switches:
                    tot += 1
    print(tot)

def box_intersection(a,b):
    # a and b are [min_x, max_x, min_y, max_y, min_z,max_z]
    min_x = max(a[0], b[0])
    max_x = min(a[1], b[1])
    min_y = max(a[2], b[2])
    max_y = min(a[3], b[3])
    min_z = max(a[4], b[4])
    max_z = min(a[5], b[5])
    if min_x <= max_x and min_y <= max_y and min_z <= max_z:
        return [min_x, max_x, min_y, max_y, min_z, max_z]
    else:
        return None

def volume(range):
    return abs(range[5]+1-range[4])*abs(range[3]+1-range[2])*abs(range[1]+1-range[0])

def cut_up_boxes(box1, box2, box_intersect):
    # box1 and box2 are [min_x, max_x, min_y, max_y, min_z,max_z]
    # representing the range of values the box spans in each dimension
    # box intersection is the intersect also of the form [min_x, max_x, min_y, max_y, min_z,max_z]
    # returns (box_intersect, box1_cuts, box2_cuts)

    # now we'll cut up the first box
    box1_cuts = []
    if box_intersect[0] > box1[0]:
        # there's a non-intersecting region on the left side of the first box in the x dimension
        box1_cuts.append([box1[0], box_intersect[0]-1, box1[2], box1[3], box1[4], box1[5]])
    if box_intersect[1] < box1[1]:
        # there's a non-intersecting region on the right side of the first box in the x dimension
        box1_cuts.append([box_intersect[1]+1, box1[1], box1[2], box1[3], box1[4], box1[5]])
    if box_intersect[2] > box1[2]:
        # there's a non-intersecting region on the bottom side of the first box in the y dimension
        box1_cuts.append([box1[0], box1[1], box1[2], box_intersect[2]-1, box1[4], box1[5]])
    if box_intersect[3] < box1[3]:
        # there's a non-intersecting region on the top side of the first box in the y dimension
        box1_cuts.append([box1[0], box1[1], box_intersect[3]+1, box1[3], box1[4], box1[5]])
    if box_intersect[4] > box1[4]:
        # there's a non-intersecting region on the back side of the first box in the z dimension
        box1_cuts.append([box1[0], box1[1], box1[2], box1[3], box1[4], box_intersect[4]-1])
    if box_intersect[5] < box1[5]:
        # there's a non-intersecting region on the front side of the first box in the z dimension
        box1_cuts.append([box1[0], box1[1], box1[2], box1[3], box_intersect[5]+1, box1[5]])
    
    # now we'll cut up the second box
    box2_cuts = []
    if box_intersect[0] > box2[0]:
        # there's a non-intersecting region on the left side of the second box in the x dimension
        box2_cuts.append([box2[0], box_intersect[0], box2[2], box2[3], box2[4], box2[5]])
    if box_intersect[1] < box2[1]:
        # there's a non-intersecting region on the right side of the second box in the x dimension
        box2_cuts.append([box_intersect[1], box2[1], box2[2], box2[3], box2[4], box2[5]])
    if box_intersect[2] > box2[2]:
        # there's a non-intersecting region on the bottom side of the second box in the y dimension
        box2_cuts.append([box2[0], box2[1], box2[2], box_intersect[2], box2[4], box2[5]])
    if box_intersect[3] < box2[3]:
        # there's a non-intersecting region on the top side of the second box in the y dimension
        box2_cuts.append([box2[0], box2[1], box_intersect[3], box2[3], box2[4], box2[5]])
    if box_intersect[4] > box2[4]:
        # there's a non-intersecting region on the back side of the second box in the z dimension
        box2_cuts.append([box2[0], box2[1], box2[2], box2[3], box2[4], box_intersect[4]])
    if box_intersect[5] < box2[5]:
        # there's a non-intersecting region on the front side of the second box in the z dimension
        box2_cuts.append([box2[0], box2[1], box2[2], box2[3], box_intersect[5], box2[5]])

    return (box_intersect, box1_cuts, box2_cuts)

i = box_intersection([0,10,0,10,0,10], [5,6,5,6,5,6])
i,a,b = cut_up_boxes([0,10,0,10,0,10], [5,6,5,6,5,6], i)
print(a[0])
print(a[1])
print(a[2])
print(volume(i), volume(a[0])+volume(a[1])+volume(a[2]), volume([0,10,0,10,0,10]))
def part2():
    sequence = []
    procedure = []
    for i, line in enumerate(input):
        action = line.split(" ")[0]
        range = ints(line)
        procedure.append((action, range, i))
        if action == "on":
            for s in sequence:
                isect = box_intersection(range, s[0])
                if isect:
                    s[1].append(isect) # append our intersection to s's offs so we don't double count
            sequence.append([range, []])
        elif action == "off":
            for s in sequence:
                isect = box_intersection(range, s[0])
                if isect:
                    s[1].append(isect)
    print(sequence)
    total = 0
    for s in sequence:
        stot = volume(s[0])
        for i, off in enumerate(s[1]):
            off_cuts = [off]
            if i > 0:
                for prev in s[1][:i]:
                    to_remove = []
                    to_add = []
                    for part in off_cuts:
                        isect = box_intersection(prev, part)
                        if isect:
                            _, more_off_cuts, _ = cut_up_boxes(part, prev, isect)
                            to_remove.append(part)
                            to_add.extend(more_off_cuts)
                    for r in to_remove:
                        off_cuts.remove(r)
                    for a in to_add:
                        off_cuts.append(a)
                stot -= sum([volume(o) for o in off_cuts])
            else:
                stot -= volume(off)
        total += stot
    print(total)




    



# @dataclass
# class Box:
#     num: int
#     ranges: list
#     state: bool
#     intersects: list

# def part2():
#     mins = (0,0,0)
#     maxes = (0,0,0)
#     boxes = {}
#     procedure = []
#     for i, line in enumerate(input):
#         action = line.split(" ")[0]
#         ranges = ints(line)
#         # if ranges[0] < -50:
#         #     break
#         mins = (min(mins[0], ranges[0]), min(mins[1], ranges[2]), min(mins[2], ranges[4]))
#         maxes = (max(maxes[0], ranges[1]), max(maxes[1], ranges[3]), max(maxes[2], ranges[5]))
#         volume = abs(ranges[5]-ranges[4])*abs(ranges[3]-ranges[2])*abs(ranges[1]-ranges[0])
#         procedure.append((volume, action, ranges, i))
#     print("***", len(procedure))
#     all_b = sorted(procedure, reverse=True)
#     print(all_b)
#     for box in all_b:
#         this_box = Box(num=box[3], ranges=box[2], state=False, intersects=[])
#         for ob in boxes.values():
#             isect = box_intersection(this_box.ranges, ob.ranges)
#             if isect != None:
#                 ob.intersects.append((this_box, isect))
#                 this_box.intersects.append((ob, isect))
#         boxes[box[3]] = this_box
#     for box in boxes.values():
#         print(len(box.intersects))





#part1() #590784
part2()