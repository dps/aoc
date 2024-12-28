from utils import *

D = [line.strip() for line in open("input")]

locks = []
keys = []

for item in bundles(D):
    if item[0] == '#####':
        lock = [0,0,0,0,0]
        for i,row in enumerate(item[1:]):
            for j,c in enumerate(row):
                if c == '#':
                    lock[j] = i+1
        locks.append(lock)
    else:
        key = [0,0,0,0,0]
        for i,row in enumerate(item):
            for j,c in enumerate(row):
                if c == '#':
                    key[j] = max(key[j], 7-(i+1))
        keys.append(key)

def fits(lock, key):
    return all((lock[i] + key[i]) <= 5 for i in range(5))

print(sum(fits(lock, key) for lock in locks for key in keys))
