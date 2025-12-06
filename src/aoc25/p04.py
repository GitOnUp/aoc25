from pathlib import Path

import aoc25.util as util


def removals(grid: list[list[str]]) -> list[(int, int)]:
    height = len(grid)
    width = len(grid[0])

    def neighboring_paper(x: int, y: int) -> int:
        if x < 0 or y < 0 or x >= width or y >= height:
            return 0
        if grid[y][x] == "@":
            return 1
        return 0

    accessible = []
    for y in range(height):
        for x in range(width):
            if grid[y][x] != "@":
                continue
            neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    neighbors += neighboring_paper(x + dx, y + dy)
            if neighbors < 4:
                accessible.append((x, y))
    return accessible


def solve(input_file: Path):
    with open(input_file, "r") as f:
        grid = [[c for c in line.strip()] for line in f.readlines()]

    removed = removals(grid)
    first_iteration = len(removed)
    all_removals = 0

    while removed:
        all_removals += len(removed)
        for x, y in removed:
            grid[y][x] = 'x'
        removed = removals(grid)

    return first_iteration, all_removals


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False)))
