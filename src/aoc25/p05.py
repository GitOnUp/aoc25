from pathlib import Path

import aoc25.util as util


def solve(input_file: Path) -> (int, int):
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
                ranges.append((low, high))
                continue

            num = int(line)
            for test_range in ranges:
                if test_range[0] <= num <= test_range[1]:
                    fresh_count += 1
                    break
    return fresh_count, count_fresh(ranges)


def count_fresh(ranges: list[tuple[int, int]]) -> int:
    ranges = list(sorted(ranges, key=lambda x: x[0]))
    print(ranges)
    compact_ranges = []
    i = 0
    while i < len(ranges):
        current_range = ranges[i]
        i_next = i + 1
        while i_next < len(ranges):
            if current_range[1] < ranges[i_next][0]:
                break
            current_range = (current_range[0], ranges[i_next][1])
            i_next += 1
        compact_ranges.append(current_range)
        i = i_next
    fresh = 0
    print(compact_ranges)
    for r in compact_ranges:
        fresh += r[1] - r[0] + 1
    return fresh


if __name__ == "__main__":
    print(solve(util.input_path("p05.example")))
