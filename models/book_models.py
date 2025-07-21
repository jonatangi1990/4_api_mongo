from pydantic import BaseModel
from typing import Optional




class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    pages: Optional[int] #asi lo ponemos de forma opcional
    
class Book(BookCreate): #de esta manera la clase Book hereda lo de BookCreate y no hay que escribir todo, solo añadir lo que quieras añadir
    id: str