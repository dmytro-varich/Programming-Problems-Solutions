"""The main entry point for the FastAPI application."""

from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import engine, Model
from models.books import  BooksModel
from routers.books import books_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for the FastAPI application."""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
  
    print("Database tables created successfully.")

    yield

    print("Application shutdown. Cleanup tasks can be performed here.")


app = FastAPI(
    title="My Library",
    version="1.0.0",
    description="A simple library application to manage books.",
    lifespan=lifespan,
)
app.include_router(books_router)
