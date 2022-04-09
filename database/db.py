import sqlite3
import time
from types import NoneType


class NotesDB:
    def __init__(self):
        self.conn = sqlite3.connect('notes.db')
        self.cur = self.conn.cursor()
        self._add_tables()

    def _add_tables(self):
        self.cur.execute("DROP TABLE IF EXISTS Notes;")
        self.cur.execute("DROP TABLE IF EXISTS Users;")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Users(
           ID_user INTEGER PRIMARY KEY,
           login TEXT);""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Notes(
           ID_user INTEGER,
           creation_date TEXT,
           text TEXT);""")

        self.conn.commit()

    def add_user(self, user_login: str):
        """Метод добавляет нового пользователя в БД 'Заметки'"""
        self.cur.execute("SELECT login FROM Users WHERE login=? LIMIT 1;", (user_login,))
        id_user = self.cur.fetchall()
        if not len(id_user):
            self.cur.execute("INSERT INTO Users (login) VALUES (?)", (user_login,))
            self.conn.commit()
        else:
            print(f"Login={user_login} has already created")

    def add_note(self, login: str, text: str):
        """Метод добавляет заметку по логину пользователя"""
        current_time = time.strftime('%Y-%m-%d', time.localtime())

        # получение ID_user по login
        self.cur.execute("SELECT ID_user FROM Users WHERE login=? LIMIT 1;", (login,))
        id_user = self.cur.fetchone()

        if not isinstance(id_user, NoneType):
            # добавление заметки в БД
            self.cur.execute("INSERT INTO Notes VALUES (?, ?, ?)", (id_user[0], current_time, text,))
            self.conn.commit()
        else:
            print(f'No user with login={login}')

    def view_users(self):
        """Метод для просмотра всей информации о пользователях"""
        print(self.cur.execute("SELECT * FROM Users").fetchall())

    def view_notes(self):
        """Метод для просмотра всей информации о заметках"""
        print(self.cur.execute("SELECT * FROM Notes").fetchall())
