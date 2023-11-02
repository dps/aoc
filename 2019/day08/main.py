from utils import *

input = [i.strip() for i in open("input.txt","r").readlines()]

def layers(image):
    while len(image) > 0:
        yield image[:25*6]
        image = image[25*6:]

def part1():
    image = input[0]
    mc = 9999
    cs = None
    for layer in layers(image):
        c = Counter(layer)
        if c["0"] < mc:
            cs = c
            mc = c["0"]
    aoc(cs["1"] * cs["2"])

def merge(zip_pixels):
    for zpix in zip_pixels:
        p = None
        for px in zpix:
            if px == "2":
                continue
            else:
                p = px
                break
        yield p

def part2():
    image = input[0]
    lays = [list(im) for im in list(layers(image))]
    group_by_pixel = zip(*lays)
    final_image = list(merge(group_by_pixel))

    for y in range(6):
        for x in range(25):
            print("🟧" if final_image[y*25+x] == "1" else "⬛️",end="")
        print()

part1()
part2()
