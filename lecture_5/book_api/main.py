from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from fastapi_pagination import Page, paginate, add_pagination
from sqlalchemy.orm import Session
from db import SessionLocal
import models
import schemas

app = FastAPI()
add_pagination(app)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/")
def add_book(
        book: schemas.AddBook,
        db: Session = Depends(get_db)
) -> None:
    book = models.Book(
        title=book.title.strip().title(),
        author=book.author.strip().title(),
        year=book.year
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    raise HTTPException(
        status_code=201,
        detail=f"Book '{book.title}' successfully added"
    )


@app.get("/books/")
def get_books(
        db: Session = Depends(get_db)
) -> Page[schemas.BookOut]:
    books = db.query(models.Book).all()
    return paginate(books)


@app.delete("/books/{book_id}")
def delete_book(
        book_id: int,
        db: Session = Depends(get_db)
) -> None:
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)
    db.commit()

    raise HTTPException(
        status_code=204,
        detail=f"Book {book_id} successfully deleted"
    )


@app.put("/books/{book_id}")
def update_book(
        book_data: schemas.UpdateBook,
        book_id: int,
        db: Session = Depends(get_db)
) -> None:
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_data.title:
        book.title = book_data.title.strip().title()

    if book_data.author:
        book.author = book_data.author.strip().title()

    if book_data.year:
        book.year = book_data.year

    db.add(book)
    db.commit()
    db.refresh(book)

    raise HTTPException(
        status_code=204,
        detail=f"Book {book_id} successfully updated"
    )


@app.get("/books/search/")
def search_books(
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None,
        db: Session = Depends(get_db)
) -> Page[schemas.BookOut]:
    query = db.query(models.Book)

    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))

    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))

    if year:
        query = query.filter(models.Book.year == year)

    books = query.all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")

    return paginate(books)