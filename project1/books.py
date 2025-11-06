from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title':'Title one', 'author':'Authur one', 'category':'Science'},
    {'title':'Title Two', 'author':'Authur Two', 'category':'Science'},
    {'title':'Title Three', 'author':'Authur Three', 'category':'History'},
    {'title':'Title Four', 'author':'Authur Fout', 'category':'Math'},
    {'title':'Title Five', 'author':'Authur Five', 'category':'Math'},
    {'title':'Title Six', 'author':'Authur Two', 'category':'Math'},
]

@app.get('/books')
async def reload_all_books():
    return BOOKS


@app.get('/books/mybooks')
async def read_all_books():
    return {'books_title': "My favorite book!"}

@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return None  # Return None if no book is found
            

@app.get('/books/category/')
async def read_category_books(category: str):
    books_to_returns = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_returns.append(book)
    return books_to_returns
    

@app.get('/books/')
async def read_author_category(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and \
        book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
