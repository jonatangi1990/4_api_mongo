from fastapi import HTTPException

#como vamos a conectarnos con bbdd mongo tengo que importar la conexion
from db.mongo import book_collection
from models.book_models import Book, BookCreate



#vamos a crear una funcion que nos permita convertir el tipo de mongo (objeto) en una clase book de python. Vamos a crear una funcion book_helper que transforme los datos de python a mongo. Nuestra propia funcion de parseo.


def book_helper(book: dict) -> Book:
    return Book(
        id = str(book["_id"]),
        title = book["title"],
        author = book["author"],
        year = book["year"],
        pages = book.get("pages"), #de esta manera como lo teniamos opcional si no lo pasamos no nos dara error
    )
    
#controlador de post para crear un libro de mongo

async def create_book(book: BookCreate):
    try:
        #model_dump() convierte un modelo en un diccionario
        new_book = book.model_dump()
        result = await book_collection.insert_one(new_book)
        book_create = await book_collection.find_one({"_id": result.inserted_id})
        return book_helper(book_create)
    except Exception as e:
        raise HTTPException(status_code= 500, detail= f"Error: {str(e)}")
