from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
from typing import List

app = FastAPI()

class OrderCreate(BaseModel):
    user_id : int
    products_id : List[int]


orders_db = [
    {
        "user_id":1,
        "list_products":[
            {"id":1,
            "name":"Arroz",
            "price":100},

            {"id":2,
             "name":"Fideo",
             "price":50}
        ]
    }
]

USERS_SERVICE_URL = "http://127.0.0.1:8000/users/"
PRODUCTS_SERVICE_URL = "http://127.0.0.1:8002/products/"

@app.post("/orders/")
def create_order(order : OrderCreate):

    user_service_response = requests.get(f"{USERS_SERVICE_URL}{order.user_id}")

    if user_service_response.status_code != 200:
        raise HTTPException(status_code=404, detail="User not found")

    list_products = []
    
    for p in order.products_id:
        response = requests.get(url=f"{PRODUCTS_SERVICE_URL}{p}")
        if response.status_code !=200:
            raise HTTPException(status_code=404, detail="Products not found")
        else:
            list_products.append(response.json())
    
    new_order = {"user_id":order.user_id, "list_products":list_products}

    orders_db.append(new_order)
    return {"mensaje":"La orden fue creada correctamente", "order":new_order}

@app.get("/orders/{user_id}")
def get_orders(user_id : int):
    user_orders = [order for order in orders_db if user_id == order["user_id"]]
    return user_orders

@app.get("/orders/")
def get_orders():
    return orders_db