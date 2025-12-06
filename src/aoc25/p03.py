from pathlib import Path

import aoc25.util as util


def largest_joltage_2(bank: str) -> int:
    largest_past = [0] * len(bank)
    largest = 0
    for i in range(len(largest_past) - 2, -1, -1):
        largest = max(largest, int(bank[i+1]))
        largest_past[i] = largest
    for i in range(0, len(bank) - 1):
        check = int(bank[i]) * 10 + largest_past[i]
        largest = max(largest, check)
    return largest


def largest_joltage_iter(bank: list[int], num: int, concat: str) -> str | None:
    if num == 0:
        return concat
    if len(bank) < num:
        return None
    for digit in range(9, 0, -1):
        for i, bank_digit in enumerate(bank):
            if bank_digit == digit:
                check = largest_joltage_iter(bank[i+1:], num-1, concat + str(digit))
                if check is not None:
                    return check
                else:
                    break
    return None


def solve(input_file: Path):
    with open(input_file) as f:
        total = 0
        total_12 = 0
        for bank in f:
            total += largest_joltage_2(bank.strip())
            total_12 += int(largest_joltage_iter([int(c) for c in bank.strip()], 12, ""))
    return total, total_12


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False)))
