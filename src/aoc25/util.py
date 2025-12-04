from pathlib import Path


def input_file(name: str) -> Path:
    return Path(__file__).parent.parent / "input" / name
