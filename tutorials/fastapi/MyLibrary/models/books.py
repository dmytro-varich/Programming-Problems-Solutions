"""SQLAlchemy models for the books table."""

from sqlalchemy.orm import Mapped, mapped_column

from database import Model


class BooksModel(Model):
    """SQLAlchemy model for the books table."""
    __tablename__ = "books"

    id: Mapped[int | None] = mapped_column(primary_key=True,
                                           autoincrement=True,
                                           init=False)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]
    pages: Mapped[int]
    is_read: Mapped[bool] = mapped_column(default=False)
