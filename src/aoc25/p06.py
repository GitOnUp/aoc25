from pathlib import Path

import aoc25.util as util


def solve1(input_file: Path) -> int:
    problems = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            i = 0
            for item in line.split(" "):
                if not item:
                    continue
                if len(problems) == i:
                    problems.append([])
                if item not in ("*", "+"):
                    item = int(item)
                problems[i].append(item)
                i += 1

    total = 0
    for problem in problems:
        if problem[-1] == "*":
            subproduct = 1
            for v in problem[:-1]:
                subproduct *= v
            total += subproduct
            continue
        total += sum(problem[:-1])
    return total


def solve2(input_file: Path) -> int:
    lines = []
    with open(input_file) as f:
        for line in f:
            lines.append(line.removesuffix("\n"))

    last_line = lines[-1]
    current_lim = len(last_line)
    result = 0
    for i in range(len(last_line)-1, -1, -1):
        if last_line[i] in ("+", "*"):
            result += solve_problem(lines, (i, current_lim))
            current_lim = i-1
    return result


def solve_problem(lines: list[str], bounds: tuple[int, int]) -> int:
    op = lines[-1][bounds[0]]
    numbers = []

    for ix in range(bounds[0], bounds[1]):
        numbers.append(int("".join([lines[i][ix] for i in range(0, len(lines)-1)])))

    if op == "+":
        return sum(numbers)

    val = 1
    for n in numbers:
        val *= n
    return val


def solve(input_file: Path):
    return solve1(input_file), solve2(input_file)


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False)))
