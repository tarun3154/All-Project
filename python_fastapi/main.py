from fastapi import FastAPI
from typing import List
from uuid import uuid4,UUID

from python_fastapi.models import User,Role,Gender,UserUpdateRequest


app= FastAPI()

db:List[User]=[
    User(
        id=uuid4(),
        first_name="Tarun",
        last_name='Sharma',
        gender=Gender.male,
        roles=[Role.admin]
    ),

     User(
        id=uuid4(),
        first_name="geeta",
        last_name='Sharma',
        gender=Gender.female,
        roles=[Role.user,Role.student]
    ),
]

@app.get('/')
def root():
    return {"hello":"wolf"}

@app.get('/api/users')
async def fetch_users():
    return db;

@app.post('/api/users')
async def register_user(user:User):
    db.append(user)
    return{'id':user.id}

@app.delete('/api/users/{user_id}')
async def delete_user(user_id:UUID):
    for user in db:
        if user_id == user_id:
            db.remove(user)
            return
    raise Exception(
        status_code =404,
        detail= f'user with id {user_id} does not exist'
    )

@app.put('/api/users/{user_id}')
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
    raise Exception(
            status_code =404,
            detail=f'user with id {user_id} does not exists'

    )