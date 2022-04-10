import sqlite3
import time
import logging
from types import NoneType


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(filename="db.log")],
    datefmt="%Y-%m-%d %H:%M:%S"
)


class NotesDB:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("database/notes.db", check_same_thread=False)
        except sqlite3.OperationalError:
            self.conn = sqlite3.connect("notes.db", check_same_thread=False)
        logging.info("Connected to db")

        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Добавление таблиц Users и Notes (если они ещё не были созданы)"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Users(
           ID_user INTEGER PRIMARY KEY,
           login TEXT);""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Notes(
           ID_user INTEGER,
           creation_date TEXT,
           text TEXT);""")

        self.conn.commit()

    def delete_table(self, table_name):
        """Удаление таблицы <table_name> из БД Notes"""
        self.cur.execute(f"DROP TABLE IF EXISTS {table_name};")
        self.conn.commit()

        logging.info(f'Delete table {table_name}')

    def delete_data_in_table(self, table_name: str):
        """Удаление данных в таблице <table_name> БД Notes"""
        try:
            self.cur.execute(f"DELETE FROM {table_name}")
        except sqlite3.OperationalError as ex:
            logging.error(f'{ex} for delete')
        else:
            self.conn.commit()
            logging.info(f'Delete table {table_name}')

    def add_user(self, login: str):
        """Добавление нового пользователя в таблицу Users БД Notes"""
        self.cur.execute("SELECT login FROM Users WHERE login=? LIMIT 1;", (login,))
        id_user = self.cur.fetchall()
        if not len(id_user):
            self.cur.execute("INSERT INTO Users (login) VALUES (?)", (login,))
            self.conn.commit()
            logging.info(f"ADD user: login='{login}'")
            return True
        else:
            logging.error(f"ADD user: Login='{login}' has already created")

    def add_note(self, login: str, text: str):
        """Добавление заметки по логину пользователя в таблицу Notes БД Notes"""
        current_time = time.strftime('%Y-%m-%d', time.localtime())

        # получение ID_user по login
        self.cur.execute("SELECT ID_user FROM Users WHERE login=? LIMIT 1;", (login,))
        id_user = self.cur.fetchone()

        if not isinstance(id_user, NoneType):
            # добавление заметки в БД
            self.cur.execute("INSERT INTO Notes VALUES (?, ?, ?)", (id_user[0], current_time, text,))
            self.conn.commit()
            logging.info(f"ADD note: login='{login}', text='{text}'")
            return True
        else:
            logging.error(f"ADD note: No user with login='{login}'")

    def view_all_data_in_table(self, table_name: str):
        """Просмотр всех строк таблицы <table_name> БД Notes"""
        try:
            all_rows = self.cur.execute(f"SELECT * FROM {table_name}").fetchall()
        except sqlite3.OperationalError as ex:
            logging.error(f"{ex} to view all data")
        else:
            logging.info(f"Viewed all rows: {all_rows}")
            return all_rows

    def view_all_user_notes(self, login):
        """Получение списка всех заметок пользователя по логину"""
        self.cur.execute("SELECT ID_user FROM Users WHERE login=? LIMIT 1;", (login,))     # получение ID_user по login

        id_user = self.cur.fetchone()

        if not isinstance(id_user, NoneType):
            # получение всех заметок по логину пользователя
            list_of_notes = self.cur.execute("SELECT creation_date, text  FROM Notes WHERE ID_user=?", (id_user[0],)).fetchall()
            logging.info(f"Viewed all user notes: login={login}, notes={list_of_notes}")
            return list_of_notes
        else:
            logging.error(f'No user with login={login}')
