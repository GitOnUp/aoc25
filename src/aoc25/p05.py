from pathlib import Path

import aoc25.util as util


def solve(input_file: Path) -> tuple[int, int]:
    ranges = []

    fresh_count = 0
    with open(input_file, "r") as f:
        in_ranges = True
        for line in f:
            line = line.strip()
            if not line:
                in_ranges = False
                continue

            if in_ranges:
                low, high = (int(i) for i in line.split('-'))
                ranges = merge_range(ranges, (low, high))
                continue

            num = int(line)
            for test_range in ranges:
                if test_range[0] <= num <= test_range[1]:
                    fresh_count += 1
                    break
    print(ranges)
    return fresh_count, count_fresh(ranges)


def count_fresh(ranges: list[tuple[int, int]]) -> int:
    fresh = 0
    for r in ranges:
        fresh += r[1] - r[0] + 1
    return fresh


def merge_range(ranges: list[tuple[int, int]], new_range: tuple[int, int]) -> list[tuple[int, int]]:
    merged_ranges = []
    removed = []
    for i, range in enumerate(ranges):
        if (
                range[0] <= new_range[0] <= range[1]
                or range[0] <= new_range[1] <= range[1]
                or new_range[0] <= range[0] <= new_range[1]
                or new_range[0] <= range[1] <= new_range[1]
        ):
            removed.append(i)
    min_range, max_range = new_range
    for i, range in enumerate(ranges):
        if i not in removed:
            merged_ranges.append(range)
            continue
        min_range = min(min_range, range[0])
        max_range = max(max_range, range[1])
    merged_ranges.append((min_range, max_range))
    return merged_ranges


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False)))
