from utils import *

D = [line.strip() for line in open("input")]

things = list(bundles(D))
trees = things[-1]
shapes = things[0:-1]

def rot_90_cw(shape):
    return [''.join(row[i] for row in shape[::-1]) for i in range(len(shape[0]))]

def flip_horizontal(shape):
    return [row[::-1] for row in shape]

def flip_vertical(shape):
    return shape[::-1]

# Generate all unique orientations
presents = defaultdict(set)
for i, shape in enumerate(shapes):
    base = shape[1:]
    presents[i].add(tuple(base))
    presents[i].add(tuple(flip_horizontal(base)))
    presents[i].add(tuple(flip_vertical(base)))
    presents[i].add(tuple(rot_90_cw(base)))
    presents[i].add(tuple(flip_horizontal(rot_90_cw(base))))
    presents[i].add(tuple(flip_vertical(rot_90_cw(base))))
    presents[i].add(tuple(rot_90_cw(rot_90_cw(base))))
    presents[i].add(tuple(flip_horizontal(rot_90_cw(rot_90_cw(base)))))
    presents[i].add(tuple(flip_vertical(rot_90_cw(rot_90_cw(base)))))
    presents[i].add(tuple(rot_90_cw(rot_90_cw(rot_90_cw(base)))))
    presents[i].add(tuple(flip_horizontal(rot_90_cw(rot_90_cw(rot_90_cw(base))))))
    presents[i].add(tuple(flip_vertical(rot_90_cw(rot_90_cw(rot_90_cw(base))))))

presents = {i: list(orientations) for i, orientations in presents.items()}

# Pre-calculate sizes
present_sizes = {}
for i, orientations in presents.items():
    size = sum(1 for row in orientations[0] for ch in row if ch == '#')
    present_sizes[i] = size

def can_place_present(grid, present, x, y):
    """Try to place a present at position (x, y). Returns (success, positions)."""
    if y + len(present) > len(grid) or x + len(present[0]) > len(grid[0]):
        return False, None
    
    positions = []
    for i, row in enumerate(present):
        for j, ch in enumerate(row):
            if ch == '#':
                if grid[y+i][x+j] == '#':
                    return False, None
                positions.append((y+i, x+j))
    return True, positions

def place_present_positions(grid, positions):
    """Place a present on the grid."""
    for py, px in positions:
        grid[py][px] = '#'

def unplace_present(grid, positions):
    """Remove a present from the grid."""
    for py, px in positions:
        grid[py][px] = '.'

def get_valid_placements(grid, present):
    """Get all valid placements for a present orientation."""
    placements = []
    max_y = len(grid) - len(present) + 1
    max_x = len(grid[0]) - len(present[0]) + 1
    
    for y in range(max_y):
        for x in range(max_x):
            success, positions = can_place_present(grid, present, x, y)
            if success:
                placements.append(positions)
    return placements

def count_valid_placements(grid, present_idx):
    """Count how many ways we can place a present type."""
    count = 0
    for present in presents[present_idx]:
        count += len(get_valid_placements(grid, present))
    return count

def can_solve(grid, counts, depth=0):
    """Recursively try to place all presents on the grid."""
    # Base case
    if sum(counts) == 0:
        return True
    
    # Early termination: total space check
    empty_cells = sum(1 for row in grid for ch in row if ch == '.')
    needed_cells = sum(counts[i] * present_sizes[i] for i in range(len(counts)) if counts[i] > 0)
    if empty_cells < needed_cells:
        return False
        
    best_present = None
    min_placements = float('inf')
    
    for i, c in enumerate(counts):
        if c > 0:
            num_placements = count_valid_placements(grid, i)
            if num_placements == 0:
                return False  # Can't place this present at all!
            if num_placements < min_placements:
                min_placements = num_placements
                best_present = i
    
    p = best_present
    
    # Try all orientations and placements of the most constrained present
    for present in presents[p]:
        for positions in get_valid_placements(grid, present):
            place_present_positions(grid, positions)
            
            new_counts = counts.copy()
            new_counts[p] -= 1
            
            if can_solve(grid, new_counts, depth + 1):
                unplace_present(grid, positions)
                return True
            
            unplace_present(grid, positions)
    
    return False

# Solve each tree region
total_solvable = 0
for idx, grid in enumerate(trees):
    x, y = ints(grid)[0], ints(grid)[1]
    print(f"Region {idx+1}: {x}x{y}")
    counts = list(map(int, grid.split(': ')[1].split(' ')))
    
    total_area = x * y
    needed_area = sum(counts[i] * present_sizes[i] for i in range(len(counts)))
    
    if needed_area > total_area:
        print(f"✗ Not solvable (need {needed_area} cells, only have {total_area})")
        continue

    if sum(counts) * 3 * 3 <= total_area:
        print("✓ Solvable (simple 3x3 tiling)")
        total_solvable += 1
        continue
    
    empty_grid = [['.' for _ in range(x)] for _ in range(y)]
    
    if can_solve(empty_grid, counts):
        print("✓ Solvable")
        total_solvable += 1
    else:
        print("✗ Not solvable")

print(f"\nAnswer: {total_solvable}")