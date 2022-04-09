# Отправить письмо с помощью FastAPI
# MyNotes с помощью FastAPI
# Gmail API
from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/statistics")
async def statistics():
    """Функция для отправки статистики отправки писем"""
    return {"message": "Hello World"}


@app.get('/info/{mail_id}')
async def info():
    """Функция для проверки статуса отправки сообщения"""
    return {}





