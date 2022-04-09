from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class MyNote(str, Enum):
    all_notes = "all notes"
    five_recent_notes = "5 recent notes"


@app.get("/")
def home():
    return {"message": "Hello, it is API for your notes"}


@app.get("/new_user/{login}")
def add_new_user(login: str):
    """Добавление нового пользователя в БД с заметками"""
    pass


@app.get("/add_note/{login}")
def add_note(login: str):
    """Добавление нового пользователя в БД с заметками"""
    pass


@app.get("/notes/{login}")
def notes(operation: MyNote, login: str):
    """Вывести все заметки/5 заметок пользователя"""
    match operation:
        case MyNote.all_notes:
            # выгрузка из БД всех заметок пользователя по логину
            return {'message': operation}
        case MyNote.five_recent_notes:
            # выгрузка из БД 5 заметок пользователя по логину
            return {'message': operation}
        # case _:   -  FastAPI сам выдаст подробную ошибку
        #     return {"message": f"Error, your GET request not in {''.join([getattr(MyNote, method) for method in dir(MyNote) if not method.startswith('__')])}"}

