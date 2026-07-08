"""Schemas for books."""

from pydantic import BaseModel, Field, ConfigDict


class SBookBase(BaseModel):
    """Base schema for a book."""
    title: str
    author: str
    year: int
    pages: int = Field(..., gt=10)
    is_read: bool = False


class SBookAdd(SBookBase):
    """Schema for adding a new book."""
    pass


class SBook(SBookBase):
    """Schema for representing a book."""
    id: int

    model_config = ConfigDict(from_attributes=True)
