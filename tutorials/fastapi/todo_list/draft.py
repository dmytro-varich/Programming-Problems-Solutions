from fastapi import FastAPI, Depends

app = FastAPI()

fake_database = [{"id": 1, "title": "Task 1"}, {"id": 2, "title": "Task 2"}]


# Dependency function
def pagination_parameters(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/tasks")
def get_tasks(pagination: dict = Depends(pagination_parameters)):
    skip = pagination["skip"]
    limit = pagination["limit"]

    return fake_database[skip : skip + limit]

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# ===============================================================
# @app.get("/tasks/{task_id}")
# def get_task(task_id: int):
#     return {"task_id": task_id, "name": f"Task #{task_id}"}

# @app.get("/tasks")
# def get_tasks(skip: int = 0, limit: int = 10):
#     return {
#         "message": "Return task list",
#         "skip": skip,
#         "limit": limit
#     }
# ===============================================================

# @app.post("/tasks")
# def create_task(task: Task):
#     return {
#         "message": "Task created successfully",
#         "task": task
#     }

# 1. READ: Get all tasks
# @app.get("/tasks")
# def get_tasks():
#     return fake_database

# 2. CREATE: create a new task
@app.post("/tasks")
def create_task(task: Task):
    # Generate ID for new task
    new_task = task.model_dump()  # Convert Pydantic-model to dictionary
    new_task["id"] = len(fake_database) + 1

    # Save to "DB"
    fake_database.append(new_task)
    return new_task

# 3. UPDATE: update the task by ID
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for idx, t in enumerate(fake_database):
        if t["id"] == task_id:
            updated_task = task.model_dump()
            updated_task["id"] = task_id
            fake_database[idx] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")

# 4. DELETE: delete the task by ID
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, task: Task):
    for idx, t in enumerate(fake_database):
        if t["id"] == task_id:
            del fake_database[idx]
            return {"message": "Task removed successfully"}
    
    raise HTTPException(status_code=404, detail="Task not found")

# FastAPI example using async function
#----------------------------------------------
import httpx

@app.get("/pokemon")
async def get_pokemon():
    # We use async client
    async with httpx.AsyncClient() as client:
        response = await client.get("https://pokeapi.co/api/v2/pokemon/ditto")
        return response.json()

# FastAPI example using common function with def
import time

@app.get("/heavy-computation")
def do_heavy_stuff():
    time.sleep(5)  # Imitation heavy process (For example: heavy SQL-query)
    return {"message": "Wow, It was really hard!"}
