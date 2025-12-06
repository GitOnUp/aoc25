from pathlib import Path


INPUT_DIR = Path(__file__).parent.parent / "input"


def input_path(caller_file: str, example: bool = False) -> Path:
    caller_path = Path(caller_file)
    suffix = ".example" if example else ".txt"
    return INPUT_DIR / caller_path.name.replace(".py", suffix)
