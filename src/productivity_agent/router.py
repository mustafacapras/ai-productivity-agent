from dataclasses import dataclass

from .agent import add_task, format_tasks, mark_task_done, delete_task, suggest_daily_plan
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


    if pending_add:
        task = add_task(tasks, text)
        save_tasks(tasks)
        return RouteResult(
            message=f"Added: [{task.id}] {task.title}",
            pending_add=False,
            should_save=True,
        )


    command = text.split(maxsplit=1)[0].lower()

    if command == "exit":
        return RouteResult(message="Goodbye 👋", should_exit=True)

    if command == "list":
        return RouteResult(message=format_tasks(tasks))

    if command == "help":
        return RouteResult(
            message=(
                "Available commands:\n"
                "  add <text>      Add a new task\n"
                "  add             Agent asks for task title\n"
                "  list            Show all tasks\n"
                "  done <id>       Mark task as completed\n"
                "  delete <id>     Delete a task\n"
                "  help            Show this help message\n"
                "  exit            Exit the agent"
            )
        )

    if command == "plan":
        suggestions = suggest_daily_plan(tasks)

        if not suggestions:
            return RouteResult(message="No pending tasks. You're all caught up 🎉")

        lines = ["Today's suggested tasks:"]
        for task in suggestions:
            lines.append(f"🕒 [{task.id}] {task.title}")

        return RouteResult(message="\n".join(lines))



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

    if command == "delete":
        parts = text.split()
        if len(parts) != 2:
            return RouteResult(message="Usage: delete <task_id>")

        try:
            task_id = int(parts[1])
        except ValueError:
            return RouteResult(message="Task id must be a number.")

        task = delete_task(tasks, task_id)
        if task is None:
            return RouteResult(message=f"No task found with id {task_id}")

        save_tasks(tasks)
        return RouteResult(
            message=f"Task [{task.id}] deleted.",
            should_save=True,
        )


    return RouteResult(message="Unknown command. Try: add, list, done <id>, exit")
