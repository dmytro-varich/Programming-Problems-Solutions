from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool = False