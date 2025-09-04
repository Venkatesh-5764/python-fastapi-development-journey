from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
app= FastAPI()
class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float
booksdb=[]
@app.post("/books/")
def create_book(book:Book):
    for b in booksdb:
        if b.id==book.id:
            raise HTTPException(status_code=404,detail="BookId already exists")
    booksdb.append(book)
    return {"message":"Book addded successfully in the Booksdb","book":book}
@app.get("/books/")
def get_books():
    return booksdb

@app.put("/books/{book_id}")
def update_book(book_id:int,update_book:Book):
    for i,book in enumerate(booksdb):
        if book.id==book_id:
            booksdb[i]=update_book
            return {"message": "Book updated","book":update_book}
    raise HTTPException(status_code=404,detail="Book not found")
@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for i, book in enumerate(booksdb):
        if book.id==book_id:
            del booksdb[i]
            return {"message":"book deleted"}
    raise HTTPException(status_code=404,detail="Book not found")
