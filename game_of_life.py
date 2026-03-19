import time
import os
import random


def create_grid(rows, cols, random_init=True):
    if random_init:
        return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return [[0] * cols for _ in range(rows)]


def count_neighbors(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = (row + dr) % rows, (col + dc) % cols
            count += grid[r][c]
    return count


def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0
    return new_grid


def display(grid):
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in grid:
        print(''.join('█' if cell else ' ' for cell in row))


def run(rows=30, cols=60, generations=200, delay=0.1):
    grid = create_grid(rows, cols)
    for gen in range(generations):
        display(grid)
        print(f"Generation: {gen + 1}")
        grid = next_generation(grid)
        time.sleep(delay)


if __name__ == "__main__":
    run()
