from fastapi import FastAPI
from models import MyNote
from database.db import NotesDB


app = FastAPI()
db = NotesDB()


@app.get("/")
def home():
    return {"message": "Hello, it is API for your notes"}


@app.get("/new_user/{login}")
@app.post("/new_user/{login}")
def add_new_user(login: str):
    """Добавление нового пользователя в БД с заметками"""
    if db.add_user(login):
        return {'status': 200, 'text': f'User with login {login} successfully added to Notes'}
    else:
        return {'status': 400, 'text': f'User with login {login} already exists in Notes'}


@app.get("/add_note/{login}/{text}")
@app.post("/add_note/{login}/{text}")
def add_note(login: str, text: str):
    """Добавление заметки по логину пользователя"""
    if db.add_note(login, text):
        return {'status': 200, 'text': 'Note successfully added to Notes'}
    else:
        return {'status': 400, 'text': f'No user with login={login}'}


@app.get("/notes/{operation}/{login}")
def notes(operation: MyNote, login: str):
    """Вывести все заметки/5 заметок пользователя"""
    match operation:
        case MyNote.all_notes:
            # выгрузка из БД всех заметок пользователя по логину
            res = db.view_all_user_notes(login)
            if res:
                return {'status': 200, 'text': res}
            return {'status': 400, 'text': f'No user with login={login}'}
        case MyNote.five_recent_notes:
            # выгрузка из БД 5 заметок пользователя по логину
            res = db.view_all_user_notes(login)
            if res:
                return {'status': 200, 'text': res[0:5]}
            return {'status': 400, 'text': f'No user with login={login}'}
