from functools import cache
from pathlib import Path

from aoc25 import util


def solve(input_file: Path) -> tuple[int, int]:
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    s = -1
    for i, c in enumerate(lines[0]):
        if c == "S":
            s = i

    return solve1(s, lines), solve2(s, lines)


def solve1(s: int, lines: list[str]) -> int:
    beams = {s}
    splits = 0
    for line in lines[1:]:
        new_beams = set()
        for beam in beams:
            if line[beam] == ".":
                new_beams.add(beam)
                continue
            splits += 1
            if beam > 0:
                new_beams.add(beam-1)
            if beam < len(line) - 1:
                new_beams.add(beam+1)
        beams = new_beams
    return splits


def solve2(beam: int, lines: list[str]) -> int:
    @cache
    def recurse(b: int, line_ix: int) -> int:
        if line_ix >= len(lines):
            return 1
        if lines[line_ix][b] == ".":
            return recurse(b, line_ix+1)
        return recurse(b+1, line_ix+1) + recurse(b-1, line_ix+1)

    return recurse(beam, 1)


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False)))
