from functools import cache
from collections import defaultdict

D = [line.strip() for line in open("input").readlines()]

start_row, start_col = 0, 0
for r in range(len(D)):
    for c in range(len(D[r])):
        if D[r][c] == 'S':
            start_row, start_col = r, c
            break

def part2():
    grid = D
        
    @cache
    def count_timelines(row, col):
        r = row
        while r < len(grid):
            if grid[r][col] == '^':
                left_count = count_timelines(r + 1, col - 1) if col > 0 else 0
                right_count = count_timelines(r + 1, col + 1) if col < len(grid[0]) - 1 else 0
                return left_count + right_count
            r += 1        
        return 1
    
    result = count_timelines(start_row + 1, start_col)
    print(result)

part2()