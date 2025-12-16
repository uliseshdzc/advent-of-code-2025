from common.utils import get_input


grid = [[c == '@' for c in row] for row in get_input(day=4).splitlines()]

def get_indices(i: int, j: int):
    return [
        (i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
        (i, j - 1), (i, j + 1),
        (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
    ]

def first_part():
    return sum(
        is_roll and sum(grid[a][b] for a, b in get_indices(i, j) if 0 <= a < len(grid) and 0 <= b < len(row)) < 4 
        for i, row in enumerate(grid)
        for j, is_roll in enumerate(row)
    )

def second_part():
    global grid
    count = 0
    while True:
        copy = [row[:] for row in grid]
        iterations = 0
        for i, row in enumerate(grid):
            for j, is_roll in enumerate(row):
                if is_roll and sum(grid[a][b] for a, b in get_indices(i, j) if 0 <= a < len(grid) and 0 <= b < len(row)) < 4:
                    iterations += 1
                    copy[i][j] = False

        if iterations == 0:
            return count
        
        count += iterations
        grid = copy

print(f"Part 1: {first_part()}")
print(f"Part 2: {second_part()}")