from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the Book model
class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: str

# Simulate a database with an in-memory list of books
books_db = [
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
]

@app.get("/books/", response_model=List[Book])
async def get_books():
    """Get all books."""
    return books_db

@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    """Create a new book."""
    books_db.append(book.dict())
    return book

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Get a single book by its index."""
    if book_id >= len(books_db) or book_id < 0:
        return {"error": "Book not found"}
    return books_db[book_id]

@app.delete("/books/{book_id}", response_model=Book)
async def delete_book(book_id: int):
    """Delete a book by its index."""
    if book_id >= len(books_db) or book_id < 0:
        return {"error": "Book not found"}
    deleted_book = books_db.pop(book_id)
    return deleted_book
