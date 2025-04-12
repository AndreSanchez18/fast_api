from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

orders_db = []

USERS_SERVICE_URL = "http://127.0.0.1:8000/users/"

@app.post("/orders/")
def create_order(order : dict):
    user_id = order.get("user_id")

    response = requests.get(f"{USERS_SERVICE_URL}{user_id}")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="User not found")
    
    orders_db.append(order)
    return {"mensaje":"La orden fue creada correctamente", "order":order}

@app.get("/orders/{user_id}")
def get_orders(user_id : int):
    user_orders = [order for order in orders_db if user_id == order["user_id"]]
    return user_orders