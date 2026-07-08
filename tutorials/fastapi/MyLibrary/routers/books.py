"""This module contains the API routes for managing books in the library application."""

from fastapi import APIRouter, status, HTTPException

from database import SessionDep
from schemas.books import SBookAdd, SBook
from repository.books import BooksRepository


books_router = APIRouter(prefix="/books", tags=["Books"])


@books_router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(books: SBookAdd, session: SessionDep) -> SBook:
    """Create a new book in the database."""
    books_model = await BooksRepository.add_one(data=books, session=session)
    return books_model


@books_router.get("")
async def read_books(session: SessionDep) -> list[SBook]:
    """Read all books from the database."""
    books = await BooksRepository.find_all(session=session)
    return books


@books_router.get("/{book_id}")
async def read_book(book_id: int, session: SessionDep) -> SBook:
    """Read one book from the database."""
    book = await BooksRepository.find_one(book_id=book_id, session=session)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@books_router.put("/{book_id}")
async def update_book(book_id: int, books: SBookAdd, session: SessionDep) -> SBook:
    """Update an existing book in the database."""
    upd_book = await BooksRepository.update_one(book_id=book_id, data=books, session=session)
    if not upd_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return upd_book


@books_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, session: SessionDep) -> None:
    """Delete a book from the database."""
    is_deleted = await BooksRepository.delete_one(book_id=book_id, session=session)
    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return None


@books_router.patch("/{book_id}/mark-read")
async def mark_book_as_read(book_id: int, session: SessionDep) -> SBook:
    """Mark a book as read in the database."""
    book = await BooksRepository.mark_as_read(book_id=book_id, session=session)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book
