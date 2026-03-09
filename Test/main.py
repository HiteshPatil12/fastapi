from fastapi import FastAPI

app = FastAPI()

books = {
    1: {"title": "Atomic Habits", "author": "James Clear"},
    2: {"title": "Deep Work", "author": "Cal Newport"},
    3: {"title": "Clean Code", "author": "Robert C Martin"}
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return books.get(book_id, {"error": "Book not found"})

@app.get("/search")
async def search_book(author: str):
    result = []

    for book in books.values():
        if book["author"] == author:
            result.append(book)

    return result

from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str

@app.post("/books")
async def create_book(book: Book):
    books[book.id] = {
        "title": book.title,
        "author": book.author
    }
    # print(f"Book added: {book.title} by {book.author} ")
    return {"message": "Book added", "book": book}

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    books[book_id] = {
        "title": book.title,
        "author": book.author
    }
    return {"message": "Book updated"}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    books.pop(book_id)
    print(f"Book with id {book_id} deleted")
    return {"message": "Book deleted"}