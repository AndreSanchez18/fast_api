from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name:str

class User(UserCreate):
    id : int

# Base de datos simulada de usuarios
users_db = [
    {"id": 1, "name": "Andrés"},
    {"id": 2, "name": "María"}
]

@app.get("/")
def intro():
    return "Base de datos de usuarios"

@app.get("/users/")
def get_users():
    return users_db


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == 1), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/")
def create_user(user: UserCreate):
    new_id = max([u["id"] for u in users_db], default=0) + 1
    new_user = {"id":new_id, "name":user.name}
    users_db.append(new_user)

    return new_user

@app.put("/users/{id}")
def update_user(id : int, user : User):
    for idx in range(len(users_db)):
        if  users_db[idx].get("id") == id:
            update_user = {"id":id, **user}
            users_db[idx]=update_user
            return update_user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/users/{id}")
def remove_user(id : int):
    for idx in range(len(users_db)):
        if  users_db[idx].get("id") == id:
            users_db.pop(idx)
            return {"msg":"Usuario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

    
        

