# MyNotes
Проект на FastAPI "Мои заметки".

## Структура проекта:
- notes.py - API для обработки запросов
- models.py - модели для FastAPI
- database/db.py - основной класс NotesDB для работы с базой данной "notes"

Для работы с API MyNotes необходимо установить веб-фреймворк FastAPI в ваше виртуальное окружение: `pip install fastapi`

### Основные запросы к API MyNotes:
- **/docs** - автоматическая документация от FastAPI с возможностью отправки запросов.
- **/add_user/{login}** - GET/POST - добавление нового пользователя.
- **/add_note/{login}/{text}** - GET/POST - создание новой заметки пользователя.
- **/notes/{operation}/{login}** - GET - (operation принимает одно из значений: all_notes, 5_recent_notes) 
вывести все заметки / 5 последних заметок пользователя с логином = login.

### Запуск сервера
Запуск локального сервера осуществляется с помощью команды:
`uvicorn notes:app --reload`


