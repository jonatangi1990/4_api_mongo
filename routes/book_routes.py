from fastapi import APIRouter
from models.book_models import BookCreate, Book
from controllers import book_controllers


router = APIRouter()

#POST crear un libro

@router.post('/', status_code=201)
async def create_book(book: BookCreate):
    return await book_controllers.create_book(book)

#GET obtener liosta de libros

@router.get('/', status_code=200)
async def get_book_list():
    return await book_controllers.get_book_list()

#GET obtener un libro por id

@router.get('/{book_id}', status_code=200)
async def get_book_by_id(book_id: str):
    return await book_controllers.get_book_by_id(book_id)

#UPDATE actualizar un libro
@router.put('/{book_id}', status_code=200)
async def update_book(book_id:str, book_data: BookCreate):
    return await book_controllers.update_book(book_id, book_data)