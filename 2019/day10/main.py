import cmath
from utils import *

input = [i.strip() for i in open("input","r").readlines()]

def angle_from_vertical(c):
    angle_from_horizontal = cmath.phase(c)
    angle_from_horizontal_degrees = math.degrees(angle_from_horizontal)
    angle_from_vertical_degrees = 90 - angle_from_horizontal_degrees
    if angle_from_vertical_degrees < 0:
        angle_from_vertical_degrees += 360
    return angle_from_vertical_degrees

def normalize(v):
    n = v / (math.sqrt(v.real*v.real + v.imag*v.imag))
    return round(n.real, 7) + 1j*(round(n.imag, 7))

def part1():
    asteroids = set()
    for y,row in enumerate(input):
        for x,ch in enumerate(row):
            if ch == "#":
                p = x + 1j*y
                asteroids.add(p)

    mm = 0
    best = None
    for a in asteroids:
        others = asteroids - {a}
        norm = set()
        for o in others:
            v = o-a
            norm.add(normalize(v))
        if len(norm) > mm:
            mm = len(norm)
            best = a
    aoc(mm)

def part2():
    mon = 23+20j
    # for test data: mon = 11+13j
    asteroids = defaultdict(list)
    angles = []
    for y,row in enumerate(input):
        for x,ch in enumerate(row):
            if ch == "#":
                p = x + 1j*y
                if p == mon:
                    continue
                v = (p - mon).real -1j * (p - mon).imag
                n = normalize(v)
                asteroids[n].append((cartesiani(mon,p), p))

    for x in asteroids.keys():
        asteroids[x] = sorted(asteroids[x])

    for i, x in enumerate(asteroids.keys()):
        angles.append((angle_from_vertical(x), i, x))

    angles = sorted(angles)
    shot = 0
    while shot < 200:
        for x in angles:
            asts = asteroids[x[2]]
            a = None
            if len(asts) > 0:
                a = asts[0]
                shot += 1
                asteroids[x] = asts[1:]
            if shot == 200:
                aoc(int(a[1].real*100 + a[1].imag))
                return
    
part1()
part2()
