import heapq
from dataclasses import dataclass, field
from math import sqrt
from pathlib import Path

from aoc25 import util


@dataclass
class JBox:
    x: int
    y: int
    z: int
    links: set["JBox"] = field(default_factory=set)
    circuit: int = -1

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other: "JBox") -> bool:
        if not isinstance(other, JBox):
            return False
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def distance(self, other: "JBox") -> float:
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)

    def link(self, other: "JBox") -> None:
        self.links.add(other)
        other.links.add(self)


def solve(input_file: Path, wire_count: int):
    return solve1(input_file, wire_count), solve2(input_file)


def solve1(input_file: Path, wire_count: int) -> int:
    boxes, distances = load_boxes_distances(input_file)
    link_boxes(distances, wire_count)
    return find_circuits(boxes)[0]


def solve2(input_file: Path) -> int:
    boxes, distances = load_boxes_distances(input_file)
    while True:
        _, box1, box2 = heapq.heappop(distances)
        box1.link(box2)
        _, num_circuits, orphans = find_circuits(boxes)
        if num_circuits == 1 and not orphans:
            return box1.x * box2.x

def load_boxes_distances(input_file: Path):
    boxes = []
    distances = []
    with open(input_file, "r") as f:
        for line in f:
            x, y, z = [int(c) for c in line.strip().split(",")]
            box = JBox(x, y, z)
            for other_box in boxes:
                heapq.heappush(distances, (box.distance(other_box), other_box, box))
            boxes.append(box)
    return boxes, distances


def link_boxes(distance_heap: list[tuple[float, JBox, JBox]], count: int) -> None:
    for i in range(count):
        _, box1, box2 = heapq.heappop(distance_heap)
        box1.link(box2)


def find_circuits(boxes: list[JBox]) -> tuple[int, int, bool]:
    cur_circuit = 0
    circuit_sizes = [0, 0, 0]
    orphans = False
    for box in boxes:
        if not box.links or box.circuit > -1:
            if not box.links:
                orphans = True
            continue
        size = assign_circuit(box, cur_circuit)
        cur_circuit += 1
        heapq.heappush(circuit_sizes, size)
        if len(circuit_sizes) > 3:
            heapq.heappop(circuit_sizes)

    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2], cur_circuit, orphans


def assign_circuit(box: JBox, circuit: int) -> int:
    traversal = [box]
    seen = set()
    while traversal:
        box = traversal.pop()
        if box.circuit == circuit or box in seen:
            continue
        seen.add(box)
        box.circuit = circuit
        traversal.extend(box.links)
    return len(seen)


if __name__ == "__main__":
    print(solve(util.input_path(__file__, example=False), 1000))
