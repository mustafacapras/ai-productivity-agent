import json
from pathlib import Path
from .models import Task

DATA_FILE = Path("data/tasks.json")


def load_tasks() -> list[Task]:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    return [Task.from_dict(item) for item in raw]


def save_tasks(tasks: list[Task]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)
