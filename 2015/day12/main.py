
from utils import *
import json

D = [i.strip() for i in open("input","r").readlines()]

# Part 1
print(sum(ints(D[0])))

obj = json.loads(D[0])

def csum(obj):
    tot = 0
    if type(obj) is dict:
        for field_name in obj:
            field = obj[field_name]
            if type(field) is int:
                tot += field
            elif type(field) is str:
                if field == "red":
                    return 0
            else:
                tot += csum(field)
    elif type(obj) is list:
        for field in obj:
            if type(field) is int:
                tot += field
            else:
                tot += csum(field)
    return tot

print(csum(obj))

