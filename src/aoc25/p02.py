from pathlib import Path

import aoc25.util as util


def is_invalid(int_id: int) -> bool:
    str_id = str(int_id)
    l = len(str_id)
    if l % 2 != 0:
        return False
    return str_id[:l//2] == str_id[l//2:]


def is_invalid_2(int_id: int) -> bool:
    str_id = str(int_id)
    for repeat_l in range(1, len(str_id) // 2 + 1):
        if len(str_id) % repeat_l != 0:
            continue
        repetitions = len(str_id) // repeat_l
        repeated = str_id[0:repeat_l]
        if str_id == repeated * repetitions:
            return True
    return False


def solve(input_file: Path):
    with open(input_file) as f:
        lines = f.read().split(",")

    result = 0
    result_2 = 0
    for line in lines:
        low_str, high_str = line.split("-")
        low, high = int(low_str), int(high_str)
        for i in range(low, high+1):
            if is_invalid(i):
                result += i
            if is_invalid_2(i):
                result_2 += i
    return result, result_2


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False)))
