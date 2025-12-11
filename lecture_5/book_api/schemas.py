from typing import Optional
from pydantic import BaseModel


class AddBook(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class BookOut(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None


class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None