from pathlib import Path

ROOT_FOLDER = Path(__file__).parent.parent

OUTPUT_FOLDER = ROOT_FOLDER / "output"

COURSE_FOLDER = ROOT_FOLDER / "docs" / "course_files"

OUTPUT_FOLDER.mkdir(exist_ok=True)
