from utils import *

D = [line.strip() for line in open("input")]

G = {}
for line in D:
    parts = line.split(': ')
    s = parts[0]
    ds = parts[1].split(' ')
    G[s] = ds

@cache
def dfs_count_paths_to_dest(src, dest):
    if src == dest:
        return 1
    if src not in G:
        return 0
    return sum(dfs_count_paths_to_dest(nxt, dest) for nxt in G[src])    

# find all paths from svr to out which pass through both fft and dac in either order.
tot = 0
tot += dfs_count_paths_to_dest('svr', 'fft') * dfs_count_paths_to_dest('fft', 'dac') * dfs_count_paths_to_dest('dac', 'out')
tot += dfs_count_paths_to_dest('svr', 'dac') * dfs_count_paths_to_dest('dac', 'fft') * dfs_count_paths_to_dest('fft', 'out')
print(tot)