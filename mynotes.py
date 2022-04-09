# Отправить письмо с помощью FastAPI
# MyNotes с помощью FastAPI
# Gmail API
from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class MyNote(str, Enum):
    all_notes = "all notes"
    five_recent_notes = "5 recent notes"


@app.get("/")
async def root():
    return {"message": "Hello, its API for your notes"}


@app.get("/notes")
async def root(operation: MyNote):
    match operation:
        case MyNote.all_notes:
            return {'message': operation}
        case MyNote.five_recent_notes:
            return {'message': operation}
        # case _:   -  FastAPI сам выдаст подробную ошибку
        #     return {"message": f"Error, your GET request not in {''.join([getattr(MyNote, method) for method in dir(MyNote) if not method.startswith('__')])}"}



# @app.get("/statistics")
# async def statistics():
#     """Функция для отправки статистики отправки писем"""
#     return {"message": "Hello World"}
#
#
# @app.get("/info/{mail_id}")
# async def info():
#     """Функция для проверки статуса отправки сообщения"""
#     return {}
