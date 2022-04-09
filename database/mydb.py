import sqlite3


conn = sqlite3.connect('notes.db')
cur = conn.cursor()

# cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")  -  для выполнения SQL запросов
# Ctrl + Shift + U - transform to upper/lower case выделенный текст
cur.execute("""CREATE TABLE IF NOT EXISTS Users(
   ID_user INTEGER PRIMARY KEY,
   login TEXT);""")

cur.execute("""CREATE TABLE IF NOT EXISTS Notes(
   ID_user INT,
   creation_date TEXT,
   text TEXT);""")
cur.execute("INSERT INTO Users (login) VALUES ('alena_poliakova')")

conn.commit()

