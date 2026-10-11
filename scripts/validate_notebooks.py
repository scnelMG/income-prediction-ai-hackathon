"""Validate notebook structure without running private-data analysis cells."""

import json
from pathlib import Path
import warnings

import nbformat


def main():
    paths = sorted((Path(__file__).resolve().parents[1] / "notebooks").glob("*.ipynb"))
    if not paths:
        raise RuntimeError("No notebooks found to validate.")
    for path in paths:
        notebook = nbformat.from_dict(json.loads(path.read_text(encoding="utf-8")))
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            nbformat.validate(notebook)
        print(f"PASS: {path.name}")


if __name__ == "__main__":
    main()
