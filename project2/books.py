from fastapi import FastAPI, Body, HTTPException

app = FastAPI()


BOOKS = [
    {'title':'Title one', 'author':'Authur One', 'category':'Science'},
    {'title':'Title Two', 'author':'Authur Two', 'category':'Science'},
    {'title':'Title Three', 'author':'Authur Three', 'category':'History'},
    {'title':'Title Four', 'author':'Authur Four', 'category':'Math'},
    {'title':'Title Five', 'author':'Authur Five', 'category':'Math'},
    {'title':'Title Six', 'author':'Authur Two', 'category':'Math'},
    {"title":"Title Seven", "author":"Authur One", "category":"Science"}
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


@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    
    
@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            

@app.delete('/books/delete_books/{book_title}')
async def delete_book(book_title: str):
    """Delete a book by title (case-insensitive).

    Returns the deleted book on success, or raises 404 if not found.
    """
    for i, book in enumerate(BOOKS):
        if book.get('title').casefold() == book_title.casefold():
            removed = BOOKS.pop(i)
            return {"deleted": removed}
    # not found
    raise HTTPException(status_code=404, detail="Book not found")


@app.get('/books/author/{author}')
async def read_book_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
            
    return books_to_return
