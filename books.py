from fastapi import FastAPI

app = FastAPI()

books = [
    {'title': 'Book1', 'author': 'Author1', 'category': "science"},
    {'title': 'Book2', 'author': 'Author2', 'category': "fiction"},
    {'title': 'Book3', 'author': 'Author3', 'category': "history"},
    {'title': 'Book4', 'author': 'Author4', 'category': "current_affairs"},
    {'title': 'Book5', 'author': 'Author5', 'category': "science"},
    {'title': 'Book6', 'author': 'Author6', 'category': "fiction"},
]
@app.get("/books")
async def read_all_books():
    return books

@app.get("/books/{book_title}")
async def read_all_books(book_title):
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param):
    return {'dynamic_param': dynamic_param}

#create an api to post new books
#create an api to remove books
#create an api to update new book

#read books from database