from .storage import load_tasks
from .router import route


def main() -> None:
    tasks = load_tasks()
    pending_add = False

    print("🧠 Personal Productivity Agent")
    print("Commands: add <text>, delete <id>, list, done <id>, plan, help, exit")

    while True:
        user_input = input("> ")

        result = route(user_input, tasks, pending_add)
        pending_add = result.pending_add

        if result.message:
            print(result.message)

        if result.should_exit:
            break


if __name__ == "__main__":
    main()
