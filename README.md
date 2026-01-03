# AI Productivity Agent (CLI)

A clean, beginner-friendly **CLI-based productivity agent** built in Python.
This project demonstrates **agent-style decision logic**, **stateful memory with JSON persistence**, and a **modular, extensible architecture**.

The goal of this repository is to show **how an AI-style agent is built from scratch**, focusing on clarity, structure, and understanding rather than heavy frameworks or hidden abstractions.

---

## ✨ Features

* Interactive command-line interface
* Agent-style input → decision → action flow
* Persistent task memory using JSON
* Context-aware behavior (asks follow-up questions when input is incomplete)
* Clean, modular architecture (router, agent, storage separation)
* Easy to extend with new commands or AI integrations

---

## 🧠 How the Agent Works

The agent follows a simple but powerful loop:

1. **Input** – User enters a command
2. **Decision** – Router interprets intent and current context
3. **Action** – Agent performs the requested operation
4. **Memory** – State is persisted to JSON
5. **Response** – Agent replies to the user

This mirrors the core idea behind modern AI agents, without unnecessary complexity.

---

## 🗂 Project Structure

```
src/productivity_agent/
├── main.py        # CLI loop and user interaction
├── router.py      # Command routing and decision logic
├── agent.py       # Core agent actions (add, list, done)
├── storage.py     # JSON-based persistence layer
├── models.py      # Task data model
└── __init__.py

data/
└── tasks.json     # Persistent task memory
```

Each module has a **single responsibility**, making the system easy to reason about, test, and extend.

---

## ▶️ Running the Project

### Requirements

* Python 3.11 or newer
* No external dependencies

### Run the agent

From the project root:

```bash
python -m src.productivity_agent.main
```

---

## ⌨️ Available Commands

```
add <task description>   Add a new task
add                      Agent asks for task title
list                     Show all tasks
done <task_id>           Mark task as completed
delete <task_id>         Delete a task
plan                     Show today's suggested tasks
help                     Show help message
exit                     Exit the agent
```

### Example Interaction

```
> add
What is the task title?
> study python
Added: [1] study python

> list
🕒 [1] study python (pending)

> done 1
Task [1] marked as done.
```

---

## 🧩 Design Decisions

* **No frameworks** – focus on fundamentals and transparency
* **JSON persistence** – simple, inspectable memory layer
* **Router pattern** – separates decision logic from I/O
* **Explicit state handling** – agent context is visible and understandable
* **Stable task IDs** – task IDs are unique identifiers and are **not reused** after deletion

Task IDs intentionally remain stable even if tasks are deleted. This mirrors real-world systems (e.g. database primary keys) and avoids hidden side effects or identity confusion.

These choices make the project ideal for learning, interviews, and portfolio review.

---

## 🚀 Future Improvements

* `help` and `delete` commands
* Task categories and priorities
* Daily planning suggestions
* LLM integration (OpenAI or local models)
* Unit tests

---

## 📌 What This Project Demonstrates

* How to design and build an AI-style agent from scratch
* Clean Python project structuring
* State management and persistence
* Decision-based program flow
* Incremental, professional development practices

---

## 📄 License

This project is open for educational and portfolio use.
