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

#create an api to post new books
#create an api to remove books
#create an api to update new book