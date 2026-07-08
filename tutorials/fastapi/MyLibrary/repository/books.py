"""Repository module for managing books in the database."""

from sqlalchemy import select
from database import SessionDep
from models.books import BooksModel
from schemas.books import SBookAdd


class BooksRepository:
    """Repository class for managing books in the database."""

    @classmethod
    async def add_one(cls, data: SBookAdd, session: SessionDep) -> BooksModel:
        """Add a new book to the database."""
        new_book = BooksModel(**data.model_dump())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    @classmethod
    async def find_all(cls, session: SessionDep) -> list[BooksModel]:
        """Retrieve all books from the database."""
        result = await session.execute(select(BooksModel))
        books = result.scalars().all()
        return books

    @classmethod
    async def find_one(cls, book_id: int, session: SessionDep) -> BooksModel | None:
        """Retrieve a single book by its ID from the database."""
        query = select(BooksModel).where(BooksModel.id == book_id)
        result = await session.execute(query)
        book = result.scalar_one_or_none()
        return book

    @classmethod
    async def update_one(cls, book_id: int, data: SBookAdd, session: SessionDep) -> BooksModel | None:
        """Update an existing book in the database."""
        book = await BooksRepository.find_one(book_id=book_id, session=session)
        if not book:
            return None
        for key, value in data.model_dump().items():
            setattr(book, key, value)
        await session.commit()
        await session.refresh(book)
        return book

    @classmethod
    async def delete_one(cls, book_id: int, session: SessionDep) -> bool:
        """Delete a book from the database."""
        book = await BooksRepository.find_one(book_id=book_id, session=session)
        if not book:
            return False
        await session.delete(book)
        await session.commit()
        return True

    @classmethod
    async def mark_as_read(cls, book_id: int, session: SessionDep) -> BooksModel | None:
        """Mark a book as read in the database."""
        book = await BooksRepository.find_one(book_id=book_id, session=session)
        if not book:
            return None
        book.is_read = True
        await session.commit()
        await session.refresh(book)
        return book
