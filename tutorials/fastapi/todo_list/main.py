from fastapi import FastAPI
from routers import tasks

app = FastAPI(
    title="To-Do List API",
    description="API for manage tasks",
    version="1.0.0"
)

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API: Go to /docs to see documentation."}
