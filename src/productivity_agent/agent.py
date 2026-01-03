from .models import Task


def next_task_id(tasks: list[Task]) -> int:
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1


def add_task(tasks: list[Task], title: str) -> Task:
    task = Task(task_id=next_task_id(tasks), title=title.strip())
    tasks.append(task)
    return task


def format_tasks(tasks: list[Task]) -> str:
    if not tasks:
        return "No tasks yet."

    lines: list[str] = []
    for t in tasks:
        status_symbol = "✅" if t.status == "done" else "🕒"
        lines.append(f"{status_symbol} [{t.id}] {t.title} ({t.status})")
    return "\n".join(lines)


def mark_task_done(tasks: list[Task], task_id: int) -> Task | None:
    for task in tasks:
        if task.id == task_id:
            task.status = "done"
            return task
    return None
