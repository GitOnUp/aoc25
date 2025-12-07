from pathlib import Path

from aoc25 import util


def solve(input_file: Path):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    s = -1
    for i, c in enumerate(lines[0]):
        if c == "S":
            s = i

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


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False)))
