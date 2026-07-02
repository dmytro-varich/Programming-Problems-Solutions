from fastapi import APIRouter, HTTPException
from models import Task


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

fake_database = []

@router.get("")
def get_tasks():
    return fake_database

@router.post("")
def create_task(task: Task):
    new_task = task.model_dump()
    new_task["id"] = len(fake_database) + 1
    fake_database.append(new_task)
    return new_task

@router.delete("/{task_id}")
def update_task(task_id: int, task: Task):
    for idx, t in enumerate(fake_database):
        if t["id"] == task_id:
            del fake_database[idx]
            return {"message": "Task created successfully"}

    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}")
def update_task(task_id: int, task: Task):
    for idx, t in enumerate(fake_database):
        if t["id"] == task_id:
            updated_task = task.model_dump()
            updated_task["id"] = task_id
            fake_database[idx] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")