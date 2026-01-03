from dataclasses import dataclass

from .agent import add_task, format_tasks, mark_task_done
from .storage import save_tasks
from .models import Task


@dataclass
class RouteResult:
    message: str
    should_exit: bool = False
    pending_add: bool = False
    should_save: bool = False


def route(user_input: str, tasks: list[Task], pending_add: bool) -> RouteResult:
    text = user_input.strip()
    if not text:
        return RouteResult(message="")

    # 1) Eğer agent az önce soru sorduyse: gelen input = task title
    if pending_add:
        task = add_task(tasks, text)
        save_tasks(tasks)
        return RouteResult(
            message=f"Added: [{task.id}] {task.title}",
            pending_add=False,
            should_save=True,
        )

    # 2) Normal komut çözümleme
    command = text.split(maxsplit=1)[0].lower()

    if command == "exit":
        return RouteResult(message="Goodbye 👋", should_exit=True)

    if command == "list":
        return RouteResult(message=format_tasks(tasks))

    if command == "add":
        parts = text.split(maxsplit=1)
        if len(parts) == 1:
            return RouteResult(message="What is the task title?", pending_add=True)

        title = parts[1]
        task = add_task(tasks, title)
        save_tasks(tasks)
        return RouteResult(
            message=f"Added: [{task.id}] {task.title}",
            should_save=True,
        )

    if command == "done":
        parts = text.split()
        if len(parts) != 2:
            return RouteResult(message="Usage: done <task_id>")

        try:
            task_id = int(parts[1])
        except ValueError:
            return RouteResult(message="Task id must be a number.")

        task = mark_task_done(tasks, task_id)
        if task is None:
            return RouteResult(message=f"No task found with id {task_id}")

        save_tasks(tasks)
        return RouteResult(
            message=f"Task [{task.id}] marked as done.",
            should_save=True,
        )

    return RouteResult(message="Unknown command. Try: add, list, done <id>, exit")
