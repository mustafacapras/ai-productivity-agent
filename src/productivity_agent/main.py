from .agent import add_task, format_tasks, mark_task_done
from .storage import load_tasks, save_tasks



def main() -> None:
    tasks = load_tasks()
    pending_add: bool = False

    print("🧠 Personal Productivity Agent")
    print("Commands: add <text>, list, exit")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        if pending_add:
            title = user_input
            task = add_task(tasks, title)
            save_tasks(tasks)
            print(f"Added: [{task.id}] {task.title}")
            pending_add = False
            continue


        command = user_input.split(maxsplit=1)[0].lower()

        if command == "exit":
            print("Goodbye 👋")
            break

        if command == "list":
            print(format_tasks(tasks))
            continue

        if command == "add":
            parts = user_input.split(maxsplit=1)

            if len(parts) == 1:
                print("What is the task title?")
                pending_add = True
                continue

            title = parts[1]
            task = add_task(tasks, title)
            save_tasks(tasks)
            print(f"Added: [{task.id}] {task.title}")
            continue

        if command == "done":
            if len(user_input.split()) != 2:
                print("Usage: done <task_id>")
                continue

            try:
                task_id = int(user_input.split()[1])
            except ValueError:
                print("Task id must be a number.")
                continue

            task = mark_task_done(tasks, task_id)
            if task is None:
                print(f"No task found with id {task_id}")
                continue

            save_tasks(tasks)
            print(f"Task [{task.id}] marked as done.")
            continue


        print("Unknown command. Try: add <text>, list, exit")


if __name__ == "__main__":
    main()
