from pathlib import Path

import aoc25.util as util


def solve(input_file: Path):
    current = 50
    total_zero = 0
    with open(input_file) as f:
        for line in f:
            if not line:
                break
            direction = line[0]
            count = int(line[1:])
            if direction == "R":
                current += count
            else:
                current -= count

            if (current % 100) == 0:
                total_zero += 1
    return total_zero


def solve2(input_file: Path):
    current = 50
    total_zero = 0
    with open(input_file) as f:
        for line in f:
            if not line:
                break
            direction = line[0]
            count = int(line[1:])
            full_turns = abs(count // 100)
            total_zero += full_turns
            count -= full_turns * 100
            previous = current
            if direction == "R":
                current += count
            else:
                current -= count
            if current < 0:
                current += 100
                if previous != 0:
                    total_zero += 1
            elif current >= 100:
                current -= 100
                if previous != 0:
                    total_zero += 1
            elif current == 0:
                total_zero += 1
    return total_zero


if __name__ =="__main__":
    print(solve(util.input_path("p01.txt")))
    print(solve2(util.input_path("p01.txt")))
