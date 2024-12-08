from fastapi import FastAPI, Path, Body, HTTPException
from pydantic import BaseModel
from typing import Annotated
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/users/{username}/{age}')
async def add_user(user: User) -> str:
    if users == []:
        new_id = 1
    else:
        new_id = max(u.id for u in users) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return f'User {new_user} is registered.'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, user_age: int, user_name: str = Body()) -> str:
    for u in users:
        if u.id == user_id:
            u.username = user_name
            u.age = user_age
            return u
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return f'{u} delete'
    raise HTTPException(status_code=404, detail='User was not found')
