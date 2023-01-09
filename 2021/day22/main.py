from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]


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

# I ended up cribbing this a bit from the solution megathread - I'd figured out this algorithm
# but had some off by one type bug and couldn't get it quite right...
def part2():
    region_counts = defaultdict(int)
    for line in input:
        action = line.split(" ")[0]
        range = tuple(ints(line))

        to_merge = defaultdict(int)
        for existing_range, current_dir in region_counts.items():
            isect = box_intersection(range, existing_range)
            if isect:
                to_merge[tuple(isect)] -= current_dir
        if action == "on":
            to_merge[range] += 1
        for range, count in to_merge.items():
            region_counts[range] += count

    print(sum(volume(range) * dir for range, dir in region_counts.items()))





    



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