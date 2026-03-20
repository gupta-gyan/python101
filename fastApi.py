# fastApi example
from fastapi import FastAPI
app = FastAPI()

BOOKS   = [{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
           {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
           {"title": "1984", "author": "George Orwell", "year": 1949}]


@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")    
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
@app.get("/hello")
async def hello():
    return {"message": "Hello, FastAPI!"};

@app.get("/books")
async def get_books():
    return BOOKS

# return book by name
@app.get("/books/{name}")
async def get_book_by_name(name: str):
    for book in BOOKS:
        if book["title"].lower() == name.lower():
            return book
    return {"error": "Book not found"}

# Add new book
@app.post("/books") 
async def add_book(book: dict):
    BOOKS.append(book)
    return {"message": "Book added successfully"}

# Update Book by name
@app.put("/books/{name}")
async def update_book(name: str, updated_book: dict):
    for book in BOOKS:
        if book["title"].lower() == name.lower():
            book.update(updated_book)
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}
# Delete Book by name
@app.delete("/books/{name}")
async def delete_book(name: str):
    global BOOKS
    BOOKS = [book for book in BOOKS if book["title"].lower() != name.lower()]
    return {"message": "Book deleted successfully"}

# To run this FastAPI application, save it to a file (e.g., main.py) and use the command:
# uvicorn main:app --reload 
# steps to test the API using a web browser or a tool like curl or Postman:
# 1. Start the FastAPI application using the command above.
# 2. Open a web browser and navigate to http://127.0.0.1:8000/ to see the root endpoint response.
# 3. To test the items endpoint, navigate to http://127.0.0 :8000/items/42?q=example to see the response with the item_id and query parameter.