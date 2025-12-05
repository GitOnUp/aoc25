from pathlib import Path

import aoc25.util as util


def solve(input_file: Path) -> int:
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
    return fresh_count


if __name__ == "__main__":
    print(solve(util.input_path("p05.txt")))
