from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:float

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        
        
class BookRequest(BaseModel):
    id:int
    title: str
    author:str
    description:str
    rating:float
    
    
    

BOOKS = [
    Book(1, 'Computer Science pro', 'Harsh', 'A Very Nice Book!',  5),
    Book(2, 'Python For Beginers', 'Harsh', 'A Very Nice Book!',  4.5),
    Book(3, 'Data Analysis', 'Khushi', 'A Very Nice Book!',  5),
    Book(4, 'Machine Learning Es', 'Khushi', 'A Very Nice Book!',  4.9),
    Book(5, 'JavaScripts', 'Bipul Kumar Singh', 'A Very Nice Book!',  5),
    Book(6, 'Peotry', 'Mirza Galib', 'A Very Nice Book!',  5),
]

@app.get('/books')
async def reload_all_books():
    return BOOKS



@app.post('/create-book')
async def create_book(book_request: BookRequest):
    # print(type(book_request))
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOKS.append(new_book)
    
    
    
    
