class Task:
    def __init__(self, task_id: int, title: str, status: str = "pending"):
        self.id = task_id
        self.title = title
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            task_id=data["id"],
            title=data["title"],
            status=data.get("status", "pending"),
        )
