from utils import *

D = [line.strip() for line in open("input")]

G = {}
for line in D:
    parts = line.split(': ')
    s = parts[0]
    ds = parts[1].split(' ')
    G[s] = ds

paths = set()

def dfs(s, path):
    if s == 'out':
        paths.add(tuple(path))
        return
    for d in G[s]:
        dfs(d, path + [d])

dfs('you', ['you'])
print(len(paths))
