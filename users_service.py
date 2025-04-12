from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de datos simulada de usuarios
users_db = [
    {"id": 1, "name": "Andrés"},
    {"id": 2, "name": "María"}
]

@app.get("/users/")
def get_users():
    return users_db


@app.get("/users/{user_id}")
def get_user(user_id: int):

    usuario = list(filter(lambda x:x["id"] == user_id, users_db))

    if not usuario:
        raise HTTPException(status_code=404, detail="User not found")
    return usuario[0]

@app.post("/users/")
def create_user(user: dict):
    users_id = []
    for u in users_db:
        users_id.append(u.get("id"))
    new_id = max(users_id) + 1
    user["id"] = new_id

    users_db.append(user)

    return user

