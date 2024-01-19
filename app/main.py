from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    username : str
    age : int


users = [{"username" : "Vasya","age" : 13}]   
@app.get('/')
async def main_page():
    return users


@app.get('/add_user')
async def get_new_route(user : User):
    print(user)
    users.append({"username" : f"{user.username}","age" : user.age})
    print(users)
    return {'response':'succesfull'}