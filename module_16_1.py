from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def welcome() -> str:
    return 'Главная страница'

@app.get('/user/admin')
async def welcome_admin() -> str:
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def welcome_user(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def user_info(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, возраст: {age}'